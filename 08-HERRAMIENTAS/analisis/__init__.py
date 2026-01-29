# Lourdes AI Analysis System
# Este modulo contiene las herramientas de analisis con IA

"""
Sistema de Analisis con IA para Practica de Psicologia

Componentes:
- transcriber: Transcripcion de audio usando Whisper API
- analyzer: Analisis de sesiones usando Claude API
- config: Configuracion y credenciales

Uso:
    from analisis import transcriber, analyzer

    # Transcribir audio
    texto = transcriber.transcribe_audio("sesion.mp3")

    # Analizar sesion
    notas = analyzer.analyze_session(texto, patient_context)
"""

__version__ = "0.1.0"
__author__ = "Lourdes"
