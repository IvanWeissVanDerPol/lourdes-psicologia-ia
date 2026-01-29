"""
Command Line Interface for Transcription System

Unified CLI that replaces all individual transcription scripts.

Usage:
    python -m transcripcion --help
    python -m transcripcion transcribe --input /path/to/audio
    python -m transcripcion check-quality --input /path/to/transcripts
    python -m transcripcion retranscribe --model small
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from transcription.config import TranscriptionConfig
from transcription.batch_processor import BatchProcessor, process_chat
from transcription.quality import QualityChecker, ISSUE_DESCRIPTIONS
from transcription.transcriber import (
    TranscriptResult,
    Transcriber,
    load_existing_transcripts,
    save_transcripts,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def cmd_transcribe(args: argparse.Namespace) -> int:
    """Transcribe audio files."""
    config = TranscriptionConfig()

    # Determine source directory
    if args.input:
        source_dir = Path(args.input)
    elif args.patient:
        source_dir = config.get_raw_dir(args.patient)
    else:
        print("Error: Either --input or --patient is required")
        return 1

    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        return 1

    # Find chat directories or process directly
    if args.chat:
        # Process specific chat subdirectory
        chat_dirs = [
            d
            for d in source_dir.iterdir()
            if d.is_dir() and args.chat.lower() in d.name.lower()
        ]
        if not chat_dirs:
            print(f"Error: No chat matching '{args.chat}' found in {source_dir}")
            return 1
    else:
        # Process all subdirectories or the directory itself
        subdirs = [d for d in source_dir.iterdir() if d.is_dir()]
        chat_dirs = subdirs if subdirs else [source_dir]

    # Determine output directory
    if args.output:
        base_output = Path(args.output)
    elif args.patient:
        base_output = config.get_transcripts_dir(args.patient)
    else:
        base_output = source_dir.parent / "transcripts"

    print(f"{'=' * 60}")
    print("VOICE NOTE TRANSCRIPTION")
    print(f"Model: {args.model} | Language: {args.language} | Workers: {args.workers}")
    print(f"{'=' * 60}")

    total_files = 0
    total_errors = 0

    for chat_dir in chat_dirs:
        chat_name = chat_dir.name
        output_dir = base_output / chat_name if len(chat_dirs) > 1 else base_output

        print(f"\nProcessing: {chat_name}")

        def progress_callback(completed: int, total: int, result: TranscriptResult):
            nonlocal total_errors
            if not result.success:
                total_errors += 1
            if completed % args.batch_size == 0 or completed == total:
                pct = 100 * completed / total
                print(f"  Progress: {completed}/{total} ({pct:.1f}%)")

        results = process_chat(
            source_dir=chat_dir,
            output_dir=output_dir,
            chat_name=chat_name,
            model=args.model,
            language=args.language,
            workers=args.workers,
            resume=args.resume,
            progress_callback=progress_callback,
        )

        total_files += len(results)
        print(f"  Completed: {len(results)} files")

    print(f"\n{'=' * 60}")
    print(f"COMPLETE: {total_files} files ({total_errors} errors)")
    print(f"Output: {base_output}")

    return 0


def cmd_check_quality(args: argparse.Namespace) -> int:
    """Check transcript quality and report issues."""
    config = TranscriptionConfig()

    # Determine transcripts directory
    if args.input:
        transcripts_dir = Path(args.input)
    elif args.patient:
        transcripts_dir = config.get_transcripts_dir(args.patient)
    else:
        print("Error: Either --input or --patient is required")
        return 1

    if not transcripts_dir.exists():
        print(f"Error: Transcripts directory not found: {transcripts_dir}")
        return 1

    checker = QualityChecker()
    all_issues: list[dict] = []
    total_checked = 0

    # Find all transcript JSON files
    json_files = list(transcripts_dir.rglob("transcripts.json"))
    if not json_files:
        print(f"No transcripts.json files found in {transcripts_dir}")
        return 1

    for json_path in json_files:
        chat_name = json_path.parent.name
        existing = load_existing_transcripts(json_path)

        for filename, result in existing.items():
            if not result.success or not result.text:
                continue

            total_checked += 1
            report = checker.check(result.text)

            if report.has_issues:
                all_issues.append(
                    {
                        "chat": chat_name,
                        "file": filename,
                        "date": result.date,
                        "problems": report.issue_summary,
                        "text": result.text,
                    }
                )

    # Sort by severity
    all_issues.sort(key=lambda x: (-len(x["problems"]), x["chat"], x["file"]))

    # Print summary
    print(f"\nChecked {total_checked} transcripts")
    print(
        f"Found {len(all_issues)} with quality issues ({100 * len(all_issues) / max(total_checked, 1):.1f}%)"
    )

    if all_issues:
        # Summary by chat
        by_chat = Counter(i["chat"] for i in all_issues)
        print("\nBy chat:")
        for chat, count in by_chat.most_common():
            print(f"  {chat}: {count}")

        # Problem types
        all_problems = []
        for i in all_issues:
            all_problems.extend([p.split(":")[0] for p in i["problems"]])
        problem_counts = Counter(all_problems)

        print("\nProblem types:")
        for prob, count in problem_counts.most_common():
            desc = ISSUE_DESCRIPTIONS.get(prob, "")
            print(f"  {prob}: {count} - {desc}")

    # Write report if requested
    if args.output:
        output_path = Path(args.output)
        _write_quality_report(output_path, all_issues, total_checked)
        print(f"\nReport saved to: {output_path}")

        # Also write simple file list
        list_path = output_path.with_name("RETRANSCRIBE_LIST.txt")
        with open(list_path, "w") as f:
            for issue in all_issues:
                f.write(f"{issue['chat']}/{issue['file']}\n")
        print(f"File list saved to: {list_path}")

    return 0


def _write_quality_report(output_path: Path, issues: list[dict], total_checked: int):
    """Write detailed quality report to markdown file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Transcript Quality Issues\n\n")
        f.write(
            f"> Checked {total_checked} transcripts, found {len(issues)} with issues "
            f"({100 * len(issues) / max(total_checked, 1):.1f}%)\n\n"
        )

        if not issues:
            f.write("No quality issues found!\n")
            return

        # Summary by chat
        by_chat = Counter(i["chat"] for i in issues)
        f.write("## Summary by Chat\n\n")
        f.write("| Chat | Issues | Severe |\n|------|--------|--------|\n")
        for chat, count in by_chat.most_common():
            chat_issues = [i for i in issues if i["chat"] == chat]
            severe = sum(1 for i in chat_issues if len(i["problems"]) > 1)
            f.write(f"| {chat} | {count} | {severe} |\n")

        # Problem types
        all_problems = []
        for i in issues:
            all_problems.extend([p.split(":")[0] for p in i["problems"]])
        problem_counts = Counter(all_problems)

        f.write("\n## Problem Types\n\n")
        f.write(
            "| Problem | Count | Description |\n|---------|-------|-------------|\n"
        )
        for prob, count in problem_counts.most_common():
            desc = ISSUE_DESCRIPTIONS.get(prob, "")
            f.write(f"| {prob} | {count} | {desc} |\n")

        # Files to retranscribe
        f.write("\n---\n\n## Files to Re-transcribe\n\n")

        for chat in sorted(set(i["chat"] for i in issues)):
            chat_issues = [i for i in issues if i["chat"] == chat]
            f.write(f"### {chat} ({len(chat_issues)} files)\n\n```\n")
            for i in chat_issues:
                probs = ", ".join(i["problems"])
                f.write(f"{i['file']}  # {probs}\n")
            f.write("```\n\n")


