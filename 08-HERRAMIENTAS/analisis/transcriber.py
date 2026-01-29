"""
Transcriptor de Audio usando OpenAI Whisper API

Este modulo maneja la transcripcion de sesiones de audio a texto.

Uso:
    from analisis.transcriber import transcribe_audio

    texto = transcribe_audio("path/to/audio.mp3")
    print(texto)
"""

import os
from pathlib import Path
from typing import Optional

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("AVISO: openai no instalado. Ejecutar: pip install openai")

from .config import config


def transcribe_audio(
    audio_path: str,
    language: str = "es",
    api_key: Optional[str] = None,
) -> str:
    """
    Transcribe un archivo de audio usando Whisper API.

    Args:
        audio_path: Ruta al archivo de audio (mp3, wav, m4a, etc.)
        language: Codigo de idioma (default: "es" para espanol)
        api_key: API key de OpenAI (opcional, usa config si no se provee)

    Returns:
        Texto transcrito de la sesion

    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el formato no es soportado
        RuntimeError: Si hay error en la API

    Ejemplo:
        >>> texto = transcribe_audio("sesion_2024_01_15.mp3")
        >>> print(texto[:100])
        "Bueno, esta semana me senti mejor porque..."
    """
    if not OPENAI_AVAILABLE:
        raise RuntimeError("openai no esta instalado. Ejecutar: pip install openai")

    # Validar archivo
    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {audio_path}")

    # Formatos soportados por Whisper
    supported_formats = {".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".wav", ".webm"}
    if path.suffix.lower() not in supported_formats:
        raise ValueError(
            f"Formato no soportado: {path.suffix}. "
            f"Formatos validos: {supported_formats}"
        )

    # Verificar tamano (Whisper tiene limite de 25MB)
    file_size_mb = path.stat().st_size / (1024 * 1024)
    if file_size_mb > 25:
        raise ValueError(
            f"Archivo muy grande: {file_size_mb:.1f}MB. "
            f"Limite de Whisper: 25MB. Considera dividir el audio."
        )

    # Configurar cliente
    key = api_key or config.openai_api_key
    if not key:
        raise ValueError(
            "API key de OpenAI no configurada. " "Usar: export OPENAI_API_KEY='tu-key'"
        )

    client = OpenAI(api_key=key)

    # Transcribir
    print(f"Transcribiendo: {path.name} ({file_size_mb:.1f}MB)...")

    try:
        with open(audio_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model=config.whisper_model,
                file=audio_file,
                language=language,
                response_format="text",
            )

        print(f"Transcripcion completada: {len(response)} caracteres")
        return response

    except Exception as e:
        raise RuntimeError(f"Error en transcripcion: {e}") from e


def estimate_cost(audio_path: str) -> float:
    """
    Estima el costo de transcribir un archivo de audio.

    Args:
        audio_path: Ruta al archivo de audio

    Returns:
        Costo estimado en USD

    Nota:
        Esta es una estimacion aproximada basada en duracion.
        El costo real puede variar.
    """
    # Estimacion muy aproximada: 1MB ~ 1 minuto de audio
    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {audio_path}")

    file_size_mb = path.stat().st_size / (1024 * 1024)
    estimated_minutes = file_size_mb  # Aproximacion gruesa

    cost = estimated_minutes * config.whisper_cost_per_minute

    return round(cost, 4)


# CLI simple para testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python transcriber.py <archivo_audio>")
        print("Ejemplo: python transcriber.py sesion.mp3")
        sys.exit(1)

    audio_file = sys.argv[1]

    try:
        # Mostrar estimacion de costo
        cost = estimate_cost(audio_file)
        print(f"Costo estimado: ${cost:.4f} USD")

        # Confirmar
        confirm = input("Continuar con transcripcion? (s/n): ")
        if confirm.lower() != "s":
            print("Cancelado.")
            sys.exit(0)

        # Transcribir
        texto = transcribe_audio(audio_file)

        # Guardar resultado
        output_file = Path(audio_file).stem + "_transcripcion.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"Transcripcion guardada en: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
