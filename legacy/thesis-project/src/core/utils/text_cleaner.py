#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text Cleaner - Utilidades para limpiar y normalizar texto

Este módulo proporciona funciones para limpiar y normalizar texto,
corrigiendo problemas de encoding y eliminando caracteres no deseados.
"""

import re
from typing import Dict


class TextCleaner:
    """
    Limpiador y normalizador de texto

    Corrige problemas comunes de encoding y formato en texto
    que puede causar problemas en la conversión.
    """

    # Mapeo de caracteres mal codificados a sus equivalentes correctos
    ENCODING_FIXES: Dict[str, str] = {
        'Ã³': 'ó',
        'Ã±': 'ñ',
        'Ã©': 'é',
        'Ã¡': 'á',
        'Ã­': 'í',
        'Ãº': 'ú',
        'Ã‰': 'É',
        'Â¿': '¿',
        'Â¡': '¡',
    }

    # Emojis y símbolos a eliminar
    SYMBOLS_TO_REMOVE = r'[📊📄📚⭐✅❌🎯🔍💡🚀📝📦🏗️🧪⚙️🔌🔄✓📈🤝📬📋🎓🐛]'

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Limpiar texto completo (encoding + símbolos)

        Args:
            text: Texto a limpiar

        Returns:
            Texto limpio

        Example:
            >>> cleaner = TextCleaner()
            >>> cleaner.clean_text("Texto con Ã³ y 📊")
            'Texto con ó y '
        """
        text = TextCleaner.fix_encoding(text)
        text = TextCleaner.remove_symbols(text)
        return text

    @staticmethod
    def fix_encoding(text: str) -> str:
        """
        Corregir problemas de encoding

        Args:
            text: Texto con posibles problemas de encoding

        Returns:
            Texto con encoding corregido

        Example:
            >>> TextCleaner.fix_encoding("CreaciÃ³n")
            'Creación'
        """
        for wrong, correct in TextCleaner.ENCODING_FIXES.items():
            text = text.replace(wrong, correct)
        return text

    @staticmethod
    def remove_symbols(text: str) -> str:
        """
        Eliminar emojis y símbolos especiales

        Args:
            text: Texto con posibles emojis

        Returns:
            Texto sin emojis

        Example:
            >>> TextCleaner.remove_symbols("Título 📊 importante")
            'Título  importante'
        """
        return re.sub(TextCleaner.SYMBOLS_TO_REMOVE, '', text)

    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """
        Normalizar espacios en blanco

        - Convierte múltiples espacios a uno solo
        - Elimina espacios al inicio y final
        - Normaliza saltos de línea

        Args:
            text: Texto a normalizar

        Returns:
            Texto con espacios normalizados

        Example:
            >>> TextCleaner.normalize_whitespace("  Texto   con   espacios  ")
            'Texto con espacios'
        """
        # Eliminar espacios múltiples
        text = re.sub(r' +', ' ', text)
        # Eliminar espacios al inicio/final
        text = text.strip()
        # Normalizar saltos de línea múltiples
        text = re.sub(r'\n\n+', '\n\n', text)
        return text

    @staticmethod
    def remove_markdown_artifacts(text: str) -> str:
        """
        Eliminar artefactos de Markdown que no se quieren en el texto final

        Args:
            text: Texto con posibles artefactos

        Returns:
            Texto limpio

        Example:
            >>> TextCleaner.remove_markdown_artifacts("Texto con `código`")
            'Texto con código'
        """
        # Eliminar backslashes de escape
        text = text.replace('\\*', '*')
        text = text.replace('\\[', '[')
        text = text.replace('\\]', ']')
        text = text.replace('\\(', '(')
        text = text.replace('\\)', ')')

        return text

    @staticmethod
    def clean_for_filename(text: str, max_length: int = 100) -> str:
        """
        Limpiar texto para usarlo como nombre de archivo

        Args:
            text: Texto a limpiar
            max_length: Longitud máxima del nombre

        Returns:
            Texto válido como nombre de archivo

        Example:
            >>> TextCleaner.clean_for_filename("Mi Tesis: Parte 1")
            'Mi_Tesis_Parte_1'
        """
        # Reemplazar caracteres no válidos
        text = re.sub(r'[<>:"/\\|?*]', '', text)
        # Reemplazar espacios con guiones bajos
        text = text.replace(' ', '_')
        # Eliminar caracteres especiales
        text = re.sub(r'[^\w\-_\.]', '', text)
        # Truncar si es muy largo
        if len(text) > max_length:
            text = text[:max_length]
        return text
