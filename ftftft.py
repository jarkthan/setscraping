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


#Update to Google Sheets
gc = gspread.service_account(filename='/Users/jarkrunglerdkriangkrai/Github/setscraping/service_account.json')
sh = gc.open("set scraping")
ws = sh.worksheet("Sheet2")

#Clear the existing contents of the worksheet
ws.clear()

#Write the dataframe to the worksheet
ws.update('A1',"Jark")