def cmd_retranscribe(args: argparse.Namespace) -> int:
    """Re-transcribe files with quality issues using a better model."""
    config = TranscriptionConfig()

    # Load issues list
    if args.issues_file:
        issues_path = Path(args.issues_file)
    elif args.patient:
        issues_path = (
            config.get_transcripts_dir(args.patient).parent / "RETRANSCRIBE_LIST.txt"
        )
    else:
        print("Error: Either --issues-file or --patient is required")
        return 1

    if not issues_path.exists():
        print(f"Error: Issues file not found: {issues_path}")
        print("Run 'check-quality' first to generate the issues list")
        return 1

    # Load issues
    issues: dict[str, list[str]] = {}
    with open(issues_path, "r") as f:
        for line in f:
            line = line.strip()
            if "/" in line:
                chat, filename = line.split("/", 1)
                if args.chat and args.chat.lower() not in chat.lower():
                    continue
                issues.setdefault(chat, []).append(filename)

    if not issues:
        print("No issues found to process")
        return 0

    total_files = sum(len(files) for files in issues.values())
    print(f"Found {total_files} files to re-transcribe across {len(issues)} chats")

    # Initialize transcriber
    transcriber = Transcriber(model=args.model, language=args.language, config=config)
    checker = QualityChecker()

    improved = 0
    still_bad = 0

    # Determine source and output directories
    if args.patient:
        source_base = config.get_raw_dir(args.patient)
        output_base = config.get_transcripts_dir(args.patient)
    else:
        # Use current directory structure
        source_base = issues_path.parent.parent / "RAW"
        output_base = issues_path.parent

    for chat_name, files in sorted(issues.items(), key=lambda x: len(x[1])):
        print(f"\n{'=' * 60}")
        print(f"Re-transcribing {chat_name}: {len(files)} files")
        print(f"Model: {args.model}")
        print(f"{'=' * 60}")

        # Find source directory
        source_dir = None
        for d in source_base.iterdir():
            if chat_name.lower() in d.name.lower():
                source_dir = d
                break

        if not source_dir:
            print(f"  Source directory not found for {chat_name}")
            continue

        # Load existing transcripts
        output_dir = output_base / chat_name
        json_path = output_dir / "transcripts.json"
        existing = load_existing_transcripts(json_path)

        for i, filename in enumerate(files):
            filepath = source_dir / filename
            if not filepath.exists():
                print(f"  [{i + 1}/{len(files)}] {filename}: NOT FOUND")
                continue

            old_result = existing.get(filename)
            old_problems = (
                checker.check(old_result.text).issue_summary
                if old_result and old_result.text
                else ["no_previous"]
            )

            # Transcribe
            result = transcriber.transcribe_file(filepath)
            new_problems = (
                checker.check(result.text).issue_summary if result.text else ["failed"]
            )

            # Update if improved
            if len(new_problems) < len(old_problems) or (
                len(new_problems) == 0 and len(old_problems) > 0
            ):
                result.retranscribed = True
                existing[filename] = result
                improved += 1
                status = "IMPROVED" if new_problems else "FIXED"
            else:
                still_bad += 1
                status = "STILL_BAD"

            print(f"  [{i + 1}/{len(files)}] {filename}: {status}")
            print(f"      Old: {old_problems} -> New: {new_problems}")

            # Memory cleanup
            if (i + 1) % 10 == 0:
                transcriber.cleanup_memory()

        # Save updated results
        save_transcripts(output_dir, list(existing.values()), chat_name)

    print(f"\n{'=' * 60}")
    print(f"SUMMARY: {improved} improved, {still_bad} still have issues")
    print(f"Improvement rate: {100 * improved / max(improved + still_bad, 1):.1f}%")

    return 0


