"""
APA 7 Converter - Convertidor de Markdown a DOCX con formato APA 7
"""

__version__ = "2.0.0"
__author__ = "Claude"
__license__ = "MIT"

from .core.converter import APAConverter
from .config.apa7_config import APAConfig

__all__ = ['APAConverter', 'APAConfig']
