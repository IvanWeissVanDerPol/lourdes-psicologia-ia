# Sistema de Análisis con IA

> **Propósito:** Documentación técnica del sistema de IA que diferencia el consultorio  
> **Estado:** En desarrollo  
> **Basado en:** Repositorio `psycology/` (metodología probada)

---

## Visión General

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DEL SISTEMA                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   INPUTS                    PROCESAMIENTO           OUTPUTS         │
│   ──────                    ─────────────           ───────         │
│                                                                     │
│   ┌──────────────┐         ┌──────────────┐        ┌─────────────┐ │
│   │ Audio Sesión │────────→│   WHISPER    │───────→│Transcripción│ │
│   └──────────────┘         │ (OpenAI API) │        └─────────────┘ │
│                            └──────────────┘              │          │
│                                                          │          │
│   ┌──────────────┐                                       │          │
│   │  WhatsApp    │─────────────────────────────────────→│          │
│   │  Export      │                                       │          │
│   └──────────────┘                                       ↓          │
│                            ┌──────────────┐        ┌─────────────┐ │
│                            │ CLAUDE/GPT   │←───────│ Texto Total │ │
│                            │  Análisis    │        └─────────────┘ │
│                            └──────────────┘              │          │
│                                   │                      │          │
│                                   ↓                      │          │
│                            ┌──────────────┐              │          │
│                            │  TEMPLATES   │←─────────────┘          │
│                            │ Generación   │                         │
│                            └──────────────┘                         │
│                                   │                                 │
│                                   ↓                                 │
│                     ┌─────────────────────────────┐                 │
│                     │        DOCUMENTOS           │                 │
│                     ├─────────────────────────────┤                 │
│                     │ • MASTER_PROFILE.md         │                 │
│                     │ • SESSION_NOTES.md          │                 │
│                     │ • TREATMENT_GOALS.md        │                 │
│                     │ • PATTERN_REPORT.md         │                 │
│                     │ • COMMUNICATION_ANALYSIS.md │                 │
│                     └─────────────────────────────┘                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Componentes del Sistema

### 1. Transcripción de Audio (Whisper)

**Propósito:** Convertir grabaciones de sesiones y notas de voz a texto.

**Tecnología:** OpenAI Whisper API

**Proceso:**
1. Grabar sesión con consentimiento del cliente
2. Subir audio a Whisper API
3. Recibir transcripción en español
4. Almacenar con metadata (fecha, cliente, tipo)

**Costo estimado:** ~$0.006/minuto = ~$0.30 por sesión de 50 min

**Script base:** `analysis/session_transcriber.py`

### 2. Parser de WhatsApp

**Propósito:** Extraer y estructurar conversaciones de WhatsApp exportadas.

**Proceso:**
1. Cliente exporta chat relevante (sin media)
2. Parser extrae: fecha, hora, remitente, mensaje
3. Filtra y limpia datos
4. Estructura para análisis

**Script base:** `analysis/whatsapp_parser.py`

### 3. Motor de Análisis (Claude/GPT)

**Propósito:** Extraer insights psicológicos del texto.

**Tecnologías:**
- Claude (Anthropic) - Preferido para análisis profundo
- GPT-4 (OpenAI) - Alternativa/complemento

**Categorías de análisis:**

| Categoría | Qué Busca | Ejemplo de Pattern |
|-----------|-----------|-------------------|
| **Estados emocionales** | Tristeza, ansiedad, enojo | "me siento...", "estoy..." |
| **Patrones de comunicación** | Evitación, defensividad | Respuestas cortas, cambios de tema |
| **Mecanismos de defensa** | Intelectualización, minimización | "no es tan grave", "lógicamente..." |
| **Necesidades expresadas** | Lo que pide o desea | "necesito...", "quiero..." |
| **Necesidades implícitas** | Lo que necesita pero no dice | Contexto, omisiones |
| **Dinámicas relacionales** | Patrones con otros | Roles, posiciones |

**Script base:** `analysis/pattern_extractor.py`

### 4. Generador de Documentos

**Propósito:** Crear documentación estructurada a partir del análisis.

**Templates disponibles:**
- `MASTER_PROFILE_TEMPLATE.md` - Perfil psicológico completo
- `SESSION_NOTES_TEMPLATE.md` - Notas de sesión estructuradas
- `TREATMENT_GOALS_TEMPLATE.md` - Plan de tratamiento
- `COMMUNICATION_ANALYSIS_TEMPLATE.md` - Análisis de comunicación

