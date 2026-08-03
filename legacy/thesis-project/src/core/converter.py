#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APA Converter - Convertidor principal Markdown → DOCX con formato APA 7

Este es el orquestador principal que coordina el parser, builder y
configuración para realizar la conversión completa.
"""

from pathlib import Path
from typing import Optional, Dict, Any
import logging

from .parsers.markdown_parser import MarkdownParser
from .builders.document_builder import DocumentBuilder
from ..config.apa7_config import APAConfig
from .utils.logger import APAConverterLogger
from .utils.exceptions import APAConverterError

logger = logging.getLogger(__name__)


class APAConverter:
    """
    Convertidor principal Markdown → DOCX con formato APA 7

    Esta clase orquesta todo el proceso de conversión:
    1. Parseo del Markdown a AST
    2. Construcción del DOCX con estilos APA
    3. Guardado del documento

    Example:
        >>> # Uso básico
        >>> converter = APAConverter.from_defaults('student')
        >>> converter.convert('tesis.md', 'tesis.docx', {'title': 'Mi Tesis'})

        >>> # Uso con configuración personalizada
        >>> config = APAConfig.from_yaml(Path('mi_config.yaml'))
        >>> converter = APAConverter(config)
        >>> converter.convert('input.md', 'output.docx')
    """

    def __init__(self, config: Optional[APAConfig] = None):
        """
        Inicializar convertidor

        Args:
            config: Configuración APA. Si es None, usa defaults para estudiante
        """
        if config is None:
            config = APAConfig.default_student()

        self.config = config
        self.parser = MarkdownParser()
        self.builder = None  # Se crea en cada conversión

        logger.debug(f"Convertidor inicializado: tipo={config.document_type}")

    @classmethod
    def from_defaults(cls, document_type: str = 'student') -> 'APAConverter':
        """
        Crear convertidor con configuración por defecto

        Args:
            document_type: 'student' o 'professional'

        Returns:
            Convertidor configurado

        Example:
            >>> converter = APAConverter.from_defaults('professional')
        """
        if document_type == 'professional':
            config = APAConfig.default_professional()
        else:
            config = APAConfig.default_student()

        return cls(config)

    @classmethod
    def from_yaml(cls, config_path: Path) -> 'APAConverter':
        """
        Crear convertidor desde archivo YAML

        Args:
            config_path: Ruta al archivo de configuración

        Returns:
            Convertidor configurado

        Example:
            >>> converter = APAConverter.from_yaml(Path('config/custom.yaml'))
        """
        config = APAConfig.from_yaml(config_path)
        return cls(config)

    def convert(
        self,
        input_path: Path,
        output_path: Path,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Convertir archivo Markdown a DOCX con formato APA 7

        Args:
            input_path: Ruta al archivo Markdown de entrada
            output_path: Ruta al archivo DOCX de salida
            metadata: Metadatos del documento (título, autor, etc.)

        Raises:
            APAConverterError: Si hay error en la conversión

        Example:
            >>> converter = APAConverter.from_defaults('student')
            >>> converter.convert(
            ...     Path('mi_tesis.md'),
            ...     Path('mi_tesis.docx'),
            ...     metadata={
            ...         'title': 'Efectividad de Intervención en TDA',
            ...         'author': 'Juan Pérez',
            ...         'institution': 'Universidad Nacional',
            ...         'course': 'Psicología 401',
            ...         'instructor': 'Dr. María González',
            ...         'date': 'Octubre 2025'
            ...     }
            ... )
        """
        try:
            logger.info("="*60)
            logger.info("INICIANDO CONVERSIÓN MARKDOWN → DOCX (APA 7)")
            logger.info("="*60)

            # 1. Parsear Markdown
            logger.info(f"[1/3] Parseando: {input_path}")
            elements = self.parser.parse_file(str(input_path))
            logger.info(f"      Parseados {len(elements)} elementos")

            # 2. Construir documento
            logger.info(f"[2/3] Construyendo documento DOCX...")
            self.builder = DocumentBuilder(self.config)
            document = self.builder.build(elements, metadata)
            logger.info(f"      Documento construido exitosamente")

            # 3. Guardar
            logger.info(f"[3/3] Guardando: {output_path}")
            self.builder.save(str(output_path))

            logger.info("="*60)
            logger.info("✓ CONVERSIÓN COMPLETADA EXITOSAMENTE")
            logger.info("="*60)
            logger.info(f"Archivo de salida: {output_path}")
            logger.info(f"Tipo de documento: {self.config.document_type}")
            logger.info(f"Elementos procesados: {len(elements)}")

            # Mostrar estadísticas
            if self.builder:
                logger.info(f"Tablas: {self.builder.table_counter}")
                logger.info(f"Figuras: {self.builder.figure_counter}")

        except FileNotFoundError as e:
            logger.error(f"Archivo no encontrado: {e}")
            raise APAConverterError(f"Archivo no encontrado: {e}")
        except Exception as e:
            logger.error(f"Error durante conversión: {e}", exc_info=True)
            raise APAConverterError(f"Error durante conversión: {e}")

    def convert_batch(
        self,
        input_dir: Path,
        output_dir: Path,
        pattern: str = "*.md",
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, bool]:
        """
        Convertir múltiples archivos en lote

        Args:
            input_dir: Directorio con archivos Markdown
            output_dir: Directorio de salida
            pattern: Patrón de archivos (default: "*.md")
            metadata: Metadatos comunes para todos los documentos

        Returns:
            Diccionario con resultados: {archivo: éxito}

        Example:
            >>> converter = APAConverter.from_defaults('student')
            >>> results = converter.convert_batch(
            ...     Path('./documentos'),
            ...     Path('./salida')
            ... )
            >>> successful = sum(results.values())
            >>> print(f"Convertidos: {successful}/{len(results)}")
        """
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)

        # Buscar archivos
        files = list(input_dir.glob(pattern))
        logger.info(f"Encontrados {len(files)} archivos para convertir")

        results = {}

        for i, input_file in enumerate(files, 1):
            output_file = output_dir / f"{input_file.stem}.docx"

            logger.info(f"\n[{i}/{len(files)}] Procesando: {input_file.name}")

            try:
                self.convert(input_file, output_file, metadata)
                results[str(input_file)] = True
                logger.info(f"✓ Éxito: {input_file.name}")
            except Exception as e:
                results[str(input_file)] = False
                logger.error(f"✗ Error en {input_file.name}: {e}")

        # Resumen
        successful = sum(results.values())
        logger.info("\n" + "="*60)
        logger.info("RESUMEN DE CONVERSIÓN POR LOTES")
        logger.info("="*60)
        logger.info(f"Total de archivos: {len(results)}")
        logger.info(f"Exitosos: {successful}")
        logger.info(f"Fallidos: {len(results) - successful}")

        return results
