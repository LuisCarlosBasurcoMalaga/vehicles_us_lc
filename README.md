# vehicles_us_lc
EN: Development and deployment of an interactive web app with Streamlit for data visualization and analysis. It will be deployed on the cloud using Streamlit Community Cloud, AWS, or Heroku.
ES: Desarrollo y despliegue de una aplicación web interactiva con Streamlit para visualización y análisis de datos. Se implementará en la nube usando Streamlit Community Cloud, AWS o Heroku.
# Análisis de Datos de Vehículos en Venta

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit** que permite analizar un conjunto de datos sobre vehículos en venta. La aplicación ofrece una interfaz para visualizar diferentes gráficos interactivos, como histogramas y diagramas de dispersión, basados en datos de vehículos.

## Descripción

La aplicación permite a los usuarios explorar el conjunto de datos `vehicles_us.csv`, que contiene información sobre vehículos en venta en los Estados Unidos. La información incluye características como el tipo de combustible, el kilometraje (odómetro), el año del modelo, el precio y más.

## Funcionalidades

- **Filtrar los datos por tipo de combustible**: El usuario puede seleccionar un tipo de combustible (gasolina, diésel, etc.) y los datos se filtrarán para mostrar solo los vehículos con ese tipo de combustible.
- **Histograma de odómetro**: Muestra un histograma interactivo del kilometraje de los vehículos seleccionados.
- **Gráfico de dispersión (Precio vs. Odómetro)**: Permite visualizar la relación entre el precio y el kilometraje de los vehículos.
- **Interactividad**: La aplicación es completamente interactiva, lo que permite al usuario cambiar los filtros y ver cómo se actualizan los gráficos en tiempo real.

## Requisitos

- **Python 3.7+**
- **Streamlit**
- **Plotly**
- **Pandas**

### Instalación

Para ejecutar este proyecto, asegúrate de tener **Python 3.7 o superior** y las siguientes dependencias instaladas:

1. Clona este repositorio o descarga los archivos.
2. Crea un entorno virtual y activa el entorno.

   ```bash
   python -m venv vehicles_env
   source vehicles_env/bin/activate  # En Mac/Linux
   vehicles_env\Scripts\activate  # En Windows
