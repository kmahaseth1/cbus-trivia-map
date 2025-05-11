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