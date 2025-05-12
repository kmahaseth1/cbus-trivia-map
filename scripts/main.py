import folium
import os
import pandas as pd

# Update the current working directory to the main project folder
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Read the updated excel workbook
final_df = pd.read_excel('data/final_trivia_list.xlsx')

# Create the base map
# Columbus's Coordinates
cbus_coords = [40.020000, -82.998795]

# Create the map
cbus_map = folium.Map(location = cbus_coords, zoom_start = 11.15)

# Create FeatureGroup to add markers and day based filter
for day in final_df['Day'].unique():
    feature_group = folium.FeatureGroup(name = day)
    day_df = final_df[final_df['Day'] == day]

    for i, row in day_df.iterrows():
        label_html = f"""
        <b>Bar Name:</b> {row['Bar']}<br>
        <b>Trivia Day:</b> {row['Day']}<br>
        <b>Company:</b> {row['Company']}<br>
        <b>Start Time:</b> {row['Start Time']}<br>
        <b>Address:</b> {row['Address']}
        """
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(label_html, max_width=500)
        ).add_to(feature_group)
    
    feature_group.add_to(cbus_map)

# Add checkbox
folium.LayerControl(collapsed=False).add_to(cbus_map)

# Save the map
cbus_map.save("output/cbus_map.html")