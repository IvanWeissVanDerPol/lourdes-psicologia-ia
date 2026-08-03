# 17. PLAN DE ANÁLISIS DE DATOS

## 17.1 Introducción

Este apartado detalla las estrategias de análisis de datos que se aplicarán para evaluar los efectos de la intervención sobre la atención sostenida y las variables asociadas. Dado que se trata de un **diseño de caso único (N=1) con cambio de criterio**, el análisis se centra en:

1. **Análisis visual de series temporales**
2. **Análisis estadístico mediante índices de no solapamiento**
3. **Análisis complementario de datos cuantitativos (pre-post)**
4. **Análisis cualitativo de entrevistas y observaciones**

El plan de análisis sigue las recomendaciones metodológicas de Kazdin (2011), Kratochwill et al. (2013), y la What Works Clearinghouse (WWC) para estudios de caso único.

---

## 17.2 Tipos de Datos Recopilados

### 17.2.1 Datos Cuantitativos

| Variable | Instrumento/Método | Tipo de Dato | Momento de Medición |
|----------|-------------------|--------------|---------------------|
| **Atención sostenida** | Tarea de cancelación de símbolos con cronómetro | Continuo (minutos de atención activa) | Línea base (Sesión 0), Sesiones 1-4, Post-evaluación (Sesión 5) |
| **Memoria de trabajo** | WISC-5: Retención de Dígitos | Continuo (puntaje bruto) | Pre (Sesión 0), Post (Sesión 5) |
| **Capacidad de resolución aritmética** | WISC-5: Aritmética | Continuo (puntaje bruto) | Pre (Sesión 0), Post (Sesión 5) |
| **Capacidad intelectual** | Test de Raven (Escala Coloreada) | Continuo (percentil) | Pre (Sesión 0) |
| **Percepción visomotora** | Test de Bender | Ordinal (indicadores de dificultad) | Pre (Sesión 0) |
| **Cumplimiento de criterio por sesión** | Registro del terapeuta | Dicotómico (Sí/No) | Sesiones 1-4 |

### 17.2.2 Datos Cualitativos

| Variable | Método de Recopilación | Tipo de Dato | Momento |
|----------|------------------------|--------------|---------|
| **Observaciones conductuales** | Registro narrativo del terapeuta | Textual | Todas las sesiones (0-5) |
| **Percepción de cambio del niño** | Entrevista semi-estructurada | Textual (transcripción) | Post (Sesión 5) |
| **Percepción de cambio de los padres** | Entrevista semi-estructurada | Textual (transcripción) | Post (Sesión 5) |
| **Uso de estrategias en contexto natural** | Reporte verbal del niño y padres | Textual | Post (Sesión 5) |

---

## 17.3 Análisis Visual de Series Temporales

El análisis visual es el método **primario y más importante** para evaluar los efectos de la intervención en diseños de caso único. Consiste en examinar gráficamente los datos a lo largo del tiempo para identificar patrones, cambios y relaciones funcionales entre la intervención y la variable dependiente.

### 17.3.1 Construcción del Gráfico de Series Temporales

**Eje X (horizontal):** Sesiones (0, 1, 2, 3, 4, 5)

**Eje Y (vertical):** Minutos de atención sostenida (rango: 0-20 minutos)

**Fases demarcadas:**
- **Fase A (Línea Base):** Sesión 0
- **Fase B1 (Criterio 7 min):** Sesión 1
- **Fase B2 (Criterio 10 min):** Sesión 2
- **Fase B3 (Criterio 12 min):** Sesión 3
- **Fase B4 (Criterio 15 min):** Sesión 4
- **Fase Follow-up (Post-evaluación):** Sesión 5

**Representación visual:**
- Puntos conectados por líneas
- Líneas verticales punteadas separando fases
- Líneas horizontales indicando los criterios de cada fase (7, 10, 12, 15 minutos)

**Ejemplo de gráfico:**

