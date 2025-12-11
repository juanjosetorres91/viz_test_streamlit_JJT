# 📋 Historial Completo de Prompts - Proyecto Storytelling

**Proyecto:** Análisis de Datos con Storytelling - Salud Global  
**Dataset:** Gapminder (esperanza de vida, PIB, población)  
**Fecha de Compilación:** 2025-12-09  
**Documento Base:** `tarea_3.pdf`

---

## 📊 Resumen Ejecutivo

Este documento recopila **todos los prompts** utilizados durante el desarrollo del proyecto de Storytelling con Ciencia de Datos, desde la concepción inicial hasta la generación de la presentación final.

### Entregables Generados

- ✅ Notebook Jupyter con análisis completo (`storytelling_executive.ipynb`)
- ✅ Presentación PowerPoint estructurada
- ✅ Prompts para generación automática con Gamma AI
- ✅ Repositorio GitHub con declaración de uso de IA

---

## 🎯 Prompts del Proyecto

### 1. Prompt Principal - Desarrollo del Notebook

#### **Contexto:** Creación inicial del notebook de storytelling

**Prompt Conceptual:**

```
Desarrollar un notebook de Jupyter que demuestre storytelling con datos usando el dataset 
de Gapminder. El análisis debe:

1. Usar el framework ABT (And-But-Therefore) para estructurar la narrativa
2. Demostrar que el progreso global oculta desigualdades estructurales
3. Enfocarse en la brecha de salud en África
4. Identificar el umbral de $4,000 USD como punto crítico de eficiencia sanitaria
5. Proponer soluciones basadas en modelos de eficiencia (Vietnam)

Requisitos técnicos:
- Estilo visual McKinsey (minimalista, profesional)
- Gráficos con insights directos, no descriptivos
- Paleta de colores corporativa
- Anotaciones "Fuente: Gapminder" en todos los gráficos
- CSS personalizado para formato de presentación
```

**Salida:** `storytelling_executive.ipynb` (281 KB)

---

### 2. Prompt para Estilo Visual McKinsey

#### **Contexto:** Aplicación de estilo corporativo al notebook

**Prompt de Configuración:**

```python
# Configuración de estilo visual ejecutivo

# 1. CSS personalizado para notebook
- Ocultar prompts de código (div.prompt)
- Tipografía profesional (Segoe UI, Roboto)
- Paleta de colores limitada y coherente
- Márgenes amplios y espaciado generoso

# 2. Template Plotly personalizado
- Fondo blanco
- Grid sutil (gris claro)
- Colores primarios: 
  * Azul corporativo: #00A3E0
  * Rojo para alertas: #E74C3C, #d62728
  * Grises neutrales: #7f7f7f, #95a5a6
- Fuente de títulos en negrita
- Anotaciones discretas en gris

# 3. Reglas de Visualización
- Títulos activos (no "Gráfico de...", sino "La Geografía como Destino")
- Fuente citada en cada gráfico
- Sin decoración innecesaria
- Foco en el insight, no en los datos
```

**Salida:** Template `mckinsey` aplicado en configuración inicial del notebook

---

### 3. Prompt para Gamma AI - Versión Completa

#### **Contexto:** Generación automática de presentación ejecutiva

**Archivo:** `informe_presentacion_gamma.md`

**Prompt Completo:**

