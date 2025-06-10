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
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")


# Getting Main text of the page
top_text = driver.find_element(By.XPATH,"//div/h1")
print(top_text.text)


# Getting text just above the form starts
form_text = driver.find_element(By.CLASS_NAME,"fw-normal")
print(form_text.text)


# ********** Sending the name in the name input place *******************
send_name = driver.find_element(By.XPATH,"//div/input[@id='name']")

# used to get the value of the placeholder attribute
print(send_name.get_attribute("placeholder"))

# .send_keys sends keys/strokes in the text field
send_name.send_keys("Aniruddh Parashar")

time.sleep(3)
# .clear is use to clear the name
send_name.clear()
send_name.send_keys("Niki Mehra")



# ************ Sending the email in the input place *********************
send_email = driver.find_element(By.XPATH,"//div/input[@id='email']")
send_email.send_keys("nikihahahah@gmail.com")

time.sleep(3)

# clicking on female radion button
click_female = driver.find_element(By.XPATH,"//label[text()='Female']/preceding-sibling::input[@type='radio']")
click_female.click()
time.sleep(2)
# Clicking on radio buttons, we will use find_elements which saves all the elements found in list
# clicking_radio_array = driver.find_elements(By.XPATH,"//div/input[@type='radio']")

# lenn = len(clicking_radio_array)

# for clicking_btn in clicking_radio_array:

#     if clicking_radio_array.index(clicking_btn) + 1 != 2:
#         clicking_btn.click()
    

# Entering the mobile nnumber
mob_locator = driver.find_element(By.ID, "mobile")
mob_locator.send_keys("9999999")
time.sleep(2)


# entering dob in calender
# Way 1 
dob_locator = driver.find_element(By.ID,"dob")
dob_locator.send_keys("1509")

dob_locator.send_keys("2000")
time.sleep(3)
dob_locator.clear()
dob_locator.send_keys("07062001")


# ** Entering the subjects ******
subject_locator = driver.find_element(By.ID,"subjects")
subject_locator.send_keys("Hindi, English, Phy, Chem")
subject_locator.send_keys(", biology")


# clicking on multiple checkboxes

checkboxes_loc = driver.find_elements(By.XPATH,"(//div/input[@type='checkbox'])[position() < 3]")
for checkbox in checkboxes_loc:
    checkbox.click()







# uploading the file
upload_loc = driver.find_element(By.XPATH,"//input[@id ='picture']")
upload_loc.send_keys("C:\\Users\\Aniruddh Parashar\\Desktop\\PESA\\padhai\\Python Selenium\\cow.png")

time.sleep(2)
# Entering the address
address_loc = driver.find_element(By.XPATH,"//textarea[@id='picture']")
address_loc.send_keys("Aligarh Delhi Mathura Haridwar Rishikesh")

# C:\Users\Aniruddh Parashar\Desktop\PESA\padhai\Python Selenium\cow.png
time.sleep(2)
# selecting state from dropdown
dropdown_loc = driver.find_element(By.ID,"state")

select_state = Select(dropdown_loc)
select_state.select_by_index(2)
time.sleep(2)
select_state.select_by_visible_text("NCR")
time.sleep(2)
select_state.select_by_value("Rajasthan")

time.sleep(3)
# selecting the city
select_loc = driver.find_element(By.ID,"city")

select_city = Select(select_loc)
select_city.select_by_index(2)



time.sleep(2)
# clickign on the login button
login_loc = driver.find_element(By.XPATH,"//div/input[@type='submit']")
login_loc.click()

# closing the browser
time.sleep(3)
driver.close()

driver.quit()
