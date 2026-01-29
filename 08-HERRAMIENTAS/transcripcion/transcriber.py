"""
Core Transcription Logic

Unified Whisper transcription with consistent output format.
Supports single file, batch, and parallel processing modes.
"""

from __future__ import annotations

import gc
import json
import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

from transcripcion.config import TranscriptionConfig, default_config
from transcripcion.ffmpeg_setup import setup_ffmpeg
from transcripcion.quality import QualityChecker

logger = logging.getLogger(__name__)


@dataclass
class TranscriptResult:
    """Result of transcribing a single file."""

    file: str
    date: Optional[str]
    text: Optional[str]
    duration: Optional[float]
    success: bool
    error: Optional[str] = None
    model: Optional[str] = None
    retranscribed: bool = False

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "file": self.file,
            "date": self.date,
            "text": self.text,
            "duration": self.duration,
            "success": self.success,
        }
        if self.error:
            result["error"] = self.error
        if self.model:
            result["model"] = self.model
        if self.retranscribed:
            result["retranscribed"] = True
        return result


class Transcriber:
    """
    Whisper-based audio transcription.

    Handles model loading, transcription, and result formatting.
    """

    def __init__(
        self,
        model: str = "base",
        language: str = "es",
        config: Optional[TranscriptionConfig] = None,
    ):
        """
        Initialize the transcriber.

        Args:
            model: Whisper model name (tiny, base, small, medium, large, turbo)
            language: Language code for transcription
            config: Optional configuration object
        """
        self.model_name = model
        self.language = language
        self.config = config or default_config
        self._model = None
        self._quality_checker = QualityChecker()

        # Ensure FFmpeg is available
        setup_ffmpeg()

    def _load_model(self):
        """Load Whisper model lazily."""
        if self._model is None:
            import whisper

            logger.info(f"Loading Whisper model '{self.model_name}'...")
            self._model = whisper.load_model(self.model_name)
            logger.info("Model loaded successfully")

    def transcribe_file(self, file_path: Path | str) -> TranscriptResult:
        """
        Transcribe a single audio file.

        Args:
            file_path: Path to the audio file.

        Returns:
            TranscriptResult with transcription or error.
        """
        file_path = Path(file_path)

        try:
            self._load_model()

            # Determine fp16 usage based on model size and GPU availability
            use_fp16 = (
                self.model_name in ("tiny", "base", "small") and self.config.use_fp16
            )

            result = self._model.transcribe(
                str(file_path),
                language=self.language,
                fp16=use_fp16,
                verbose=False,
            )

            text = result["text"]
            if isinstance(text, str):
                text = text.strip()
            else:
                text = str(text).strip() if text else ""

            return TranscriptResult(
                file=file_path.name,
                date=self._parse_date(file_path.name),
                text=text,
                duration=result.get("duration"),
                success=True,
                model=self.model_name,
            )

        except Exception as e:
            logger.error(f"Error transcribing {file_path}: {e}")
            return TranscriptResult(
                file=file_path.name,
                date=self._parse_date(file_path.name),
                text=None,
                duration=None,
                success=False,
                error=str(e),
            )

    def _parse_date(self, filename: str) -> Optional[str]:
        """Extract date from filename in format AUDIO-YYYYMMDD-..."""
        try:
            parts = filename.split("-")
            if len(parts) >= 2:
                date_str = parts[1]
                if len(date_str) == 8 and date_str.isdigit():
                    return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        except Exception:
            pass
        return None

    def check_quality(self, text: str) -> list[str]:
        """Check quality of transcribed text."""
        report = self._quality_checker.check(text)
        return report.issue_summary

    def cleanup_memory(self):
        """Clean up GPU memory."""
        gc.collect()
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except ImportError:
            pass


def save_transcripts(
    output_dir: Path,
    results: list[TranscriptResult],
    chat_name: str,
) -> tuple[Path, Path]:
    """
    Save transcripts to JSON and Markdown files.

    Args:
        output_dir: Directory to save files in.
        results: List of transcript results.
        chat_name: Name of the chat/source for headers.

    Returns:
        Tuple of (json_path, markdown_path).
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save JSON
    json_path = output_dir / "transcripts.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump([r.to_dict() for r in results], f, ensure_ascii=False, indent=2)

    # Group by date for Markdown
    by_date: dict[str, list[TranscriptResult]] = {}
    for r in results:
        date = r.date or "unknown"
        by_date.setdefault(date, []).append(r)

    # Save Markdown
    md_path = output_dir / "transcripts.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Voice Note Transcripts: {chat_name}\n\n")
        f.write(f"> Generated: {datetime.now():%Y-%m-%d %H:%M}\n")
        f.write(f"> Total files: {len(results)}\n")

        success_count = sum(1 for r in results if r.success)
        if success_count < len(results):
            f.write(f"> Success rate: {success_count}/{len(results)}\n")

        f.write("\n---\n\n")

        for date in sorted(by_date.keys()):
            f.write(f"## {date}\n\n")
            for r in sorted(by_date[date], key=lambda x: x.file):
                f.write(f"### {r.file}\n\n")
                if r.error:
                    f.write(f"**ERROR:** {r.error}\n\n")
                elif r.text:
                    f.write(f"{r.text}\n\n")
                else:
                    f.write("*[Empty or inaudible]*\n\n")
            f.write("---\n\n")

    return json_path, md_path


def load_existing_transcripts(json_path: Path) -> dict[str, TranscriptResult]:
    """
    Load existing transcripts from JSON file.

    Args:
        json_path: Path to transcripts.json file.

    Returns:
        Dictionary mapping filename to TranscriptResult.
    """
    if not json_path.exists():
        return {}

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return {
            item["file"]: TranscriptResult(
                file=item["file"],
                date=item.get("date"),
                text=item.get("text"),
                duration=item.get("duration"),
                success=item.get("success", bool(item.get("text"))),
                error=item.get("error"),
                model=item.get("model"),
                retranscribed=item.get("retranscribed", False),
            )
            for item in data
        }
    except Exception as e:
        logger.warning(f"Error loading existing transcripts from {json_path}: {e}")
        return {}
