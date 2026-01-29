"""
Transcript Quality Checking

Consolidated quality checking logic extracted from check_quality.py,
retranscribe_bad.py, and retranscribe_turbo.py.

Detects common Whisper transcription issues:
- Asian character hallucinations
- Repetitive patterns
- Too short transcripts
- Punctuation spam
- Language mixing
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class QualityIssue:
    """Represents a quality issue found in a transcript."""

    issue_type: str
    severity: str  # "low", "medium", "high"
    detail: str
    value: Optional[int | float] = None


@dataclass
class QualityReport:
    """Report of quality issues for a transcript."""

    issues: list[QualityIssue] = field(default_factory=list)
    text_length: int = 0
    word_count: int = 0

    @property
    def has_issues(self) -> bool:
        return len(self.issues) > 0

    @property
    def is_usable(self) -> bool:
        """Check if transcript is usable despite issues."""
        high_severity = sum(1 for i in self.issues if i.severity == "high")
        return high_severity == 0

    @property
    def issue_summary(self) -> list[str]:
        """Get a simple list of issue descriptions."""
        return [f"{i.issue_type}:{i.detail}" for i in self.issues]


class QualityChecker:
    """Check transcript quality and identify issues."""

    # Quality thresholds (can be configured)
    MIN_WORDS = 3
    MAX_ASIAN_CHARS = 3
    MAX_ENGLISH_WORDS = 8
    MAX_GIBBERISH_CLUSTERS = 3

    # Asian character ranges for hallucination detection
    ASIAN_CHAR_PATTERN = re.compile(
        r"[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]"
    )

    # Common English words that shouldn't appear frequently in Spanish
    ENGLISH_WORDS_PATTERN = re.compile(
        r"\b(the|and|but|with|for|this|that|what|have|from|are|was|were|been|will|would|could|should)\b",
        re.IGNORECASE,
    )

    # Repetitive phrase pattern (same 15+ char sequence repeated 3+ times)
    REPETITIVE_PHRASE_PATTERN = re.compile(r"(.{15,})\1{2,}")

    # Word repetition pattern (same word 4+ times in a row)
    WORD_REPETITION_PATTERN = re.compile(r"\b(\w+)\s+\1\s+\1\s+\1\b", re.IGNORECASE)

    # Punctuation spam
    PUNCT_SPAM_PATTERN = re.compile(r"\.{5,}|\?{4,}|!{4,}")

    # Consonant clusters unusual for Spanish (gibberish indicator)
    GIBBERISH_PATTERN = re.compile(r"[bcdfghjklmnpqrstvwxyz]{5,}", re.IGNORECASE)

    def check(self, text: str) -> QualityReport:
        """
        Check transcript text for quality issues.

        Args:
            text: The transcript text to check.

        Returns:
            QualityReport with any issues found.
        """
        if not text:
            return QualityReport(
                issues=[QualityIssue("empty", "high", "empty_text")],
                text_length=0,
                word_count=0,
            )

        report = QualityReport(
            text_length=len(text),
            word_count=len(text.split()),
        )

        # 1. Check for Asian characters (Whisper hallucination)
        asian_chars = len(self.ASIAN_CHAR_PATTERN.findall(text))
        if asian_chars > self.MAX_ASIAN_CHARS:
            report.issues.append(
                QualityIssue(
                    "asian_chars",
                    "high",
                    f"{asian_chars} chars",
                    asian_chars,
                )
            )

        # 2. Check for too short
        if report.word_count < self.MIN_WORDS:
            report.issues.append(
                QualityIssue(
                    "too_short",
                    "medium",
                    f"{report.word_count}w",
                    report.word_count,
                )
            )

        # 3. Check for repetitive phrases
        if self.REPETITIVE_PHRASE_PATTERN.search(text):
            report.issues.append(
                QualityIssue("repetitive_phrase", "high", "repeated_15+_chars")
            )

        # 4. Check for word repetition
        if self.WORD_REPETITION_PATTERN.search(text):
            report.issues.append(
                QualityIssue("word_repetition", "medium", "word_4x")
            )

        # 5. Check for punctuation spam
        if self.PUNCT_SPAM_PATTERN.search(text):
            report.issues.append(
                QualityIssue("punct_spam", "medium", "excessive_punctuation")
            )

        # 6. Check for high English content in Spanish audio
        english_words = len(self.ENGLISH_WORDS_PATTERN.findall(text))
        if english_words > self.MAX_ENGLISH_WORDS:
            report.issues.append(
                QualityIssue(
                    "english_mix",
                    "low",
                    f"{english_words} words",
                    english_words,
                )
            )

        # 7. Check for gibberish (unusual consonant clusters)
        gibberish_count = len(self.GIBBERISH_PATTERN.findall(text))
        if gibberish_count > self.MAX_GIBBERISH_CLUSTERS:
            report.issues.append(
                QualityIssue(
                    "gibberish",
                    "medium",
                    f"{gibberish_count} clusters",
                    gibberish_count,
                )
            )

        return report


# Convenience function for backward compatibility
def check_quality(text: str) -> list[str]:
    """
    Check transcript quality and return list of issue strings.

    This is a simplified interface for backward compatibility with existing scripts.

    Args:
        text: The transcript text to check.

    Returns:
        List of issue strings in format "issue_type:detail"
    """
    checker = QualityChecker()
    report = checker.check(text)
    return report.issue_summary


def is_clean_transcript(text: str) -> bool:
    """
    Check if a transcript is clean enough to use.

    Args:
        text: The transcript text to check.

    Returns:
        True if the transcript is usable.
    """
    if not text or len(text) < 30:
        return False

    checker = QualityChecker()
    report = checker.check(text)
    return report.is_usable


# Issue descriptions for reports
ISSUE_DESCRIPTIONS = {
    "asian_chars": "Korean/Chinese/Japanese characters (Whisper hallucination)",
    "too_short": "Less than 3 words",
    "repetitive_phrase": "Same phrase repeated 3+ times",
    "word_repetition": "Same word 4+ times in a row",
    "punct_spam": "Excessive punctuation",
    "english_mix": "Many English words in Spanish audio",
    "gibberish": "Unusual consonant clusters (nonsense)",
    "empty": "Empty or no text",
}