---

## Flujo de Trabajo por Nivel de Servicio

### Nivel 1: Terapia + Notas IA

```
Sesión Presencial
      │
      ↓
[Grabación audio]
      │
      ↓
[Whisper transcribe]
      │
      ↓
[Claude resume]
      │
      ↓
SESSION_NOTES.md
      │
      ↓
Terapeuta revisa y usa en siguiente sesión
```

### Nivel 2: Terapia + Análisis WhatsApp

```
Sesión + Export WhatsApp del cliente
      │
      ├──→ [Whisper transcribe sesión]
      │
      └──→ [Parser procesa WhatsApp]
               │
               ↓
      [Ambos textos → Claude analiza]
               │
               ↓
      COMMUNICATION_ANALYSIS.md
               │
               ↓
      Discutir insights en siguiente sesión
```

### Nivel 3: Programa Intensivo

```
Múltiples sesiones + WhatsApp + Historial
      │
      ↓
[Acumulación de datos]
      │
      ↓
[Análisis profundo con Claude]
      │
      ├──→ MASTER_PROFILE.md (completo)
      │
      ├──→ TREATMENT_GOALS.md (basado en datos)
      │
      └──→ PATTERN_REPORT.md (evolución)
```

---

## Estructura de Documentación por Cliente

```
clients/
├── [ID_CLIENTE_001]/
│   ├── profile/
│   │   └── MASTER_PROFILE.md          # Perfil psicológico principal
│   │
│   ├── sessions/
│   │   ├── 2026-01-15_session.md      # Notas de sesión
│   │   ├── 2026-01-22_session.md
│   │   └── ...
│   │
│   ├── whatsapp/
│   │   ├── raw/                       # Exports originales (cifrados)
│   │   │   └── export_2026-01.txt
│   │   └── analysis/                  # Análisis procesados
│   │       └── 2026-01_patterns.md
│   │
│   ├── treatment/
│   │   ├── TREATMENT_GOALS.md         # Objetivos de tratamiento
│   │   └── PROGRESS_LOG.md            # Seguimiento de progreso
│   │
│   └── reports/
│       └── MONTHLY_SUMMARY.md         # Resumen mensual
│
├── [ID_CLIENTE_002]/
│   └── ...
```

---

## Templates de Documentación

### MASTER_PROFILE_TEMPLATE.md

```markdown
# [Nombre/Pseudónimo] - Perfil Psicológico

> **Última Actualización:** [Fecha]
> **Sesiones Completadas:** [N]
> **Estado:** [Activo/En pausa/Alta]

---

## Información General

| Campo | Valor |
|-------|-------|
| **Edad** | [X] años |
| **Ocupación** | [Descripción] |
| **Estado civil** | [Estado] |
| **Motivo de consulta** | [Motivo principal] |

---

## Presentación del Caso

[Resumen de 2-3 párrafos]

---

## Patrones Identificados

### Estados Emocionales Predominantes
- [Listado con evidencia]

### Mecanismos de Defensa
| Mecanismo | Evidencia | Frecuencia |
|-----------|-----------|------------|
| [Nombre] | "[Cita]" | Alta/Media/Baja |

### Patrones de Comunicación
- [Descripción de patrones observados en WhatsApp y sesiones]

---

## Dinámicas Relacionales

### Familia
[Análisis]

### Pareja (si aplica)
[Análisis]

### Trabajo/Social
[Análisis]

---

## Necesidades Identificadas

### Explícitas (lo que pide)
- [Lista]

### Implícitas (lo que parece necesitar)
- [Lista con justificación]

---

## Objetivos de Tratamiento

| Objetivo | Prioridad | Estado |
|----------|-----------|--------|
| [Objetivo 1] | Alta | En progreso |
| [Objetivo 2] | Media | Pendiente |

---

## Notas Clínicas

[Observaciones del terapeuta]

---

## Historial de Actualizaciones

| Fecha | Cambio |
|-------|--------|
| [Fecha] | [Descripción] |
```

### SESSION_NOTES_TEMPLATE.md

