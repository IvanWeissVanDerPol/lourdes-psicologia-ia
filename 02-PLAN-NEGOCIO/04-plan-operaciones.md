# PLAN DE OPERACIONES

---

## Resumen de Operaciones

| Aspecto | Detalle |
|---------|---------|
| **Modalidad** | Consultorio presencial + online opcional |
| **Horario** | 6-8 horas/día, 5-6 días/semana |
| **Capacidad** | 5-7 sesiones/día (máx 35-42/semana) |
| **Ubicación** | Asunción, zona accesible (por definir) |

---

## Flujo de Operaciones Diario

### **Día Típico de Trabajo**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DÍA TÍPICO - LOURDES                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   07:30 - 08:00    Preparación                                      │
│                    • Revisar agenda del día                         │
│                    • Leer notas de clientes programados            │
│                    • Preparar espacio                               │
│                                                                     │
│   08:00 - 12:00    Bloque Matutino (4 sesiones)                    │
│                    • Sesión 1: 08:00-08:50                         │
│                    • Descanso: 08:50-09:00                         │
│                    • Sesión 2: 09:00-09:50                         │
│                    • Descanso: 09:50-10:00                         │
│                    • Sesión 3: 10:00-10:50                         │
│                    • Descanso largo: 10:50-11:10                   │
│                    • Sesión 4: 11:10-12:00                         │
│                                                                     │
│   12:00 - 14:00    Almuerzo + Admin                                │
│                    • Procesar transcripciones mañana               │
│                    • Responder mensajes                            │
│                    • Almuerzo                                       │
│                                                                     │
│   14:00 - 18:00    Bloque Vespertino (3-4 sesiones)                │
│                    • Sesión 5: 14:00-14:50                         │
│                    • Sesión 6: 15:00-15:50                         │
│                    • Sesión 7: 16:00-16:50                         │
│                    • [Opcional] Sesión 8: 17:00-17:50              │
│                                                                     │
│   18:00 - 19:00    Cierre                                          │
│                    • Procesar transcripciones tarde                │
│                    • Actualizar perfiles de clientes               │
│                    • Preparar agenda siguiente día                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Proceso por Sesión

### **Pre-Sesión (5 minutos)**

1. **Revisar perfil del cliente**
   - Notas de última sesión
   - Tareas asignadas
   - Alertas del sistema IA

2. **Preparar espacio**
   - Ambiente adecuado
   - Agua disponible
   - Equipo de grabación listo

3. **Verificar consentimientos**
   - Grabación autorizada
   - Análisis WhatsApp (si aplica)

### **Durante la Sesión (50 minutos)**

1. **Inicio (5 min)**
   - Recibir al cliente
   - Check-in breve
   - Confirmar grabación

2. **Desarrollo (40 min)**
   - Trabajo terapéutico
   - Grabación en curso
   - Notas mentales de puntos clave

3. **Cierre (5 min)**
   - Resumen de la sesión
   - Tareas para la semana
   - Agendar próxima cita

### **Post-Sesión (10-15 minutos)**

1. **Procesar grabación**
   - Subir audio a Whisper
   - Esperar transcripción (~2-3 min)

2. **Análisis IA**
   - Enviar transcripción a Claude
   - Generar notas de sesión
   - Revisar y ajustar

3. **Actualizar perfil**
   - Agregar insights nuevos
   - Actualizar estado de tareas
   - Programar follow-up si necesario

---

## Gestión de Clientes

### **Ciclo de Vida del Cliente**

```
PROSPECTO → PRIMERA CONSULTA → CLIENTE ACTIVO → MANTENIMIENTO → ALTA
    ↓              ↓                  ↓              ↓           ↓
 Marketing    Evaluación         Tratamiento    Seguimiento  Cierre
 WhatsApp     Consentimientos    Sesiones       Mensual      Documentar
             Perfil inicial     Análisis IA    Check-ins    Referir si
                                                            necesario
```

### **Primera Consulta (Protocolo)**

