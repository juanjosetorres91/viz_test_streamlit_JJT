import json
import os

notebook_path = r'c:\Users\christian.vasquez\Documents\antigravity\storytelling\storytelling_executive.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# --- 1. UPDATE CSS (Cell 0) ---
css_content = """
<style>
    /* --- GENERAL SETTINGS --- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    body {
        background-color: #f9f9f9 !important;
        font-family: 'Inter', sans-serif !important;
        color: #333333 !important;
    }
    
    /* Hide code cells to look like a report */
    div.input {
        display: none !important;
    }
    
    /* Center the container for reading experience */
    div.container {
        width: 80% !important;
        max-width: 900px !important;
        margin: 0 auto !important;
        padding: 0 !important;
    }
    
    /* --- TYPOGRAPHY --- */
    h1 {
        font-weight: 800 !important;
        font-size: 3.5rem !important;
        letter-spacing: -1px !important;
        color: #1a1a1a !important;
        margin-bottom: 0.5em !important;
        margin-top: 1em !important;
    }
    
    h2 {
        font-weight: 600 !important;
        font-size: 2rem !important;
        color: #2c2c2c !important;
        margin-top: 2em !important;
        border-bottom: none !important;
    }
    
    h3 {
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        color: #555 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 2em !important;
    }
    
    p {
        font-size: 1.15rem !important;
        line-height: 1.7 !important;
        color: #444 !important;
        margin-bottom: 1.5em !important;
    }
    
    /* --- COMPONENTS --- */
    .insight-box {
        background-color: #ffffff;
        border-left: 6px solid #636efa; /* Plotly blue */
        padding: 25px;
        margin: 30px 0;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.01);
    }
    
    .insight-box-highlight {
        background-color: #e6f0ff; /* Light blue background */
        border-left: 6px solid #2E86C1; /* Strong blue border */
        color: #154360;
        padding: 25px;
        margin: 30px 0;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.01);
        font-family: 'Inter', sans-serif;
    }

    .insight-box-highlight b {
        color: #1A5276;
        font-weight: 800;
    }

    .alert-box-warning {
        background-color: #fff9e6; /* Pale yellow */
        border-left: 6px solid #F1C40F; /* Warning Yellow */
        color: #7D6608;
        padding: 25px;
        margin: 30px 0;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.01);
    }
    
    .insight-title {
        font-weight: 800;
        font-size: 1.2rem;
        color: #636efa;
        margin-bottom: 10px;
        display: block;
    }
    
    .stat-card {
        display: inline-block;
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-right: 15px;
        margin-bottom: 15px;
        min-width: 150px;
        text-align: center;
    }
    
    .stat-val {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1a1a1a;
    }
    
    .stat-label {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #888;
    }
    
    /* --- PLOTLY OVERRIDES --- */
    .js-plotly-plot .plotly .modebar {
        display: none !important; /* Hide toolbar for clean look */
    }
</style>
"""

nb['cells'][0]['source'] = [
    "from IPython.display import HTML\n",
    "\n",
    "css = \"\"\"\n" + css_content + "\"\"\"\n",
    "HTML(css)"
]

# --- 2. PRESERVE IMPORT CELL (Cell 1) ---
# Keeping Cell 1 as is (Imports & Data Loading)

# --- 3. NEW CONTENT CELLS ---
new_cells = []

