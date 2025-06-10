import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(6)

all_links = driver.find_elements(By.TAG_NAME, value='a')
print(f"Total number of links on the website: {len(all_links)}")

valid_links = {}

for link in all_links:
    href = link.get_attribute('href')
    if href is None or "javascript" in href.lower():
        continue  # skip empty or JS links

    try:
        response = requests.head(href, allow_redirects=True, timeout=5)
        code = response.status_code
        valid_links[href] = code
        if code >= 400:
            print(f"[BROKEN] {href} : {code}")
        else:
            print(f"[OK]     {href} : {code}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR]  {href} : {e}")

driver.quit()
