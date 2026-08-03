#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APA 7 Style Definitions

Este módulo define todos los estilos según la 7ª edición del manual APA.
Usa dataclasses inmutables para garantizar consistencia y facilitar testing.

Referencias:
    Publication Manual of the American Psychological Association (7th ed., 2020)
"""

from dataclasses import dataclass, field
from typing import Optional
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


@dataclass(frozen=True)
class APAStyleDefinition:
    """
    Definición inmutable de un estilo APA 7

    Esta clase define todos los parámetros de formato para un estilo específico.
    Es inmutable (frozen=True) para prevenir modificaciones accidentales y
    facilitar el testing.

    Attributes:
        name: Nombre del estilo (debe coincidir con nombre en Word)
        font_name: Nombre de la fuente
        font_size: Tamaño de fuente en puntos
        bold: Si el texto es negrita
        italic: Si el texto es cursiva
        alignment: Alineación del párrafo
        line_spacing: Espaciado entre líneas (2.0 = doble espacio)
        space_before: Espacio antes del párrafo en puntos
        space_after: Espacio después del párrafo en puntos
        first_line_indent: Sangría de primera línea en pulgadas
        left_indent: Sangría izquierda del párrafo en pulgadas
        keep_with_next: Si mantener con siguiente párrafo
    """
    name: str
    font_name: str = 'Times New Roman'
    font_size: Pt = field(default_factory=lambda: Pt(12))
    bold: bool = False
    italic: bool = False
    alignment: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.LEFT
    line_spacing: float = 2.0
    space_before: Pt = field(default_factory=lambda: Pt(0))
    space_after: Pt = field(default_factory=lambda: Pt(0))
    first_line_indent: Inches = field(default_factory=lambda: Inches(0.5))
    left_indent: Inches = field(default_factory=lambda: Inches(0))
    keep_with_next: bool = False


# ===== ESTILO NORMAL (Texto del cuerpo) =====
# Según APA 7:
# - Times New Roman 12pt
# - Doble espacio
# - Sangría primera línea 0.5"
# - Alineación izquierda

APA_NORMAL = APAStyleDefinition(
    name='Normal',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=False,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0.5),
    left_indent=Inches(0),
    keep_with_next=False
)


# ===== ENCABEZADO NIVEL 1 =====
# Según APA 7 (página 47):
# - Centrado
# - Negrita
# - Title Case (Mayúsculas y Minúsculas)
# - Times New Roman 12pt
# - Sin sangría de primera línea

APA_HEADING_1 = APAStyleDefinition(
    name='Heading 1',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=True,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.CENTER,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0),
    keep_with_next=True
)


# ===== ENCABEZADO NIVEL 2 =====
# Según APA 7 (página 47):
# - Alineado a la izquierda
# - Negrita
# - Title Case
# - Times New Roman 12pt
# - Sin sangría de primera línea

APA_HEADING_2 = APAStyleDefinition(
    name='Heading 2',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=True,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0),
    keep_with_next=True
)


# ===== ENCABEZADO NIVEL 3 =====
# Según APA 7 (página 47):
# - Alineado a la izquierda
# - Negrita y Cursiva
# - Title Case
# - Times New Roman 12pt
# - Sin sangría de primera línea

APA_HEADING_3 = APAStyleDefinition(
    name='Heading 3',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=True,
    italic=True,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0),
    keep_with_next=True
)


# ===== ENCABEZADO NIVEL 4 =====
# Según APA 7 (página 47):
# - Sangrado (0.5")
# - Negrita y Cursiva
# - Title Case
# - Termina con punto
# - El texto continúa en la misma línea

APA_HEADING_4 = APAStyleDefinition(
    name='Heading 4',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=True,
    italic=True,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0.5),
    keep_with_next=True
)


# ===== ENCABEZADO NIVEL 5 =====
# Según APA 7 (página 47):
# - Sangrado (0.5")
# - Negrita y Cursiva
# - Sentence case (solo primera letra mayúscula)
# - Termina con punto
# - El texto continúa en la misma línea

APA_HEADING_5 = APAStyleDefinition(
    name='Heading 5',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=True,
    italic=True,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0.5),
    keep_with_next=True
)


# ===== CITAS EN BLOQUE (Block Quote) =====
# Según APA 7 (página 272):
# - Para citas de 40 palabras o más
# - Sangría de 0.5" desde el margen izquierdo
# - Sin comillas
# - Doble espacio
# - Sin sangría adicional de primera línea

APA_QUOTE = APAStyleDefinition(
    name='Quote',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=False,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0.5),
    keep_with_next=False
)


# ===== REFERENCIAS (Sangría francesa) =====
# Según APA 7 (página 303):
# - Sangría francesa (hanging indent) de 0.5"
# - Primera línea alineada al margen
# - Líneas subsiguientes sangradas 0.5"
# - Doble espacio entre y dentro de referencias

APA_REFERENCE = APAStyleDefinition(
    name='Reference',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=False,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(-0.5),  # Negativo para sangría francesa
    left_indent=Inches(0.5),         # Sangría del cuerpo
    keep_with_next=False
)


# ===== RESUMEN/ABSTRACT =====
# Según APA 7 (página 38):
# - Sin sangría de primera línea
# - Doble espacio
# - Alineado a la izquierda
# - 150-250 palabras para estudiantes

APA_ABSTRACT = APAStyleDefinition(
    name='Abstract',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=False,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),  # Sin sangría
    left_indent=Inches(0),
    keep_with_next=False
)


# ===== TÍTULO DE TABLA =====
# Según APA 7 (página 198):
# - Cursiva
# - Sin negrita
# - Alineado a la izquierda
# - Va debajo del número de tabla

APA_TABLE_TITLE = APAStyleDefinition(
    name='Table Title',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=False,
    italic=True,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0),
    keep_with_next=False
)


# ===== NÚMERO DE TABLA =====
# Según APA 7 (página 198):
# - Negrita
# - Sin cursiva
# - Alineado a la izquierda
# - Formato: "Tabla 1"

APA_TABLE_NUMBER = APAStyleDefinition(
    name='Table Number',
    font_name='Times New Roman',
    font_size=Pt(12),
    bold=True,
    italic=False,
    alignment=WD_ALIGN_PARAGRAPH.LEFT,
    line_spacing=2.0,
    space_before=Pt(0),
    space_after=Pt(0),
    first_line_indent=Inches(0),
    left_indent=Inches(0),
    keep_with_next=True
)


# ===== LISTA DE TODOS LOS ESTILOS APA 7 =====
ALL_APA_STYLES = [
    APA_NORMAL,
    APA_HEADING_1,
    APA_HEADING_2,
    APA_HEADING_3,
    APA_HEADING_4,
    APA_HEADING_5,
    APA_QUOTE,
    APA_REFERENCE,
    APA_ABSTRACT,
    APA_TABLE_TITLE,
    APA_TABLE_NUMBER,
]


def get_style_by_name(style_name: str) -> Optional[APAStyleDefinition]:
    """
    Obtiene una definición de estilo por nombre

    Args:
        style_name: Nombre del estilo a buscar

    Returns:
        Definición del estilo o None si no se encuentra

    Example:
        >>> style = get_style_by_name('Heading 1')
        >>> print(style.bold)
        True
    """
    for style in ALL_APA_STYLES:
        if style.name == style_name:
            return style
    return None


def get_heading_style(level: int) -> Optional[APAStyleDefinition]:
    """
    Obtiene el estilo de encabezado por nivel

    Args:
        level: Nivel del encabezado (1-5)

    Returns:
        Definición del estilo o None si el nivel es inválido

    Example:
        >>> style = get_heading_style(1)
        >>> print(style.alignment)
        CENTER (1)
    """
    styles = {
        1: APA_HEADING_1,
        2: APA_HEADING_2,
        3: APA_HEADING_3,
        4: APA_HEADING_4,
        5: APA_HEADING_5,
    }
    return styles.get(level)
