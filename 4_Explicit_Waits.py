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

# Importing ActionChains to use actions like hover, right click, double left click
from selenium.webdriver.common.action_chains import ActionChains

# **********  Opening a browser with Selenium /**********
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Maximizing the window
driver.maximize_window()
# opening the below mentioned link
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

# Making object for the webdriver wait
wait = WebDriverWait(driver,6,0.2)
"""
Here we made the object for the class WebDriverWait and inside it is the driver address
maximum time it needs to wait ( secs ) and it'll retry after every 0.2 seconds to look for the element
"""


# Making object of Actions Chains to use it
actions = ActionChains(driver, duration=2000)
# Here we are giving driver address and duration in how much time the pointer point to the particular element






#  --------------------------------------------------------------------------------------------

"""
This script wont work if time.sleep ain't there, so to avoid writing time.sleep() multiple time
we'll use Implicit Waits

Here Implicit Waits works but there are places where Implicit Waits wont work, only Explicit Wait Works
So using Explicit Wait
"""
# driver.implicitly_wait(7)
# time.sleep(3)
# clicking on element dropdown button
dropdown_loc = driver.find_element(By.ID,"headingOne")
dropdown_loc.click()
# time.sleep(3)
print("Clicked on dropdown button")


wait.until(EC.visibility_of_all_elements_located(By.XPATH,"//li/a[@href='dynamic-prop.php']"))

# clicking the dynamic properties button inside the elements

dynamic_prop = driver.find_element(By.XPATH,"//li/a[@href='dynamic-prop.php']")
dynamic_prop.click()
print("Clicked on dynamic properties button")


# time.sleep(3)


# colorChange
# clicking on color chainging button
color_change_loc = driver.find_element(By.ID,"colorChange")
print("located")
color_change_loc.click()
print("Clicked on color change button")


# time.sleep(6)
wait.until(EC.visibility_of_all_elements_located(By.ID,"visibleAfter"))

# button visible after 5 secs after clicking colorChange button
after_visible = driver.find_element(By.ID,"visibleAfter")
after_visible.click()
print("Clicked on after visible")


# print(after_visible.get_attribute)
print(after_visible.text)
# time.sleep(3)
print("done yeah")

driver.close()