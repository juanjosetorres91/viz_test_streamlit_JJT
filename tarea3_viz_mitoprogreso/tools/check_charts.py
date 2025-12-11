"""
Script para extraer graficos del HTML del notebook y usarlos en el PPT
"""
import os
import base64
import re
from bs4 import BeautifulSoup

def extract_plotly_from_html(html_file, output_dir):
    """Extrae graficos Plotly del HTML del notebook"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Buscar todos los divs de Plotly
    plotly_divs = soup.find_all('div', class_='plotly-graph-div')
    
    print(f"Encontrados {len(plotly_divs)} graficos Plotly en el HTML")
    
    # Intentar encontrar imagenes incrustadas
    img_tags = soup.find_all('img')
    print(f"Encontradas {len(img_tags)} imagenes en el HTML")
    
    # Buscar scripts de Plotly que contienen los datos
    plotly_scripts = soup.find_all('script', type='text/javascript')
    plotly_count = 0
    
    for script in plotly_scripts:
        if script.string and 'Plotly.newPlot' in script.string:
            plotly_count += 1
            print(f"  Grafico Plotly #{plotly_count} encontrado")
    
    print("\nNota: Los graficos estan embebidos como JavaScript interactivo.")
    print("Para exportarlos como imagenes estaticas, necesitas ejecutar el notebook.")
    
    return plotly_count

if __name__ == "__main__":
    html_file = "storytelling_executive.html"
    output_dir = "plots"
    
    count = extract_plotly_from_html(html_file, output_dir)
    print(f"\n{'='*50}")
    print(f"Total: {count} graficos detectados")
    print(f"Para generar PNGs: ejecuta el notebook en Jupyter")
    print(f"{'='*50}")
