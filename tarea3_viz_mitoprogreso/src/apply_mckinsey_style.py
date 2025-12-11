import nbformat
import os

# Define the path
notebook_path = r'c:\Users\christian.vasquez\Documents\antigravity\storytelling\storytelling_executive.ipynb'

# Read the notebook
if not os.path.exists(notebook_path):
    print(f"Error: Notebook not found at {notebook_path}")
    exit(1)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Print current cell count
print(f"Original cell count: {len(nb.cells)}")

# -------------------------------------------------------------------------
# DEFINE NEW CELLS
# -------------------------------------------------------------------------

new_cells = []

# --- SECTION 2: INEQUALITY (La Geografía como Destino) ---
cell_2_markdown = nbformat.v4.new_markdown_cell(source="""
<h3>2. EL CONTEXTO</h3>
<h1>La Geografía como Destino</h1>

<div class="insight-box">
    <h3>💡 Insight</h3>
    <p>Nacer en Europa garantiza, en promedio, <strong>23 años más de vida</strong> que nacer en África. Esta brecha estructural no se ha cerrado significativamente en las últimas décadas.</p>
</div>

<p>
    Aunque el mundo avanza, la distribución de la longevidad sigue siendo profundamente desigual. 
    Al analizar la esperanza de vida por continente en 2007, observamos que África no solo tiene el promedio más bajo, 
    sino también la mayor dispersión, indicando una inestabilidad interna crítica.
</p>
""")
new_cells.append(cell_2_markdown)

cell_2_code = nbformat.v4.new_code_cell(source="""
# Filtrar datos 2007
df_2007 = df[df['year'] == 2007]

# Crear Box Plot
fig = px.box(
    df_2007, 
    x='continent', 
    y='lifeExp', 
    color='continent',
    color_discrete_map=colors, # Usar mapa de colores definido anteriormente
    points="outliers" # Mostrar solo outliers para limpieza visual
)

# Ajustes de Estilo "McKinsey"
fig.update_layout(
    title="<b>El lugar de nacimiento sigue dictando la longevidad</b><br><span style='font-size:14px; color:gray'>Esperanza de vida por continente (2007)</span>",
    xaxis_title="",
    yaxis_title="Años de Vida",
    showlegend=False,
    margin=dict(t=80, l=0, r=0, b=0),
    height=450
)

# Anotación destacada para África
median_africa = df_2007[df_2007['continent']=='Africa']['lifeExp'].median()
fig.add_annotation(
    x="Africa", y=median_africa,
    text=f"Mediana: {median_africa:.1f} años",
    showarrow=True, arrowhead=0, ax=40, ay=0,
    font=dict(color=colors['alert'], size=12)
)

fig.show()
""")
new_cells.append(cell_2_code)

# --- SECTION 3: WEALTH VS HEALTH (La Curva de la Prosperidad) ---
cell_3_markdown = nbformat.v4.new_markdown_cell(source="""
<h3>3. EL ANÁLISIS</h3>
<h1>La Curva de la Prosperidad</h1>

<div class="kpi-card">
    <span class="kpi-value">$5,000</span>
    <span class="kpi-label">Umbral de Eficiencia</span>
</div>

<p>
    Existe una correlación positiva innegable entre riqueza (PIB per cápita) y salud. 
    Sin embargo, esta relación no es lineal. Existe un punto de <strong>rendimientos decrecientes</strong>. 
    A partir de los $5,000 USD per cápita, ganar más dinero aporta cada vez menos años adicionales de vida, 
    sugiriendo que la infraestructura básica de salud es más determinante que la riqueza extrema.
</p>
""")
new_cells.append(cell_3_markdown)

