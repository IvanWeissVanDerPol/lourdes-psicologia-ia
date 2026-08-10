# 001-LOURDES - Ejemplo de Datos

Este directorio contiene un ejemplo completo de datos para el sistema de analisis.

---

## Contenido

### RAW/ - Datos Originales

Export de Messaging con:
- `_chat.txt` - Historial completo del chat
- `*.opus` - ~1900 notas de voz
- `*.webp` - Stickers e imagenes

### CLINICA/ - Datos Procesados

Transcripciones generadas por el sistema:
- `TRANSCRIPTS/*/transcripts.json` - Formato estructurado
- `TRANSCRIPTS/*/transcripts.md` - Formato legible

### METADATA/ - Analisis

Estadisticas y analisis del chat:
- `chat_stats.json` - Metricas de volumen
- `chat_analysis.json` - Analisis procesado
- `debug_media.json` - Info de archivos multimedia

---

## Uso

```bash
# Transcribir audios
cd 08-HERRAMIENTAS
python -m transcription transcribe --input ../07-DATOS/PACIENTES/001-LOURDES/RAW

# Verificar calidad
python -m transcription check-quality --input ../07-DATOS/PACIENTES/001-LOURDES/CLINICA
```

---

## Estructura

```
001-LOURDES/
├── README.md           # Este archivo
├── RAW/
│   └── Messaging Chat - .../
│       ├── _chat.txt
│       └── *.opus (1900+ archivos)
├── CLINICA/
│   └── TRANSCRIPTS/
│       └── Messaging Chat - .../
│           ├── transcripts.json
│           └── transcripts.md
└── METADATA/
    ├── chat_stats.json
    ├── chat_analysis.json
    └── debug_media.json
```