```
Crea una presentación ejecutiva de 6 diapositivas con el siguiente contenido. 
Usa un diseño minimalista estilo McKinsey, fondo blanco, tipografía sans-serif 
profesional, y gráficos limpios con acentos en azul (#00A3E0) y rojo (#E74C3C) 
para destacar África.

Slide 1: Título
- Título principal: "De los Datos a la Acción: El Mito del Progreso"
- Subtítulo: "Análisis de Brechas Estructurales en la Salud Global"

Slide 2: Tendencia Global
- Título: "El Espejismo Global"
- Gráfico de línea ascendente mostrando esperanza de vida global de 1952 a 2007 
  (de 48 a 67 años)
- Nota: "Fuente: Gapminder"

Slide 3: Geografía
- Título: "Alta Dispersión en África: La Geografía como Destino"
- Boxplot comparando esperanza de vida por continente en 2007
- Destacar África en rojo (caja amplia, posición baja)
- Nota: "Fuente: Gapminder"

Slide 4: Crisis VIH
- Título: "La Crisis de los 90s: Cuando África se Separó del Mundo"
- Gráfico de líneas: Mundo (gris) vs África (rojo)
- Anotación en 1990-1995: "Epidemia VIH/SIDA"
- Nota: "Fuente: Gapminder"

Slide 5: Umbral $4,000
- Título: "El 80% del Progreso Ocurre Antes de $4,000 USD"
- Scatterplot: PIB per cápita (log) vs Esperanza de vida
- Línea vertical en $4,000 USD
- África en rojo, resto en gris
- Destacar Vietnam en el cuadrante "pobres pero sanos"
- Nota: "Fuente: Gapminder"

Slide 6: Resolución
- Título: "Estrategia: Eficiencia Sanitaria Temprana"
- 3 bullets con iconos:
  * 🎯 Focalización: Salud básica prioritaria
  * ⚡ Eficiencia: Copiar modelo Vietnam
  * 📊 Monitoreo: Medir brechas, no promedios
```

