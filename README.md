# vehicles_us_lc
Vehicle Data Analysis  Exploratory data analysis project using Streamlit, pandas, and Plotly Express. It enables visualizing trends and patterns in vehicle data through an interactive web interface.
# 🚗 Vehicle Sales Analysis with Python

## 📋 Project Overview
This project analyzes vehicle sales data in the United States, focusing on trends, pricing, and key vehicle characteristics. The dataset used is `vehicles_us.csv`, which contains essential information about vehicles listed for sale.

## 📊 Exploratory Data Analysis (EDA)
The `EDA.ipynb` file explores the dataset in detail, presenting various visualizations and insights:

- **📉 Price Distribution:** A histogram showcasing the distribution of vehicle prices.
- **📅 Model Year vs. Price:** A scatter plot highlighting the relationship between model year and vehicle price.
- **🛣️ Odometer Reading Analysis:** A box plot comparing odometer readings based on vehicle condition.
- **🏆 Top 10 Most Sold Models:** A bar chart showing the most frequently listed vehicle models.
- **🔥 Correlation Matrix:** A heatmap illustrating the correlation between numerical variables.

## 🖥️ Interactive Web Application
The `app.py` file provides an interactive Streamlit app for users to explore the data with dynamic filtering options:

- **⛽ Fuel Type Filter:** Filter vehicles by their fuel type.
- **⚙️ Transmission Filter:** Select specific transmission types.
- **📊 Price Distribution:** Interactive histogram visualizing the distribution of prices based on selected filters.
- **📈 Model Year vs. Price:** Interactive scatter plot showing how vehicle prices vary by model year.
- **📦 Odometer by Condition:** Box plot comparing mileage for vehicles with different conditions.
- **🏆 Top Models in Demand:** A bar chart displaying the most frequently listed vehicle models.
- **🔥 Correlation Matrix:** Heatmap showcasing the relationship between numerical variables.

## 🛠️ Technologies Used
- **Python**: Data analysis and visualization
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **Seaborn & Matplotlib**: Enhanced data visualization
- **Streamlit**: Interactive web app development
- 
Dataset

The dataset (vehicles_us.csv) contains the following key columns:

💰 price: Vehicle sale price

📅 model_year: Year the vehicle was manufactured

🚗 model: Vehicle model name

🛠️ condition: Vehicle condition (e.g., excellent, good, fair)

🔧 cylinders: Engine cylinder count

⛽ fuel: Fuel type (e.g., gasoline, diesel, electric)

🛣️ odometer: Vehicle mileage

⚙️ transmission: Transmission type

🚜 type: Vehicle type (e.g., SUV, sedan, truck)

🎨 paint_color: Exterior paint color

❄️ is_4wd: Whether the vehicle has four-wheel drive

🗓️ date_posted: Date the vehicle listing was posted

📆 days_listed: Number of days the vehicle listing was active

Future Improvements

🚨 Enhance outlier detection methods for improved data accuracy.

📊 Implement advanced visualizations for deeper insights.

🤖 Add machine learning models to predict vehicle prices based on provided features.

**Author**

**Luis Carlos - Data Scientist and Industrial Engineer specializing in business analytics and data visualization.**

## 🚀 Demo de la aplicación

Puedes probar la aplicación en el siguiente enlace:

👉 [Aplicación desplegada en Render](https://vehicles-us-lc.onrender.com)





