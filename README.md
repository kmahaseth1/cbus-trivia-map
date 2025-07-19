# Interactive Map of Bar Trivia events in Columbus, Ohio
An end-to-end data visualization project that geocodes, and displays live events data on an interactive map using Python.

[Demo]('demo.mov')

## Overview
This project uses Python, Pandas, and the Folium mapping library to generate an interactive map of bar trivia nights in Columbus, Ohio. Data is sourced from a public Google Sheet shared in a [Reddit post](https://www.reddit.com/r/Columbus/comments/1cwl7eo/columbus_area_trivia_master_list/?rdt=46370) on r/Columbus by user [smf1114](https://www.reddit.com/user/smf1114/). The final product is an intuitive `.html` map that can be opened in any modern browser.

## Output
View the interactive map [here](https://kmahaseth1.github.io/cbus-trivia-map/output/cbus_map.html)

## Tech Stack & Tools
- Python: data extraction, transformation, and visualization
- Pandas: data cleaning and manipulation
- Folium: interactive leaflet maps in Python
- OpenCage Geocoder: address-to-coordinate conversion for mapping

## Features
- Plots each event on a Folium map with popups showing:
    - Bar name
    - Event day
    - Trvia Company
    - Start Time
    - Bar address
- Uses OpenCage Geocoder to convert venue addresses into latitude/longitude
- Adds interactive filtering by day of the week, allowing users to view only events happening on specific days
- Exports the final product as a standalone HTML map file

## Before You Go
The trivia information displayed on this map is based on data from the Google Sheets linked in the original Reddit post. Please note that changes to event dates, times, or cancellations may not be reflected here. If you plan to attend an event, it's best to confirm the details directly with the hosting establishment.
