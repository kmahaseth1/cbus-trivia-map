import folium
import os
import pandas as pd
import calendar as cd

# Update the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create DataFrames for each day
df = pd.read_excel('cbus_trivia_list_updated.xlsx')

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
constant_cols = ['Bar', 'Company', 'Host', 'Time', 'Address', 'Address 2']

# Add day column to each DataFrame
for i, df in enumerate(dfs):
    df.columns = constant_cols
    df["Day"] = days[i]

# Create the primary DataFrame
cbus_trivia_df = pd.concat(dfs, ignore_index=True)
cbus_trivia_df = cbus_trivia_df[cbus_trivia_df['Bar'].notna()]

# Extract coordinates from maps link

# Add latitude and longitude columns to the DataFrame

# Create the base map
# Columbus's Coordinates
# cbus_coords = [39.971178, -82.998795]

# Create the map
# cbus_map = folium.Map(location = cbus_coords, zoom_start = 11.15)

# Add markers

# Add filters

# Save the map
#cbus_map.save("cbus_map.html")