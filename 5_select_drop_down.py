from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

drop_down_box_element = '//select[@id="dropdown-class-example"]'

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
drop_down = Select(driver.find_element(By.XPATH, drop_down_box_element))
drop_down.select_by_visible_text('Option2')
time.sleep(2)
driver.quit()
