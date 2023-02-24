import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd
import numpy as np
from selenium import webdriver
import gspread
from google.oauth2 import service_account
import json
import google.auth
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
from oauth2client.service_account import ServiceAccountCredentials

## Siamchart Historical
# Run Selenium
driver2 = webdriver.Chrome(r'/Users/jarkrunglerdkriangkrai/Github/setscraping/chromedriver')
driver2.get('http://siamchart.com/stock-financial/')
data2 = driver2.page_source

# Read Data
df2 = pd.read_html(data2)[0].drop('No.', axis=1)

# Loop to clean
for col in df2.columns:
    # replace values in column if it's a string type
    if df2[col].dtype == 'O':
        df2[col] = df2[col].str.replace(r'\s*\([^\)]*\)\s*', '', regex=True)

# Connect to Google Sheets
gc2 = gspread.service_account(filename='/Users/jarkrunglerdkriangkrai/Github/setscraping/service_account.json')
sh2 = gc2.open('set scraping')
ws2 = sh2.worksheet("Sheet2")

# Clear the existing contents of the worksheet
ws2.clear()

# Write the dataframe to the worksheet
set_with_dataframe(ws2,df2)

# Close Selenium
driver2.quit()