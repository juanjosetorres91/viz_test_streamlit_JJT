De los Datos a la Acción: El Mito del Progreso

# 📊 De los Datos a la Acción: El Mito del Progreso

Proyecto de Storytelling con Datos – Framework ABT (And–But–Therefore)

Dataset: Gapminder FiveYearData (1952–2007)

# 🎯 Objetivo del Proyecto

Este proyecto utiliza técnicas de storytelling con datos para mostrar cómo los promedios globales pueden ocultar desigualdades profundas en salud a nivel mundial. A través del framework ABT (And–But–Therefore), se revela que:

El 80% de las ganancias en esperanza de vida ocurren ANTES de alcanzar los $4,000 USD de PIB per cápita.

Esto demuestra que los países de bajos ingresos pueden lograr mejoras sanitarias sustanciales sin necesidad de crecimiento económico ilimitado, tomando como ejemplo el caso de Vietnam.

# 🧩 Mensaje Central

El progreso global en salud es real, pero está distribuido de manera profundamente desigual; y la eficiencia sanitaria temprana puede cerrar la brecha sin esperar a que los países se enriquezcan.

# 📁 Estructura del Repositorio

tarea3_viz_mitoprogreso/

├── .gitignore                                 # Ignora archivos temporales y de entorno

├── README.md                                  # Documentación principal del proyecto

├── LICENSE                                    # Licencia de código abierto (ej. MIT)

├── requirements.txt                           # Lista de dependencias de Python (pandas, plotly, pptx, etc.)

├── run_app.bat                                # Script para ejecutar la aplicación Streamlit

|

├── src/ <--- Código de producción (Apps y generación de artefactuals)

│   ├── app.py                                 # Versión simple de la aplicación Streamlit

│   ├── app_pro.py                             # Versión profesional (con CSS) de la aplicación Streamlit

│   │   ├── apply_mckinsey_style.py                # Script para aplicar estilos al notebook

│   ├── generate_plots.py                      # Script para generar los gráficos de alta resolución

│   └── generate_plots_simple.py               # Script para generar gráficos de prueba

|

├── notebooks/

│   ├── storytelling.ipynb                     # Notebook inicial con el EDA

│   ├── storytelling_enhanced.ipynb            # Notebook mejorado

│   ├── storytelling_executive.ipynb           # ⭐ Notebook final y ordenado (el entregable principal)

│   ├── storytelling_executive_backup.ipynb    # Copia de seguridad automática

│   ├── storytelling_executive_error.ipynb     # Versión que falló en alguna ejecución (para debug)

│   └── storytelling_executive.html            # Resultado final del notebook en HTML (para visualización directa)

|

├── tools/ <--- Scripts de utilidad y automatización

│   ├── analyze_structure.py                   # Script para revisar la estructura del notebook

│   ├── check_charts.py                        # Script para validar la presencia de gráficos en el HTML

│   ├── debug_notebook.py                      # Script de prueba rápida de ejecución de datos

│   ├── find_sections.py                       # Script para localizar secciones narrativas

│   ├── reorder_notebook.py                    # Script para reordenar las celdas del notebook

│   ├── run_notebook.py                        # Script para ejecutar el notebook desde la línea de comandos

│   ├── update_content.py                      # Script para modificar el contenido de las celdas

│   └── update_notebook.py                     # Script para actualizar la configuración/metadatos del notebook

|

├── docs/ <--- Documentación, guiones y archivos fuente

│   ├── frameworks.txt                         # Notas sobre los frameworks narrativos (ABT, Setup-Insight-Implicación)

│   ├── gamma.txt                              # Guía y prompts para la herramienta Gamma AI

│   ├── informe_presentacion_gamma.md          # ⭐ Entregable: Guión oral de 12 minutos y prompt final para Gamma

│   ├── RESUMEN_FINAL.md                       # Resumen ejecutivo y check-list final

│   ├── HISTORIAL_PROMPTS.md                   # Documentación completa del uso de IA (prompts utilizados)

│   ├── structure.txt                          # Archivo de salida de `analyze_structure.py`

│   ├── tarea_3.pdf                            # Enunciado/Rúbrica de la tarea

