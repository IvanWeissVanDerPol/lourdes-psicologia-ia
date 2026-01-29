"""
FFmpeg Path Management

Consolidated FFmpeg path setup extracted from multiple transcription scripts.
Handles platform-specific path detection and PATH environment setup.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Optional

from transcripcion.config import FFMPEG_SEARCH_PATHS


def find_ffmpeg() -> Optional[Path]:
    """
    Find FFmpeg installation by searching common paths.

    Returns:
        Path to FFmpeg bin directory, or None if not found.
    """
    # First check if ffmpeg is already in PATH
    if shutil.which("ffmpeg"):
        return None  # Already available, no need to add to PATH

    # Search known paths
    for path_str in FFMPEG_SEARCH_PATHS:
        if path_str is None:
            continue

        path = Path(path_str)
        if path.exists():
            ffmpeg_exe = path / "ffmpeg.exe" if os.name == "nt" else path / "ffmpeg"
            if ffmpeg_exe.exists():
                return path

    return None


def setup_ffmpeg() -> bool:
    """
    Set up FFmpeg by adding it to PATH if needed.

    Returns:
        True if FFmpeg is available (either already in PATH or added).

    Raises:
        RuntimeError: If FFmpeg cannot be found.
    """
    # Check if already available
    if shutil.which("ffmpeg"):
        return True

    # Find FFmpeg
    ffmpeg_path = find_ffmpeg()
    if ffmpeg_path is None:
        raise RuntimeError(
            "FFmpeg not found. Please install FFmpeg and either:\n"
            "1. Add it to your PATH, or\n"
            "2. Set the FFMPEG_PATH environment variable, or\n"
            "3. Install via: winget install Gyan.FFmpeg (Windows) or brew install ffmpeg (macOS)"
        )

    # Add to PATH
    os.environ["PATH"] = str(ffmpeg_path) + os.pathsep + os.environ.get("PATH", "")

    # Verify it works now
    if shutil.which("ffmpeg"):
        return True

    raise RuntimeError(
        f"FFmpeg found at {ffmpeg_path} but still not accessible after adding to PATH"
    )


def get_ffmpeg_version() -> Optional[str]:
    """Get FFmpeg version string if available."""
    import subprocess

    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            # First line typically contains version info
            first_line = result.stdout.split("\n")[0]
            return first_line
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass

    return None


# Auto-setup on module import
try:
    setup_ffmpeg()
except RuntimeError as e:
    # Log warning but don't fail import - let the actual transcription fail if needed
    import warnings

    warnings.warn(str(e), RuntimeWarning)