```
Minutos de Atención Sostenida a lo Largo de las Sesiones

20 |                                                         ●
   |                                                    ●
18 |                                               ●
   |
16 |                                          ●
   |
14 |                                     ●
   |                               ●
12 |                          ● --|--Criterio 12 min------
   |                     ●
10 |                ● --|--Criterio 10 min-----------------
   |           ●
 8 |      ● --|--Criterio 7 min------------------------
   | ●
 6 |
   |
 4 |
   |
 2 |
   |
 0 |_____|_____|_____|_____|_____|_____|
      S0    S1    S2    S3    S4    S5
    Línea  B1    B2    B3    B4   Post
    Base
```

### 17.3.2 Criterios de Análisis Visual (Parsonson & Baer, 1978)

El análisis visual evalúa **seis dimensiones** de los datos:

#### 1. **Nivel (Level)**

**Definición:** El valor promedio de los datos dentro de cada fase.

**Análisis:**
- Calcular la media de atención sostenida en la línea base.
- Calcular la media en cada fase de intervención.
- Comparar niveles entre fases: ¿Hay un aumento progresivo?

**Ejemplo:**
- Línea base: Media = 5 minutos
- Fase B1: Media = 7 minutos
- Fase B2: Media = 10 minutos
- Fase B3: Media = 12 minutos
- Fase B4: Media = 15 minutos

**Interpretación:** Aumento progresivo del nivel indica efecto de la intervención.

#### 2. **Tendencia (Trend)**

**Definición:** La dirección y magnitud del cambio dentro de una fase (ascendente, descendente, o estable).

**Análisis:**
- Inspeccionar visualmente la pendiente de la línea en cada fase.
- Utilizar la técnica de "split-middle" (dividir la fase a la mitad y comparar medias) para calcular la tendencia.

**Interpretación:**
- Tendencia ascendente en fases de intervención: Mejora progresiva.
- Tendencia estable en línea base: Estabilidad pre-intervención (ideal).

#### 3. **Variabilidad (Variability)**

**Definición:** El grado de fluctuación de los datos alrededor de la media.

**Análisis:**
- Calcular el rango (valor máximo - valor mínimo) dentro de cada fase.
- Calcular la desviación estándar (si hay múltiples mediciones por fase).
- Inspeccionar visualmente la dispersión de los puntos.

**Interpretación:**
- **Baja variabilidad** (datos estables): Facilita la detección de cambios debidos a la intervención.
- **Alta variabilidad** (datos erráticos): Dificulta la interpretación; puede indicar influencia de variables no controladas.

#### 4. **Inmediatez del Efecto (Immediacy of Effect)**

**Definición:** Qué tan rápido se observa un cambio al introducir la intervención.

**Análisis:**
- Comparar el último dato de una fase con el primer dato de la siguiente fase.
- Calcular la diferencia: ¿Hay un "salto" inmediato?

**Interpretación:**
- **Cambio inmediato y abrupto:** Fuerte evidencia de efecto de la intervención.
- **Cambio gradual:** Efecto más débil o influencia de otras variables.

#### 5. **Solapamiento (Overlap)**

**Definición:** El grado en que los datos de diferentes fases se superponen en el rango de valores.

**Análisis:**
- Determinar cuántos puntos de la fase de intervención caen dentro del rango de la línea base.
- **Bajo solapamiento** (0-25%): Efecto fuerte.
- **Solapamiento moderado** (25-50%): Efecto moderado.
- **Alto solapamiento** (>50%): Efecto débil o nulo.

**Interpretación:**
- Idealmente, los datos de intervención deben estar **completamente por encima** de los datos de línea base en estudios de aumento de conducta (como atención sostenida).

#### 6. **Consistencia de los Datos entre Fases Similares (Consistency)**

**Definición:** Si se replican fases (ej: múltiples líneas base), ¿los patrones son consistentes?

**Análisis:**
- En este estudio, no hay replicación de fases idénticas, pero se evalúa la **consistencia del patrón de mejora progresiva** a través de las fases B1-B4.

**Interpretación:**
- Si cada fase muestra mejora respecto a la anterior, hay consistencia que apoya la validez del efecto.

---

### 17.3.3 Decisión Basada en Análisis Visual

Después del análisis visual, se tomará una **decisión sobre la efectividad de la intervención**:

