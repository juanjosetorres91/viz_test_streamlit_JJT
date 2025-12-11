import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Impacto Global: La Historia de los Datos",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR "PRO" LOOK ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Brandy elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Metrics Cards */
    div[data-testid="metric-container"] {
        background-color: #262730;
        border: 1px solid #3d3d3d;
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    
    /* Custom Headers */
    .section-header {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #FF4B4B, #FF914D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .insight-box {
        background-color: #1E1E1E;
        border-left: 5px solid #FF4B4B;
        padding: 20px;
        border-radius: 0 10px 10px 0;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- DATA LOADING ---
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
        st.error(f"Error crítico: No se encontró '{file_name}'.")
        return None
        
    return pd.read_csv(file_path)

df = load_data()

if df is not None:
    # --- HERO SECTION ---
    st.markdown('<div style="text-align: center; padding: 50px 0;">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 4rem; margin-bottom: 0;">EL PROGRESO GLOBAL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.5rem; color: #888;">Una narrativa visual basada en datos de Gapminder</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # --- 1. SETUP ---
    st.markdown('<div class="section-header">1. El Punto de Partida (1952)</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h3>Un Mundo Dividido</h3>
            <p>En la década de 1950, la línea divisoria era brutal. No había clase media global. 
            El mundo se dividía estrictamente entre occidentales ricos y longevos, y el resto del mundo.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # KPI Metrics
        life_exp_1952 = df[df['year']==1952]['lifeExp'].mean()
        gdp_1952 = df[df['year']==1952]['gdpPercap'].mean()
        
        c1, c2 = st.columns(2)
        c1.metric("Esp. Vida Promedio", f"{life_exp_1952:.1f} años")
        c2.metric("PIB Promedio", f"${gdp_1952:.0f}")

    with col2:
        fig_1952 = px.scatter(
            df[df['year'] == 1952],
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
            template="plotly_dark",
            height=500,
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_1952.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=0, l=0, r=0, b=0)
        )
        st.plotly_chart(fig_1952, use_container_width=True)

    st.markdown("---")

    # --- 2. INSIGHT ---
    st.markdown('<div class="section-header">2. La Evolución (1952-2007)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #262730; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
        <h3>El Ascenso de Asia y el Desafío Africano</h3>
        <p>Observa cómo las burbujas (países) se mueven hacia la esquina superior derecha (salud y riqueza). 
        Asia rompe el patrón, mientras África lucha por despegar.</p>
    </div>
    """, unsafe_allow_html=True)

    fig_anim = px.scatter(
        df,
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
        template="plotly_dark",
        height=600,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    
    fig_anim.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        updatemenus=[dict(type='buttons', showactive=False,
            y=1.05,
            x=1.15,
            xanchor='right',
            yanchor='top',
            pad=dict(t=0, r=10),
            buttons=[dict(label='▶ Reproducir Historia',
                          method='animate',
                          args=[None, dict(frame=dict(duration=600, redraw=True), 
                                           fromcurrent=True, 
                                           mode='immediate')])])],
         sliders=[{
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Año: ',
                'visible': True,
                'xanchor': 'right'
            },
            'transition': {'duration': 300, 'easing': 'cubic-in-out'},
            'pad': {'b': 10, 't': 50},
            'len': 0.9,
            'x': 0.1,
            'y': 0,
            'steps': []
        }]
    )
    
    # Re-generate steps for correct slider connection (Plotly glitch fix)
    sliders_dict = fig_anim.layout.sliders[0]
    for step in sliders_dict['steps']:
        step['args'][1]['frame']['duration'] = 600
        
    st.plotly_chart(fig_anim, use_container_width=True)

    st.markdown("---")

    # --- 3. IMPLICATION ---
    st.markdown('<div class="section-header">3. El Futuro Posible</div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns([2, 1])
    
    with col3:
        asia_trend = df[df['continent'] == 'Asia'].groupby('year')[['gdpPercap', 'lifeExp']].mean().reset_index()
        africa_2007 = df[(df['continent'] == 'Africa') & (df['year'] == 2007)]
        
        fig_imp = go.Figure()
        
        fig_imp.add_trace(go.Scatter(
            x=asia_trend['gdpPercap'], 
            y=asia_trend['lifeExp'],
            mode='lines+markers',
            name='Trayectoria de Asia',
            line=dict(color='#00CC96', width=4)
        ))
        
        fig_imp.add_trace(go.Scatter(
            x=africa_2007['gdpPercap'],
            y=africa_2007['lifeExp'],
            mode='markers',
            name='África (2007)',
            marker=dict(size=12, color='#EF553B', opacity=0.8)
        ))
        
        fig_imp.update_layout(
            title="Comparativa de Oportunidad",
            xaxis_type="log",
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            height=500
        )
        st.plotly_chart(fig_imp, use_container_width=True)
        
    with col4:
        st.markdown("""
        <div class="insight-box" style="border-left-color: #00CC96;">
            <h3>La Hoja de Ruta</h3>
            <p>Muchos países africanos hoy están donde Asia estaba hace 30 años.</p>
            <p><strong>La Inversión Inteligente:</strong></p>
            <ul>
                <li>💉 Salud Preventiva</li>
                <li>🎓 Educación Universal</li>
                <li>🔧 Infraestructura Básica</li>
            </ul>
            <p>Asia demostró que es posible salir de la pobreza extrema en una generación. África es el siguiente gigante dormido.</p>
        </div>
        """, unsafe_allow_html=True)
