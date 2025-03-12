import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Definir la ruta del archivo CSV
file_path = "vehicles_us_lc/vehicles_us.csv"

# Verificar si el archivo existe
if os.path.exists(file_path):
    car_data = pd.read_csv(file_path)

    # Encabezado
    st.header("🚗 Análisis de Vehículos en Venta")

    # Filtro por tipo de combustible
    fuel_types = car_data["fuel"].unique()
    selected_fuel = st.selectbox("Selecciona un tipo de combustible:", fuel_types)

    # Filtrar datos por tipo de combustible
    filtered_df = car_data[car_data["fuel"] == selected_fuel]

    # Casilla de verificación para el histograma
    if st.checkbox("📊 Mostrar histograma del odómetro"):
        st.write(f"Histograma del odómetro para vehículos con {selected_fuel}")
        fig = px.histogram(filtered_df, x="odometer", title=f"Histograma del Odómetro ({selected_fuel})")
        st.plotly_chart(fig, use_container_width=True)

    # Casilla de verificación para el gráfico de dispersión
    if st.checkbox("🔵 Mostrar gráfico de dispersión Precio vs Odómetro"):
        st.write(f"Gráfico de dispersión: Precio vs Odómetro para {selected_fuel}")
        fig = px.scatter(filtered_df, x="odometer", y="price", title=f"Precio vs Odómetro ({selected_fuel})")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.error(f"❌ No se encontró el archivo `{file_path}`. Verifica la ruta.")