| Criterio | Decisión |
|----------|----------|
| **Cambio de nivel marcado + Tendencia ascendente + Bajo solapamiento + Inmediatez del efecto** | **Intervención EFECTIVA** |
| **Cambio de nivel moderado + Variabilidad baja + Solapamiento parcial** | **Intervención PROBABLEMENTE EFECTIVA** |
| **Sin cambio de nivel + Alto solapamiento + Tendencia inestable** | **Intervención NO EFECTIVA** |

---

## 17.4 Análisis Estadístico: Índices de No Solapamiento

Aunque el análisis visual es primario, se complementará con **índices estadísticos de no solapamiento** para cuantificar la magnitud del efecto (Kratochwill et al., 2013).

### 17.4.1 Porcentaje de Datos No Solapantes (PND - Percentage of Non-Overlapping Data)

**Definición:** El porcentaje de datos de la fase de intervención que exceden el punto más alto de la fase de línea base.

**Fórmula:**

\[
PND = \frac{\text{Número de puntos de intervención que superan el máximo de línea base}}{\text{Total de puntos de intervención}} \times 100
\]

**Ejemplo:**
- Línea base (Sesión 0): 5 minutos (punto único)
- Sesiones de intervención (S1-S4): 7, 10, 12, 15 minutos
- Máximo de línea base: 5 minutos
- Puntos de intervención que superan 5 min: 4 de 4
- PND = (4/4) × 100 = **100%**

**Interpretación (Scruggs & Mastropieri, 1998):**
- **PND > 90%:** Tratamiento muy efectivo
- **PND 70-90%:** Tratamiento efectivo
- **PND 50-70%:** Tratamiento cuestionable
- **PND < 50%:** Tratamiento inefectivo

### 17.4.2 Porcentaje de Todos los Datos No Solapantes (PAND)

**Definición:** Similar al PND, pero considera todos los datos (no solo el punto más alto de línea base).

**Ventaja:** Más sensible que PND cuando hay variabilidad.

### 17.4.3 No Solapamiento de Todos los Pares (NAP - Nonoverlap of All Pairs)

**Definición:** Compara cada dato de intervención con cada dato de línea base y calcula el porcentaje de comparaciones favorables.

**Fórmula:**

\[
NAP = \frac{\text{Número de pares en que intervención > línea base}}{\text{Total de pares}} \times 100
\]

**Interpretación:**
- **NAP > 0.93:** Efecto muy grande
- **NAP 0.66-0.92:** Efecto grande
- **NAP 0.50-0.65:** Efecto mediano
- **NAP < 0.50:** Efecto pequeño o nulo

### 17.4.4 Tau-U

**Definición:** Índice que combina el no solapamiento con el control de tendencia baseline.

**Ventaja:** Controla la tendencia en línea base, lo cual es importante si ya había mejora antes de la intervención.

**Interpretación:**
- **Tau-U > 0.80:** Efecto grande
- **Tau-U 0.60-0.80:** Efecto moderado
- **Tau-U < 0.60:** Efecto pequeño

**Software recomendado para cálculo:** Web-based Tau-U calculator (disponible en línea gratuitamente).

---

## 17.5 Análisis Pre-Post de Variables Cuantitativas

Para las variables evaluadas antes y después de la intervención (memoria de trabajo, aritmética), se realizará un **análisis descriptivo comparativo**:

### 17.5.1 Tabla de Comparación Pre-Post

| Variable | Pre (Sesión 0) | Post (Sesión 5) | Diferencia | Cambio (%) |
|----------|----------------|-----------------|------------|------------|
| **Retención de Dígitos (WISC-5)** | [puntaje] | [puntaje] | [diferencia] | [%] |
| **Aritmética (WISC-5)** | [puntaje] | [puntaje] | [diferencia] | [%] |
| **Atención sostenida (tarea de cancelación)** | [X min] | [Y min] | [Y-X min] | [(Y-X)/X × 100] |

**Interpretación:**
- **Diferencia positiva:** Mejora post-intervención.
- **Diferencia negativa:** Deterioro (poco probable en este contexto).
- **Sin diferencia:** Sin cambio.

