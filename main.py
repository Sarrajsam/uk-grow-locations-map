import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

df = pd.read_csv("Growlocations.csv")
print(df.head(10))
print(df.dtypes)
# Converting
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df = df.dropna() # Drop missing or invalid values

# define variables for dimensions
Longitude_minimum = -10.592
Longitude_maximum = 1.6848
Latitude_minimum = 50.681 
Latitude_maximum = 57.985
# Columns reversed where the error is present
df = df[(df["Longitude"] >= Latitude_minimum) 
        & (df["Longitude"] <= Latitude_maximum)]
df = df[(df["Latitude"] >= Longitude_minimum) 
        & (df["Latitude"] <= Longitude_maximum)]
points = gpd.points_from_xy(df["Latitude"], 
                            df["Longitude"], crs="EPSG:4326") 
# The crs="EPSG:4326" parameter specifies the Coordinate Reference System (CRS) for the geospatial data.

gdf = gpd.GeoDataFrame(df, geometry=points) 
set = set(points)
print(len(set)) # Print number of points

img = mpimg.imread("map7.png")
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(img, extent=[Longitude_minimum, Longitude_maximum, Latitude_minimum, Latitude_maximum])
gdf.plot(ax=ax, color="red", markersize=10)
plt.title("GROW Locations - Python Assignment 2")
plt.show()