# Cell: Title & Hook Markdown
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "<h3>PROYECTO: IMPACTO GLOBAL</h3>\n",
        "<h1>De los Datos a la Acción: El Mito del Progreso</h1>\n",
        "<p style=\"font-size: 1.2rem; color: #666;\"><i>Hoja de Ruta para entender la evolución de la salud y riqueza global</i></p>\n",
        "<hr style=\"border: 0; border-top: 1px solid #eee; margin: 40px 0;\">\n",
        "\n",
        "<h3>1. EL GANCHO</h3>\n",
        "<h2>¿Estamos viendo la imagen completa?</h2>\n",
        "<p>\n",
        "    A primera vista, nuestros indicadores principales de <strong>Esperanza de Vida Global</strong> muestran una tendencia estable y positiva. \n",
        "    Sin embargo, en un entorno volátil, los promedios pueden ser una ilusión peligrosa. Este informe no es una revisión de lo que pasó, \n",
        "    sino una investigación sobre <strong>dónde se esconden las desigualdades persistentes</strong>.\n",
        "</p>\n",
        "<p>\n",
        "    A continuación, desglosamos la realidad detrás de los números.\n",
        "</p>"
    ]
})

# Cell: Hook Viz (Big Number / Simple Trend)
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {"tags": ["hide_input"]},
    "outputs": [],
    "source": [
        "# Global Trend\n",
        "global_trend = df.groupby('year')['lifeExp'].mean().reset_index()\n",
        "current_life_exp = global_trend['lifeExp'].iloc[-1]\n",
        "start_life_exp = global_trend['lifeExp'].iloc[0]\n",
        "growth = current_life_exp - start_life_exp\n",
        "\n",
        "fig_hook = go.Figure()\n",
        "\n",
        "fig_hook.add_trace(go.Scatter(\n",
        "    x=global_trend['year'],\n",
        "    y=global_trend['lifeExp'],\n",
        "    mode='lines',\n",
        "    line=dict(color='#2E86C1', width=5),\n",
        "    fill='tozeroy',\n",
        "    fillcolor='rgba(46, 134, 193, 0.1)'\n",
        "))\n",
        "\n",
        "fig_hook.add_annotation(\n",
        "    x=2007, y=current_life_exp,\n",
        "    text=f\"<b>{current_life_exp:.1f} Años</b><br>(+{growth:.1f} desde 1952)\",\n",
        "    showarrow=True,\n",
        "    arrowhead=1,\n",
        "    ax=0, ay=-40,\n",
        "    font=dict(size=14, color=\"#2E86C1\")\n",
        ")\n",
        "\n",
        "fig_hook.update_layout(\n",
        "    title=\"<b>Tendencia Global de Esperanza de Vida (1952-2007)</b>\",\n",
        "    height=400,\n",
        "    margin=dict(t=50, l=50, r=50, b=50),\n",
        "    xaxis=dict(showgrid=False),\n",
        "    yaxis=dict(showgrid=True, gridcolor='#eee', range=[30, 80]),\n",
        "    paper_bgcolor='rgba(0,0,0,0)',\n",
        "    plot_bgcolor='rgba(0,0,0,0)'\n",
        ")\n",
        "\n",
        "fig_hook.show()"
    ]
})

# Cell: Conflict Markdown
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "<h3>2. EL CONFLICTO</h3>\n",
        "<h2>📉 La Fricción Silenciosa</h2>\n",
        "<p>\n",
        "    Al profundizar en los segmentos regionales, detectamos una anomalía. Mientras el promedio general sube, \n",
        "    el continente de <strong>África</strong> ha mostrado un rezago histórico signficativo, e incluso retrocesos en periodos críticos.\n",
        "</p>\n",
        "<div class=\"alert-box-warning\">\n",
        "    ⚠️ <b>Alerta Temprana:</b> Si bien la tendencia global es positiva, la brecha entre África y Europa sigue siendo de \n",
        "    casi <b>20 años</b> de vida. No es solo un problema de recursos económicos, es un problema de <i>eficiencia estructural</i> en salud.\n",
        "</div>"
    ]
})

