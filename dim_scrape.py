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

#Run Selenium
driver = webdriver.Chrome(r"/Users/jarkrunglerdkriangkrai/Github/setscraping/chromedriver")
driver.get('import gspread')
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

#Run Selenium
driver = webdriver.Chrome(r"/Users/jarkrunglerdkriangkrai/Github/setscraping/chromedriver")
driver.get('https://www.set.or.th/th/market/get-quote/stock/')
data = driver.page_source

#Read Data
df = pd.read_html(data)[2].drop(['No.','Links','CG','Sign','MG%'],axis=1).tail(-1)

#Update to Google Sheets
gc = gspread.service_account(filename='/Users/jarkrunglerdkriangkrai/Github/setscraping/service_account.json')
sh = gc.open("set scraping")
ws = sh.worksheet("Sheet1")

#Clear the existing contents of the worksheet
ws.clear()

#Write the dataframe to the worksheet
set_with_dataframe(ws, df)
data = driver.page_source

#Read Data
df = pd.read_html(data)[2].drop(['No.','Links','CG','Sign','MG%'],axis=1).tail(-1)

#Update to Google Sheets
gc = gspread.service_account(filename='/Users/jarkrunglerdkriangkrai/Github/setscraping/service_account.json')
sh = gc.open("set scraping")
ws = sh.worksheet("Sheet1")

#Clear the existing contents of the worksheet
ws.clear()

#Write the dataframe to the worksheet
set_with_dataframe(ws, df)