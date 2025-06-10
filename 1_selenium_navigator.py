from selenium import webdriver
import time
from selenium.webdriver.common.by import By # By is a class which has all the locators
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import *  # If you really want everything from `ui`

import pytest

from selenium.webdriver.chrome.options import Options # to stop closing of the browser
options = Options() #making object for the class we imported => Options
options.add_experimental_option("detach", True)


# Navigating to the element in the webpage
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# locating the element
driver.find_element(By.CSS_SELECTOR,"[value='radio2']").click()
driver.find_element(By.XPATH,"//input[@id = 'name']").send_keys("Aniruddh")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id = 'name']").clear()

driver.find_element(By.XPATH,"//input[@id = 'name']").send_keys("Niki")
# //div[@class='block large-row-spacer']//fieldset[@class='pull-right']/legend

alert_ex_text = driver.find_element(By.XPATH,"//div[@class='block large-row-spacer']//fieldset[@class='pull-right']/legend").text
print(alert_ex_text)


# check_boxes = driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
# print(check_boxes, len(check_boxes))

# for check_box in check_boxes:
#     if check_boxes.index(check_box) + 1 != 2:
#         check_box.click()


# dropdowns
# static_dropdown = driver.find_element(By.ID, "dropdown-class-example")

# select = Select(static_dropdown)
# select.select_by_index(2)
# time.sleep(3)
# select.select_by_visible_text("Option1")
# time.sleep(3)

# select.select_by_value("option3")
# time.sleep(3)
# driver.close()



# Blinking text attribute value
# blinking_text = driver.find_element(By.XPATH, "//header/a[@class = 'blinkingText']")
# print(blinking_text.get_attribute("href"))




# ******************  Opening a new window  *******************
new_window = driver.find_element(By.XPATH,"//button[@id='openwindow']")
new_window.click()

new_tab = driver.find_element(By.XPATH,"//a[@id='opentab']")
new_tab.click()
driver.get_t