import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

try:
    # Configuración estética para gráficos impactantes
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.family'] = 'sans-serif'

    # Cargar datos
    file_path = 'gapminder-FiveYearData.csv'
    df = pd.read_csv(file_path)

    # Vista rápida
    print("Head:")
    print(df.head())

    # 1. Setup
    data_1952 = df[df['year'] == 1952]
    plt.figure(figsize=(12, 7))
    sns.scatterplot(
        data=data_1952,
        x='gdpPercap',
        y='lifeExp',
        size='pop',
        hue='continent',
        sizes=(20, 1000),
        alpha=0.7,
        palette='muted'
    )
    plt.xscale('log')
    plt.close() # Close to avoid display issues in script
    print("Setup plot created successfully")

    # 2. Insight
    evolution = df.groupby(['continent', 'year'])['lifeExp'].mean().reset_index()
    plt.figure(figsize=(12, 7))
    sns.lineplot(data=evolution, x='year', y='lifeExp', hue='continent', linewidth=2.5)
    plt.close()
    print("Insight plot 1 created successfully")

except Exception as e:
    print(f"ERROR CAUGHT: {e}")