**Uso:** Copiar y pegar en [gamma.app](https://gamma.app)  
**Salida esperada:** Presentación de 6 diapositivas automáticamente formateada

---

### 4. Prompt para Gamma AI - Versión Simplificada

#### **Contexto:** Alternativa concisa para generación rápida

**Archivo:** `gamma.txt`

**Prompt:**

```
Actúa como un consultor de estrategia de McKinsey. Crea una presentación de 
6 diapositivas sobre 'La Brecha de Salud en África'. Usa un tono profesional, 
minimalista y basado en datos.

Título: De los Datos a la Acción.
Slide: El mundo mejora en promedio (gráfico lineal ascendente).
Slide: Pero África tiene alta desigualdad (boxplot).
Slide: La crisis del VIH en los 90s causó el rezago (gráfico de línea con caída).
Slide: Insight Clave: El 80% de la salud se gana antes de los $4,000 USD de PIB 
       (scatterplot).
Slide: Estrategia: Copiar modelos eficientes como Vietnam (texto y bullets).
```

**Ventaja:** Más rápido de copiar, menos detalles técnicos

---

### 5. Prompts de Estructura Narrativa (Framework ABT)

#### **Contexto:** Organización del contenido según metodología ABT

**Prompt de Estructura:**

```
Reorganizar el análisis siguiendo el framework ABT (And-But-Therefore):

AND (Contexto - 2 minutos):
  → "El Espejismo Global"
  → Tendencia ascendente de esperanza de vida global
  → Establecer que los promedios ocultan desigualdades

BUT (Conflicto - 4 minutos):
  → "La Geografía como Destino"
  → Boxplot mostrando dispersión por continente
  → África destaca por alta desigualdad y baja esperanza
  
  → "La Crisis de los 90s"
  → Gráfico temporal mostrando colapso por VIH/SIDA
  → África se separa del resto del mundo

THEREFORE (Análisis + Resolución - 6 minutos):
  → "El Mito del PIB"
  → Scatterplot PIB vs Esperanza de Vida
  → Identificar umbral de $4,000 USD (80% de ganancias)
  
  → "Eficiencia Sanitaria Temprana"
  → Destacar caso Vietnam (bajo PIB, alta esperanza)
  → Proponer 3 pilares estratégicos

Resultado: Narrativa coherente que transforma datos en acción estratégica
```

**Salida:** Secciones del notebook reordenadas según esta estructura

---

### 6. Prompts de Visualización Específica

#### **6.1 Gráfico de Tendencia Global**

```python
# Gráfico de línea - Esperanza de vida global

Especificaciones:
- Tipo: Línea con marcadores
- Datos: Promedio global 1952-2007
- Color: Azul corporativo (#00A3E0)
- Grosor: 4px
- Rango Y: 45-70 años
- Título: "La Esperanza de Vida Global Crece Constantemente"
- Anotación: "Fuente: Gapminder"
```

#### **6.2 Boxplot por Continente**

```python
# Diagrama de caja - Dispersión por geografía

Especificaciones:
- Tipo: Boxplot
- Datos: Esperanza de vida 2007, agrupado por continente
- Destacado: África en rojo (#ff6b6b)
- Resto: Grises/azules neutros
- Rango Y: 40-85 años
- Título: "Alta Dispersión en África: La Geografía como Destino"
- Insight: Caja amplia = alta desigualdad interna
```

#### **6.3 Crisis Temporal - VIH**

```python
# Gráfico de líneas comparativo

Especificaciones:
- Tipo: Doble línea temporal
- Línea 1: Mundo (gris claro, delgada)
- Línea 2: África (rojo #E74C3C, gruesa 4px)
- Anotación: "Epidemia VIH/SIDA" en 1990-1995
- Título: "La Crisis de los 90s: Cuando África se Separó del Mundo"
```

#### **6.4 Scatterplot PIB vs Salud**

```python
# Gráfico de dispersión con umbral

Especificaciones:
- Tipo: Scatterplot con burbujas
- Eje X: PIB per cápita (escala logarítmica)
- Eje Y: Esperanza de vida
- Tamaño burbuja: Población
- Colores:
  * África: Rojo (#d62728)
  * Resto: Gris claro
- Línea especial: Vertical punteada en $4,000 USD
- Destacados: Vietnam (cuadrante superior izquierdo)
- Título: "El 80% del Progreso Ocurre Antes de $4,000 USD"
```

---

### 7. Prompts de Guión para Presentación Oral

#### **Contexto:** Speaker notes para presentadores

**Estructura de Guión (12 minutos totales):**

```
Slide 1 - Introducción (2 min):
"Buenos días. Si miramos los datos agregados, la historia de la humanidad en 
los últimos 50 años parece un éxito rotundo. La esperanza de vida global ha 
crecido ininterrumpidamente. Vivimos más y mejor que nunca.

Sin embargo, los promedios son peligrosos. Esconden las grietas del sistema. 
Hoy no vengo a celebrar el éxito global, sino a hablar de quienes se han 
quedado atrás y por qué."

Slide 2 - Geografía (2 min):
"Pero cuando desagregamos esa línea perfecta, encontramos una fricción silenciosa. 
Miren este gráfico. Cada caja representa un continente.

Mientras Europa y América se agrupan en la cima con alta esperanza de vida y 
poca desigualdad, África nos cuenta una historia distinta. No solo está más 
abajo; es enormemente desigual. La geografía, lamentablemente, sigue siendo 
un predictor de destino. Nacer en el continente equivocado te quita décadas de vida."

Slide 3 - Crisis VIH (2 min):
"¿Por qué África se rezagó tan brutalmente? Aquí está la evidencia. En los años 90, 
mientras el mundo avanzaba gracias a la tecnología y la paz, África enfrentó su 
tormenta perfecta: la epidemia del VIH/SIDA combinada con inestabilidad política.

No fue un estancamiento suave, fue un colapso. Perdieron años de progreso en una 
sola década. Esto creó una brecha estructural de la que apenas se están recuperando."

Slide 4 - Umbral PIB (3 min):
"Muchos asumen que para arreglar la salud, primero necesitamos hacernos ricos. 
Que el PIB lo cura todo.

Nuestros datos demuestran que eso es falso. Miren este análisis de correlación. 
La relación entre dinero y vida no es lineal. Es logarítmica.

El hallazgo clave es este: El 80% de la ganancia en esperanza de vida ocurre 
ANTES de llegar a los $4,000 dólares per cápita. Después de ese punto, necesitas 
cantidades obscenas de dinero para ganar solo un año más de vida."

Slide 5 - Modelo Vietnam (2 min):
"Por lo tanto, la estrategia para África no puede ser 'esperar a ser ricos como 
Europa'. Eso tardará cien años.

La estrategia debe ser la Eficiencia Sanitaria Temprana. Miren a Vietnam en este 
gráfico. Tienen el mismo PIB que muchos países africanos, pero una esperanza de 
vida de primer mundo.

África no tiene un problema de falta de dinero solamente; tiene un problema de 
conversión de recursos. Necesitamos copiar los modelos de eficiencia sanitaria 
que funcionan con bajo presupuesto."

Slide 6 - Conclusión (1 min):
"Para cerrar, nuestra recomendación ejecutiva se basa en tres pilares:

1. Focalización: Inversión prioritaria en salud básica hasta alcanzar el umbral 
   de los $4,000 USD.
2. Eficiencia: Replicar modelos de bajo costo y alto impacto como Vietnam.
3. Monitoreo: Dejar de mirar promedios globales y medir la reducción de brechas.

Muchas gracias."
```

---

## 🔧 Prompts Técnicos - Solución de Problemas

### 8. Prompt para Solución de Error Kaleido

#### **Contexto:** Eliminar dependencia de exportación de imágenes

**Problema:** Error `kaleido` al intentar `fig.write_image()`

**Solución Aplicada:**

```python
# Eliminar todas las referencias a write_image del notebook
# Motivo: Kaleido requiere instalación compleja y no es necesario
#         si se usa Gamma AI para generar la presentación

# Códigos eliminados:
# - fig.write_image('plots/nombre_grafico.png')
# - Todas las exportaciones PNG

# Resultado:
# ✅ Notebook ejecuta sin errores
# ✅ Gráficos se muestran correctamente en Jupyter
# ✅ Gamma AI genera imágenes desde especificaciones, no archivos
```

**Archivo de documentación:** `SOLUCION_ERROR_KALEIDO.md`

---

### 9. Prompt para Reestructuración del Notebook

#### **Contexto:** Reorganización según feedback de revisión

**Cambios Solicitados:**

```
1. Reordenar secciones según framework ABT
2. Mover "Geografía" y "Crisis VIH" a sección de Conflicto
3. Cambiar título a "De los Datos a la Acción: El Mito del Progreso"
4. Agregar anotaciones "Fuente: Gapminder" en todos los gráficos
5. Incluir ejemplo de Vietnam explícitamente
6. Asegurar que títulos sean activos, no descriptivos
```

**Script Python generado:**

```python
# reorder_notebook.py
# Reorganiza celdas del notebook según nueva estructura ABT

import nbformat

# Leer notebook original
with open('storytelling_executive.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Definir nuevo orden de secciones
new_order = [
    'titulo',
    'and_contexto',
    'but_geografia',
    'but_crisis_vih',
    'therefore_analisis',
    'therefore_resolucion'
]

# Reorganizar celdas...
# (código completo en archivo)
```

---

## 📚 Contexto del Proyecto

### Historia de Desarrollo (Conversaciones)

Basado en el historial proporcionado:

#### **Conversación 8305e924** (2025-12-09)

- **Objetivo:** Refinar el notebook de storytelling
- **Acciones:** Solución de error de exportación de imágenes, verificación de artefactos
- **Prompt implícito:** "Asegurar que el notebook ejecute sin errores de kaleido"

#### **Conversación 724b18cf** (2025-12-09)

- **Objetivo:** Refinamiento basado en feedback
- **Acciones:** Reordenamiento de secciones, mejora de visuales, citación de fuentes
- **Prompt principal:** "Reestructurar según ABT, mejorar gráficos, preparar deliverables"

#### **Conversación 3dfe6d71** (2025-12-06)

- **Objetivo:** Aplicar estilo McKinsey
- **Prompt clave:** "Configurar tema visual corporativo minimalista"
- **Resultado:** Template `mckinsey` personalizado para Plotly

#### **Conversación 8ded8ca0** (2025-12-07)

- **Objetivo:** Continuar desarrollo del notebook
- **Prompt principal:** "Seguir reglas estrictas de HTML/CSS, Plotly styling, estructura de presentación"

#### **Conversación 87329c4b** (2025-12-05)

- **Objetivo:** Inicio del desarrollo
- **Prompt fundacional:** "Interpretar tarea_3.pdf y crear notebook de storytelling con dataset simple"

---

## 🎯 Datos Clave Utilizados en Prompts

Valores numéricos que se repiten en todos los prompts:

```
Esperanza de vida global:
- 1952: 48 años
- 2007: 67 años
- Crecimiento: +19 años en 55 años

África:
- Promedio 2007: ~54 años
- Alta dispersión interna
- Colapso en los 90s por VIH/SIDA

Umbral crítico:
- $4,000 USD PIB per cápita
- 80% de las ganancias en salud ocurren antes de este punto

Caso de éxito:
- Vietnam: PIB ~$2,500 USD, esperanza de vida 74 años
- Demuestra eficiencia sanitaria temprana
```

---

## 📁 Archivos Asociados a Prompts

| Archivo | Tipo de Prompt | Propósito |
|---------|---------------|-----------|
| `informe_presentacion_gamma.md` | Prompt completo para IA | Generar presentación automática |
| `gamma.txt` | Prompt simplificado | Versión rápida para Gamma AI |
| `storytelling_executive.ipynb` | Código ejecutable | Implementación del análisis |
| `frameworks.txt` | Guía conceptual | Framework ABT explicado |
| `RESUMEN_FINAL.md` | Documentación | Guía de uso de prompts |
| `INSTRUCCIONES_CRITICAS.md` | Troubleshooting | Solución técnica |

---

## ✅ Checklist de Validación de Prompts

Antes de usar cualquier prompt de este proyecto, verificar:

- [ ] El prompt incluye el framework ABT (And-But-Therefore)
- [ ] Se especifica estilo McKinsey/minimalista
- [ ] Los colores están definidos (azul #00A3E0, rojo #E74C3C)
- [ ] Se menciona la fuente "Gapminder" en gráficos
- [ ] Los títulos son activos (insights), no descriptivos
- [ ] Se incluye el umbral de $4,000 USD
- [ ] Vietnam aparece como caso de eficiencia
- [ ] La estructura es de 6 diapositivas/secciones

---

## 🚀 Uso Recomendado

### Para Generar Presentación

1. Copiar prompt completo de `informe_presentacion_gamma.md`
2. Abrir [gamma.app](https://gamma.app)
3. Pegar y generar
4. ⏱️ Tiempo estimado: 5 minutos

### Para Ejecutar Notebook

1. Abrir `storytelling_executive.ipynb`
2. Kernel → Restart & Clear Output
3. Cell → Run All
4. ⏱️ Tiempo estimado: 2 minutos

### Para Adaptar a Otro Dataset

- Mantener estructura ABT
- Reemplazar datos numéricos clave
- Conservar paleta de colores
- Adaptar insight central (umbral $4,000 es específico de Gapminder)

---

## 📊 Métricas del Proyecto

```
Total de prompts documentados: 9
Prompts para IA generativa: 2 (Gamma AI)
Prompts técnicos (Python): 4
Prompts de estructura narrativa: 3

Archivos generados: 12+
Tamaño del notebook final: 281 KB
Líneas de código Python: ~800
Gráficos generados: 5 principales
```

---

## 🎓 Conclusión

Este proyecto demuestra el uso sistemático de prompts en múltiples niveles:

1. **Prompts conceptuales** → Definen la narrativa (Framework ABT)
2. **Prompts técnicos** → Configuran visualizaciones (Plotly, CSS)
3. **Prompts generativos** → Automatizan deliverables (Gamma AI)
4. **Prompts de troubleshooting** → Solucionan problemas (Kaleido)

**Principio clave:** Cada prompt debe ser específico, reproducible y alineado con el objetivo final de transformar datos en acción estratégica.

---

**Documento compilado:** 2025-12-09  
**Autores:** Proyecto Storytelling - GRUPO 4  
**Licencia:** Académico - Incluye declaración de uso de IA