│   └── transcripcion.docx                     # Transcripción de clase (referencia conceptual)

|

├── data/ <--- Conjunto de datos

│   └── gapminder-FiveYearData.csv             # El dataset Gapminder original

└── plots/                                 # Directorio de salida para los gráficos estáticos (PNG, SVG)

# 🚀 Instalación y Ejecución

1. Crear entorno virtual

python -m venv venv

source venv/bin/activate      # macOS / Linux

venv\Scripts\activate         # Windows

2. Instalar dependencias

pip install -r requirements.txt

3. Ejecutar el notebook

jupyter notebook notebooks/storytelling_executive.ipynb

4. Ejecutar la app Streamlit (opcional)

streamlit run src/app_pro.py

# 🎨 Framework Narrativo: ABT (And–But–Therefore)

1️⃣ AND — Contexto

La esperanza de vida global ha crecido de forma sostenida (1952–2007).

A primera vista, el mundo parece estar progresando.

2️⃣ BUT — Conflicto

África se ha rezagado significativamente respecto al resto del mundo.

Su dispersión interna en esperanza de vida es alta y persistente.

La crisis del VIH/SIDA en los 90 provocó un colapso sanitario.

Este quiebre creó una brecha estructural difícil de cerrar.

3️⃣ THEREFORE — Resolución

La relación PIB–Salud no es lineal: es logarítmica.

El 80% del progreso ocurre antes de los $4,000 USD per cápita.

Países pobres pueden mejorar salud de forma “eficiente” sin depender del crecimiento económico.

Vietnam es el benchmark: bajo ingreso, alta esperanza de vida.

La recomendación es la estrategia de Eficiencia Sanitaria Temprana.

# 📊 Visualizaciones Incluidas

Gráfico de tendencia global: Esperanza de vida 1952–2007

Boxplot por continente: Dispersión geográfica

Serie temporal del VIH/SIDA: Colapso en los 90

Scatterlog PIB vs Esperanza de vida: Umbral de $4,000 USD

Caso Vietnam: Outlier positivo en eficiencia sanitaria

Visualización de síntesis: Mensaje central del proyecto

Todas las gráficas incluyen:

Títulos activos

Anotaciones

Uso estratégico del color (azul corporativo y rojo para África)

Fuente: Gapminder

# 💡 Recomendación Accionable

Invertir de forma prioritaria en salud básica y estrategias de eficiencia sanitaria hasta el umbral de $4,000 USD per cápita, siguiendo modelos exitosos como el de Vietnam.

Esta estrategia produce mejoras sanitarias significativas sin necesidad de esperar décadas de crecimiento económico.

# 🧠 Transparencia sobre el Uso de IA

(Obligatorio según pauta)

Este proyecto utilizó herramientas de IA generativa como asistencia complementaria, sin reemplazar el análisis, razonamiento ni narrativa del equipo.

Herramientas utilizadas (con links oficiales)

ChatGPT (OpenAI): https://chat.openai.com

Gemini (Google): https://gemini.google.com

Claude (Anthropic): https://claude.ai

Gamma (Presentaciones): https://gamma.app

Archivo con prompts completos

Todos los prompts usados se encuentran en el archivo:

/prompts/HISTORIAL_PROMPTS.md

# 📚 Bibliografía y Fuentes de Datos

Dataset

Gapminder Foundation – Esperanza de vida, PIB per cápita, población (1952–2007)

https://www.gapminder.org/data/

Metodología y Storytelling

Olson, R. (2015). Houston, We Have a Narrative: The ABT Framework.

Duarte, N. (2010). Resonate: Present Visual Stories.

Visualización

Plotly Documentation — https://plotly.com/python

McKinsey & Co. — Principios de Comunicación Visual: https://www.mckinsey.com/

# 👥 Autores

Claudio Ballerini

Juan José Torres

Cristian Vargas

Christian Vásquez

Proyecto de Storytelling con Datos

Curso de Visualización de Datos y Storytelling

Diciembre 2025

# 📦 Licencia

Uso estrictamente académico.

Se prohíbe su reutilización literal en evaluaciones de terceros.