from selenium import webdriver
from selenium.webdriver.common.by import By
import time


suggestion_box_element = '//input[@type="text" and @placeholder="Type to Select Countries"]'
suggestion_word = 'ind'
required_suggestion = '//ul[@id="ui-id-1"]/li[2]/div'
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
suggestion_box = driver.find_element(By.XPATH, suggestion_box_element)
suggestion_box.send_keys(suggestion_word)
time.sleep(2)
select_suggestion = driver.find_element(By.XPATH, required_suggestion)
select_suggestion.click()
time.sleep(2)
driver.quit()


