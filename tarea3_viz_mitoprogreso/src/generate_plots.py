import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os

# Ensure output directory exists
if not os.path.exists("plots"):
    os.makedirs("plots")

# Load Data
print("Loading data...")
# url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
# Use local file if available
local_file = "gapminder-FiveYearData.csv"
if os.path.exists(local_file):
    print(f"Reading from local file: {local_file}")
    df = pd.read_csv(local_file)
else:
    print("Local file not found, downloading...")
    url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
    df = pd.read_csv(url)

# Define Colors
colors = {
    'primary': '#051C2C',
    'secondary': '#00A3E0',
    'accent': '#E74C3C',
    'background': '#FFFFFF',
    'text': '#333333',
    'asia': '#3498db',
    'africa': '#ff6b6b',
    'americas': '#95a5a6',
    'europe': '#0f2537',
    'oceania': '#95a5a6'
}

# 1. Global Trend (Slide 2: Context)
print("Generating Global Trend...")
global_trend = df.groupby('year')['lifeExp'].mean().reset_index()
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=global_trend['year'], 
    y=global_trend['lifeExp'],
    mode='lines+markers',
    line=dict(color=colors['secondary'], width=4),
    name='Global Average'
))
fig1.update_layout(
    title="La esperanza de vida global ha crecido constantemente",
    template="plotly_white",
    xaxis_title="Año",
    yaxis_title="Esperanza de Vida"
)
fig1.add_annotation(text="Fuente: Gapminder", xref="paper", yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=10, color="gray"))
# Use engine='kaleido' explicitly
fig1.write_image("plots/1_global_trend.png", width=1920, height=1080, engine="kaleido")

# 2. HIV Crisis (Slide 3: Conflict 1)
print("Generating HIV Crisis...")
africa_df = df[df['continent'] == 'Africa']
africa_trend = africa_df.groupby('year')['lifeExp'].mean().reset_index()
global_trend = df.groupby('year')['lifeExp'].mean().reset_index() # Redefine ensuring scope

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=global_trend['year'], y=global_trend['lifeExp'], name='Mundo', line=dict(color='lightgray')))
fig2.add_trace(go.Scatter(x=africa_trend['year'], y=africa_trend['lifeExp'], name='África', line=dict(color=colors['accent'], width=4)))
fig2.update_layout(title="La Crisis de los 90s: África se separa del mundo", template="plotly_white")
fig2.add_annotation(x=1995, y=55, text="Epidemia VIH/SIDA", showarrow=True, arrowhead=2)
fig2.add_annotation(text="Fuente: Gapminder", xref="paper", yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=10, color="gray"))
fig2.write_image("plots/2_hiv_crisis.png", width=1920, height=1080)

# 3. Geography Boxplot (Slide 4: Conflict 2)
print("Generating Boxplot...")
df_2007 = df[df['year'] == 2007]
fig3 = px.box(df_2007, x='continent', y='lifeExp', color='continent',
             color_discrete_map={
                 'Asia': colors['asia'], 'Africa': colors['africa'], 
                 'Americas': colors['americas'], 'Europe': colors['europe'], 'Oceania': colors['oceania']
             })
fig3.update_layout(title="La Geografía como Destino: Alta dispersión en África", template="plotly_white", showlegend=False)
fig3.add_annotation(text="Fuente: Gapminder", xref="paper", yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=10, color="gray"))
fig3.write_image("plots/3_geography_gap.png", width=1920, height=1080)

# 4. Scatterplot Analysis (Slide 5-6: Climax)
print("Generating Scatterplot...")
fig4 = px.scatter(
    df_2007, x='gdpPercap', y='lifeExp', size='pop', color='continent',
    log_x=True, size_max=60,
    color_discrete_map={'Asia': 'lightgray', 'Africa': '#d62728', 'Americas': 'lightgray', 'Europe': 'lightgray', 'Oceania': 'lightgray'}
)
fig4.update_layout(title="El Umbral de los $4,000 USD", template="plotly_white", showlegend=False)
fig4.add_vline(x=4000, line_dash="dash", line_color="black", annotation_text="Umbral de Eficiencia")
fig4.add_annotation(x=4000, y=55, text="África", showarrow=False, font=dict(color="#d62728", size=14))
fig4.add_annotation(x=20000, y=85, text="Resto del Mundo", showarrow=False, font=dict(color="gray", size=12))
fig4.add_annotation(text="Fuente: Gapminder", xref="paper", yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=10, color="gray"))
fig4.write_image("plots/4_threshold_scatter.png", width=1920, height=1080)

print("All plots generated via Kaleido.")
