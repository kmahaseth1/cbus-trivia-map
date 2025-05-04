import openpyxl as xl
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Update the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the data on trivia list
trivia_wb = xl.load_workbook('cbus_trivia_list.xlsx')
sheet = trivia_wb.active

# Set up Selenium
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Create two additional columns for each trivia night event 
# One for initial URL and another for the full URL
link_cols = [1, 6, 11, 16, 21]

for col in reversed(link_cols):
    new_idx = col + 4
    sheet.insert_cols(new_idx)
    sheet.cell(row=1, column=new_idx).value = 'Initial URL'

    new_idx2 = new_idx + 1
    sheet.insert_cols(new_idx2)
    sheet.cell(row=1, column=new_idx2).value = 'Full URL'

    for row in range(2, sheet.max_row + 1):
        source_cell = sheet.cell(row=row, column=col)
        if source_cell.hyperlink:
            initial_url = source_cell.hyperlink.target
            sheet.cell(row=row, column=new_idx).value = initial_url

        try:
            if initial_url:
                driver.get(initial_url)
                time.sleep(2)
                full_url = driver.current_url
                sheet.cell(row=row, column=new_idx2).value = full_url
        except Exception as e:
            sheet.cell(row=row, column=new_idx2).value = f"Error: {str(e)}"

# Save the workbook
trivia_wb.save('cbus_trivia_list_updated.xlsx')