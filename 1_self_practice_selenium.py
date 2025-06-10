from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options # to stop closing of the browser
options = Options() #making object for the class we imported => Options

# **********  Opening a browser with Selenium /**********
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://direct.asda.com/george/clothing/10,default,sc.html")

time.sleep(3)
# Searched for condion accept button and clicks it
try:
    driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
except:
    print("element not found ID")

time.sleep(3)
# searched_for flipkart suggestion button and crosses it
try:

    driver.find_element(By.XPATH,"//button[@class='close']").click()
except:
    print("element not found xpath")

# below line find title of the page
title = driver.title

# below line finds current link of the page
current_url = driver.current_url

# below line checks whether the title of the page is exactly mentioned below or not, if it is not then it raises an assertion error
assert title != "Clothing, Toys & Baby Products | George at ASDA " 
# Clothing, Toys & Baby Products | George at ASDA


print(title, "\n", current_url)

driver.close()