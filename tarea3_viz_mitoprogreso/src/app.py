import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuración de la página
st.set_page_config(
    page_title="Narrativa Visual: El Progreso Global",
    page_icon="🌍",
    layout="wide"
)

# Cargar datos de manera robusta
@st.cache_data
def load_data():
    file_name = 'gapminder-FiveYearData.csv'
    possible_paths = [
        file_name,
        os.path.join('data', file_name),
        os.path.join('..', file_name),
        r'c:\Users\christian.vasquez\Documents\antigravity\storytelling\gapminder-FiveYearData.csv'
    ]
    
    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break
            
    if file_path is None:
        st.error(f"No se encontró el archivo '{file_name}'.")
        return None
        
    return pd.read_csv(file_path)

df = load_data()

if df is not None:
    # Sidebar
    st.sidebar.title("🌍 Filtros y Navegación")
    st.sidebar.markdown("**Historia:** Evolución de la salud y riqueza (1952-2007).")
    
    selected_continents = st.sidebar.multiselect(
        "Seleccionar Continentes:",
        options=df['continent'].unique(),
        default=df['continent'].unique()
    )
    
    # Filtrar datos
    df_filtered = df[df['continent'].isin(selected_continents)]

    # Título Principal
    st.title("Narrativa Visual: El Progreso Global y las Brechas Persistentes")
    st.markdown("### Framework: Setup – Insight – Implicación")
    st.markdown("---")

    # 1. SETUP
    st.header("1. Setup: La Brecha Abismal de 1952")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Todo comienza en 1952.**
        
        En este punto de partida, el mundo estaba claramente dividido:
        - **Occidente y Europa:** Ricos y longevos.
        - **África y Asia:** Atrapados en la pobreza con baja esperanza de vida.
        
        *Observa la esquina inferior izquierda: ahí vivía la mayoría de la humanidad.*
        """)
    
    with col2:
        fig_1952 = px.scatter(
            df_filtered[df_filtered['year'] == 1952],
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
            title="1952: Un Mundo Dividido"
        )
        st.plotly_chart(fig_1952, use_container_width=True)

    st.markdown("---")

    # 2. INSIGHT
    st.header("2. Insight: El Milagro Asiático y el Rezagado Africano")
    
    st.markdown("""
    **Revelación:** A lo largo de 55 años, la historia cambió dramáticamente.
    - **Asia** (especialmente China e India) se disparó hacia arriba y a la derecha.
    - **África** vio mejoras, pero mucho más lentas y estancadas en los 90s.
    
    *Dale play a la animación a continuación para ver esta evolución.*
    """)
    
    fig_anim = px.scatter(
        df_filtered,
        x="gdpPercap",
        y="lifeExp",
        animation_frame="year",
        animation_group="country",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=55,
        range_x=[100, 100000],
        range_y=[25, 90],
        title="Evolución Dinámica (1952-2007)"
    )
    st.plotly_chart(fig_anim, use_container_width=True)

    st.markdown("---")

    # 3. IMPLICATION
    st.header("3. Implicación: Inversión Focalizada")
    
    st.markdown("""
    **Conclusión:** El desarrollo es posible.
    
    Muchos países de África en 2007 están donde Asia estaba hace décadas.
    > **Acción:** Replicar las inversiones en **salud pública y educación** que impulsaron a Asia es la clave para desbloquear el potencial de África.
    """)
    
    # Gráfico comparativo final
    # Trayectoria Asia vs Africa 2007
    asia_trend = df[df['continent'] == 'Asia'].groupby('year')[['gdpPercap', 'lifeExp']].mean().reset_index()
    africa_2007 = df[(df['continent'] == 'Africa') & (df['year'] == 2007)]
    
    import plotly.graph_objects as go
    
    fig_imp = go.Figure()
    
    # Asia Trend
    fig_imp.add_trace(go.Scatter(
        x=asia_trend['gdpPercap'], 
        y=asia_trend['lifeExp'],
        mode='lines+markers',
        name='Trayectoria Histórica Asia',
        line=dict(color='blue', dash='dash')
    ))
    
    # Africa 2007
    fig_imp.add_trace(go.Scatter(
        x=africa_2007['gdpPercap'],
        y=africa_2007['lifeExp'],
        mode='markers',
        name='Países Africanos (2007)',
        marker=dict(size=10, color='orange')
    ))
    
    fig_imp.update_layout(
        title="El Camino a Seguir: Comparando Trayectorias",
        xaxis_type="log",
        xaxis_title="PIB per Cápita (log)",
        yaxis_title="Esperanza de Vida"
    )
    
    st.plotly_chart(fig_imp, use_container_width=True)
