# vehicles_us_lc
Vehicle Data Analysis  Exploratory data analysis project using Streamlit, pandas, and Plotly Express. It enables visualizing trends and patterns in vehicle data through an interactive web interface.
# Vehicle Sales Data Analysis

This project analyzes vehicle sales data using Python and visualizes key insights through an interactive dashboard built with Streamlit. The dataset used is `vehicles_us.csv` and includes various features such as vehicle price, model year, fuel type, transmission, and more.

## Project Structure
- **`EDA.ipynb`** - Exploratory Data Analysis (EDA) notebook containing visualizations and insights from the dataset.
- **`app.py`** - Interactive dashboard for data exploration.
- **`requirements.txt`** - List of required libraries for the project.
- **`vehicles_us.csv`** - Dataset containing vehicle information.

## Exploratory Data Analysis (EDA)
The `EDA.ipynb` notebook explores the dataset through various visualizations:

### 1. **Price Distribution**
- **Description:** A histogram showing the distribution of vehicle prices.
- **Insight:** Highlights the most common price ranges and potential outliers.

### 2. **Model Year vs. Price**
- **Description:** A scatter plot that visualizes the relationship between vehicle model year and price.
- **Insight:** Newer vehicles generally have higher prices, with some exceptions for older, high-value models.

### 3. **Odometer Reading by Vehicle Condition**
- **Description:** A box plot displaying odometer readings grouped by vehicle condition.
- **Insight:** Vehicles in better condition tend to have lower mileage.

### 4. **Most Popular Vehicle Models**
- **Description:** A bar chart showcasing the top 10 most common vehicle models in the dataset.
- **Insight:** Certain models dominate the listings, indicating potential trends in the used car market.

### 5. **Correlation Matrix**
- **Description:** A heatmap illustrating the correlation between numerical variables.
- **Insight:** Identifies strong and weak correlations to better understand variable relationships.

## Interactive Dashboard (`app.py`)
The interactive dashboard enhances data exploration with user-friendly features:

### Features:
- **Fuel Type Filter:** Select a specific fuel type to filter the dataset.
- **Transmission Filter:** Filter vehicles based on transmission type.
- **Price Distribution Chart:** Interactive histogram showing filtered vehicle prices.
- **Model Year vs. Price Scatter Plot:** Visualizes trends based on user-selected criteria.
- **Odometer by Condition Box Plot:** Displays mileage distribution for selected vehicle types.
- **Top 10 Models Bar Chart:** Highlights the most frequently listed models.
- **Correlation Heatmap:** Visualizes correlations for selected data subsets.

## Dataset
The dataset (`vehicles_us.csv`) contains the following key columns:
- **price**: Vehicle sale price
- **model_year**: Year the vehicle was manufactured
- **model**: Vehicle model name
- **condition**: Vehicle condition (e.g., excellent, good, fair)
- **cylinders**: Engine cylinder count
- **fuel**: Fuel type (e.g., gasoline, diesel, electric)
- **odometer**: Vehicle mileage
- **transmission**: Transmission type
- **type**: Vehicle type (e.g., SUV, sedan, truck)
- **paint_color**: Exterior paint color
- **is_4wd**: Whether the vehicle has four-wheel drive
- **date_posted**: Date the vehicle listing was posted
- **days_listed**: Number of days the vehicle listing was active

## Future Improvements
- Enhance outlier detection methods for improved data accuracy.
- Implement advanced visualizations for deeper insights.
- Add machine learning models to predict vehicle prices based on provided features.

## Author
**Luis Carlos** - Data Scientist and Industrial Engineer specializing in business analytics and data visualization.
