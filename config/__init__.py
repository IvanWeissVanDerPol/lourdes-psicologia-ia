"""
Configuration package for LourdesBusiness.

Usage:
    from config import settings

    # Access configuration
    data_dir = settings.DATA_DIR
    patients_dir = settings.PATIENTS_DIR
"""

from config.settings import settings, Settings

__all__ = ["settings", "Settings"]
