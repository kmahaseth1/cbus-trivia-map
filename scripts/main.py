
import folium
import os
from create_pd import cbus_trivia_df

# Update the current working directory to the main project folder
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create the base map
# Columbus's Coordinates
cbus_coords = [39.971178, -82.998795]

# Create the map
cbus_map = folium.Map(location = cbus_coords, zoom_start = 11.15)

# Create FeatureGroup to add markers and day based filter
for day in cbus_trivia_df['Day'].unique():
    feature_group = folium.FeatureGroup(name = day)
    day_df = cbus_trivia_df[cbus_trivia_df['Day'] == day]

    for i, row in day_df.iterrows():
        label_html = f"""
        <b>Bar Name:</b> {row['Bar']}<br>
        <b>Trivia Day:</b> {row['Day']}<br>
        <b>Company:</b> {row['Company']}<br>
        <b>Start Time:</b> {row['Start Time']}
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