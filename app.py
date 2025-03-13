import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Definir la ruta del archivo CSV
file_path = "vehicles_us_lc/vehicles_us.csv"

# Verificar si el archivo existe
if os.path.exists(file_path):
    car_data = pd.read_csv(file_path)

    # Encabezado
    st.header("🚗 Análisis Profesional de Vehículos en Venta")

    # Filtro por tipo de combustible
    fuel_types = car_data["fuel"].unique()
    selected_fuel = st.selectbox("Selecciona un tipo de combustible:", fuel_types)
    filtered_df = car_data[car_data["fuel"] == selected_fuel]

    # Filtro por transmisión
    transmission_types = car_data["transmission"].unique()
    selected_transmission = st.selectbox("Selecciona un tipo de transmisión:", transmission_types)
    filtered_df = filtered_df[filtered_df["transmission"] == selected_transmission]

    # Histograma de precios
    if st.checkbox("📊 Distribución de Precios"):
        st.write(f"Distribución de precios para {selected_fuel} con transmisión {selected_transmission}")
        fig = px.histogram(filtered_df, x="price", nbins=50, title="Distribución de Precios")
        st.plotly_chart(fig, use_container_width=True)

    # Gráfico de dispersión Año del Modelo vs. Precio
    if st.checkbox("📈 Relación Año del Modelo vs. Precio"):
        st.write(f"Tendencia de precios según el año del modelo para {selected_fuel}")
        fig = px.scatter(filtered_df, x="model_year", y="price", color="condition", title="Precio vs. Año del Modelo")
        st.plotly_chart(fig, use_container_width=True)

    # Boxplot de Odómetro por Condición
    if st.checkbox("📦 Comparación de Odómetro por Condición del Vehículo"):
        st.write("Distribución del kilometraje según el estado del vehículo")
        fig = px.box(filtered_df, x="condition", y="odometer", title="Odómetro por Condición del Vehículo")
        st.plotly_chart(fig, use_container_width=True)

    # Comparación de Modelos Más Vendidos
    if st.checkbox("🏆 Modelos más Comunes en Venta"):
        top_models = car_data["model"].value_counts().head(10)
        fig = px.bar(x=top_models.index, y=top_models.values, title="Top 10 Modelos más Vendidos")
        st.plotly_chart(fig, use_container_width=True)

    # Heatmap de Correlación
    if st.checkbox("🔥 Matriz de Correlación entre Variables"):
        st.write("Análisis de correlación entre variables numéricas")
        corr_matrix = filtered_df.select_dtypes(include=["float64", "int64"]).corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
        st.pyplot(fig)

else:
    st.error(f"❌ No se encontró el archivo `{file_path}`. Verifica la ruta.")
