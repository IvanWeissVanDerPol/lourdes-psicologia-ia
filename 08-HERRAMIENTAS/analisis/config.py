"""
Configuracion del Sistema de Analisis con IA

IMPORTANTE:
- Nunca commitear este archivo con API keys reales
- Usar variables de entorno en produccion
- Este archivo es un TEMPLATE
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class AIConfig:
    """Configuracion para APIs de IA"""

    # OpenAI (Whisper)
    openai_api_key: str = ""
    whisper_model: str = "whisper-1"

    # Anthropic (Claude)
    anthropic_api_key: str = ""
    claude_model: str = "claude-sonnet-4-20250514"

    # Costos estimados (USD)
    whisper_cost_per_minute: float = 0.006
    claude_cost_per_1k_tokens: float = 0.003

    # Limites
    max_audio_duration_minutes: int = 60
    max_transcript_tokens: int = 100000

    @classmethod
    def from_env(cls) -> "AIConfig":
        """Cargar configuracion desde variables de entorno"""
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY", ""),
        )

    def validate(self) -> bool:
        """Verificar que la configuracion es valida"""
        errors = []

        if not self.openai_api_key:
            errors.append("OPENAI_API_KEY no configurada")

        if not self.anthropic_api_key:
            errors.append("ANTHROPIC_API_KEY no configurada")

        if errors:
            print("Errores de configuracion:")
            for error in errors:
                print(f"  - {error}")
            return False

        return True


# Configuracion por defecto
# En produccion, usar: config = AIConfig.from_env()
config = AIConfig()


# Prompts del sistema
SYSTEM_PROMPTS = {
    "session_analysis": """Eres un asistente de analisis para una psicologa.
Tu rol es ayudar a identificar patrones y temas importantes en las sesiones.

IMPORTANTE:
- NO hagas diagnosticos clinicos
- NO sugieras medicacion
- Solo identifica patrones, temas y posibles areas de exploracion
- Usa lenguaje profesional pero accesible
- Respeta la confidencialidad del paciente

Formato de salida:
1. Resumen de la sesion (2-3 oraciones)
2. Temas principales identificados
3. Patrones emocionales observados
4. Sugerencias para proxima sesion
5. Notas adicionales relevantes
""",

    "whatsapp_analysis": """Eres un asistente que analiza conversaciones de WhatsApp
entre una psicologa y su paciente.

Tu rol es identificar:
- Estado emocional general del paciente
- Temas recurrentes
- Cambios de animo a lo largo de la conversacion
- Posibles puntos a abordar en la proxima sesion

IMPORTANTE:
- NO hagas diagnosticos
- Solo identifica patrones observables
- Usa lenguaje profesional
""",
}


# Templates de salida
OUTPUT_TEMPLATES = {
    "session_notes": """
# Notas de Sesion - {fecha}

## Paciente
- ID: {patient_id}
- Sesion #: {session_number}

## Resumen
{resumen}

## Temas Principales
{temas}

## Patrones Observados
{patrones}

## Para Proxima Sesion
{sugerencias}

## Notas Adicionales
{notas}

---
*Generado con asistencia de IA - Revisar antes de usar*
""",
}


if __name__ == "__main__":
    # Test de configuracion
    test_config = AIConfig.from_env()
    print(f"Configuracion cargada: {test_config}")
    print(f"Valida: {test_config.validate()}")
