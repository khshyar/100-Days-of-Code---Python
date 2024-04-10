from shapely.ops import split
from shapely.geometry import Polygon, LineString
import folium
import numpy as np

# Points, ensuring the polygon is a closed loop by repeating the first point
points = [
    [50.148298, 8.746891],
    [50.148346, 8.746451],
    [50.148698, 8.746861],
    [50.148298, 8.746891]  # Closing the loop by repeating the first point
]

# Creating a Shapely Polygon from the provided points
polygon = Polygon(points)

# Calculating the bounds for the polygon to determine the range for division
minx, miny, maxx, maxy = polygon.bounds

# Division logic for a vertical split based on the percentage
dividing_longitude = minx + (maxx - minx) * (60 / 100)

# Line that cuts across the polygon vertically at the calculated division point
division_line = LineString(
    [(dividing_longitude, miny), (dividing_longitude, maxy)])

# Splitting the polygon along the division line
split_polygons = split(polygon, division_line)

# Initialize a folium map centered around the mean of the points
map_center = np.mean(points, axis=0).tolist()
m = folium.Map(location=map_center, zoom_start=16)

# Adding the original polygon to the map for reference
folium.GeoJson(polygon, style_function=lambda x: {
               'fillColor': 'white', 'color': 'black'}).add_to(m)

# Loop through each part of the split polygons and add them to the map
for part in split_polygons.geoms:
    folium.GeoJson(part, style_function=lambda x: {
                   'fillColor': 'blue', 'color': 'blue', 'fillOpacity': 0.6}).add_to(m)

# Save the map to an HTML file
map_file_path = 'shapely_divided_polygon_map.html'
m.save(map_file_path)
