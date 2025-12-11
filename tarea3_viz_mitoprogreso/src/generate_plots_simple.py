"""
Script simplificado para generar solo los gráficos esenciales
"""
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os

# Create output directory
os.makedirs("plots", exist_ok=True)

# Load data
print("Cargando datos...")
df = pd.read_csv("gapminder-FiveYearData.csv")

# Define colors
colors = {
    'primary': '#051C2C',
    'secondary': '#00A3E0',
    'accent': '#E74C3C',
    'africa': '#ff6b6b'
}

print("Generando grafico 1: Tendencia Global...")
# Chart 1: Global Trend
global_trend = df.groupby('year')['lifeExp'].mean().reset_index()
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=global_trend['year'], 
    y=global_trend['lifeExp'],
    mode='lines+markers',
    line=dict(color=colors['secondary'], width=4)
))
fig1.update_layout(
    title="La Esperanza de Vida Global Crece Constantemente",
    template="plotly_white",
    xaxis_title="Año",
    yaxis_title="Esperanza de Vida (años)",
    font=dict(family="Arial", size=12)
)
fig1.add_annotation(
    text="Fuente: Gapminder", 
    xref="paper", yref="paper", 
    x=1, y=-0.15, 
    showarrow=False, 
    font=dict(size=10, color="gray")
)

try:
    fig1.write_image("plots/1_tendencia_global.png", width=1200, height=800, engine="kaleido")
    print("  ✓ Guardado: plots/1_tendencia_global.png")
except Exception as e:
    print(f"  ✗ Error: {e}")

print("\nGenerando grafico 2: Boxplot Geografia...")
# Chart 2: Geography Boxplot
df_2007 = df[df['year'] == 2007]
fig2 = px.box(
    df_2007, 
    x='continent', 
    y='lifeExp',
    color='continent',
    color_discrete_map={
        'Africa': colors['africa'],
        'Americas': '#95a5a6',
        'Asia': '#3498db',
        'Europe': '#0f2537',
        'Oceania': '#95a5a6'
    }
)
fig2.update_layout(
    title="Alta Dispersión en África: La Geografía como Destino",
    template="plotly_white",
    xaxis_title="Continente",
    yaxis_title="Esperanza de Vida (años)",
    showlegend=False,
    font=dict(family="Arial", size=12)
)
fig2.add_annotation(
    text="Fuente: Gapminder", 
    xref="paper", yref="paper", 
    x=1, y=-0.15, 
    showarrow=False, 
    font=dict(size=10, color="gray")
)

try:
    fig2.write_image("plots/2_geografia_boxplot.png", width=1200, height=800, engine="kaleido")
    print("  ✓ Guardado: plots/2_geografia_boxplot.png")
except Exception as e:
    print(f"  ✗ Error: {e}")

print("\nGenerando grafico 3: Crisis VIH...")
# Chart 3: HIV Crisis Timeline
africa_trend = df[df['continent'] == 'Africa'].groupby('year')['lifeExp'].mean().reset_index()
world_trend = df.groupby('year')['lifeExp'].mean().reset_index()

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=world_trend['year'], 
    y=world_trend['lifeExp'],
    name='Mundo',
    line=dict(color='lightgray', width=3)
))
fig3.add_trace(go.Scatter(
    x=africa_trend['year'], 
    y=africa_trend['lifeExp'],
    name='África',
    line=dict(color=colors['accent'], width=4)
))
fig3.update_layout(
    title="La Crisis de los 90s: Cuando África se Separó del Mundo",
    template="plotly_white",
    xaxis_title="Año",
    yaxis_title="Esperanza de Vida (años)",
    font=dict(family="Arial", size=12)
)
fig3.add_annotation(
    x=1995, y=55,
    text="Epidemia VIH/SIDA",
    showarrow=True,
    arrowhead=2,
    arrowcolor=colors['accent']
)
fig3.add_annotation(
    text="Fuente: Gapminder", 
    xref="paper", yref="paper", 
    x=1, y=-0.15, 
    showarrow=False, 
    font=dict(size=10, color="gray")
)

try:
    fig3.write_image("plots/3_crisis_vih.png", width=1200, height=800, engine="kaleido")
    print("  ✓ Guardado: plots/3_crisis_vih.png")
except Exception as e:
    print(f"  ✗ Error: {e}")

print("\nGenerando grafico 4: Umbral $4000...")
# Chart 4: The $4000 Threshold
fig4 = px.scatter(
    df_2007,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    log_x=True,
    size_max=60,
    color_discrete_map={
        'Africa': '#d62728',
        'Americas': 'lightgray',
        'Asia': 'lightgray',
        'Europe': 'lightgray',
        'Oceania': 'lightgray'
    }
)
fig4.update_layout(
    title="El 80% del Progreso Ocurre Antes de $4,000 USD",
    template="plotly_white",
    xaxis_title="PIB per Cápita (USD, log)",
    yaxis_title="Esperanza de Vida (años)",
    showlegend=False,
    font=dict(family="Arial", size=12)
)
fig4.add_vline(
    x=4000, 
    line_dash="dash", 
    line_color="black",
    annotation_text="Umbral"
)
fig4.add_annotation(
    text="Fuente: Gapminder", 
    xref="paper", yref="paper", 
    x=1, y=-0.15, 
    showarrow=False, 
    font=dict(size=10, color="gray")
)

try:
    fig4.write_image("plots/4_umbral_4000.png", width=1200, height=800, engine="kaleido")
    print("  ✓ Guardado: plots/4_umbral_4000.png")
except Exception as e:
    print(f"  ✗ Error: {e}")

print("\n¡Proceso completado!")
