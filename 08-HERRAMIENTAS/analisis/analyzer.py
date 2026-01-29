"""
Analizador de Sesiones usando Claude API

Este modulo genera notas estructuradas de sesiones de terapia/coaching
usando Claude para identificar patrones y temas importantes.

Uso:
    from analisis.analyzer import analyze_session

    notas = analyze_session(transcripcion, patient_context)
    print(notas)
"""

from datetime import datetime
from typing import Optional

try:
    import anthropic

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("AVISO: anthropic no instalado. Ejecutar: pip install anthropic")

from .config import config, SYSTEM_PROMPTS, OUTPUT_TEMPLATES


def analyze_session(
    transcript: str,
    patient_id: str = "ANONIMO",
    session_number: int = 1,
    additional_context: str = "",
    api_key: Optional[str] = None,
) -> str:
    """
    Analiza una transcripcion de sesion y genera notas estructuradas.

    Args:
        transcript: Texto transcrito de la sesion
        patient_id: Identificador anonimizado del paciente
        session_number: Numero de sesion con este paciente
        additional_context: Contexto adicional (notas previas, etc.)
        api_key: API key de Anthropic (opcional)

    Returns:
        Notas de sesion en formato markdown

    Raises:
        ValueError: Si la transcripcion esta vacia
        RuntimeError: Si hay error en la API
    """
    if not ANTHROPIC_AVAILABLE:
        raise RuntimeError(
            "anthropic no esta instalado. Ejecutar: pip install anthropic"
        )

    if not transcript or len(transcript.strip()) < 50:
        raise ValueError("Transcripcion muy corta o vacia")

    # Configurar cliente
    key = api_key or config.anthropic_api_key
    if not key:
        raise ValueError(
            "API key de Anthropic no configurada. "
            "Usar: export ANTHROPIC_API_KEY='tu-key'"
        )

    client = anthropic.Anthropic(api_key=key)

    # Construir prompt
    user_prompt = f"""Analiza la siguiente transcripcion de sesion de coaching/bienestar.

CONTEXTO DEL PACIENTE:
- ID: {patient_id}
- Sesion numero: {session_number}
{f"- Contexto adicional: {additional_context}" if additional_context else ""}

TRANSCRIPCION DE LA SESION:
---
{transcript}
---

Por favor genera notas estructuradas siguiendo el formato indicado.
Recuerda: NO hagas diagnosticos clinicos, solo identifica patrones y temas."""

    print(f"Analizando sesion ({len(transcript)} caracteres)...")

    try:
        response = client.messages.create(
            model=config.claude_model,
            max_tokens=4096,
            system=SYSTEM_PROMPTS["session_analysis"],
            messages=[{"role": "user", "content": user_prompt}],
        )

        analysis = response.content[0].text

        # Formatear con template
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        notas = f"""# Notas de Sesion - {fecha}

## Informacion
- **Paciente ID:** {patient_id}
- **Sesion #:** {session_number}
- **Generado:** {fecha}

## Analisis

{analysis}

---
*Notas generadas con asistencia de IA - REVISAR antes de usar clinicamente*
*Modelo: {config.claude_model}*
"""

        print(f"Analisis completado: {len(notas)} caracteres")
        return notas

    except Exception as e:
        raise RuntimeError(f"Error en analisis: {e}") from e


def analyze_whatsapp_conversation(
    messages: str,
    patient_id: str = "ANONIMO",
    api_key: Optional[str] = None,
) -> str:
    """
    Analiza una conversacion de WhatsApp para identificar patrones.

    Args:
        messages: Texto exportado de WhatsApp
        patient_id: Identificador del paciente
        api_key: API key de Anthropic (opcional)

    Returns:
        Analisis de la conversacion
    """
    if not ANTHROPIC_AVAILABLE:
        raise RuntimeError(
            "anthropic no esta instalado. Ejecutar: pip install anthropic"
        )

    if not messages or len(messages.strip()) < 50:
        raise ValueError("Conversacion muy corta o vacia")

    key = api_key or config.anthropic_api_key
    if not key:
        raise ValueError("API key de Anthropic no configurada")

    client = anthropic.Anthropic(api_key=key)

    user_prompt = f"""Analiza la siguiente conversacion de WhatsApp entre una profesional
de coaching/bienestar y su paciente.

PACIENTE ID: {patient_id}

CONVERSACION:
---
{messages}
---

Identifica:
1. Estado emocional general observado
2. Temas recurrentes en la conversacion
3. Posibles puntos a abordar en la proxima sesion
4. Observaciones relevantes

Recuerda: NO diagnostiques, solo observa patrones."""

    try:
        response = client.messages.create(
            model=config.claude_model,
            max_tokens=2048,
            system=SYSTEM_PROMPTS["whatsapp_analysis"],
            messages=[{"role": "user", "content": user_prompt}],
        )

        return response.content[0].text

    except Exception as e:
        raise RuntimeError(f"Error en analisis de WhatsApp: {e}") from e


def estimate_cost(text: str) -> float:
    """
    Estima el costo de analizar un texto.

    Args:
        text: Texto a analizar

    Returns:
        Costo estimado en USD
    """
    # Estimacion aproximada: 4 caracteres ~ 1 token
    estimated_tokens = len(text) / 4

    # Input + Output estimado (output ~ 1/4 del input para este caso)
    total_tokens = estimated_tokens * 1.25

    cost = (total_tokens / 1000) * config.claude_cost_per_1k_tokens

    return round(cost, 4)


# CLI simple para testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python analyzer.py <archivo_transcripcion>")
        print("Ejemplo: python analyzer.py sesion_transcripcion.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            transcript = f.read()

        # Estimar costo
        cost = estimate_cost(transcript)
        print(f"Costo estimado: ${cost:.4f} USD")

        # Confirmar
        confirm = input("Continuar con analisis? (s/n): ")
        if confirm.lower() != "s":
            print("Cancelado.")
            sys.exit(0)

        # Analizar
        notas = analyze_session(transcript)

        # Guardar
        output_file = input_file.replace(".txt", "_notas.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(notas)

        print(f"Notas guardadas en: {output_file}")
        print("\n--- PREVIEW ---")
        print(notas[:500] + "...")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
