# Checklist de Lanzamiento Completo

> **Uso:** Verificar que todo esta listo antes de empezar a operar
> **Aplica a:** Fase 1 (Estudiante) inicialmente

---

## Semana 1: Identidad y Setup Basico

### Identidad de Marca

- [ ] **Elegir nombre de fantasia**
  - Opciones: Debug Mental, MindSet Lab, Espacio Calma, Reset Button
  - Ver `08-LEGAL-BRANDING/branding/GUIA-MARCA.md`

- [ ] **Definir estilo visual**
  - Colores primarios elegidos
  - Tipografia definida
  - Tono de comunicacion claro

### Cuentas y Perfiles

- [ ] **Instagram profesional**
  - Username disponible y reservado
  - Foto de perfil profesional
  - Bio completa con CTA
  - Link en bio (Linktree o similar)

- [ ] **WhatsApp Business**
  - Numero separado del personal
  - Perfil de negocio configurado
  - Catalogo de servicios
  - Respuestas automaticas

- [ ] **Discord (opcional)**
  - Servidor creado
  - Canales basicos configurados
  - Reglas de comunidad

- [ ] **Calendly/Cal.com**
  - Cuenta creada
  - Horarios disponibles configurados
  - Integracion con Google Calendar
  - Link personalizado

---

## Semana 2: Contenido Inicial

### Instagram

- [ ] **9 posts iniciales creados** (llenar grid)
  - 3 posts educativos
  - 3 posts personales/storytelling
  - 3 posts de servicio

- [ ] **Bio optimizada**
  ```
  [Nombre] | Coach de Bienestar Tech
  Estudiante de Psicologia - 5to ano
  Disponible 24/7 | Text-first
  Agenda tu sesion
  [Link]
  ```

- [ ] **Highlights configurados**
  - Sobre mi
  - Servicios
  - Testimonios (cuando los tengas)
  - FAQ

### WhatsApp

- [ ] **Mensaje de bienvenida**
  ```
  Hola! Gracias por contactarme.

  Soy [Nombre], estudiante de psicologia especializada en bienestar para profesionales tech.

  ¿En que puedo ayudarte?
  1. Quiero agendar una sesion
  2. Tengo preguntas sobre el servicio
  3. Solo estoy explorando

  Respondo en menos de 24 horas (usualmente mucho antes).
  ```

- [ ] **Mensaje fuera de horario**
  ```
  Hola! Estoy descansando ahora (1am-5:30am).
  Tu mensaje es importante para mi y te respondo apenas despierte.

  Si es urgente y necesitas hablar con alguien AHORA:
  [Linea de crisis Paraguay]
  ```

---

## Semana 3: Legal y Administrativo

### Documentos Legales

- [ ] **Consentimiento informado impreso/digital**
  - Incluye divulgacion de estado estudiante
  - Explicacion clara del servicio
  - Limites de confidencialidad
  - Ver `08-LEGAL-BRANDING/legal/consentimiento-informado.md`

- [ ] **Politica de privacidad**
  - Disponible para compartir si preguntan
  - Ver `08-LEGAL-BRANDING/legal/politica-privacidad.md`

- [ ] **Consentimiento IA (si usas)**
  - Solo si vas a usar el sistema de analisis
  - Ver `08-LEGAL-BRANDING/legal/consentimiento-analisis-ia.md`

### Finanzas

- [ ] **Metodo de pago configurado**
  - Transferencia bancaria
  - Billetera electronica (Tigo Money, Personal Pay)
  - Datos para factura simple

- [ ] **Precios finales definidos**
  | Tarifa | Precio |
  |--------|--------|
  | Student | Gs. ___ |
  | Junior | Gs. ___ |
  | Night Owl | Gs. ___ |

- [ ] **Politica de cancelacion**
  - 24 horas de anticipacion
  - Que pasa si no avisa
  - Reprogramacion

### Red de Referencia

- [ ] **2-3 psicologos licenciados** para derivar casos clinicos
  - Nombre: ___
  - Contacto: ___

- [ ] **1 psiquiatra** para casos que necesiten medicacion
  - Nombre: ___
  - Contacto: ___

- [ ] **Lineas de crisis Paraguay**
  - Numero: ___

---

## Semana 4: Beta Test

### Reclutamiento

- [ ] **Lista de 5+ beta testers**
  - Amigos/conocidos del rubro TI
  - Dispuestos a dar feedback honesto

- [ ] **Propuesta clara**
  ```
  "Estoy lanzando mi servicio de coaching de bienestar
  para gente de tech. ¿Te gustaria probar una sesion
  gratis a cambio de feedback honesto?"
  ```

### Ejecucion

- [ ] **3-5 sesiones de prueba completadas**

- [ ] **Feedback recopilado**
  - ¿Que funciono?
  - ¿Que no funciono?
  - ¿Pagarias por esto? ¿Cuanto?
  - ¿Me referirias a alguien?

- [ ] **Ajustes realizados** segun feedback

---

## Post-Lanzamiento: Primeras 2 Semanas

### Operaciones

- [ ] **Primer cliente pagado** (no beta)
- [ ] **Flujo completo validado**
  - Contacto → Agenda → Pago → Sesion → Seguimiento

- [ ] **Sistema de notas funcionando**
  - Notion/Obsidian configurado
  - Template de sesion listo

### Marketing

- [ ] **Publicacion consistente**
  - 3-5 posts por semana
  - Stories diarias (opcional)

- [ ] **Primeros referidos** solicitados
  ```
  "Si conoces a alguien que podria beneficiarse
  de esto, me ayudarias mucho compartiendole mi perfil."
  ```

---

## Sistema IA (Opcional - Cuando Estes Lista)

### Setup Tecnico

- [ ] **API keys configuradas**
  - OPENAI_API_KEY en variables de entorno
  - ANTHROPIC_API_KEY en variables de entorno

- [ ] **Dependencias instaladas**
  ```bash
  pip install -r 10-AI-SYSTEM/analysis/requirements.txt
  ```

- [ ] **Test con audio de prueba**
  ```bash
  python -m analysis.transcriber audio_prueba.mp3
  ```

- [ ] **Test con transcripcion**
  ```bash
  python -m analysis.analyzer transcripcion_prueba.txt
  ```

### Integracion al Flujo

- [ ] **Consentimiento IA firmado** por cliente
- [ ] **Proceso de grabacion** definido
- [ ] **Almacenamiento seguro** de transcripciones

---

## Verificacion Final

### Go/No-Go Checklist

| Item | Listo | Bloqueante |
|------|-------|------------|
| Instagram activo | [ ] | Si |
| WhatsApp configurado | [ ] | Si |
| Consentimiento listo | [ ] | Si |
| Metodo de pago | [ ] | Si |
| Al menos 1 beta test | [ ] | Si |
| Red de referencia | [ ] | Si |
| Calendly funcionando | [ ] | No |
| Discord listo | [ ] | No |
| Sistema IA probado | [ ] | No |

**Si todos los items "Bloqueante: Si" estan listos, podes lanzar.**

---

## Notas

- No necesitas todo perfecto para empezar
- Es mejor lanzar y ajustar que esperar eternamente
- Los primeros clientes van a ayudarte a mejorar
- El sistema IA puede agregarse despues

---

*Checklist actualizado - Enero 2026*
