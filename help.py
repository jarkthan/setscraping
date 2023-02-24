from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# create a webdriver instance
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.set.or.th/th/market/get-quote/stock/')

# wait for the table to load
#wait = WebDriverWait(driver, 10)
#table = wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-info"]')))

# create an empty list to store the data

data = driver.page_source

df = pd.read_html(data)

#dff = []
#df.append(dff)
# loop through the pages
#while True:
    # wait for the table to load
    #wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-info"]')))
    
    # scrape the data from the table
    #table = driver.find_element(By.XPATH, '//table[@class="table table-info"]')
    #rows = table.find_elements(By.TAG_NAME, "tr")
    
        
        # append the data to the list
    
    # check if there is a next page button
#    next_page_button = driver.find_element(By.XPATH, '//button[@aria-label="Go to next page"]')
#    if 'disabled' in next_page_button.get_attribute('class'):
#        break
        
    # click the next page button
#    driver.execute_script("arguments[0].click();", next_page_button)
    
# create a dataframe from the data
#df = pd.DataFrame(data, columns=['ชื่อย่อหลักทรัพย์', 'ชื่อเต็มหลักทรัพย์จดทะเบียน', 'ตลาด', 'กลุ่มอุตสาหกรรม', 'หมวดธุรกิจ', 'Factsheet'])
print(df)
# close the webdriver instance
driver.quit()
