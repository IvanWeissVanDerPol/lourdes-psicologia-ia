# Lourdes - Psicologia Tech & Bienestar Digital

**Cliente:** Lourdes
**Estado:** Estudiante de Psicologia (5to ano, tesis en curso)
**Nicho:** Profesionales Tech, Ingenieros, Developers, Gamers
**Modelo:** 100% Online/Hibrido - Bootstrapping Total

---

## Inicio Rapido

1. Abri [`01-INICIO/README.md`](01-INICIO/README.md)
2. Segui el plan de lanzamiento
3. Usa las plantillas en `04-PLANTILLAS/`

---

## Estructura del Repositorio

```
LourdesBusiness/
│
├── 01-INICIO/                 # Empezar aqui - guia rapida
│   ├── README.md
│   └── INICIO-RAPIDO.md
│
├── 02-PLAN-NEGOCIO/           # Plan de negocio completo
│   ├── 01-resumen-ejecutivo.md
│   ├── 02-descripcion-empresa.md
│   ├── 03-analisis-mercado.md
│   ├── 04-plan-operaciones.md
│   ├── 05-estrategia-marketing.md
│   └── 06-plan-financiero.md
│
├── 03-IMPLEMENTACION/         # Guias de implementacion
│   ├── FASE-1-ESTUDIANTE.md
│   ├── FASE-2-LICENCIADA.md
│   ├── TRANSICION-PLAN.md
│   └── CHECKLIST-LANZAMIENTO.md
│
├── 04-PLANTILLAS/             # Templates para uso diario
│   ├── FICHA-CLIENTE-INICIAL.md
│   ├── NOTA-SESION-MANUAL.md
│   ├── PLAN-BIENESTAR.md
│   ├── FACTURA-RECIBO.md
│   └── SEGUIMIENTO-CLIENTE.md
│
├── 05-MARKETING/              # Materiales de marketing
│   ├── INSTAGRAM-CONTENT-PLAN.md
│   ├── WHATSAPP-SCRIPTS.md
│   ├── ELEVATOR-PITCH.md
│   └── FAQ-CLIENTES.md
│
├── 06-LEGAL/                  # Documentos legales
│   └── legal/
│       ├── consentimiento-informado.md
│       ├── consentimiento-analisis-ia.md
│       └── politica-privacidad.md
│
├── 07-DATOS/                  # Datos y ejemplos
│   └── PACIENTES/
│       └── 001-LOURDES/       # Ejemplo con datos reales
│           ├── RAW/           # Audios originales
│           ├── CLINICA/       # Transcripciones
│           └── METADATA/      # Analisis
│
├── 08-HERRAMIENTAS/           # Sistema de IA
│   ├── analisis/              # Modulo de analisis
│   ├── transcripcion/         # Sistema de transcripcion
│   └── plantillas/            # Templates de salida
│
├── config/                    # Configuracion
├── scripts/                   # Scripts (DEPRECADO - Ver 08-HERRAMIENTAS)
└── .sisyphus/                 # Notas internas
```

---

## Orden Logico de Trabajo

| #   | Carpeta        | Proposito   | Cuando Usar    |
| --- | -------------- | ----------- | -------------- |
| 01  | INICIO         | Orientacion | Primero        |
| 02  | PLAN-NEGOCIO   | Fundamentos | Planificacion  |
| 03  | IMPLEMENTACION | Como hacer  | Ejecucion      |
| 04  | PLANTILLAS     | Templates   | Dia a dia      |
| 05  | MARKETING      | Promocion   | Captacion      |
| 06  | LEGAL          | Documentos  | Compliance     |
| 07  | DATOS          | Ejemplos    | Referencia     |
| 08  | HERRAMIENTAS   | IA/Tech     | Automatizacion |

---

## Sistema de Transcripcion (Nuevo)

```bash
# Transcribir audios
python -m transcripcion transcribe --input 07-DATOS/PACIENTES/001-LOURDES/RAW

# Verificar calidad
python -m transcription check-quality --input 07-DATOS/PACIENTES/001-LOURDES/CLINICA

# Ayuda
python -m transcription --help
```

---

## Modelo de Negocio

### FASE 1: Estudiante (Actual)

| Aspecto       | Detalle                                         |
| ------------- | ----------------------------------------------- |
| **Servicios** | Coaching de bienestar (NO terapia clinica)      |
| **Target**    | Estudiantes de ingenieria, juniors tech, gamers |
| **Modalidad** | 100% Online                                     |
| **Legal**     | Divulgar estado estudiante                      |

### FASE 2: Licenciada (2027+)

| Aspecto            | Detalle                                 |
| ------------------ | --------------------------------------- |
| **Servicios**      | Psicoterapia completa + Analisis IA     |
| **Target**         | Profesionales Tech, CTOs                |
| **Diferenciacion** | Unica psicologa tech-native en Paraguay |

---

## Precios

| Tarifa    | Target              | Precio       |
| --------- | ------------------- | ------------ |
| Student   | Universitarios      | Gs. 70-90K   |
| Junior    | Young Professionals | Gs. 100-180K |
| Pro       | Seniors/Lideres     | Gs. 200-300K |
| Night Owl | Madrugada           | Gs. 250-350K |

---

## Aviso Legal

**FASE 1 (estudiante) - PUEDE:**

- Coaching de bienestar
- Apoyo emocional
- Mindfulness

**NO PUEDE:**

- Diagnosticos clinicos
- Tratamiento de trastornos
- Usar titulo "psicologa"

---

**Ultima Actualizacion:** Enero 2026
**Version:** 4.0
