#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo básico de uso del APA 7 Converter

Este ejemplo muestra cómo usar el convertidor de forma programática.
"""

from pathlib import Path
from src.core.converter import APAConverter

def main():
    # Ejemplo 1: Uso básico con configuración por defecto (estudiante)
    print("="*60)
    print("EJEMPLO 1: Conversión básica (estudiante)")
    print("="*60)

    converter = APAConverter.from_defaults('student')

    converter.convert(
        input_path=Path('tests/fixtures/sample_simple.md'),
        output_path=Path('ejemplo_basico.docx'),
        metadata={
            'title': 'Ejemplo de Documento Estudiantil',
            'author': 'Juan Pérez',
            'institution': 'Universidad Nacional',
            'course': 'Psicología 401',
            'instructor': 'Dr. María González',
            'date': 'Octubre 2025'
        }
    )

    print("\n✓ Documento creado: ejemplo_basico.docx\n")


    # Ejemplo 2: Documento profesional
    print("="*60)
    print("EJEMPLO 2: Documento profesional con running head")
    print("="*60)

    converter_prof = APAConverter.from_defaults('professional')

    converter_prof.convert(
        input_path=Path('tests/fixtures/sample_simple.md'),
        output_path=Path('ejemplo_profesional.docx'),
        metadata={
            'title': 'Efectividad de Intervención en TDA',
            'author': 'Dr. Juan Pérez',
            'institution': 'Universidad Nacional de Psicología',
            'running_head': 'INTERVENCIÓN TDA'
        }
    )

    print("\n✓ Documento creado: ejemplo_profesional.docx\n")


    # Ejemplo 3: Con configuración personalizada
    print("="*60)
    print("EJEMPLO 3: Con configuración YAML personalizada")
    print("="*60)

    # Crear configuración personalizada (si existe)
    config_path = Path('config/apa7_student.yaml')
    if config_path.exists():
        converter_custom = APAConverter.from_yaml(config_path)

        converter_custom.convert(
            input_path=Path('tests/fixtures/sample_with_table.md'),
            output_path=Path('ejemplo_custom.docx'),
            metadata={
                'title': 'Documento con Configuración Personalizada',
                'author': 'Ana López'
            }
        )

        print("\n✓ Documento creado: ejemplo_custom.docx\n")
    else:
        print(f"\n⚠ Config no encontrado: {config_path}\n")


if __name__ == '__main__':
    main()
