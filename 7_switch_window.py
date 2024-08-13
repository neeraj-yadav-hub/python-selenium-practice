from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.switch_to import SwitchTo
import time

switch_window_button = '//button[@id="openwindow"]'
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
current_window = driver.current_window_handle
window = driver.find_element(By.XPATH,switch_window_button)
window.click()
time.sleep(2)
list_of_windows_open = driver.window_handles
driver.switch_to.window(list_of_windows_open[1])
print(driver.title)
driver.quit()