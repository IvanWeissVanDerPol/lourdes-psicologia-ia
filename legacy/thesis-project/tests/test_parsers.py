#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Markdown Parser

Tests unitarios para el módulo de parseo de Markdown.
"""

import pytest
from src.core.parsers.markdown_parser import MarkdownParser, ElementType
from src.core.parsers.inline_formatter import InlineFormatter


class TestMarkdownParser:
    """Tests para MarkdownParser"""

    @pytest.fixture
    def parser(self):
        return MarkdownParser()

    def test_parse_heading_1(self, parser):
        """Test: parsear heading nivel 1"""
        content = "# Título Principal"
        elements = parser.parse_content(content)

        assert len(elements) == 1
        assert elements[0].type == ElementType.HEADING_1
        assert "Título Principal" in elements[0].content

    def test_parse_all_heading_levels(self, parser):
        """Test: parsear todos los niveles de heading"""
        content = """# Nivel 1
## Nivel 2
### Nivel 3
#### Nivel 4
##### Nivel 5"""

        elements = parser.parse_content(content)

        assert len(elements) == 5
        assert elements[0].type == ElementType.HEADING_1
        assert elements[1].type == ElementType.HEADING_2
        assert elements[2].type == ElementType.HEADING_3
        assert elements[3].type == ElementType.HEADING_4
        assert elements[4].type == ElementType.HEADING_5

    def test_parse_paragraph(self, parser):
        """Test: parsear párrafo normal"""
        content = "Este es un párrafo normal."
        elements = parser.parse_content(content)

        assert len(elements) == 1
        assert elements[0].type == ElementType.PARAGRAPH

    def test_parse_bullet_list(self, parser):
        """Test: parsear lista con bullets"""
        content = """- Item 1
- Item 2
- Item 3"""

        elements = parser.parse_content(content)

        assert len(elements) == 3
        assert all(e.type == ElementType.LIST_BULLET for e in elements)

    def test_parse_numbered_list(self, parser):
        """Test: parsear lista numerada"""
        content = """1. Primero
2. Segundo
3. Tercero"""

        elements = parser.parse_content(content)

        assert len(elements) == 3
        assert all(e.type == ElementType.LIST_NUMBERED for e in elements)

    def test_parse_blockquote(self, parser):
        """Test: parsear blockquote"""
        content = "> Esta es una cita"
        elements = parser.parse_content(content)

        assert len(elements) == 1
        assert elements[0].type == ElementType.BLOCKQUOTE

    def test_empty_content(self, parser):
        """Test: contenido vacío"""
        elements = parser.parse_content("")
        assert len(elements) == 0


class TestInlineFormatter:
    """Tests para InlineFormatter"""

    def test_parse_bold(self):
        """Test: parsear texto en negrita"""
        parts = InlineFormatter.parse("Texto **negrita** normal")

        assert len(parts) == 3
        assert parts[0].text == "Texto "
        assert parts[1].text == "negrita"
        assert parts[1].bold == True
        assert parts[2].text == " normal"

    def test_parse_italic(self):
        """Test: parsear texto en cursiva"""
        parts = InlineFormatter.parse("Texto *cursiva* normal")

        assert len(parts) == 3
        assert parts[1].text == "cursiva"
        assert parts[1].italic == True

    def test_parse_bold_italic(self):
        """Test: parsear texto negrita y cursiva"""
        parts = InlineFormatter.parse("***negrita cursiva***")

        assert len(parts) == 1
        assert parts[0].bold == True
        assert parts[0].italic == True

    def test_parse_code(self):
        """Test: parsear código inline"""
        parts = InlineFormatter.parse("Función `print()`")

        assert len(parts) == 2
        assert parts[1].text == "print()"
        assert parts[1].code == True

    def test_has_formatting(self):
        """Test: detectar si texto tiene formato"""
        assert InlineFormatter.has_formatting("Texto **bold**") == True
        assert InlineFormatter.has_formatting("Texto normal") == False
