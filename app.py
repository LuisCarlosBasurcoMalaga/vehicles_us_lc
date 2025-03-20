import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the CSV file path
file_path = 'vehicles_us.csv'

# Check if the file exists
if os.path.exists(file_path):
    car_data = pd.read_csv(file_path)

    # Header
    st.header("🚗 Professional Vehicle Sales Analysis")

    # Filter by fuel type
    fuel_types = car_data["fuel"].unique()
    selected_fuel = st.selectbox("Select a fuel type:", fuel_types)
    
    filtered_df = car_data[car_data["fuel"] == selected_fuel]

    # Filter by transmission type
    transmission_types = car_data["transmission"].unique()
    selected_transmission = st.selectbox("Select a transmission type:", transmission_types)
    filtered_df = filtered_df[filtered_df["transmission"] == selected_transmission]

    # Price histogram
    if st.checkbox("📊 Price Distribution"):
        st.write(f"Price distribution for {selected_fuel} with {selected_transmission} transmission")
        fig = px.histogram(filtered_df, x="price", nbins=50, title="Price Distribution")
        st.plotly_chart(fig, use_container_width=True)

    # Scatter plot: Model Year vs. Price
    if st.checkbox("📈 Model Year vs. Price Relationship"):
        st.write(f"Price trend by model year for {selected_fuel}")
        fig = px.scatter(filtered_df, x="model_year", y="price", color="condition", title="Price vs. Model Year")
        st.plotly_chart(fig, use_container_width=True)

    # Boxplot: Odometer by Condition
    if st.checkbox("📦 Odometer Comparison by Vehicle Condition"):
        st.write("Mileage distribution by vehicle condition")
        fig = px.box(filtered_df, x="condition", y="odometer", title="Odometer by Vehicle Condition")
        st.plotly_chart(fig, use_container_width=True)

    # Most Sold Models Comparison
    if st.checkbox("🏆 Most Common Models on Sale"):
        top_models = car_data["model"].value_counts().head(10)
        fig = px.bar(x=top_models.index, y=top_models.values, title="Top 10 Most Sold Models")
        st.plotly_chart(fig, use_container_width=True)

    # Correlation Heatmap
    if st.checkbox("🔥 Correlation Matrix Between Variables"):
        st.write("Correlation analysis between numerical variables")
        corr_matrix = filtered_df.select_dtypes(include=["float64", "int64"]).corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
        st.pyplot(fig)

else:
    st.error(f"❌ File `{file_path}` not found. Please verify the path.")

