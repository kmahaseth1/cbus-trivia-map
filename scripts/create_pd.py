import os
import pandas as pd
import calendar as cd
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv

# Update the current working directory to the main project folder
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Access the OpenCage API key
load_dotenv()
api_key = os.getenv('OPENCAGE_API')

# Create DataFrames for each day
df = pd.read_excel('data/cbus_trivia_list_updated.xlsx')

df_mon = df.iloc[:11, 0:5]
df_tue = df.iloc[:57, 6:11]
df_wed = df.iloc[:63, 12:17]
df_thu = df.iloc[:40, 18:23]
df_fri = df.iloc[:5, 24:29]
df_sat = df.iloc[7:11, 24:29]
df_sun = df.iloc[14:20, 24:29]

# Update column headers
dfs = [df_mon, df_tue, df_wed, df_thu, df_fri, df_sat, df_sun]
days = list(cd.day_name)
constant_cols = ['Bar', 'Company', 'Host', 'Start Time', 'Address']

# Add day column to each DataFrame
for i, df in enumerate(dfs):
    df.columns = constant_cols
    df["Day"] = days[i]

# Create the primary DataFrame
cbus_trivia_df = pd.concat(dfs, ignore_index=True)
cbus_trivia_df = cbus_trivia_df[cbus_trivia_df['Bar'].notna()]
cbus_trivia_df = cbus_trivia_df[cbus_trivia_df['Address'].notna()]

# Extract coordinates from the street address
lat = []
lon = []
geocoder = OpenCageGeocode(api_key)
for a in cbus_trivia_df['Address']:
    coord = geocoder.geocode(a)
    if coord and len(coord):
        lat.append(coord[0]['geometry']['lat'])
        lon.append(coord[0]['geometry']['lng'])
    else:
        lat.append(None)
        lon.append(None)

# Add latitude and longitude columns to the DataFrame
cbus_trivia_df['Latitude'] = lat
cbus_trivia_df['Longitude'] = lon

# Save df as an excel file to enable manual update of coordinates
cbus_trivia_df.to_excel('data/final_trivia_list.xlsx')