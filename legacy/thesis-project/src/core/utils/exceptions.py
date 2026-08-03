#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Exceptions for APA 7 Converter

Este módulo define excepciones personalizadas para manejar diferentes
tipos de errores durante la conversión.
"""


class APAConverterError(Exception):
    """Excepción base para todos los errores del convertidor"""
    pass


class FileNotFoundError(APAConverterError):
    """Error cuando no se encuentra el archivo de entrada"""
    pass


class InvalidMarkdownError(APAConverterError):
    """Error cuando el Markdown no es válido o tiene formato incorrecto"""
    pass


class StyleApplicationError(APAConverterError):
    """Error al aplicar estilos al documento"""
    pass


class ParsingError(APAConverterError):
    """Error durante el parseo del Markdown"""
    pass


class BuildError(APAConverterError):
    """Error durante la construcción del documento DOCX"""
    pass


class ConfigurationError(APAConverterError):
    """Error en la configuración"""
    pass


class ValidationError(APAConverterError):
    """Error de validación (documento no cumple APA 7)"""
    pass
