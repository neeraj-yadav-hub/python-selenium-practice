from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
radio = driver.find_element(By.XPATH, '//input[@value="radio1"]')
radio.click()
time.sleep(5)
driver.quit()