cell_3_code = nbformat.v4.new_code_cell(source="""
# Crear Bubble Chart
fig = px.scatter(
    df_2007, 
    x='gdpPercap', 
    y='lifeExp', 
    size='pop', 
    color='continent',
    log_x=True, # Escala logarítmica para ver mejor la distribución
    hover_name='country',
    color_discrete_map=colors,
    size_max=60
)

fig.update_layout(
    title="<b>El dinero compra años, pero con rendimientos decrecientes</b><br><span style='font-size:14px; color:gray'>Relación PIB per Cápita vs Esperanza de Vida (2007)</span>",
    xaxis_title="PIB per Cápita (Escala Log)",
    yaxis_title="Esperanza de Vida",
    margin=dict(t=80, l=0, r=0, b=0),
    height=500,
    legend=dict(title=None)
)

# Línea de umbral visual (ejemplo visual)
fig.add_vline(x=5000, line_width=1, line_dash="dash", line_color="gray", opacity=0.5)
fig.add_annotation(x=np.log10(5000), y=40, text="Umbral de Eficiencia", showarrow=False, xshift=10, font=dict(size=10, color="gray"))

fig.show()
""")
new_cells.append(cell_3_code)

# --- SECTION 4: THE CRISIS (Cuando el Progreso se Detiene) ---
cell_4_markdown = nbformat.v4.new_markdown_cell(source="""
<h3>4. EL QUIEBRE</h3>
<h1>Cuando el Progreso se Detiene: La Crisis de los 90s</h1>

<div class="alert-box">
    <h3>⚠️ La Década Perdida</h3>
    <p>Mientras Asia disparó su esperanza de vida gracias a la industrialización, África sufrió un estancamiento brutal en los años 90. Esto no fue un fallo económico, fue una crisis sanitaria: <strong>la epidemia del VIH/SIDA</strong>.</p>
</div>
""")
new_cells.append(cell_4_markdown)

cell_4_code = nbformat.v4.new_code_cell(source="""
# Preparar datos agregados
df_group = df.groupby(['year', 'continent'])['lifeExp'].median().reset_index()

# Filtrar solo Asia y África para contraste directo
df_contrast = df_group[df_group['continent'].isin(['Asia', 'Africa'])]

fig = px.line(
    df_contrast, 
    x='year', 
    y='lifeExp', 
    color='continent',
    color_discrete_map={'Asia': colors['success'], 'Africa': colors['alert']}, # Verde vs Rojo
    markers=True
)

fig.update_layout(
    title="<b>África perdió una década de progreso en los 90s</b><br><span style='font-size:14px; color:gray'>Comparativa Mediana Esperanza de Vida: Asia vs África (1952-2007)</span>",
    xaxis_title="Año",
    yaxis_title="Esperanza de Vida (Mediana)",
    margin=dict(t=80, l=0, r=0, b=0),
    height=450,
    showlegend=True
)

# Anotación del estancamiento
fig.add_shape(
    type="rect",
    x0=1990, y0=40, x1=2000, y1=60,
    fillcolor="red", opacity=0.1, layer="below", line_width=0,
)
fig.add_annotation(
    x=1995, y=50,
    text="Crisis VIH/SIDA",
    showarrow=False,
    font=dict(color=colors['alert'], size=12, weight="bold")
)

fig.show()
""")
new_cells.append(cell_4_code)

# --- SECTION 5: CONCLUSION ---
cell_5_markdown = nbformat.v4.new_markdown_cell(source="""
<hr style="border: 0; border-top: 1px solid #ddd; margin: 40px 0;">

<h1>Conclusiones Estratégicas</h1>

<div class="insight-box" style="background-color: #f0f7fb; border-left-color: #0f2537;">
    <h3>🚀 Takeaways para el Board</h3>
    <ul style="margin-top:10px">
        <li><strong>El crecimiento global es real, pero desigual:</strong> Hemos ganado 18 años de vida en promedio, pero no todos los mercados maduraron igual.</li>
        <li><strong>Foco en Mercados Emergentes (Asia):</strong> La historia de éxito de Asia demuestra que la inversión en infraestructura paga dividendos masivos en salud.</li>
        <li><strong>Gestión de Riesgos (África):</strong> La volatilidad sanitaria es el mayor riesgo para el desarrollo. Invertir en salud preventiva es invertir en estabilidad económica.</li>
    </ul>
</div>
""")
new_cells.append(cell_5_markdown)


# -------------------------------------------------------------------------
# APPEND AND SAVE
# -------------------------------------------------------------------------

# Append new cells to the notebook
nb.cells.extend(new_cells)

# Save the updated notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print(f"Successfully added {len(new_cells)} cells. New cell count: {len(nb.cells)}")
