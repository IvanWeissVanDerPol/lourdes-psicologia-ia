#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APA 7 Configuration System

Sistema de configuración basado en YAML para documentos APA 7.
Permite personalizar todos los aspectos del formato.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any
import yaml
import logging

from ..core.utils.exceptions import ConfigurationError

logger = logging.getLogger(__name__)


@dataclass
class APAConfig:
    """
    Configuración completa para conversión APA 7

    Attributes:
        document_type: Tipo de documento ('student' o 'professional')
        margins: Márgenes del documento
        font: Configuración de fuente
        running_head: Configuración de running head
        cover_page: Configuración de portada
        abstract: Configuración de resumen
        references: Configuración de referencias
        tables: Configuración de tablas
    """
    document_type: str
    margins: Dict[str, Any]
    font: Dict[str, Any]
    running_head: Dict[str, Any]
    cover_page: Dict[str, Any]
    abstract: Dict[str, Any]
    references: Dict[str, Any]
    tables: Dict[str, Any]

    @classmethod
    def from_yaml(cls, yaml_path: Path) -> 'APAConfig':
        """
        Cargar configuración desde archivo YAML

        Args:
            yaml_path: Ruta al archivo YAML

        Returns:
            Objeto APAConfig

        Raises:
            ConfigurationError: Si hay error cargando la configuración

        Example:
            >>> config = APAConfig.from_yaml(Path('config/apa7_student.yaml'))
            >>> config.document_type
            'student'
        """
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            logger.info(f"Configuración cargada desde: {yaml_path}")

            return cls(
                document_type=data['document']['type'],
                margins=data['document']['margins'],
                font=data['document']['font'],
                running_head=data['document'].get('running_head', {}),
                cover_page=data.get('cover_page', {}),
                abstract=data.get('abstract', {}),
                references=data.get('references', {}),
                tables=data.get('tables', {})
            )

        except FileNotFoundError:
            raise ConfigurationError(f"Archivo de configuración no encontrado: {yaml_path}")
        except yaml.YAMLError as e:
            raise ConfigurationError(f"Error parseando YAML: {e}")
        except KeyError as e:
            raise ConfigurationError(f"Clave faltante en configuración: {e}")
        except Exception as e:
            raise ConfigurationError(f"Error cargando configuración: {e}")

    @classmethod
    def default_student(cls) -> 'APAConfig':
        """
        Configuración por defecto para documento estudiantil

        Returns:
            APAConfig con valores por defecto para estudiantes
        """
        return cls(
            document_type='student',
            margins={
                'top': 1.0,
                'bottom': 1.0,
                'left': 1.0,
                'right': 1.0,
                'units': 'inches'
            },
            font={
                'name': 'Times New Roman',
                'size': 12,
                'line_spacing': 2.0
            },
            running_head={
                'enabled': False
            },
            cover_page={
                'enabled': True,
                'elements': ['title', 'author', 'institution', 'course', 'instructor', 'date']
            },
            abstract={
                'enabled': True,
                'keywords': True,
                'max_words': 250
            },
            references={
                'hanging_indent': 0.5,
                'hanging_indent_units': 'inches',
                'auto_detect': True
            },
            tables={
                'borders': {
                    'top': 'single',
                    'bottom': 'single',
                    'left': 'none',
                    'right': 'none',
                    'inside_vertical': 'none',
                    'inside_horizontal': 'single'
                }
            }
        )

    @classmethod
    def default_professional(cls) -> 'APAConfig':
        """
        Configuración por defecto para documento profesional

        Returns:
            APAConfig con valores por defecto para profesionales
        """
        return cls(
            document_type='professional',
            margins={
                'top': 1.0,
                'bottom': 1.0,
                'left': 1.0,
                'right': 1.0,
                'units': 'inches'
            },
            font={
                'name': 'Times New Roman',
                'size': 12,
                'line_spacing': 2.0
            },
            running_head={
                'enabled': True,
                'max_length': 50
            },
            cover_page={
                'enabled': True,
                'elements': ['title', 'author', 'institution', 'author_note']
            },
            abstract={
                'enabled': True,
                'keywords': True,
                'max_words': 250
            },
            references={
                'hanging_indent': 0.5,
                'hanging_indent_units': 'inches',
                'auto_detect': True
            },
            tables={
                'borders': {
                    'top': 'single',
                    'bottom': 'single',
                    'left': 'none',
                    'right': 'none',
                    'inside_vertical': 'none',
                    'inside_horizontal': 'single'
                }
            }
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convertir configuración a diccionario

        Returns:
            Diccionario con la configuración
        """
        return {
            'document': {
                'type': self.document_type,
                'margins': self.margins,
                'font': self.font,
                'running_head': self.running_head
            },
            'cover_page': self.cover_page,
            'abstract': self.abstract,
            'references': self.references,
            'tables': self.tables
        }

    def save_to_yaml(self, yaml_path: Path) -> None:
        """
        Guardar configuración a archivo YAML

        Args:
            yaml_path: Ruta donde guardar el archivo
        """
        try:
            with open(yaml_path, 'w', encoding='utf-8') as f:
                yaml.dump(self.to_dict(), f, default_flow_style=False, allow_unicode=True)
            logger.info(f"Configuración guardada en: {yaml_path}")
        except Exception as e:
            raise ConfigurationError(f"Error guardando configuración: {e}")
