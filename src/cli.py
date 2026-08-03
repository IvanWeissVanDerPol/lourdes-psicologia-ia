#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI Interface for APA 7 Converter

Interfaz de línea de comandos profesional usando Click.
"""

import click
from pathlib import Path
import sys
import logging

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from .core.converter import APAConverter
from .config.apa7_config import APAConfig
from .core.utils.logger import APAConverterLogger
from .core.utils.exceptions import APAConverterError


@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Modo verbose (DEBUG)')
@click.option('--quiet', '-q', is_flag=True, help='Modo silencioso (solo errores)')
@click.option('--log-file', type=click.Path(), help='Guardar logs en archivo')
@click.version_option(version='2.0.0', prog_name='apa-converter')
@click.pass_context
def cli(ctx, verbose, quiet, log_file):
    """
    APA 7 Converter - Convertidor Markdown → DOCX con formato APA 7

    Convierte archivos Markdown a documentos Word (.docx) con formato
    profesional según la 7ª edición del manual APA.

    Ejemplos:

        \b
        # Conversión básica
        apa-converter convert tesis.md tesis.docx

        \b
        # Documento profesional con metadata
        apa-converter convert tesis.md tesis.docx --type professional \\
            --title "Mi Tesis" --author "Juan Pérez"

        \b
        # Conversión por lotes
        apa-converter batch ./documentos --output-dir ./salida
    """
    # Configurar logging
    level = 'DEBUG' if verbose else ('ERROR' if quiet else 'INFO')
    log_dir = Path(log_file).parent if log_file else None

    APAConverterLogger.setup_logger(
        'apa_converter',
        level=level,
        log_to_file=bool(log_file),
        log_dir=log_dir
    )

    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--type', '-t',
              type=click.Choice(['student', 'professional']),
              default='student',
              help='Tipo de documento (default: student)')
@click.option('--config', '-c',
              type=click.Path(exists=True),
              help='Archivo de configuración YAML personalizado')
@click.option('--title', help='Título del documento')
@click.option('--author', help='Nombre del autor')
@click.option('--institution', help='Institución')
@click.option('--course', help='Curso (solo estudiante)')
@click.option('--instructor', help='Instructor (solo estudiante)')
@click.option('--date', help='Fecha de entrega')
@click.option('--running-head', help='Running head (solo profesional, max 50 caracteres)')
def convert(input_file, output_file, type, config, title, author,
            institution, course, instructor, date, running_head):
    """
    Convertir archivo Markdown a DOCX con formato APA 7

    INPUT_FILE: Archivo Markdown de entrada (.md)

    OUTPUT_FILE: Archivo DOCX de salida (.docx)

    Ejemplos:

        \b
        # Conversión básica
        apa-converter convert tesis.md tesis.docx

        \b
        # Con metadata completa
        apa-converter convert tesis.md tesis.docx \\
            --title "Efectividad de Intervención en TDA" \\
            --author "Juan Pérez" \\
            --institution "Universidad Nacional" \\
            --course "Psicología 401" \\
            --instructor "Dr. María González" \\
            --date "Octubre 2025"

        \b
        # Documento profesional con running head
        apa-converter convert tesis.md tesis.docx \\
            --type professional \\
            --running-head "INTERVENCIÓN TDA"
    """
    try:
        # Cargar configuración
        if config:
            converter = APAConverter.from_yaml(Path(config))
        else:
            converter = APAConverter.from_defaults(type)

        # Preparar metadata
        metadata = {}
        if title:
            metadata['title'] = title
        if author:
            metadata['author'] = author
        if institution:
            metadata['institution'] = institution
        if course:
            metadata['course'] = course
        if instructor:
            metadata['instructor'] = instructor
        if date:
            metadata['date'] = date
        if running_head:
            metadata['running_head'] = running_head

        # Convertir
        converter.convert(
            Path(input_file),
            Path(output_file),
            metadata if metadata else None
        )

        click.echo(click.style('\n✓ Conversión exitosa', fg='green', bold=True))
        click.echo(f'Archivo guardado: {output_file}')

    except APAConverterError as e:
        click.echo(click.style(f'\n✗ Error: {e}', fg='red'), err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(click.style(f'\n✗ Error inesperado: {e}', fg='red'), err=True)
        sys.exit(1)


@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--output-dir', '-o', type=click.Path(),
              help='Directorio de salida (default: mismo que entrada)')
@click.option('--pattern', '-p', default='*.md',
              help='Patrón de archivos a convertir (default: *.md)')
@click.option('--type', '-t',
              type=click.Choice(['student', 'professional']),
              default='student',
              help='Tipo de documento (default: student)')
@click.option('--config', '-c',
              type=click.Path(exists=True),
              help='Archivo de configuración YAML personalizado')
def batch(directory, output_dir, pattern, type, config):
    """
    Convertir múltiples archivos en lote

    DIRECTORY: Directorio con archivos Markdown

    Ejemplos:

        \b
        # Convertir todos los .md en un directorio
        apa-converter batch ./documentos

        \b
        # Con directorio de salida específico
        apa-converter batch ./documentos --output-dir ./salida

        \b
        # Solo archivos que coincidan con patrón
        apa-converter batch ./documentos --pattern "tesis_*.md"
    """
    try:
        input_dir = Path(directory)
        out_dir = Path(output_dir) if output_dir else input_dir

        # Cargar configuración
        if config:
            converter = APAConverter.from_yaml(Path(config))
        else:
            converter = APAConverter.from_defaults(type)

        # Convertir en lote
        click.echo(f'\nConvirtiendo archivos de: {input_dir}')
        click.echo(f'Patrón: {pattern}')
        click.echo(f'Salida: {out_dir}\n')

        results = converter.convert_batch(input_dir, out_dir, pattern)

        # Mostrar resultados
        successful = sum(results.values())
        total = len(results)

        click.echo('\n' + '='*60)
        if successful == total:
            click.echo(click.style(f'✓ Todos los archivos convertidos ({successful}/{total})',
                                  fg='green', bold=True))
        else:
            failed = total - successful
            click.echo(click.style(f'⚠ Completado con errores:', fg='yellow', bold=True))
            click.echo(f'  Exitosos: {successful}')
            click.echo(f'  Fallidos: {failed}')

        click.echo('='*60)

    except APAConverterError as e:
        click.echo(click.style(f'\n✗ Error: {e}', fg='red'), err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(click.style(f'\n✗ Error inesperado: {e}', fg='red'), err=True)
        sys.exit(1)


@cli.command()
@click.option('--type', '-t',
              type=click.Choice(['student', 'professional']),
              required=True,
              help='Tipo de configuración')
@click.argument('output_file', type=click.Path())
def generate_config(type, output_file):
    """
    Generar archivo de configuración YAML

    OUTPUT_FILE: Archivo YAML de salida

    Ejemplos:

        \b
        # Generar configuración para estudiantes
        apa-converter generate-config --type student mi_config.yaml

        \b
        # Generar configuración profesional
        apa-converter generate-config --type professional config_prof.yaml
    """
    try:
        if type == 'professional':
            config = APAConfig.default_professional()
        else:
            config = APAConfig.default_student()

        config.save_to_yaml(Path(output_file))

        click.echo(click.style(f'\n✓ Configuración generada', fg='green', bold=True))
        click.echo(f'Archivo: {output_file}')
        click.echo(f'Tipo: {type}')

    except Exception as e:
        click.echo(click.style(f'\n✗ Error: {e}', fg='red'), err=True)
        sys.exit(1)


@cli.command()
def version():
    """Mostrar versión del programa"""
    click.echo('APA 7 Converter v2.0.0')
    click.echo('Convertidor Markdown → DOCX con formato APA 7')
    click.echo('\nBasado en: Publication Manual APA 7th Edition (2020)')


if __name__ == '__main__':
    cli()
