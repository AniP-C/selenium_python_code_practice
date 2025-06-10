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
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")

driver.implicitly_wait(6)


print(driver.window_handles)

time.sleep(2)
# clickign new tab
new_tab_loc = driver.find_element(By.XPATH,"//div/button[text() = 'New Tab']")
new_tab_loc.click()
time.sleep(2)
# switching to the new tab
driver.switch_to.window(driver.window_handles[1])

# operations in new tab
new_tab_text_loc = driver.find_element(By.XPATH,"//div/h1[text() = 'New Tab']")
print(new_tab_text_loc.text)

# switching to the original tab
driver.switch_to.window(driver.window_handles[0])

print(driver.window_handles)

time.sleep(2)

# clicking on the original page icon new window
new_window_loc = driver.find_element(By.XPATH,"//div/button[text() = 'New Window']")
new_window_loc.click()

# navigating to the newly opened window
driver.switch_to.window(driver.window_handles[2])

# extracting text from new window
new_win_text_loc = driver.find_element(By.XPATH,"//div/h1[text() = 'New Window']")
print(new_win_text_loc.text)


# coming back to the original window
driver.switch_to.window(driver.window_handles[0])







# # switching to the new window
# driver.switch_to.window(driver.window_handles[2])

print(driver.window_handles)




time.sleep(2)


















driver.quit()
driver.close()