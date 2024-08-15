from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

hover_element = '//button[@id="mousehover"]'
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
hover = driver.find_element(By.XPATH, hover_element)
action = ActionChains(driver)
top_element = action.move_to_element(hover)
time.sleep(5)
top = driver.find_element(By.XPATH, '//a[@href="#top"]')
time.sleep(5)
top_element.move_to_element(top).click().perform()
time.sleep(2)
driver.quit()