def main(argv: list[str] | None = None) -> int:
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        prog="transcription",
        description="Unified Voice Note Transcription System",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Transcribe command
    p_transcribe = subparsers.add_parser("transcribe", help="Transcribe audio files")
    p_transcribe.add_argument("--input", "-i", help="Input directory with audio files")
    p_transcribe.add_argument("--output", "-o", help="Output directory for transcripts")
    p_transcribe.add_argument(
        "--patient", "-p", help="Patient ID (uses configured data paths)"
    )
    p_transcribe.add_argument("--chat", "-c", help="Filter to specific chat")
    p_transcribe.add_argument(
        "--model",
        "-m",
        default="base",
        choices=["tiny", "base", "small", "medium", "large", "turbo"],
        help="Whisper model (default: base)",
    )
    p_transcribe.add_argument(
        "--language", "-l", default="es", help="Language code (default: es)"
    )
    p_transcribe.add_argument(
        "--workers", "-w", type=int, default=4, help="Parallel workers (default: 4)"
    )
    p_transcribe.add_argument(
        "--resume",
        "-r",
        action="store_true",
        default=True,
        help="Skip already transcribed (default: True)",
    )
    p_transcribe.add_argument(
        "--no-resume",
        action="store_false",
        dest="resume",
        help="Don't skip already transcribed",
    )
    p_transcribe.add_argument(
        "--batch-size", type=int, default=50, help="Progress update frequency"
    )

    # Check quality command
    p_quality = subparsers.add_parser("check-quality", help="Check transcript quality")
    p_quality.add_argument("--input", "-i", help="Transcripts directory")
    p_quality.add_argument("--output", "-o", help="Output report path")
    p_quality.add_argument(
        "--patient", "-p", help="Patient ID (uses configured data paths)"
    )

    # Retranscribe command
    p_retrans = subparsers.add_parser(
        "retranscribe", help="Re-transcribe files with quality issues"
    )
    p_retrans.add_argument("--issues-file", "-f", help="Path to RETRANSCRIBE_LIST.txt")
    p_retrans.add_argument(
        "--patient", "-p", help="Patient ID (uses configured data paths)"
    )
    p_retrans.add_argument("--chat", "-c", help="Filter to specific chat")
    p_retrans.add_argument(
        "--model",
        "-m",
        default="small",
        choices=["small", "medium", "large", "turbo"],
        help="Whisper model (default: small)",
    )
    p_retrans.add_argument(
        "--language", "-l", default="es", help="Language code (default: es)"
    )

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "transcribe":
        return cmd_transcribe(args)
    elif args.command == "check-quality":
        return cmd_check_quality(args)
    elif args.command == "retranscribe":
        return cmd_retranscribe(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