```markdown
# Notas de Sesión - [Fecha]

**Cliente:** [ID/Pseudónimo]
**Sesión #:** [N]
**Duración:** [X] minutos
**Modalidad:** Presencial / Online

---

## Resumen de la Sesión

[Resumen generado por IA de 3-5 oraciones]

---

## Temas Principales

1. **[Tema 1]**
   - [Puntos clave]
   - [Citas relevantes]

2. **[Tema 2]**
   - [Puntos clave]

---

## Emociones Observadas

| Emoción | Intensidad | Contexto |
|---------|------------|----------|
| [Emoción] | Alta/Media/Baja | [Cuándo apareció] |

---

## Patrones Notables

- [Patrón observado con evidencia]

---

## Intervenciones Realizadas

| Intervención | Respuesta del Cliente |
|--------------|----------------------|
| [Descripción] | [Cómo respondió] |

---

## Para Siguiente Sesión

- [ ] [Tema a retomar]
- [ ] [Pregunta a explorar]

---

## Tareas Asignadas

| Tarea | Descripción |
|-------|-------------|
| [Tarea] | [Detalles] |

---

## Notas Adicionales del Terapeuta

[Espacio para observaciones manuales]
```

---

## Consideraciones de Privacidad

### Consentimiento Requerido

1. **Consentimiento de grabación** - Para transcribir sesiones
2. **Consentimiento de análisis WhatsApp** - Para procesar conversaciones
3. **Consentimiento de almacenamiento** - Para guardar datos
4. **Consentimiento de uso de IA** - Para procesar con modelos externos

### Medidas de Seguridad

| Aspecto | Implementación |
|---------|----------------|
| **Transmisión** | HTTPS/TLS para todas las APIs |
| **Almacenamiento** | Cifrado en reposo (AES-256) |
| **Identificación** | Pseudónimos, no nombres reales en análisis |
| **Retención** | Política de eliminación definida |
| **Acceso** | Solo terapeuta autorizado |

### Cumplimiento Legal

- **Ley 1682/01 (Paraguay)** - Protección de datos personales
- **Secreto profesional** - Código de ética psicología
- **HIPAA-style practices** - Mejores prácticas internacionales

---

## Costos del Sistema

### Costos por Sesión (Estimado)

| Componente | Costo Unitario | Por Sesión |
|------------|----------------|------------|
| **Whisper (transcripción)** | $0.006/min | ~$0.30 |
| **Claude (análisis)** | $0.008/1K tokens | ~$0.50-1.00 |
| **Almacenamiento** | Negligible | ~$0.01 |
| **TOTAL** | | **~$1-2/sesión** |

### Costo Mensual (50 sesiones)

| Ítem | Costo |
|------|-------|
| **APIs (variable)** | $50-100 |
| **Almacenamiento** | $5-10 |
| **Infraestructura** | $10-20 |
| **TOTAL** | **~$65-130/mes** |
| **En Guaraníes** | **~Gs. 500K-1M/mes** |

---

## Roadmap de Desarrollo

### Fase 1: MVP (Durante estudios)
- [ ] Script de transcripción funcionando
- [ ] Parser de WhatsApp básico
- [ ] Prompts de análisis definidos
- [ ] Templates de documentación
- [ ] Pruebas con casos de práctica

### Fase 2: Producción (Post-licencia)
- [ ] Interfaz de usuario básica
- [ ] Automatización de flujos
- [ ] Cifrado completo
- [ ] Backup automático
- [ ] Consentimientos digitales

### Fase 3: Escalabilidad (Año 2+)
- [ ] Dashboard de métricas
- [ ] Análisis de progreso longitudinal
- [ ] API para otros profesionales
- [ ] Modelo de licenciamiento

---

## Próximos Pasos

1. **Configurar APIs** - Crear cuentas en OpenAI y Anthropic
2. **Desarrollar scripts base** - Transcripción y parsing
3. **Definir prompts** - Instrucciones para análisis
4. **Crear templates** - Documentación estructurada
5. **Probar con datos de práctica** - Validar sistema
6. **Documentar procedimientos** - Manuales de uso

---

## Recursos

### APIs
- [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text)
- [Anthropic Claude](https://docs.anthropic.com/)
- [OpenAI GPT-4](https://platform.openai.com/docs/)

### Referencia
- Repositorio `psycology/` - Metodología probada
- `psycology/scripts/` - Scripts de análisis existentes

---

## Contacto Técnico

**Soporte de desarrollo:** [Ivan - para consultas técnicas]
