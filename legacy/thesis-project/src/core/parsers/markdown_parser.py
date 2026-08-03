#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown Parser - Parser principal de Markdown a AST

Este módulo implementa el parser principal que convierte Markdown a una
representación abstracta (AST) que luego puede ser convertida a DOCX.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Any
from enum import Enum
import re
import logging

from ..utils.text_cleaner import TextCleaner
from ..utils.exceptions import ParsingError

logger = logging.getLogger(__name__)


class ElementType(Enum):
    """Tipos de elementos Markdown"""
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    HEADING_4 = "heading_4"
    HEADING_5 = "heading_5"
    PARAGRAPH = "paragraph"
    LIST_BULLET = "list_bullet"
    LIST_NUMBERED = "list_numbered"
    TABLE = "table"
    CODE_BLOCK = "code_block"
    BLOCKQUOTE = "blockquote"
    HORIZONTAL_RULE = "horizontal_rule"
    EMPTY = "empty"


@dataclass
class MarkdownElement:
    """
    Representa un elemento parseado del Markdown

    Attributes:
        type: Tipo de elemento
        content: Contenido del elemento (puede ser str, list, dict, etc.)
        line_number: Número de línea en el archivo original
        metadata: Metadatos adicionales
    """
    type: ElementType
    content: Any
    line_number: int
    metadata: dict = field(default_factory=dict)

    def __repr__(self):
        content_preview = str(self.content)[:50] if self.content else ""
        return f"MarkdownElement({self.type.value}, line={self.line_number}, content='{content_preview}...')"


