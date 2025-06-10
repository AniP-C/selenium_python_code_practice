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

driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

# Waiting period 
driver.implicitly_wait(6)


alert_btn_loc = driver.find_element(By.XPATH,"//div/button[text()='Alert']")
alert_btn_loc.click()
pop_up = driver.switch_to.alert
print(pop_up.text)
time.sleep(3)
assert 'Hello world!' in pop_up.text
pop_up.accept()

time.sleep(2)

# validating ok text
both_btn_loc = driver.find_element(By.XPATH,"(//div/button[text()='Click Me'])[2]")
both_btn_loc.click()

time.sleep(2)
accept_btn_both = driver.switch_to.alert
time.sleep(3)
accept_btn_both.accept()
time.sleep(1)

finding_validing_text_loc = driver.find_element(By.ID,"desk")
assert "You pressed OK!" in finding_validing_text_loc.text

time.sleep(3)

driver.switch_to.default_content
# validating dismissing text
both_btn_loc = driver.find_element(By.XPATH,"(//div/button[text()='Click Me'])[2]")
both_btn_loc.click()
time.sleep(2)
accept_btn_both = driver.switch_to.alert
time.sleep(3)
accept_btn_both.dismiss()
time.sleep(1)

finding_validing_text_loc = driver.find_element(By.ID,"desk")
assert "You pressed Cancel!" in finding_validing_text_loc.text
time.sleep(2)



# # text option alert
# text_insert_alert_loc = driver.find_element(By.XPATH,"(//div/button[text()='Click Me'])[3]")
# text_insert_alert_loc.click()

# prompt_alert = driver.switch_to.alert
# time.sleep(2)
# prompt_alert.send_keys("hi")
# time.sleep(3)
# text_1 = prompt_alert.text
# assert "hi" in text_1
# prompt_alert.accept()
# time.sleep(3)
# text option alert
text_insert_alert_loc = driver.find_element(By.XPATH,"(//div/button[text()='Click Me'])[3]")
text_insert_alert_loc.click()

# Wait for alert and interact
WebDriverWait(driver, 10).until(EC.alert_is_present())
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("hi")
prompt_alert.accept()

# Wait and verify the result message on the page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "desk")))
result_text = driver.find_element(By.ID, "desk").text
assert "hi" in result_text  # Confirm the input was submitted and shown
print("Prompt input reflected correctly on the page:", result_text)

driver.close()

