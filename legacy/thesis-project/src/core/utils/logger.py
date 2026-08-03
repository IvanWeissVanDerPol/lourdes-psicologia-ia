#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Professional Logging System for APA 7 Converter

Este módulo proporciona un sistema de logging profesional con múltiples
niveles, handlers, y formateo adecuado.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional


class ColoredFormatter(logging.Formatter):
    """
    Formatter con colores para consola (compatible con Windows via colorama)
    """

    # Colores ANSI
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[32m',      # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
        'RESET': '\033[0m'       # Reset
    }

    def format(self, record):
        # Agregar color al nivel
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{self.COLORS['RESET']}"

        return super().format(record)


class APAConverterLogger:
    """
    Sistema de logging profesional para APA Converter

    Proporciona logging a consola y archivo con diferentes niveles
    y formatos.
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self._loggers = {}

    @staticmethod
    def setup_logger(
        name: str = 'apa_converter',
        level: str = 'INFO',
        log_to_file: bool = False,
        log_dir: Optional[Path] = None,
        use_colors: bool = True
    ) -> logging.Logger:
        """
        Configurar un logger

        Args:
            name: Nombre del logger
            level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_to_file: Si se debe guardar en archivo
            log_dir: Directorio para archivos de log
            use_colors: Si usar colores en consola

        Returns:
            Logger configurado

        Example:
            >>> logger = APAConverterLogger.setup_logger('apa_converter', 'DEBUG')
            >>> logger.info("Iniciando conversión")
        """
        logger = logging.getLogger(name)

        # Si ya tiene handlers, no agregar más
        if logger.handlers:
            return logger

        logger.setLevel(getattr(logging, level.upper()))

        # Handler para consola
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        if use_colors:
            try:
                # Intentar usar colores (requiere colorama en Windows)
                import colorama
                colorama.init()
                console_formatter = ColoredFormatter(
                    '%(levelname)s - %(message)s'
                )
            except ImportError:
                # Si no hay colorama, usar formato simple
                console_formatter = logging.Formatter(
                    '%(levelname)s - %(message)s'
                )
        else:
            console_formatter = logging.Formatter(
                '%(levelname)s - %(message)s'
            )

        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # Handler para archivo (opcional)
        if log_to_file:
            if log_dir is None:
                log_dir = Path.cwd() / 'logs'

            log_dir = Path(log_dir)
            log_dir.mkdir(exist_ok=True, parents=True)

            log_file = log_dir / f"apa_converter_{datetime.now():%Y%m%d_%H%M%S}.log"
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)

            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            logger.info(f"Log file created: {log_file}")

        return logger

    @staticmethod
    def get_logger(name: str = 'apa_converter') -> logging.Logger:
        """
        Obtener logger existente o crear uno nuevo con configuración por defecto

        Args:
            name: Nombre del logger

        Returns:
            Logger

        Example:
            >>> logger = APAConverterLogger.get_logger(__name__)
            >>> logger.debug("Debug message")
        """
        logger = logging.getLogger(name)

        # Si no tiene handlers, configurar con defaults
        if not logger.handlers:
            APAConverterLogger.setup_logger(name)

        return logger


# Logger por defecto
def get_logger(name: str = __name__) -> logging.Logger:
    """
    Función de conveniencia para obtener logger

    Args:
        name: Nombre del logger (usar __name__ del módulo)

    Returns:
        Logger configurado

    Example:
        >>> from src.core.utils.logger import get_logger
        >>> logger = get_logger(__name__)
        >>> logger.info("Starting process")
    """
    return APAConverterLogger.get_logger(name)
