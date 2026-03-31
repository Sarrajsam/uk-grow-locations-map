# uk-grow-locations-map
Python project for cleaning, processing, and visualizing geospatial GROW location data on a UK map
# 📍 GROW Locations Geospatial Visualization

## 🎓 Project Overview

This project was developed as part of my coursework at the **University of Dundee**. It focuses on using Python to clean, process, and visualize geospatial data for **GROW locations**.

The project demonstrates how location data can be converted into a geographic format and plotted on a map using Python libraries commonly used in data analysis and GIS-related tasks.

---

## 🚀 Key Features

* Reads location data from a CSV file
* Cleans and validates latitude and longitude values
* Converts tabular data into geospatial points
* Uses a geographic coordinate reference system (**EPSG:4326**)
* Visualizes location points on a UK map

---

## 🛠️ Technologies Used

* Python
* Pandas
* GeoPandas
* Matplotlib

---

## ⚙️ How It Works

### 1. Load the Data

The program reads location records from a CSV file.

### 2. Clean and Prepare Coordinates

* Converts latitude and longitude columns into numeric values
* Removes invalid or missing records
* Filters coordinates based on expected UK map boundaries

### 3. Create Geospatial Points

The cleaned data is converted into geographic points using **GeoPandas** and the **EPSG:4326** coordinate reference system.

### 4. Visualize the Results

The final points are plotted on top of a background UK map image to create a clear geographic visualization of GROW locations.

---

## 📂 Project Files

```text
.
├── main.py
├── GrowLocations.csv
├── map7.png
└── README.md
```

---

## ▶️ How to Run

1. Install the required libraries:

```bash
pip install pandas geopandas matplotlib
```

2. Make sure the following files are in the same folder:

* `main.py`
* `GrowLocations.csv`
* `map7.png`

3. Run the script:

```bash
python main.py
```

---

## 📊 Output

The program generates a visualization showing GROW locations as plotted points on a UK map.

---

## 💡 What I Learned

* Working with real-world geographic datasets
* Cleaning and validating coordinate data
* Using GeoPandas for geospatial processing
* Visualizing geographic information with Python
* Combining data analysis with mapping techniques

---

## 🔮 Possible Improvements

* Add interactive maps using Folium or Plotly
* Improve coordinate validation logic
* Add labels or clustering for locations
* Export the final map as an image automatically
* Make file paths configurable by the user

---

## 👤 Author

**Sarraj Alsammak**
University of Dundee

---

> This project reflects my ability to work with data cleaning, geospatial analysis, and Python-based visualization — skills relevant to data analysis and GIS-related roles.