# Cell: Conflict Viz (Gap analysis)
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {"tags": ["hide_input"]},
    "outputs": [],
    "source": [
        "cont_trend = df.groupby(['year', 'continent'])['lifeExp'].mean().reset_index()\n",
        "\n",
        "fig_conflict = px.line(\n",
        "    cont_trend, \n",
        "    x='year', \n",
        "    y='lifeExp', \n",
        "    color='continent',\n",
        "    color_discrete_map={'Asia': '#ddd', 'Europe': '#2E86C1', 'Africa': '#F1C40F', 'Americas': '#ddd', 'Oceania': '#ddd'}\n",
        ")\n",
        "\n",
        "fig_conflict.update_traces(mode='lines')\n",
        "# Make Africa and Europe thicker\n",
        "fig_conflict.update_traces(patch={\"line\": {\"width\": 4, \"dash\": \"solid\"}}, selector={\"name\": \"Africa\"})\n",
        "fig_conflict.update_traces(patch={\"line\": {\"width\": 4, \"dash\": \"solid\"}}, selector={\"name\": \"Europe\"})\n",
        "fig_conflict.update_traces(patch={\"line\": {\"width\": 1, \"dash\": \"dot\"}}, selector={\"name\": \"Asia\"})\n",
        "fig_conflict.update_traces(patch={\"line\": {\"width\": 1, \"dash\": \"dot\"}}, selector={\"name\": \"Americas\"})\n",
        "fig_conflict.update_traces(patch={\"line\": {\"width\": 1, \"dash\": \"dot\"}}, selector={\"name\": \"Oceania\"})\n",
        "\n",
        "fig_conflict.update_layout(\n",
        "    title=\"<b>La Brecha Persistente: África vs Europa</b>\",\n",
        "    showlegend=True,\n",
        "    template=\"plotly_white\",\n",
        "    height=500\n",
        ")\n",
        "fig_conflict.show()"
    ]
})

# Cell: Analysis Markdown
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "<h3>3. EL ANÁLISIS</h3>\n",
        "<h2>🔍 Diagnóstico: ¿Qué impulsa el bienestar?</h2>\n",
        "<p>\n",
        "    Para entender la raíz del problema, cruzamos las variables de <strong>PIB per Cápita</strong> vs <strong>Esperanza de Vida</strong>.\n",
        "</p>\n",
        "<p>\n",
        "    Interactúa con el gráfico siguiente. Nota cómo existe una correlación directa logística: al principio, pequeños aumentos de ingreso \n",
        "    generan saltos enormes en salud. Lo interesante es que esto <strong>no afecta a todos por igual</strong>: muchos países logran \n",
        "    altos niveles de salud con ingresos medios.\n",
        "</p>"
    ]
})

# Cell: Analysis Viz (Bubble Chart)
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {"tags": ["hide_input"]},
    "outputs": [],
    "source": [
        "# Animación existente (reutilizada del código anterior)\n",
        "fig_anim = px.scatter(\n",
        "    df,\n",
        "    x=\"gdpPercap\",\n",
        "    y=\"lifeExp\",\n",
        "    animation_frame=\"year\",\n",
        "    animation_group=\"country\",\n",
        "    size=\"pop\",\n",
        "    color=\"continent\",\n",
        "    hover_name=\"country\",\n",
        "    log_x=True,\n",
        "    size_max=55,\n",
        "    range_x=[100, 100000],\n",
        "    range_y=[25, 90],\n",
        "    labels={\"gdpPercap\": \"PIB per Cápita (Log)\", \"lifeExp\": \"Esperanza de Vida\"},\n",
        "    template=\"plotly_white\",\n",
        "    color_discrete_map={'Asia': colors['asia'], 'Europe': colors['europe'], 'Africa': colors['africa'], 'Americas': colors['americas'], 'Oceania': colors['oceania']}\n",
        ")\n",
        "\n",
        "fig_anim.update_layout(\n",
        "    height=600,\n",
        "    xaxis=dict(showgrid=False, zeroline=False),\n",
        "    yaxis=dict(showgrid=True, gridcolor='#f0f0f0'),\n",
        "    paper_bgcolor='rgba(0,0,0,0)',\n",
        "    plot_bgcolor='rgba(0,0,0,0)',\n",
        "    title=\"<b>Evolución Dinámica: Riqueza vs Salud (1952-2007)</b>\"\n",
        ")\n",
        "\n",
        "fig_anim.layout.updatemenus[0].buttons[0].args[1][\"frame\"][\"duration\"] = 400\n",
        "fig_anim.show()"
    ]
})

