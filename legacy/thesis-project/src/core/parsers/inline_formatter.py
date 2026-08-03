#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inline Formatter - Procesa formato inline (negrita, cursiva, código)

Este módulo maneja el formato inline de Markdown como **negrita**,
*cursiva*, `código`, etc.
"""

import re
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class InlineFormat:
    """Representa un fragmento de texto con formato"""
    text: str
    bold: bool = False
    italic: bool = False
    code: bool = False


class InlineFormatter:
    """
    Procesa formato inline de Markdown

    Convierte marcadores de Markdown (**bold**, *italic*, `code`)
    en objetos InlineFormat que pueden ser aplicados al DOCX.
    """

    # Patrón para detectar formato inline
    # Captura: ***text***, **text**, *text*, `text`
    INLINE_PATTERN = r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*|`.*?`)'

    @staticmethod
    def parse(text: str) -> List[InlineFormat]:
        """
        Parse texto con formato inline

        Args:
            text: Texto con marcadores de Markdown

        Returns:
            Lista de fragmentos con formato

        Example:
            >>> formatter = InlineFormatter()
            >>> parts = formatter.parse("Texto **negrita** y *cursiva*")
            >>> len(parts)
            4
            >>> parts[1].bold
            True
        """
        parts = re.split(InlineFormatter.INLINE_PATTERN, text)
        result = []

        for part in parts:
            if not part:
                continue

            formatted = InlineFormatter._parse_part(part)
            if formatted.text:  # Solo agregar si hay texto
                result.append(formatted)

        return result

    @staticmethod
    def _parse_part(part: str) -> InlineFormat:
        """
        Parse un fragmento individual

        Args:
            part: Fragmento de texto

        Returns:
            InlineFormat con el formato aplicado
        """
        # Negrita + Cursiva (***text***)
        if part.startswith('***') and part.endswith('***') and len(part) > 6:
            return InlineFormat(
                text=part[3:-3],
                bold=True,
                italic=True
            )

        # Negrita (**text**)
        elif part.startswith('**') and part.endswith('**') and len(part) > 4:
            return InlineFormat(
                text=part[2:-2],
                bold=True
            )

        # Cursiva (*text*)
        elif part.startswith('*') and part.endswith('*') and len(part) > 2 and not part.startswith('**'):
            return InlineFormat(
                text=part[1:-1],
                italic=True
            )

        # Código (`text`)
        elif part.startswith('`') and part.endswith('`'):
            return InlineFormat(
                text=part[1:-1],
                code=True
            )

        # Texto normal
        else:
            return InlineFormat(text=part)

    @staticmethod
    def has_formatting(text: str) -> bool:
        """
        Verifica si el texto contiene formato inline

        Args:
            text: Texto a verificar

        Returns:
            True si contiene formato, False en caso contrario

        Example:
            >>> InlineFormatter.has_formatting("Texto normal")
            False
            >>> InlineFormatter.has_formatting("Texto **negrita**")
            True
        """
        return bool(re.search(InlineFormatter.INLINE_PATTERN, text))
