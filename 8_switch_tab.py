from selenium import webdriver
from selenium.webdriver.common.by import By
import time

switch_tab_button = '//a[@id="opentab"]'
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
current_window = driver.current_window_handle
tab = driver.find_element(By.XPATH,switch_tab_button)
tab.click()
time.sleep(2)
list_of_tab_open = driver.window_handles
print(list_of_tab_open)
driver.switch_to.window(list_of_tab_open[1])
print(driver.title)
driver.quit()
