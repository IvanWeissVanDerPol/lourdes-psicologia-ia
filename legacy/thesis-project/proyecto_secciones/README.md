# PROYECTO DE INVESTIGACIÓN - ESTRUCTURA MODULAR

## 📁 Organización del Proyecto

Este proyecto está organizado en **archivos individuales por sección** para facilitar:
- ✅ Edición colaborativa (cada persona trabaja en su archivo)
- ✅ Control de versiones más claro
- ✅ Facilidad para revisar secciones específicas
- ✅ Consolidación automática en documento final

---

## 📂 Estructura de Archivos

```
proyecto_secciones/
│
├── 00_portada.md                      # Portada del proyecto
├── 01_indice.md                       # Índice general
├── 02_resumen.md                      # Resumen (247 palabras)
├── 03_palabras_clave.md               # Palabras clave
├── 04_introduccion.md                 # Introducción
├── 05_politicas_institucionales.md    # Políticas y pertinencia
├── 06_fundamentacion_teorica.md       # Antecedentes, marco conceptual, justificación
├── 07_planteamiento_problema.md       # Planteamiento del problema
├── 08_hipotesis.md                    # Hipótesis general y específicas
├── 09_objetivos.md                    # Objetivo general y específicos
├── 10_variables.md                    # Variables de estudio (exhaustivo)
├── 11_metodologia.md                  # Metodología completa
├── 12_estrategia_implementacion.md    # Estrategia de implementación
├── 13_descripcion_sesiones.md         # Descripción detallada de sesiones
├── 14_cronograma.md                   # Plan de trabajo y cronograma
├── 15_presupuesto.md                  # Presupuesto y recursos
├── 16_aspectos_eticos.md              # Aspectos éticos
├── 17_analisis_datos.md               # Plan de análisis de datos
├── 18_resultados_esperados.md         # Resultados esperados
├── 19_limitaciones.md                 # Limitaciones del estudio
├── 20_aportes.md                      # Aportes y relevancia
├── 21_referencias.md                  # Referencias bibliográficas (APA 7)
├── 22_anexos.md                       # Anexos
│
├── dividir_proyecto.py                # Script gestor principal
├── extraer_secciones.py               # Script extractor de secciones
└── consolidar.py                      # Script de consolidación rápida
```

---

## 🚀 CÓMO USAR

### 1. Verificar Estado del Proyecto

```bash
python dividir_proyecto.py verificar
```

Esto muestra:
- ✅ Qué secciones ya existen
- ⚠️ Qué secciones faltan
- 📊 Estadísticas (tamaño, completitud)

### 2. Editar una Sección

1. Abrir el archivo correspondiente (ej: `09_objetivos.md`)
2. Editar el contenido
3. Guardar

**Ejemplo**: Para editar los objetivos, abrir `09_objetivos.md` y modificar.

### 3. Consolidar Todo en un Documento Final

```bash
python dividir_proyecto.py consolidar
```

Esto crea el archivo:
```
../PROYECTO_FINAL_CONSOLIDADO.md
```

Con TODAS las secciones en orden, listo para:
- Convertir a Word
- Enviar al profesor
- Imprimir

### 4. Crear Plantillas para Secciones Faltantes

```bash
python dividir_proyecto.py crear-plantillas
```

Esto crea archivos de plantilla para las secciones que aún no existen.

---

## 👥 TRABAJO EN EQUIPO

### Asignación de Secciones por Persona

**AYELEN** (responsable de formato y estructura):
- `00_portada.md` - Completar datos personales
- `01_indice.md` - Actualizar números de página
- `14_cronograma.md` - Crear cronograma detallado con fechas
- `19_limitaciones.md` - Identificar limitaciones y sesgos
- `21_referencias.md` - Formatear todas las referencias en APA 7

**VIVIAN** (responsable de metodología e instrumentos):
- `10_variables.md` - Verificar y completar si falta algo
- `11_metodologia.md` - Verificar instrumentos descritos
- Agregar cualquier detalle faltante sobre control de variables

**MIRANDA** (responsable de ética y resultados):
- `16_aspectos_eticos.md` - Desarrollar completamente
- `18_resultados_esperados.md` - Especificar resultados vinculados a hipótesis
- `20_aportes.md` - Describir aportes del estudio

**LOURDES** (responsable de sesiones y logística):
- `12_estrategia_implementacion.md` - Detallar estrategia
- `13_descripcion_sesiones.md` - Protocolo sesión por sesión
- `15_presupuesto.md` - Tabla detallada de presupuesto
- `22_anexos.md` - Organizar todos los anexos

**TODAS** (revisión):
- `17_analisis_datos.md` - Plan de cómo analizar los resultados

### Flujo de Trabajo Recomendado

1. **Cada persona trabaja en sus archivos asignados**
   - Editar localmente
   - Guardar frecuentemente

2. **Comunicación en grupo**
   - Messaging/email para coordinación
   - Revisar que no haya contradicciones entre secciones

