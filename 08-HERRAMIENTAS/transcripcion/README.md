# Transcription Module

Unified voice note transcription system using OpenAI Whisper.

## Features

- **Single file transcription**: Transcribe individual audio files
- **Batch processing**: Process entire directories with parallel workers
- **Quality checking**: Detect and report transcription issues
- **Re-transcription**: Fix problematic transcripts with better models
- **Resume support**: Continue interrupted transcription sessions

## Installation

```bash
# Install dependencies
pip install openai-whisper torch

# Ensure FFmpeg is installed
winget install Gyan.FFmpeg  # Windows
brew install ffmpeg         # macOS
```

## Usage

### Command Line

```bash
# Transcribe audio files
python -m transcription transcribe --input /path/to/audio --model base

# Check transcript quality
python -m transcription check-quality --input /path/to/transcripts

# Re-transcribe problematic files
python -m transcription retranscribe --model small

# Show help
python -m transcription --help
```

### As Library

```python
from transcription import Transcriber, QualityChecker

# Transcribe a file
transcriber = Transcriber(model="base", language="es")
result = transcriber.transcribe_file("audio.opus")
print(result.text)

# Check quality
checker = QualityChecker()
report = checker.check(result.text)
if report.has_issues:
    print(f"Issues: {report.issue_summary}")
```

## Configuration

Set environment variables for customization:

```bash
# Data directory (outside git repo)
export LOURDES_DATA_DIR=/path/to/data

# Whisper settings
export WHISPER_MODEL=base
export WHISPER_LANGUAGE=es

# FFmpeg path (if not in PATH)
export FFMPEG_PATH=/path/to/ffmpeg/bin
```

## Quality Issues Detected

| Issue | Description |
|-------|-------------|
| `asian_chars` | Korean/Chinese/Japanese characters (hallucination) |
| `too_short` | Less than 3 words |
| `repetitive_phrase` | Same phrase repeated 3+ times |
| `word_repetition` | Same word 4+ times in a row |
| `punct_spam` | Excessive punctuation |
| `english_mix` | Many English words in Spanish audio |
| `gibberish` | Unusual consonant clusters |

## Models

| Model | Speed | Quality | VRAM |
|-------|-------|---------|------|
| `tiny` | Fastest | Basic | ~1GB |
| `base` | Fast | Good | ~1GB |
| `small` | Medium | Better | ~2GB |
| `medium` | Slow | Great | ~5GB |
| `large` | Slowest | Best | ~10GB |
| `turbo` | Fast | Great | ~6GB |

## File Structure

```
transcription/
├── __init__.py        # Package exports
├── __main__.py        # Module entry point
├── cli.py             # Command line interface
├── config.py          # Configuration management
├── ffmpeg_setup.py    # FFmpeg path handling
├── quality.py         # Quality checking
├── transcriber.py     # Core transcription
├── batch_processor.py # Parallel processing
└── README.md          # This file
```
