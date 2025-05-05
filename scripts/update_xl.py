import openpyxl as xl
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Update the current working directory to the main project folder
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Read the trivia list data
trivia_wb = xl.load_workbook('data/cbus_trivia_list.xlsx')
sheet = trivia_wb.active

# Set up Selenium
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Create two additional columns for each trivia event 
# One for initial URL and another for the full URL
link_cols = [1, 6, 11, 16, 21]

for col in reversed(link_cols):
    new_idx = col + 4
    sheet.insert_cols(new_idx)
    sheet.cell(row=1, column=new_idx).value = 'Initial URL'

    new_idx2 = new_idx + 1
    sheet.insert_cols(new_idx2)
    sheet.cell(row=1, column=new_idx2).value = 'Full URL'

    num_empty_rows = 0
    custom_max_row = sheet.max_row
    for row in range(2, sheet.max_row + 1):
        source_cell = sheet.cell(row=row, column=col)

        if not source_cell.value:
           num_empty_rows += 1
        else:
           num_empty_rows = 0

        if num_empty_rows >=4:
            custom_max_row = row - 4
            break

    for row in range(2, custom_max_row+ 1):
        source_cell = sheet.cell(row=row, column=col)
        initial_url = None

        if source_cell.hyperlink:
            initial_url = source_cell.hyperlink.target
            sheet.cell(row=row, column=new_idx).value = initial_url

        try:
            # If the initial URL exists, retrieve the full URL
            if initial_url:
                driver.get(initial_url)
                time.sleep(20)
                full_url = driver.current_url
                sheet.cell(row=row, column=new_idx2).value = full_url
            else:
                sheet.cell(row=row, column=new_idx2).value = ''
        except Exception as e:
            sheet.cell(row=row, column=new_idx2).value = f"Error: {str(e)}"

# Save the new columns in a new workbook
trivia_wb.save('data/cbus_trivia_list_updated.xlsx')