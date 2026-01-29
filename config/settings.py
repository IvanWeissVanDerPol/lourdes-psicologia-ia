"""
Central Configuration for LourdesBusiness

This module provides centralized configuration management.
All paths and API settings are externalized here for easy modification.

Usage:
    from config.settings import settings

    # Access paths
    data_dir = settings.DATA_DIR
    patients_dir = settings.PATIENTS_DIR

    # Access API keys (from environment)
    openai_key = settings.OPENAI_API_KEY

IMPORTANT:
    - NEVER commit this file with actual API keys
    - Use environment variables for sensitive data
    - Data directory should be OUTSIDE the git repository
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Settings:
    """Central settings for the business toolkit."""

    # ===========================================================================
    # DATA PATHS (EXTERNALIZED FROM REPOSITORY)
    # ===========================================================================

    # Base data directory - MUST be outside git repo for privacy
    DATA_DIR: Path = field(default_factory=lambda: Path(
        os.getenv(
            "LOURDES_DATA_DIR",
            str(Path(__file__).parent.parent.parent / "LourdesBusiness-DATA")
        )
    ))

    @property
    def PATIENTS_DIR(self) -> Path:
        """Directory containing patient data folders."""
        return self.DATA_DIR / "PACIENTES"

    # ===========================================================================
    # WHISPER / TRANSCRIPTION SETTINGS
    # ===========================================================================

    WHISPER_MODEL: str = field(default_factory=lambda: os.getenv("WHISPER_MODEL", "base"))
    WHISPER_LANGUAGE: str = field(default_factory=lambda: os.getenv("WHISPER_LANGUAGE", "es"))
    TRANSCRIPTION_WORKERS: int = field(default_factory=lambda: int(os.getenv("TRANSCRIPTION_WORKERS", "4")))

    # ===========================================================================
    # API KEYS (FROM ENVIRONMENT ONLY)
    # ===========================================================================

    @property
    def OPENAI_API_KEY(self) -> Optional[str]:
        """OpenAI API key for Whisper API (optional - local whisper doesn't need it)."""
        return os.getenv("OPENAI_API_KEY")

    @property
    def ANTHROPIC_API_KEY(self) -> Optional[str]:
        """Anthropic API key for Claude analysis."""
        return os.getenv("ANTHROPIC_API_KEY")

    # ===========================================================================
    # FFMPEG CONFIGURATION
    # ===========================================================================

    FFMPEG_PATHS: list[str] = field(default_factory=lambda: [
        os.getenv("FFMPEG_PATH", ""),
        r"C:\Users\Alejandro\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin",
        r"C:\ffmpeg\bin",
        r"C:\Program Files\ffmpeg\bin",
        "/usr/local/bin",
        "/usr/bin",
    ])

    # ===========================================================================
    # VALIDATION
    # ===========================================================================

    def validate(self) -> list[str]:
        """
        Validate settings and return list of errors.

        Returns:
            List of error messages (empty if valid).
        """
        errors = []

        # Check data directory
        if not self.DATA_DIR.exists():
            errors.append(
                f"Data directory does not exist: {self.DATA_DIR}\n"
                f"  Create it or set LOURDES_DATA_DIR environment variable"
            )
        elif not self.PATIENTS_DIR.exists():
            errors.append(
                f"Patients directory does not exist: {self.PATIENTS_DIR}\n"
                f"  Create the PACIENTES folder in your data directory"
            )

        # Validate Whisper model
        valid_models = ("tiny", "base", "small", "medium", "large", "turbo")
        if self.WHISPER_MODEL not in valid_models:
            errors.append(
                f"Invalid Whisper model: {self.WHISPER_MODEL}\n"
                f"  Valid models: {', '.join(valid_models)}"
            )

        return errors

    def print_status(self):
        """Print current settings status."""
        print("=" * 60)
        print("LOURDES BUSINESS SETTINGS")
        print("=" * 60)
        print()

        print("Data Paths:")
        print(f"  DATA_DIR:     {self.DATA_DIR} {'✓' if self.DATA_DIR.exists() else '✗'}")
        print(f"  PATIENTS_DIR: {self.PATIENTS_DIR} {'✓' if self.PATIENTS_DIR.exists() else '✗'}")
        print()

        print("Whisper Settings:")
        print(f"  Model:    {self.WHISPER_MODEL}")
        print(f"  Language: {self.WHISPER_LANGUAGE}")
        print(f"  Workers:  {self.TRANSCRIPTION_WORKERS}")
        print()

        print("API Keys:")
        print(f"  OPENAI_API_KEY:    {'✓ Set' if self.OPENAI_API_KEY else '✗ Not set'}")
        print(f"  ANTHROPIC_API_KEY: {'✓ Set' if self.ANTHROPIC_API_KEY else '✗ Not set'}")
        print()

        errors = self.validate()
        if errors:
            print("Validation Errors:")
            for error in errors:
                print(f"  ✗ {error}")
        else:
            print("Validation: ✓ All checks passed")


# Default settings instance
settings = Settings()


if __name__ == "__main__":
    # Run validation when executed directly
    settings.print_status()
