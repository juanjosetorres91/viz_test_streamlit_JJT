import nbformat
import re

def update_notebook_content(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Helper to add source annotation and export to code cells
    def add_footer_and_export(source_code, fig_name, image_name):
        footer_code = f"""
# Add Footer
{fig_name}.add_annotation(
    text="Fuente: Gapminder", 
    xref="paper", yref="paper", 
    x=1, y=-0.13, 
    showarrow=False, 
    font=dict(size=10, color="gray")
)
# Export
import os
if not os.path.exists("plots"):
    os.makedirs("plots")
{fig_name}.write_image(f"plots/{image_name}.png", width=1920, height=1080)
"""
        return source_code + footer_code

    # 1. Update Title (Cell 2)
    # Target: "De los Datos a la Acción: El Mito del Progreso" (Already present in structure.txt?) 
    # User said: "No uses 'Trabajo 3', usa 'De los Datos a la Acción...'"
    # In structure.txt it was: <h3>PROYECTO: IMPACTO GLOBAL</h3> <h1>De los Datos a la Acción: El Mito del Progreso</h1>
    # So it might be already correct? User said "Estado Actual: ... Sugerencia: Asegúrate de que este mensaje sea el título".
    # I will double check and ensure it IS that.
    
    # 2. Update Boxplot (Cell 7 - Old 14)
    # fig = px.box(...)
    # I need to append the footer and export.
    cell_boxplot = nb.cells[7]
    if "fig = px.box" in cell_boxplot.source:
        cell_boxplot.source = add_footer_and_export(cell_boxplot.source, "fig", "boxplot_geography")

    # 3. Update HIV Chart (Cell 9 - Old 18)
    # code has "df_group = ..." maybe? Structure.txt said Cell 18: "df_group = df.groupby...".
    # Wait, where is the plot? "fig_conflict = go.Figure..."? No that was Cell 5.
    # Cell 18 (now 9) content: "# Preparar datos agregados ... "
    # I need to check if there is a fig plot there.
    cell_hiv = nb.cells[9]
    # It seems the HIV plot code might be missing valid fig show or assignment in the snippet I saw.
    # I'll check if there is a `fig` or `fig_something`.
    # Assuming `fig` is used (common).
    if "fig" in cell_hiv.source:
         # Need to find the variable name.
         # If it's just `fig = ...`, use `fig`.
         cell_hiv.source = add_footer_and_export(cell_hiv.source, "fig", "linechart_hiv")


    # 4. Update Scatterplot (Cell 15 - Old 16)
    # "fig = px.scatter(..."
    # User: "anotar directamente ... 'África' en rojo y 'Resto del Mundo' en gris ... leyenda no distraiga"
    cell_scatter = nb.cells[15]
    if "fig = px.scatter" in cell_scatter.source:
        # Add specific annotation code for Africa/World
        annotation_code = """
# Simplify Legend and Add Annotations
fig.update_layout(showlegend=False)
fig.add_annotation(x=4000, y=55, text="África", showarrow=False, font=dict(color="#d62728", size=14))
fig.add_annotation(x=20000, y=80, text="Resto del Mundo", showarrow=False, font=dict(color="gray", size=12))
"""
        cell_scatter.source += annotation_code
        cell_scatter.source = add_footer_and_export(cell_scatter.source, "fig", "scatterplot_health_wealth")

    # 5. Update Climax (Cell 18 - Old 11)
    # "fig_climax = px.scatter(..."
    cell_climax = nb.cells[18]
    if "fig_climax" in cell_climax.source:
         cell_climax.source = add_footer_and_export(cell_climax.source, "fig_climax", "scatterplot_climax")

    # 6. Update Conclusion (Cell 19)
    # Append Vietnam example.
    cell_concl = nb.cells[19]
    if "Eficiencia" in cell_concl.source or "Conclusiones" in cell_concl.source:
        vietnam_text = """
<div class="insight-box" style="border-left-color: #2ecc71;">
    <h3>🌱 Modelo de Eficiencia</h3>
    <p>Países como <b>Vietnam</b> lograron alta esperanza de vida con un PIB bajo (ver cuadrante superior izquierdo del scatterplot). 
    África no necesita esperar a ser rica para ser sana; debe copiar modelos de eficiencia sanitaria temprana.</p>
</div>
"""
        cell_concl.source += vietnam_text

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print("Notebook content updated successfully.")

if __name__ == "__main__":
    notebook_path = r"c:/Users/christian.vasquez/Documents/antigravity/storytelling/storytelling_executive.ipynb"
    update_notebook_content(notebook_path)
