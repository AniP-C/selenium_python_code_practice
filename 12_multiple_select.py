from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options # to stop closing of the browser


options = Options() #making object for the class we imported => Options
# **********  Opening a browser with Selenium /**********
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# Maximizing the window
driver.maximize_window()
# opening the below mentioned link

driver.get("https://www.tutorialspoint.com/selenium/practice/select-menu.php")

 
# Using select for multiple dropdowns
# select_multiple_dwn_loc = driver.find_element(By.ID,"demo-multiple-select-input")
# select_multiple_state = Select(select_multiple_dwn_loc)
# time.sleep(3)
# select_multiple_state.select_by_index(1)
# time.sleep(4)

store_elements = []
select_multiple_dwn_loc = driver.find_element(By.XPATH,"//*[@id='mbsc-control-0']/div/label/span[2]/span[1]")
time.sleep(2)
select_multiple_dwn_loc.click()
time.sleep(3)
print('loc found')

# select_first_ele_loc = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[41]")
# select_first_ele_loc.click()
# time.sleep(4)
list_store = driver.find_elements(By.XPATH,"//div[contains(@class, 'mbsc-wheel-item-multi') and normalize-space(text()) != '']")
print("list store found")
for items in list_store:
    print("came inside the list")
    if items.is_displayed():
        print('came inside if')
        items.click()
        time.sleep(3)
time.sleep(3)
driver.quit()