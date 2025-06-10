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

driver.get("https://omayo.blogspot.com/")

# Waiting period 
driver.implicitly_wait(6)

enable_btn_loc = driver.find_element(By.ID,"but2")
if enable_btn_loc.is_enabled():
    assert "Button2" in enable_btn_loc.text
    print("Enabled")
else:
    print("Not enabled")
time.sleep(2)
enable_btn_loc.send_keys("haha")
time.sleep(3)
driver.close()