### 17.5.2 Cambio Clínicamente Significativo

Más allá de la significancia estadística (no aplicable en N=1 con test de hipótesis tradicional), se evaluará la **significancia clínica**:

**Criterio:** ¿La mejora observada es suficientemente grande para tener un impacto práctico en la vida del niño?

**Ejemplo:**
- Si la atención sostenida aumenta de 5 a 15 minutos (mejora del 200%), esto tiene **alta significancia clínica** porque permite al niño completar tareas escolares que antes no podía.
- Si aumenta de 5 a 6 minutos (mejora del 20%), aunque haya cambio, la **significancia clínica es baja**.

**Referencia:** Jacobson & Truax (1991) - Reliable Change Index (RCI)

---

## 17.6 Análisis Cualitativo

### 17.6.1 Análisis de Observaciones Conductuales

**Método:** Análisis temático de las notas de campo del terapeuta.

**Procedimiento:**
1. Leer todas las observaciones conductuales de las sesiones 0-5.
2. Identificar **patrones recurrentes** (ej: "inquietud motora disminuye progresivamente", "uso espontáneo de respiración en sesión 4").
3. Codificar observaciones en **categorías temáticas**:
   - Autorregulación emocional
   - Uso espontáneo de estrategias
   - Persistencia ante dificultades
   - Interacción con el terapeuta
   - Motivación
4. Redactar síntesis narrativa de cada categoría.

### 17.6.2 Análisis de Entrevistas

**Método:** Análisis de contenido de las entrevistas finales (niño y padres).

**Procedimiento:**
1. **Transcripción:** Transcribir literalmente las entrevistas de audio (si se grabaron) o utilizar notas detalladas.
2. **Lectura inicial:** Familiarizarse con el contenido completo.
3. **Codificación abierta:** Identificar unidades de significado relevantes (frases, oraciones).
4. **Categorización:** Agrupar códigos en categorías temáticas:
   - **Percepción de cambio** (¿El niño/padres notan mejora?)
   - **Generalización de estrategias** (¿Usa las técnicas en casa/escuela?)
   - **Impacto en vida cotidiana** (¿Hay cambios en tareas escolares, rutinas?)
   - **Satisfacción con la intervención** (¿Qué les gustó? ¿Qué mejorarían?)
5. **Triangulación:** Comparar datos cualitativos (entrevistas) con datos cuantitativos (mejora en atención) para buscar consistencia o discrepancias.

**Ejemplo de cita textual:**
> "Antes [nombre del niño] no podía hacer la tarea de matemática sin levantarse cada dos minutos. Ahora se sienta, respira como le enseñaron, y puede trabajar 10-15 minutos seguidos. Es un cambio enorme." (Madre del participante, Sesión 5)

---

## 17.7 Integración de Resultados: Triangulación de Datos

La **triangulación** consiste en integrar múltiples fuentes de datos (cuantitativos y cualitativos) para obtener una comprensión completa y robusta de los efectos de la intervención.

### 17.7.1 Matriz de Triangulación

| Dimensión | Datos Cuantitativos | Datos Cualitativos | Convergencia |
|-----------|---------------------|--------------------|--------------| |
| **Mejora en atención sostenida** | Aumento de 5 a 15 minutos en tarea de cancelación (PND=100%) | Padres reportan: "Puede hacer la tarea sin distraerse tanto" | ✓ **Convergente** |
| **Uso de estrategias** | Observación directa en sesiones: uso de respiración antes de tareas | Niño reporta: "Uso la respiración cuando tengo que estudiar" | ✓ **Convergente** |
| **Impacto académico** | Mejora en subtest Aritmética WISC-5 (pre: X, post: X+2) | Docentes reportan mejora en seguimiento de instrucciones (si se recopila) | ✓ **Convergente** |

**Interpretación:**
- **Convergencia:** Los datos cuantitativos y cualitativos apuntan en la misma dirección → **Alta confiabilidad de los resultados**.
- **Divergencia:** Los datos cuantitativos muestran mejora pero los cualitativos no (o viceversa) → **Requiere análisis adicional y cautela en las conclusiones**.

