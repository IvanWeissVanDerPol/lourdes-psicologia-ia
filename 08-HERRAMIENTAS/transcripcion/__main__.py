"""
Allow running the transcription module as: python -m transcription
"""

from transcription.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
