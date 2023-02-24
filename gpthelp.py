from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# set up driver and go to website
driver = webdriver.Chrome()
driver.get("https://www.set.or.th/th/market/get-quote/stock/")

# wait for the table to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-info")))

# scrape data from the first page
table = driver.find_element_by_class_name("table-info")
data = []
for row in table.find_elements_by_tag_name("tr"):
    cols = row.find_elements_by_tag_name("td")
    cols = [col.text for col in cols]
    if cols:
        data.append(cols)
df = pd.DataFrame(data[1:], columns=data[0])

# loop through all pages and append data to dataframe
while True:
    try:
        next_button = driver.find_element_by_xpath("//a[@class='fa fa-angle-right']")
        next_button.click()
        wait.until(EC.staleness_of(table))
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-info")))
        table = driver.find_element_by_class_name("table-info")
        for row in table.find_elements_by_tag_name("tr"):
            cols = row.find_elements_by_tag_name("td")
            cols = [col.text for col in cols]
            if cols:
                data.append(cols)
    except:
        break

# create dataframe and print results
df = pd.DataFrame(data[1:], columns=data[0])
print(df)
