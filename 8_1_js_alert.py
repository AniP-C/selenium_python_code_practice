# Handling JS Alerts in the browser

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

# Waiting period 
driver.implicitly_wait(6)

# sending keys 
enter_text_loc = driver.find_element(By.ID,"name")
enter_text_loc.send_keys("Aniruddh")


# clicking on alert
click_alert_btn = driver.find_element(By.ID,"alertbtn")
click_alert_btn.click()

switch_to_alert = driver.switch_to.alert
print(switch_to_alert.text)

switch_to_alert_text = switch_to_alert.text
assert "Hello Aniruddh, share this practice page and share your knowledge" in switch_to_alert_text


switch_to_alert.accept()




driver.close()