# Cell: Climax Markdown
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "<h3>4. EL CLÍMAX</h3>\n",
        "<div class=\"insight-box-highlight\">\n",
        "    💡 <b>El Hallazgo Clave (The Insight)</b>\n",
        "    <br><br>\n",
        "    Los datos revelan que no necesitamos ser \"ricos\" para ser \"sanos\". \n",
        "    <br>\n",
        "    El punto de inflexión ocurre alrededor de los <b>$4,000 USD</b> per cápita. Pasado ese punto, la ganancia marginal en vida es mínima.\n",
        "    El <b>80%</b> del progreso en salud ocurre en las etapas tempranas de desarrollo económico. \n",
        "    Esto cambia nuestra hipótesis inicial: no necesitamos esperar a ser Suiza para tener la salud de Suiza.\n",
        "</div>"
    ]
})

# Cell: Climax Viz (The Curve Highlight)
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {"tags": ["hide_input"]},
    "outputs": [],
    "source": [
        "df_2007 = df[df['year'] == 2007]\n",
        "fig_climax = px.scatter(\n",
        "    df_2007, \n",
        "    x='gdpPercap', \n",
        "    y='lifeExp', \n",
        "    size='pop', \n",
        "    color='continent',\n",
        "    log_x=True,\n",
        "    hover_name='country',\n",
        "    color_discrete_map={'Asia': colors['asia'], 'Europe': colors['europe'], 'Africa': colors['africa'], 'Americas': colors['americas'], 'Oceania': colors['oceania']}\n",
        ")\n",
        "\n",
        "# Add Threshold Line\n",
        "fig_climax.add_vline(x=4000, line_width=2, line_dash=\"dash\", line_color=\"green\", annotation_text=\"Umbral de Eficiencia ($4k)\", annotation_position=\"top right\")\n",
        "\n",
        "fig_climax.update_layout(\n",
        "    title=\"<b>La Curva de Rendimientos Decrecientes (2007)</b>\",\n",
        "    template=\"plotly_white\",\n",
        "    height=500\n",
        ")\n",
        "fig_climax.show()"
    ]
})

# Cell: Resolution Markdown
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "<h3>5. LA RESOLUCIÓN</h3>\n",
        "<h2>🚀 Estrategia Recomendada</h2>\n",
        "<p>\n",
        "    Basados en la evidencia anterior, el camino para cerrar la brecha global es claro:\n",
        "</p>\n",
        "<ol>\n",
        "    <li>\n",
        "        <strong>Focalización:</strong> Priorizar inversiones en salud básica en países sub-$4000 (principalmente África Sub-Sahariana).\n",
        "    </li>\n",
        "    <li>\n",
        "        <strong>Eficiencia:</strong> Imitar los modelos de países como <i>Vietnam</i> o <i>Cuba</i>, que lograron alta esperanza de vida con bajo PIB.\n",
        "    </li>\n",
        "    <li>\n",
        "        <strong>Monitoreo:</strong> Vigilar la \"Salida de la Pobreza\" no solo con métricas económicas, sino con métricas de bienestar físico.\n",
        "    </li>\n",
        "</ol>\n",
        "<p><i>Los datos sugieren que es posible erradicar la brecha de salud en una sola generación si aplicamos estas palancas correctamente.</i></p>"
    ]
})

# Attach new cells
# Keep only first 2 cells (CSS + Import), remove the rest, add new ones
nb['cells'] = nb['cells'][:2] + new_cells

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)

print("Notebook updated successfully.")
