# Plan de Implementación - Estandarización al Español

## Problema

El repositorio tiene una mezcla de inglés y español ("Spanglish"), inconsistencias en nombres de carpetas y riesgos de privacidad (ya mitigados).

## Cambios Propuestos

### 1. Documentación Raíz (Renombrar y Traducir)

- `ROAST.md` (Inglés) -> **`AUDITORIA_CRITICA.md`** (Contenido traducido al Español)
- `REPO_CLEANUP_WALKTHROUGH.md` (Inglés) -> **`RESUMEN_LIMPIEZA.md`** (Contenido traducido al Español)
- `IMPLEMENTATION_PLAN.md` (Inglés) -> **`PLAN_IMPLEMENTACION.md`** (Contenido traducido al Español)
- `SETUP.md` -> **`INSTALACION.md`**
- `REPO_AUDIT.md` -> **`AUDITORIA_GENERAL.md`**

### 2. Estructura de Directorios

- `scripts/` -> **`scripts_obsoletos/`**
- `07-DATOS/.../QUESTIONAIR` -> **`CUESTIONARIOS`**
- `08-HERRAMIENTAS/`
  - `transcription/` -> **`transcripcion/`**
  - `analysis/` -> **`analisis/`**
  - `templates/` -> **`plantillas/`**

### 3. Contenido (Nuevo Requerimiento)

- **CUESTIONARIOS/**:
  - Crear `CUESTIONARIO_FAMILIA.md`
  - Crear `CUESTIONARIO_AMIGOS.md`
  - Crear `CUESTIONARIO_PAREJA.md`
  - _Nota: Se pre-llenarán con detalles basados en el contexto de Lourdes._

### 4. Código y Configuración

- Actualizar referencias en `README.md`.
- Refactorizar código Python para soportar el cambio de nombre de módulos (`transcription` -> `transcripcion`).

## Plan de Verificación

### Pruebas Automatizadas

- `python -m transcripcion --help` -> Debe funcionar sin errores.
- Verificar existencia de carpetas en español.

### Verificación Manual

- Revisar que la documentación sea legible y coherente en español.
