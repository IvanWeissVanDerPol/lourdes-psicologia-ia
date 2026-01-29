# Guia de Instalacion

Esta guia explica como configurar el entorno para usar las herramientas de LourdesBusiness.

---

## Requisitos Previos

- Python 3.10+ instalado
- FFmpeg instalado (para transcripcion de audio)
- Git instalado

---

## Paso 1: Crear Directorio de Datos

**IMPORTANTE:** Los datos de pacientes NUNCA van en el repositorio git.

Crear el directorio de datos separado:

```bash
# Windows
mkdir "C:\Users\TU_USUARIO\Documents\LourdesBusiness-DATA"
mkdir "C:\Users\TU_USUARIO\Documents\LourdesBusiness-DATA\PACIENTES"

# macOS/Linux
mkdir -p ~/Documents/LourdesBusiness-DATA/PACIENTES
```

---

## Paso 2: Instalar FFmpeg

### Windows

```powershell
winget install Gyan.FFmpeg
```

### macOS

```bash
brew install ffmpeg
```

### Linux

```bash
sudo apt install ffmpeg
```

---

## Paso 3: Instalar Dependencias Python

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install openai-whisper torch

# Para analisis con IA (opcional)
pip install anthropic openai
```

---

## Paso 4: Configurar Variables de Entorno

Copiar el archivo de ejemplo y editarlo:

```bash
# Copiar template
cp env.example .env

# Editar con tus valores
# Windows: notepad .env
# macOS/Linux: nano .env
```

Contenido minimo de `.env`:

```env
# Directorio de datos (FUERA del repo)
LOURDES_DATA_DIR=C:\Users\TU_USUARIO\Documents\LourdesBusiness-DATA

# Modelo de Whisper
WHISPER_MODEL=base
WHISPER_LANGUAGE=es
```

---

## Paso 5: Verificar Instalacion

```bash
# Verificar configuracion
python config/settings.py

# Deberia mostrar:
# ============================================================
# LOURDES BUSINESS SETTINGS
# ============================================================
# Data Paths:
#   DATA_DIR:     ... ✓
#   PATIENTS_DIR: ... ✓
# ...
# Validation: ✓ All checks passed
```

---

## Paso 6: Probar Transcripcion

```bash
# Ver ayuda
python -m transcription --help

# Probar con un archivo de audio
python -m transcription transcribe --input /path/to/audio.opus
```

---

## Estructura Final

Despues de la instalacion, deberia tener:

```
Documents/
├── LourdesBusiness/              # Repositorio git
│   ├── .gitignore
│   ├── .env                      # Configuracion local (NO commitear)
│   ├── config/
│   ├── 10-AI-SYSTEM/
│   │   └── transcription/
│   └── ...
│
└── LourdesBusiness-DATA/         # Datos (FUERA de git)
    └── PACIENTES/
        └── 001-XXX/
            ├── RAW/
            ├── CLINICA/
            └── METADATA/
```

---

## Solucion de Problemas

### Error: "FFmpeg not found"

```bash
# Verificar que FFmpeg esta instalado
ffmpeg -version

# Si no funciona, agregar al PATH o configurar FFMPEG_PATH en .env
```

### Error: "Data directory does not exist"

```bash
# Crear el directorio
mkdir -p "$(grep LOURDES_DATA_DIR .env | cut -d= -f2)"
```

### Error: "No module named 'whisper'"

```bash
# Instalar whisper
pip install openai-whisper
```

### Error: "torch not found" o "CUDA not available"

```bash
# Instalar PyTorch (CPU version)
pip install torch

# O con CUDA (si tienes GPU NVIDIA)
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

---

## Siguiente Paso

Ver [`10-AI-SYSTEM/transcription/README.md`](10-AI-SYSTEM/transcription/README.md) para aprender a usar el sistema de transcripcion.
