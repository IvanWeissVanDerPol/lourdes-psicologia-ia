"""
Central Configuration for Transcription System

All paths and settings are externalized here for easy modification.
Use environment variables for deployment flexibility.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class TranscriptionConfig:
    """Configuration for the transcription system."""

    # Data directory (OUTSIDE the git repository for privacy)
    data_dir: Path = field(default_factory=lambda: Path(
        os.getenv("LOURDES_DATA_DIR", str(Path(__file__).parent.parent.parent.parent / "LourdesBusiness-DATA"))
    ))

    # Whisper settings
    model: str = field(default_factory=lambda: os.getenv("WHISPER_MODEL", "base"))
    language: str = field(default_factory=lambda: os.getenv("WHISPER_LANGUAGE", "es"))
    use_fp16: bool = True  # Use GPU half-precision if available

    # Processing settings
    workers: int = field(default_factory=lambda: int(os.getenv("TRANSCRIPTION_WORKERS", "4")))
    batch_size: int = 50  # Progress update frequency

    # Quality thresholds
    min_words: int = 3
    max_asian_chars: int = 3
    max_english_words: int = 8

    @property
    def patients_dir(self) -> Path:
        """Directory containing patient data folders."""
        return self.data_dir / "PACIENTES"

    @property
    def raw_audio_pattern(self) -> str:
        """Pattern for finding raw audio files."""
        return "RAW/**/*.opus"

    @property
    def transcripts_dir_pattern(self) -> str:
        """Pattern for transcript output directories."""
        return "CLINICA/TRANSCRIPTS"

    def get_patient_dir(self, patient_id: str) -> Path:
        """Get the directory for a specific patient."""
        return self.patients_dir / patient_id

    def get_raw_dir(self, patient_id: str) -> Path:
        """Get the raw audio directory for a patient."""
        return self.get_patient_dir(patient_id) / "RAW"

    def get_transcripts_dir(self, patient_id: str) -> Path:
        """Get the transcripts output directory for a patient."""
        return self.get_patient_dir(patient_id) / "CLINICA" / "TRANSCRIPTS"

    def validate(self) -> list[str]:
        """Validate configuration and return list of errors."""
        errors = []

        if not self.data_dir.exists():
            errors.append(f"Data directory does not exist: {self.data_dir}")
        elif not self.patients_dir.exists():
            errors.append(f"Patients directory does not exist: {self.patients_dir}")

        if self.model not in ("tiny", "base", "small", "medium", "large", "turbo"):
            errors.append(f"Invalid Whisper model: {self.model}")

        if self.workers < 1:
            errors.append(f"Workers must be at least 1, got: {self.workers}")

        return errors

    @classmethod
    def from_env(cls) -> TranscriptionConfig:
        """Create configuration from environment variables."""
        return cls()


# Default configuration instance
default_config = TranscriptionConfig()


# FFmpeg paths to search (platform-specific)
FFMPEG_SEARCH_PATHS = [
    os.getenv("FFMPEG_PATH"),
    r"C:\Users\Alejandro\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin",
    r"C:\ffmpeg\bin",
    r"C:\Program Files\ffmpeg\bin",
    "/usr/local/bin",
    "/usr/bin",
]
