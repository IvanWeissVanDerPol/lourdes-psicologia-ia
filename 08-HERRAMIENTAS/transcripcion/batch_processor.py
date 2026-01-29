"""
Batch Processing for Transcription

Supports both threading (for I/O parallelism with shared model)
and multiprocessing (for true parallelism with separate models).
"""

from __future__ import annotations

import logging
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional

from transcripcion.config import TranscriptionConfig, default_config
from transcripcion.transcriber import (
    TranscriptResult,
    Transcriber,
    load_existing_transcripts,
    save_transcripts,
)

logger = logging.getLogger(__name__)


# Global transcriber for multiprocessing workers
_worker_transcriber: Optional[Transcriber] = None
_worker_config: tuple[str, str] = ("", "")


def _init_worker(model: str, language: str):
    """Initialize transcriber in worker process."""
    global _worker_transcriber, _worker_config
    if _worker_transcriber is None or _worker_config != (model, language):
        _worker_transcriber = Transcriber(model=model, language=language)
        _worker_config = (model, language)


def _transcribe_worker(args: tuple[str, str, str]) -> dict:
    """Worker function for multiprocessing."""
    file_path, model, language = args
    _init_worker(model, language)
    result = _worker_transcriber.transcribe_file(file_path)
    return result.to_dict()


class BatchProcessor:
    """
    Process multiple audio files with progress tracking.

    Supports:
    - Threading mode: Uses single model with thread pool (memory efficient)
    - Multiprocessing mode: Uses multiple models in separate processes (faster)
    """

    def __init__(
        self,
        model: str = "base",
        language: str = "es",
        workers: int = 4,
        use_multiprocessing: bool = True,
        config: Optional[TranscriptionConfig] = None,
    ):
        """
        Initialize batch processor.

        Args:
            model: Whisper model name
            language: Language code
            workers: Number of parallel workers
            use_multiprocessing: Use multiprocessing (True) or threading (False)
            config: Optional configuration
        """
        self.model = model
        self.language = language
        self.workers = workers
        self.use_multiprocessing = use_multiprocessing
        self.config = config or default_config

        # For threading mode
        self._transcriber: Optional[Transcriber] = None

    def process_files(
        self,
        files: list[Path],
        progress_callback: Optional[
            Callable[[int, int, TranscriptResult], None]
        ] = None,
    ) -> list[TranscriptResult]:
        """
        Process a list of audio files.

        Args:
            files: List of file paths to process.
            progress_callback: Optional callback(completed, total, result)

        Returns:
            List of TranscriptResult objects.
        """
        if not files:
            return []

        results: list[TranscriptResult] = []
        completed = 0
        start_time = datetime.now()

        if self.use_multiprocessing:
            results = self._process_multiprocessing(files, progress_callback)
        else:
            results = self._process_threading(files, progress_callback)

        elapsed = (datetime.now() - start_time).total_seconds()
        logger.info(
            f"Processed {len(results)} files in {elapsed:.1f}s "
            f"({len(results) / elapsed:.2f} files/sec)"
        )

        return results

    def _process_multiprocessing(
        self,
        files: list[Path],
        progress_callback: Optional[Callable[[int, int, TranscriptResult], None]],
    ) -> list[TranscriptResult]:
        """Process files using multiprocessing."""
        results = []
        completed = 0

        # Prepare work items
        work_items = [(str(f), self.model, self.language) for f in files]

        with ProcessPoolExecutor(max_workers=self.workers) as executor:
            future_to_file = {
                executor.submit(_transcribe_worker, item): item[0]
                for item in work_items
            }

            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    result_dict = future.result()
                    result = TranscriptResult(
                        file=result_dict["file"],
                        date=result_dict.get("date"),
                        text=result_dict.get("text"),
                        duration=result_dict.get("duration"),
                        success=result_dict.get("success", False),
                        error=result_dict.get("error"),
                        model=result_dict.get("model"),
                    )
                except Exception as e:
                    logger.error(f"Error processing {file_path}: {e}")
                    result = TranscriptResult(
                        file=Path(file_path).name,
                        date=None,
                        text=None,
                        duration=None,
                        success=False,
                        error=str(e),
                    )

                results.append(result)
                completed += 1

                if progress_callback:
                    progress_callback(completed, len(files), result)

        return results

    def _process_threading(
        self,
        files: list[Path],
        progress_callback: Optional[Callable[[int, int, TranscriptResult], None]],
    ) -> list[TranscriptResult]:
        """Process files using threading with shared model."""
        if self._transcriber is None:
            self._transcriber = Transcriber(
                model=self.model,
                language=self.language,
                config=self.config,
            )

        results = []
        completed = 0

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            future_to_file = {
                executor.submit(self._transcriber.transcribe_file, f): f for f in files
            }

            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    result = future.result()
                except Exception as e:
                    logger.error(f"Error processing {file_path}: {e}")
                    result = TranscriptResult(
                        file=file_path.name,
                        date=None,
                        text=None,
                        duration=None,
                        success=False,
                        error=str(e),
                    )

                results.append(result)
                completed += 1

                if progress_callback:
                    progress_callback(completed, len(files), result)

        return results


def process_chat(
    source_dir: Path,
    output_dir: Path,
    chat_name: str,
    model: str = "base",
    language: str = "es",
    workers: int = 4,
    resume: bool = True,
    file_pattern: str = "*.opus",
    progress_callback: Optional[Callable[[int, int, TranscriptResult], None]] = None,
) -> list[TranscriptResult]:
    """
    Process all audio files from a chat directory.

    Args:
        source_dir: Directory containing audio files
        output_dir: Directory for output transcripts
        chat_name: Name for the chat (used in output)
        model: Whisper model to use
        language: Language code
        workers: Number of parallel workers
        resume: Skip already transcribed files
        file_pattern: Glob pattern for audio files
        progress_callback: Optional progress callback

    Returns:
        List of TranscriptResult objects
    """
    # Find all audio files
    files = sorted(source_dir.glob(file_pattern))
    if not files:
        logger.warning(f"No files matching '{file_pattern}' found in {source_dir}")
        return []

    logger.info(f"Found {len(files)} files in {source_dir}")

    # Load existing transcripts if resuming
    existing: dict[str, TranscriptResult] = {}
    if resume:
        json_path = output_dir / "transcripts.json"
        existing = load_existing_transcripts(json_path)

        # Filter out already transcribed files
        files_to_process = [
            f for f in files if f.name not in existing or not existing[f.name].success
        ]

        if len(files_to_process) < len(files):
            logger.info(
                f"Resuming: {len(files) - len(files_to_process)} already done, "
                f"{len(files_to_process)} remaining"
            )
            files = files_to_process

    if not files:
        logger.info("All files already transcribed")
        return list(existing.values())

    # Process files
    processor = BatchProcessor(
        model=model,
        language=language,
        workers=workers,
        use_multiprocessing=True,
    )

    new_results = processor.process_files(files, progress_callback)

    # Merge with existing results
    all_results = list(existing.values()) + new_results

    # Save results
    save_transcripts(output_dir, all_results, chat_name)

    return all_results