---

## 17.8 Criterios de Éxito de la Intervención

Se considerará que la intervención fue **exitosa** si se cumplen los siguientes criterios:

| Criterio | Indicador | Meta |
|----------|-----------|------|
| **1. Aumento en atención sostenida** | Minutos de atención en tarea de cancelación | ≥ 10 minutos de aumento (de 5 a 15 min) |
| **2. Cumplimiento de criterios progresivos** | Número de sesiones en que se cumplió el criterio | ≥ 3 de 4 sesiones de intervención |
| **3. Análisis visual positivo** | Patrón de datos en gráfico de series temporales | Cambio de nivel + Tendencia ascendente + Bajo solapamiento |
| **4. Índice PND** | Porcentaje de datos no solapantes | PND ≥ 70% |
| **5. Percepción subjetiva de mejora** | Entrevistas con niño y padres | Reporte positivo de cambio en contexto natural |
| **6. Generalización de estrategias** | Uso de técnicas en casa/escuela | Reporte de uso en al menos 2 contextos diferentes |

**Resultado final:**
- **Éxito completo:** Se cumplen 5-6 criterios.
- **Éxito parcial:** Se cumplen 3-4 criterios.
- **No exitoso:** Se cumplen ≤2 criterios.

---

## 17.9 Software y Herramientas de Análisis

### 17.9.1 Software para Análisis Cuantitativo

| Software | Uso | Costo | Acceso |
|----------|-----|-------|--------|
| **Microsoft Excel** | Gráficos de series temporales, cálculos de PND, NAP | Incluido en Microsoft Office (licencia institucional) | Disponible |
| **GraphPad Prism** | Gráficos de alta calidad para publicación | Licencia comercial (~USD 99/año) | Opcional |
| **Jamovi** | Análisis estadístico descriptivo, alternativa gratuita a SPSS | Gratuito | Disponible |
| **Tau-U Calculator** (web) | Cálculo de Tau-U | Gratuito | www.singlecaseresearch.org |
| **R (paquete "scan")** | Análisis avanzado de diseños de caso único | Gratuito | Disponible (requiere aprendizaje) |

**Recomendación:** Usar **Excel** para análisis básico y gráficos, complementar con **Tau-U calculator** online para índices de no solapamiento.

### 17.9.2 Software para Análisis Cualitativo

| Software | Uso | Costo | Acceso |
|----------|-----|-------|--------|
| **NVivo** | Análisis de contenido, codificación | Licencia comercial (~USD 300/año) | Opcional |
| **ATLAS.ti** | Análisis de contenido | Licencia comercial | Opcional |
| **Análisis manual** | Codificación en Word/Excel | Gratuito | Disponible |

**Recomendación:** Dado el volumen reducido de datos cualitativos (2-3 entrevistas), el **análisis manual** en Word/Excel es suficiente y apropiado.

---

## 17.10 Cronograma de Análisis de Datos

| Semana | Actividad de Análisis | Tiempo Estimado |
|--------|----------------------|-----------------|
| **Semana 13** | Ingreso de datos cuantitativos en Excel | 4 horas |
| **Semana 13** | Elaboración de gráfico de series temporales | 2 horas |
| **Semana 13** | Análisis visual según criterios de Parsonson & Baer | 3 horas |
| **Semana 13** | Cálculo de índices PND, NAP, Tau-U | 2 horas |
| **Semana 13** | Análisis pre-post de WISC-5 | 2 horas |
| **Semana 14** | Transcripción y lectura de entrevistas | 4 horas |
| **Semana 14** | Codificación temática de datos cualitativos | 4 horas |
| **Semana 14** | Análisis de observaciones conductuales | 3 horas |
| **Semana 14** | Triangulación de datos cuanti-cuali | 2 horas |
| **Semana 14** | Redacción de sección "Resultados" | 6 horas |
| **Total** | | **32 horas** |

---

## 17.11 Presentación de Resultados

### 17.11.1 Estructura de la Sección "Resultados" del Informe

