# Drag n Drop

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
from selenium.webdriver.common.action_chains import ActionChains

options = Options() #making object for the class we imported => Options
# **********  Opening a browser with Selenium /**********
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# Maximizing the window
driver.maximize_window()
# opening the below mentioned link

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

box_1_loc = driver.find_element(By.ID,"column-a")
box_2_loc = driver.find_element(By.ID,"column-b")
actions = ActionChains(driver)
time.sleep(3)
actions.drag_and_drop(box_1_loc,box_2_loc).perform()
time.sleep(3)


driver.close()