| Paso | Tiempo | Actividad |
|------|--------|-----------|
| 1 | 10 min | Bienvenida, explicar servicio y sistema IA |
| 2 | 5 min | Revisar y firmar consentimientos |
| 3 | 30 min | Evaluación inicial, motivo de consulta |
| 4 | 10 min | Explicar plan propuesto, nivel de servicio |
| 5 | 5 min | Agendar siguientes sesiones, cobro |

### **Seguimiento Entre Sesiones**

| Nivel | Seguimiento |
|-------|-------------|
| **Básico** | Ninguno (solo en sesión) |
| **Premium** | Mensaje de check-in semanal (opcional) |
| **Intensivo** | Análisis WhatsApp continuo, alertas si necesario |

---

## Sistema de Citas

### **Canales de Agenda**

| Canal | Uso |
|-------|-----|
| **WhatsApp Business** | Principal - mensajes directos |
| **Google Calendar** | Gestión interna |
| **[Futuro] Calendly/Similar** | Auto-agendamiento |

### **Políticas de Citas**

| Política | Detalle |
|----------|---------|
| **Cancelación** | 24 horas de anticipación mínimo |
| **No-show** | Se cobra 50% si no avisa |
| **Reagendamiento** | Máximo 2 por mes sin cargo |
| **Lista de espera** | Contactar si hay cancelación |

### **Template de Confirmación (WhatsApp)**

```
Hola [Nombre]! 👋

Te confirmo tu cita:
📅 [Día], [Fecha]
⏰ [Hora]
📍 [Dirección/Link si online]

Recordá:
- Llegar 5 min antes
- Si necesitás cancelar, avisame con 24hs de anticipación

¡Nos vemos! 🙂
```

---

## Gestión del Sistema IA

### **Flujo de Procesamiento**

```
GRABACIÓN          TRANSCRIPCIÓN        ANÁLISIS           DOCUMENTACIÓN
    │                   │                  │                    │
    ↓                   ↓                  ↓                    ↓
[Audio .mp3]  →  [Whisper API]  →  [Claude API]  →  [SESSION_NOTES.md]
                      │                  │
                      ↓                  ↓
               [Texto plano]      [Insights JSON]
```

### **Tiempos de Procesamiento**

| Tarea | Tiempo Estimado |
|-------|-----------------|
| Transcripción (50 min audio) | 2-3 minutos |
| Análisis de sesión | 30-60 segundos |
| Análisis WhatsApp (1 mes) | 1-2 minutos |
| Generación de perfil completo | 3-5 minutos |

### **Mantenimiento del Sistema**

| Frecuencia | Tarea |
|------------|-------|
| **Diario** | Backup de archivos nuevos |
| **Semanal** | Revisar uso de APIs, costos |
| **Mensual** | Actualizar prompts si necesario |
| **Trimestral** | Auditar seguridad, limpiar datos obsoletos |

---

## Espacio Físico

### **Requisitos del Consultorio**

| Aspecto | Requisito |
|---------|-----------|
| **Tamaño** | Mínimo 15-20 m² |
| **Ubicación** | Zona accesible, transporte público |
| **Privacidad** | Insonorización adecuada |
| **Ambiente** | Iluminación natural, ventilación |
| **Baño** | Acceso cercano |
| **Estacionamiento** | Deseable pero no crítico |

### **Equipamiento Necesario**

| Categoría | Ítems |
|-----------|-------|
| **Mobiliario** | Sillón/diván, escritorio, sillas, estantes |
| **Tecnología** | Laptop, micrófono grabación, WiFi estable |
| **Ambiente** | Plantas, cuadros, iluminación regulable |
| **Consumibles** | Agua, pañuelos, snacks ligeros |
| **Seguridad** | Candados, backup de datos |

### **Layout Sugerido**