1. **Introducción**
   - Recordatorio de objetivos e hipótesis

2. **Resultados Cuantitativos**
   - **Gráfico de series temporales** (figura principal)
   - **Análisis visual:** Descripción de nivel, tendencia, variabilidad, inmediatez, solapamiento
   - **Índices estadísticos:** Tabla con PND, NAP, Tau-U
   - **Comparación pre-post:** Tabla con datos de WISC-5 y atención sostenida

3. **Resultados Cualitativos**
   - **Observaciones conductuales:** Síntesis narrativa con ejemplos concretos
   - **Percepción de cambio:** Citas textuales de entrevistas con niño y padres
   - **Generalización:** Descripción de uso de estrategias en contextos naturales

4. **Integración de Resultados**
   - **Matriz de triangulación:** Tabla comparativa
   - **Síntesis:** Respuesta a cada hipótesis específica

5. **Cumplimiento de Criterios de Éxito**
   - Tabla resumen indicando si se cumplió cada criterio

### 17.11.2 Figuras y Tablas Esperadas

| Figura/Tabla | Título | Contenido |
|--------------|--------|-----------|
| **Figura 1** | Gráfico de series temporales de atención sostenida a lo largo de las sesiones | Datos de minutos de atención por sesión con fases demarcadas |
| **Tabla 1** | Índices de no solapamiento | PND, NAP, Tau-U con interpretación |
| **Tabla 2** | Comparación pre-post de variables cognitivas | Retención de Dígitos, Aritmética, Atención sostenida |
| **Tabla 3** | Cumplimiento de criterios por sesión | Sesiones 1-4, criterio establecido, minutos logrados, cumplimiento (Sí/No) |
| **Tabla 4** | Criterios de éxito de la intervención | Los 6 criterios con indicadores y cumplimiento |

---

## 17.12 Limitaciones del Análisis

### 17.12.1 Limitaciones Inherentes al Diseño N=1

- **Generalización limitada:** Los resultados son específicos a este participante; no se pueden generalizar automáticamente a todos los niños con TDA.
- **Ausencia de grupo control:** No hay comparación con un grupo que no recibe intervención (aunque el diseño de cambio de criterio mitiga parcialmente esta limitación).
- **Efecto del evaluador:** El terapeuta que implementa la intervención es quien registra los datos (posible sesgo).

### 17.12.2 Estrategias para Mitigar Limitaciones

- **Registro objetivo de la variable dependiente:** Uso de cronómetro y criterios operacionales claros para minimizar subjetividad.
- **Análisis visual + estadístico:** Complementar ambos enfoques para mayor robustez.
- **Triangulación:** Integrar múltiples fuentes de datos (cuantitativos, cualitativos, percepción de terceros).
- **Replicación conceptual:** Recomendar replicación del estudio con otros participantes para evaluar generalización.

---

## 17.13 Consideraciones Éticas del Análisis de Datos

- **Honestidad:** Se reportarán todos los datos tal como fueron recopilados, sin omitir datos "inconvenientes" o negativos.
- **Transparencia:** Se describirán detalladamente los métodos de análisis para permitir replicación.
- **Confidencialidad:** En la presentación de resultados cualitativos (citas textuales), se eliminarán nombres y datos identificables.

---

## 17.14 Conclusión

Este plan de análisis de datos proporciona una estrategia integral, rigurosa y apropiada para evaluar los efectos de una intervención conductual-cognitiva en un diseño de caso único con cambio de criterio. La combinación de:

- **Análisis visual detallado**
- **Índices estadísticos de no solapamiento**
- **Análisis pre-post de variables complementarias**
- **Análisis cualitativo de percepciones y observaciones**
- **Triangulación de múltiples fuentes de datos**

...asegura que los resultados sean **válidos, confiables y significativos** tanto desde una perspectiva científica como clínica.

El análisis permitirá responder con confianza si la intervención fue efectiva para aumentar la atención sostenida del participante y si las técnicas de psicohigiene y reforzamiento positivo lograron generalizarse a contextos naturales, cumpliendo así con los objetivos del estudio.

---
