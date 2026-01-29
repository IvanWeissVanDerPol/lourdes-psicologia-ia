"""
Transcription Module - Unified Voice Note Transcription System

This module consolidates all transcription functionality into a clean, maintainable package.

Usage:
    # Command line
    python -m transcripcion --help
    python -m transcripcion transcribe --input /path/to/audio --model base
    python -m transcripcion check-quality --input /path/to/transcripts
    python -m transcripcion retranscribe --model small

    # As library
    from transcripcion import Transcriber, QualityChecker

    transcriber = Transcriber(model="base", language="es")
    result = transcriber.transcribe_file("/path/to/audio.opus")
"""

from transcripcion.config import TranscriptionConfig
from transcripcion.ffmpeg_setup import setup_ffmpeg
from transcripcion.quality import QualityChecker, check_quality
from transcripcion.transcriber import Transcriber

__all__ = [
    "TranscriptionConfig",
    "setup_ffmpeg",
    "QualityChecker",
    "check_quality",
    "Transcriber",
]

__version__ = "1.0.0"
