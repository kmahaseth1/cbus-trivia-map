import folium
import os
import pandas as pd
import calendar as cd
import re

# Update the current working directory to the main project folder
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create DataFrames for each day
df = pd.read_excel('data/cbus_trivia_list_updated.xlsx')

df_mon = df.iloc[:11, 0:6]
df_tue = df.iloc[:57, 7:13]
df_wed = df.iloc[:63, 14:20]
df_thu = df.iloc[:40, 21:27]
df_fri = df.iloc[:5, 28:34]
df_sat = df.iloc[7:11, 28:34]
df_sun = df.iloc[14:20, 28:34]

# Update column headers
dfs = [df_mon, df_tue, df_wed, df_thu, df_fri, df_sat, df_sun]
days = list(cd.day_name)
constant_cols = ['Bar', 'Company', 'Host', 'Start Time', 'Address', 'Address 2']

# Add day column to each DataFrame
for i, df in enumerate(dfs):
    df.columns = constant_cols
    df["Day"] = days[i]

# Create the primary DataFrame
cbus_trivia_df = pd.concat(dfs, ignore_index=True)
cbus_trivia_df = cbus_trivia_df[cbus_trivia_df['Bar'].notna()]

# Extract coordinates from the full url
lat = []
lon = []
for i in cbus_trivia_df['Address 2']:
    match = re.search(r"@(-?\d+\.\d+),(-?\d+\.\d+)", i)

    if match:
        lat.append(match.group(1))
        lon.append(match.group(2))

# Add latitude and longitude columns to the DataFrame
cbus_trivia_df['Latitude'] = lat
cbus_trivia_df['Longitude'] = lon

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