class MarkdownParser:
    """
    Parser principal de Markdown a AST

    Convierte texto Markdown en una lista de MarkdownElement que
    representan la estructura del documento.
    """

    def __init__(self):
        """Inicializar parser"""
        self.text_cleaner = TextCleaner()
        self.current_line = 0
        self.total_lines = 0

    def parse_file(self, file_path: str) -> List[MarkdownElement]:
        """
        Parse un archivo Markdown completo

        Args:
            file_path: Ruta al archivo Markdown

        Returns:
            Lista de elementos parseados

        Raises:
            FileNotFoundError: Si el archivo no existe
            ParsingError: Si hay error parseando el contenido

        Example:
            >>> parser = MarkdownParser()
            >>> elements = parser.parse_file('documento.md')
            >>> len(elements)
            42
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            logger.info(f"Archivo leído: {file_path}")
            return self.parse_content(content)
        except FileNotFoundError as e:
            logger.error(f"Archivo no encontrado: {file_path}")
            raise
        except UnicodeDecodeError as e:
            logger.error(f"Error de encoding en {file_path}: {e}")
            raise ParsingError(f"Error de encoding: {e}")
        except Exception as e:
            logger.error(f"Error inesperado parseando {file_path}: {e}")
            raise ParsingError(f"Error parseando archivo: {e}")

    def parse_content(self, content: str) -> List[MarkdownElement]:
        """
        Parse contenido Markdown a lista de elementos

        Args:
            content: Contenido Markdown como string

        Returns:
            Lista de elementos parseados

        Example:
            >>> parser = MarkdownParser()
            >>> elements = parser.parse_content("# Título\\n\\nPárrafo")
            >>> len(elements)
            2
        """
        lines = content.split('\n')
        self.total_lines = len(lines)
        elements = []

        i = 0
        while i < len(lines):
            self.current_line = i + 1

            if self.current_line % 1000 == 0:
                logger.debug(f"Procesando línea {self.current_line}/{self.total_lines}")

            line = lines[i]

            # Parse la línea
            element, lines_consumed = self._parse_line(line, lines, i)

            if element:
                elements.append(element)

            i += lines_consumed

        logger.info(f"Parseados {len(elements)} elementos de {self.total_lines} líneas")
        return elements

    def _parse_line(self, line: str, all_lines: List[str], current_index: int) -> tuple:
        """
        Determina el tipo de elemento y lo parsea

        Args:
            line: Línea actual
            all_lines: Todas las líneas del documento
            current_index: Índice de la línea actual

        Returns:
            Tupla (elemento, líneas_consumidas)
        """
        stripped = line.strip()

        # Línea vacía
        if not stripped:
            return None, 1

        # Bloques de código (```...```)
        if stripped.startswith('```'):
            return self._parse_code_block(all_lines, current_index)

        # Tablas (|...|)
        if '|' in stripped and stripped.startswith('|'):
            return self._parse_table(all_lines, current_index)

        # Headings (#, ##, ###, etc.)
        if stripped.startswith('#'):
            return self._parse_heading(stripped), 1

        # Listas con bullets (-, *, +)
        if re.match(r'^[\-\*\+]\s+', stripped):
            return self._parse_bullet_list(stripped), 1

        # Listas numeradas (1., 2., etc.)
        if re.match(r'^\d+\.\s+', stripped):
            return self._parse_numbered_list(stripped), 1

        # Blockquotes (>)
        if stripped.startswith('>'):
            return self._parse_blockquote(stripped), 1

        # Separadores horizontales (---, ***, ___)
        if stripped in ['---', '___', '***']:
            return self._parse_horizontal_rule(stripped), 1

        # Párrafo normal
        return self._parse_paragraph(line), 1

    def _parse_heading(self, line: str) -> MarkdownElement:
        """Parse un heading (#, ##, ###, etc.)"""
        # Contar número de #
        level = len(line) - len(line.lstrip('#'))
        level = min(level, 5)  # Máximo 5 niveles en APA 7

        # Extraer texto
        text = line.lstrip('#').strip()
        text = self.text_cleaner.clean_text(text)

        element_type = {
            1: ElementType.HEADING_1,
            2: ElementType.HEADING_2,
            3: ElementType.HEADING_3,
            4: ElementType.HEADING_4,
            5: ElementType.HEADING_5
        }[level]

        return MarkdownElement(
            type=element_type,
            content=text,
            line_number=self.current_line,
            metadata={'level': level}
        )

    def _parse_paragraph(self, line: str) -> MarkdownElement:
        """Parse un párrafo normal"""
        text = self.text_cleaner.clean_text(line)

        return MarkdownElement(
            type=ElementType.PARAGRAPH,
            content=text,
            line_number=self.current_line
        )

    def _parse_bullet_list(self, line: str) -> MarkdownElement:
        """Parse un item de lista con bullet"""
        # Eliminar bullet y espacios
        text = re.sub(r'^[\-\*\+]\s+', '', line.strip())
        text = self.text_cleaner.clean_text(text)

        return MarkdownElement(
            type=ElementType.LIST_BULLET,
            content=text,
            line_number=self.current_line
        )

    def _parse_numbered_list(self, line: str) -> MarkdownElement:
        """Parse un item de lista numerada"""
        # Extraer número y texto
        match = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
        if match:
            number = int(match.group(1))
            text = match.group(2)
            text = self.text_cleaner.clean_text(text)

            return MarkdownElement(
                type=ElementType.LIST_NUMBERED,
                content=text,
                line_number=self.current_line,
                metadata={'number': number}
            )

        # Fallback
        text = re.sub(r'^\d+\.\s+', '', line.strip())
        text = self.text_cleaner.clean_text(text)

        return MarkdownElement(
            type=ElementType.LIST_NUMBERED,
            content=text,
            line_number=self.current_line
        )

    def _parse_blockquote(self, line: str) -> MarkdownElement:
        """Parse un blockquote (>)"""
        text = line.strip()[1:].strip()  # Eliminar '>'
        text = self.text_cleaner.clean_text(text)

        return MarkdownElement(
            type=ElementType.BLOCKQUOTE,
            content=text,
            line_number=self.current_line
        )

    def _parse_horizontal_rule(self, line: str) -> MarkdownElement:
        """Parse un separador horizontal"""
        return MarkdownElement(
            type=ElementType.HORIZONTAL_RULE,
            content='',
            line_number=self.current_line
        )

    def _parse_code_block(self, lines: List[str], start_index: int) -> tuple:
        """Parse un bloque de código (```...```)"""
        code_lines = []
        current = start_index + 1  # Saltar la línea de apertura ```

        # Extraer lenguaje si existe (```python)
        language = lines[start_index].strip()[3:].strip()

        # Leer hasta encontrar el cierre ```
        while current < len(lines):
            if lines[current].strip().startswith('```'):
                # Encontrado cierre
                break
            code_lines.append(lines[current])
            current += 1

        lines_consumed = (current - start_index) + 1

        content = '\n'.join(code_lines)

        return MarkdownElement(
            type=ElementType.CODE_BLOCK,
            content=content,
            line_number=self.current_line,
            metadata={'language': language}
        ), lines_consumed

    def _parse_table(self, lines: List[str], start_index: int) -> tuple:
        """Parse una tabla (|...|)"""
        rows = []
        current = start_index

        # Leer todas las líneas de la tabla
        while current < len(lines) and '|' in lines[current]:
            line = lines[current].strip()

            # Detectar línea separadora (|---|---|)
            if self._is_table_separator(line):
                current += 1
                continue

            # Parsear fila
            cells = self._parse_table_row(line)
            if cells:
                rows.append(cells)

            current += 1

        lines_consumed = current - start_index

        return MarkdownElement(
            type=ElementType.TABLE,
            content=rows,
            line_number=self.current_line,
            metadata={
                'rows': len(rows),
                'cols': len(rows[0]) if rows else 0
            }
        ), lines_consumed

    def _parse_table_row(self, line: str) -> List[str]:
        """Parse una fila de tabla"""
        # Quitar | iniciales y finales
        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]

        # Separar celdas
        cells = [self.text_cleaner.clean_text(cell.strip()) for cell in line.split('|')]
        return cells

    def _is_table_separator(self, line: str) -> bool:
        """Detecta si es línea separadora de tabla (|---|---|)"""
        cells = line.split('|')[1:-1]  # Eliminar primero y último vacío
        return all(re.match(r'^-+$', cell.strip()) for cell in cells if cell.strip())
