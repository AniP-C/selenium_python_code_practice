# Window tabs changes here

# hover - Right click - double click
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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(6)
time.sleep(3)
# Clicking on the embedded frame
frame_1_loc = driver.find_element(By.ID,"courses-iframe")
driver.switch_to.frame(frame_1_loc) #This is used to switch our script inside the frame
time.sleep(3)

# Clicking on somethign inside the fram.
# frame_ins_loc = driver.find_element(By.XPATH,"//li[@class='current']//a[@href = 'learning-path']")
frame_ins_loc = driver.find_element(By.XPATH,"//a[@href = 'learning-path']")

# frame_ins_loc = driver.find_element(By.XPATH,"//a[@href='consulting']")

frame_ins_loc.click()




# driver.quit()
# driver.close()