3. **Consolidación periódica**
   - Una vez por semana, consolidar para ver el documento completo
   - Revisar coherencia entre secciones

4. **Revisión cruzada**
   - Intercambiar secciones para revisión
   - Cada una revisa el trabajo de otra

5. **Consolidación final**
   - Antes de entregar, consolidar versión final
   - Revisar TODO el documento juntas
   - Aplicar formato APA en Word

---

## 📊 ESTADO ACTUAL DEL PROYECTO

### ✅ Secciones Completadas (12)

1. ✅ **Portada** - Completa (falta llenar nombres)
2. ✅ **Índice** - Completo
3. ✅ **Resumen** - Completo (247 palabras)
4. ✅ **Palabras clave** - Completo
5. ✅ **Introducción** - Completa (exhaustiva)
6. ✅ **Políticas Institucionales** - Completa (6 subsecciones)
7. ✅ **Fundamentación Teórica** - Completa (antecedentes + marco + justificación)
8. ✅ **Planteamiento del Problema** - Completo
9. ✅ **Hipótesis** - Completas (5 específicas + nula)
10. ✅ **Objetivos** - Completos (1 general + 11 específicos)
11. ✅ **Variables** - COMPLETO (exhaustivo, 22KB)
12. ✅ **Metodología** - COMPLETA (exhaustiva, 34KB)

### ⏳ Secciones Pendientes (10)

13. ⏳ **Estrategia de Implementación**
14. ⏳ **Descripción Detallada de Sesiones**
15. ⏳ **Cronograma**
16. ⏳ **Presupuesto**
17. ⏳ **Aspectos Éticos**
18. ⏳ **Plan de Análisis de Datos**
19. ⏳ **Resultados Esperados**
20. ⏳ **Limitaciones**
21. ⏳ **Aportes**
22. ⏳ **Referencias**
23. ⏳ **Anexos**

### 📈 Progreso: 54% completo (12/22 secciones)

---

## 🛠️ HERRAMIENTAS DISPONIBLES

### Script 1: `dividir_proyecto.py` (Principal)

**Comandos**:
```bash
python dividir_proyecto.py verificar          # Ver estado
python dividir_proyecto.py consolidar         # Crear documento final
python dividir_proyecto.py crear-plantillas   # Crear plantillas faltantes
```

### Script 2: `extraer_secciones.py` (Extractor)

Extrae secciones de archivos existentes y crea archivos individuales.

```bash
python extraer_secciones.py
```

### Script 3: `consolidar.py` (Consolidación rápida)

Versión simplificada que solo consolida:

```bash
python consolidar.py
```

---

## 📝 TIPS PARA EDITAR

### Formato Markdown

- Títulos: `#` para título principal, `##` para subsecciones, `###` para sub-subsecciones
- Listas: `- ` para viñetas, `1. ` para numeradas
- Negritas: `**texto**`
- Cursivas: `*texto*`
- Tablas: Usar `|` para separar columnas

### Ejemplo de Tabla

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
```

### Citas Bibliográficas

Formato temporal en markdown:
```
(Autor, Año)
```

Al final, en `21_referencias.md`, formato APA completo:
```
Autor, A. A. (Año). Título del artículo. *Nombre de la Revista*, volumen(número), páginas. https://doi.org/xxx
```

---

## ⚠️ IMPORTANTE

1. **NO borrar los separadores `---`** al final de cada archivo
2. **Mantener la numeración** de secciones coherente
3. **Guardar en UTF-8** para evitar problemas de tildes
4. **No cambiar nombres** de archivos (afecta consolidación)
5. **Hacer backup** antes de cambios grandes

---

## 🎯 OBJETIVO FINAL

Tener un proyecto de investigación completo de **aproximadamente 80-100 páginas** que incluya:

- ✅ Marco teórico exhaustivo
- ✅ Metodología detallada y replicable
- ✅ Todas las variables operacionalizadas
- ✅ Protocolo de sesiones minuto a minuto
- ✅ Aspectos éticos completos
- ✅ Plan de análisis
- ✅ Referencias en APA 7
- ✅ Todos los anexos necesarios

---

## 📞 SOPORTE

Si tienen dudas sobre:
- **Contenido académico**: Consultar al profesor/supervisor
- **Formato APA**: Manual APA 7ma edición
- **Scripts Python**: Revisar comentarios en el código o preguntar

---

## ✅ CHECKLIST ANTES DE ENTREGAR

- [ ] Todas las secciones completadas
- [ ] Consolidación realizada
- [ ] Revisión ortográfica
- [ ] Revisión de coherencia entre secciones
- [ ] Formato APA aplicado
- [ ] Referencias verificadas
- [ ] Anexos incluidos
- [ ] Portada con datos correctos
- [ ] Índice actualizado
- [ ] Revisión por todas las integrantes

---

**¡Mucho éxito con el proyecto!** 🎓

Fecha de última actualización: Octubre 30, 2025