```
┌─────────────────────────────────────┐
│                                     │
│   ┌─────┐           ┌─────────┐    │
│   │Sillón│           │Escritorio│   │
│   │Cliente│          │ + Laptop│    │
│   └─────┘           └─────────┘    │
│                                     │
│   ┌─────┐                          │
│   │Silla │     🌱 Planta           │
│   │Lourdes│                         │
│   └─────┘                          │
│                                     │
│   ════════════════════════════════  │
│   Estante con libros/decoración    │
│                                     │
└─────────────────────────────────────┘
       [Puerta]
```

---

## Facturación y Cobros

### **Métodos de Pago**

| Método | Comisión | Notas |
|--------|----------|-------|
| **Efectivo** | 0% | Preferido para evitar comisiones |
| **Transferencia bancaria** | 0% | Confirmar antes de sesión |
| **Tarjeta de crédito** | 3-5% | Si cliente lo requiere |
| **QR (Tigo Money, etc.)** | 1-2% | Conveniente |

### **Política de Cobro**

- **Cobro:** Al final de cada sesión (o inicio, según preferencia)
- **Paquetes:** Pago adelantado con descuento
- **Planes mensuales:** Débito automático o pago al inicio del mes

### **Facturación**

| Tipo de Cliente | Documento |
|-----------------|-----------|
| **Persona física** | Boleta simple o factura |
| **Empresa (convenio)** | Factura con RUC |
| **Seguro médico** | Según requisitos del seguro |

---

## Contingencias

### **Plan B para Problemas Comunes**

| Problema | Solución |
|----------|----------|
| **Falla de internet** | Hotspot móvil de respaldo |
| **Falla de grabación** | Tomar notas manuales, transcribir después |
| **API no disponible** | Procesar en batch al final del día |
| **Cliente en crisis** | Protocolo de emergencia, referir si necesario |
| **Cancelación tardía** | Ofrecer reagendamiento, aplicar política |

### **Protocolo de Emergencia**

Si un cliente presenta riesgo:

1. **Evaluar nivel de riesgo** (ideación vs. plan activo)
2. **No dejar solo al cliente**
3. **Contactar a familiar/contacto de emergencia**
4. **Si riesgo inminente:** Acompañar a emergencias o llamar 911
5. **Documentar** todo lo ocurrido
6. **Seguimiento** en 24-48 horas

---

## Métricas Operativas

### **KPIs a Monitorear**

| Métrica | Meta | Frecuencia |
|---------|------|------------|
| **Sesiones/semana** | 30-35 | Semanal |
| **Tasa de ocupación** | 70-80% | Semanal |
| **Cancelaciones** | <15% | Mensual |
| **No-shows** | <5% | Mensual |
| **Tiempo promedio de procesamiento IA** | <15 min/sesión | Mensual |
| **Satisfacción cliente (NPS)** | >40 | Trimestral |

### **Dashboard Semanal**

```
SEMANA: [Fecha]
─────────────────────────────────────
Sesiones completadas:    [X] / [Y] programadas
Nuevos clientes:         [N]
Cancelaciones:           [N] ([%])
Ingresos brutos:         Gs. [X]M
Costo APIs:              Gs. [X]K
─────────────────────────────────────
```

---

## Herramientas de Gestión

### **Stack Tecnológico**

| Función | Herramienta |
|---------|-------------|
| **Agenda** | Google Calendar |
| **Comunicación** | WhatsApp Business |
| **Documentación** | Markdown (local) / Notion |
| **Facturación** | Excel / Software contable |
| **Transcripción** | OpenAI Whisper API |
| **Análisis** | Claude API / GPT-4 API |
| **Backup** | Google Drive (cifrado) |

### **Automatizaciones Futuras**

- [ ] Auto-confirmación de citas (24h antes)
- [ ] Recordatorio de tareas para clientes
- [ ] Alertas de patrones preocupantes
- [ ] Generación automática de reportes mensuales

---

## Documentos Relacionados

- [Plan Financiero](./06-plan-financiero.md) - Costos operativos
- [Sistema de IA](../10-AI-SYSTEM/README.md) - Detalles técnicos
- [Estrategia de Marketing](./05-estrategia-marketing.md) - Adquisición de clientes
