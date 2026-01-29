# 07-DATOS - Datos y Ejemplos

Este directorio contiene datos de ejemplo para el sistema de analisis.

> **Nota:** Este es un repositorio privado. Los datos incluidos son del propietario
> y se usan como ejemplo/referencia para el sistema.

---

## Estructura

```
07-DATOS/
└── PACIENTES/
    └── 001-LOURDES/           # Ejemplo completo con datos reales
        │
        ├── RAW/               # Datos originales
        │   └── WhatsApp Chat.../
        │       ├── _chat.txt  # Historial de chat exportado
        │       └── *.opus     # Notas de voz (~1900 archivos)
        │
        ├── CLINICA/           # Datos procesados
        │   └── TRANSCRIPTS/   # Transcripciones generadas
        │       └── WhatsApp Chat.../
        │           ├── transcripts.json
        │           └── transcripts.md
        │
        └── METADATA/          # Estadisticas y analisis
            ├── chat_stats.json
            ├── chat_analysis.json
            └── debug_media.json
```

---

## Uso

### Transcribir Audios

```bash
# Desde la raiz del repo
cd 08-HERRAMIENTAS
python -m transcription transcribe --input ../07-DATOS/PACIENTES/001-LOURDES/RAW
```

### Verificar Calidad

```bash
python -m transcription check-quality --input ../07-DATOS/PACIENTES/001-LOURDES/CLINICA
```

### Ver Transcripciones

Las transcripciones estan en formato:
- **JSON** - `transcripts.json` - Para procesamiento programatico
- **Markdown** - `transcripts.md` - Para lectura humana

---

## Agregar Nuevos Pacientes

Para agregar un nuevo paciente/cliente:

```
07-DATOS/PACIENTES/
├── 001-LOURDES/      # Existente
└── 002-NUEVO/        # Nuevo
    ├── RAW/
    ├── CLINICA/
    └── METADATA/
```

1. Crear carpeta con ID secuencial
2. Exportar chat de WhatsApp a `RAW/`
3. Ejecutar transcripcion
4. Revisar resultados en `CLINICA/`

---

## Formatos de Archivo

| Extension | Tipo | Contenido |
|-----------|------|-----------|
| `.opus` | Audio | Notas de voz WhatsApp |
| `.webp` | Imagen | Stickers WhatsApp |
| `_chat.txt` | Texto | Historial de chat |
| `.json` | Datos | Transcripciones/analisis |
| `.md` | Documento | Transcripciones legibles |

---

## Ver Tambien

- [`08-HERRAMIENTAS/transcription/`](../08-HERRAMIENTAS/transcription/) - Sistema de transcripcion
- [`04-PLANTILLAS/`](../04-PLANTILLAS/) - Templates para documentacion clinica
- [`06-LEGAL/`](../06-LEGAL/) - Consentimientos y politicas
