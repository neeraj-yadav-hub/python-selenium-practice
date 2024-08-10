from selenium import webdriver
from selenium.webdriver.common.by import By
import time

search_box_element = '//textarea[@id="APjFqb"]'
search_text_element = '//span[contains(text(),"selenium")]'
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
search_box = driver.find_element(By.XPATH, search_box_element)
search_box.send_keys("selenium")
time.sleep(2)
search_elements = driver.find_elements(By.XPATH, search_text_element)
print(len(search_elements))
for i in search_elements:
    print(i.text) 
    if i.text == "selenium webdriver":
        i.click()
        time.sleep(5)
        break