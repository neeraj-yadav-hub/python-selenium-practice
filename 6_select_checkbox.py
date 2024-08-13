from selenium import webdriver
from selenium.webdriver.common.by import By
import time


check_box_element = '//input[@id="checkBoxOption2"]'
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check_box = driver.find_element(By.XPATH, check_box_element)
check_box.click()
time.sleep(2)
driver.quit()