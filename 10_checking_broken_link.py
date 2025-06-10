# Checking broken links in the website
# Handling JS Alerts in the browser
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options # to stop closing of the browser
# Importing Explicit Wait
from selenium.webdriver.support.wait import WebDriverWait
# Importing expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
options = Options() #making object for the class we imported => Options
# **********  Opening a browser with Selenium /**********
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# Maximizing the window
driver.maximize_window()
# opening the below mentioned link

# driver.get("https://jquery.com/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.get("www.rahulshettyacademy.com")

# Waiting period 
driver.implicitly_wait(6)

all_links = driver.find_elements(By.TAG_NAME,value='a')
print(f"Total no. of links in the website are: {len(all_links)}")

dikt = {}

for link in all_links:
    hrefs = link.get_attribute('href')
    response = requests.get(hrefs)
    response_codes = response.status_code
    dikt = {hrefs,response}
    print(hrefs," : ", response_codes)
    

driver.close()