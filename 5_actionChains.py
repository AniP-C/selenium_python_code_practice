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

# Importing ActionChains to use actions like hover, right click, double left click
from selenium.webdriver.common.action_chains import ActionChains

# **********  Opening a browser with Selenium /**********
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Maximizing the window
driver.maximize_window()
# opening the below mentioned link
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

driver.implicitly_wait(6)


# Making object of Actions Chains to use it
actions = ActionChains(driver, duration=2000)
# Here we are giving driver address and duration in how much time the pointer point to the particular element


dropdown_loc = driver.find_element(By.ID,"headingOne")
dropdown_loc.click()
# time.sleep(3)
print("Clicked on dropdown button")



# clicking on button link inside the element tab
button_loc = driver.find_element(By.XPATH,"//li/a[@href = 'buttons.php']")
button_loc.click()
print("Button clicked")
time.sleep(3)

# hovering on the click me button
click_me_loc = driver.find_element(By.XPATH,"//div/button[text() = 'Click Me']")
actions.move_to_element(click_me_loc).click().perform()


# Perform is used to execute the commands
time.sleep(3)
print("sucessfully hovered and clicked")

time.sleep(3)
# Right clicking the button
right_click_btn = driver.find_element(By.XPATH,"//div/button[text() = 'Right Click Me']")
actions.context_click(right_click_btn).perform()

print("Right click successfully")

time.sleep(3)

# Double clicking the button
right_click_btn = driver.find_element(By.XPATH,"//div/button[text() = 'Double Click Me']")
actions.double_click(right_click_btn).perform()
# right_click_btn.click()
# right_click_btn.click()


print("Double click successfully")
time.sleep(5)



driver.close()