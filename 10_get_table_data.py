from selenium import webdriver
from selenium.webdriver.common.by import By
import time


table_element = '//table[@id="product" and @name="courses"]'
table_req_data_element = '//table[@id="product" and @name="courses"]//tr[7]/td[3]'
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#to get full table data
table = driver.find_element(By.XPATH, table_element)
print(table.text)

#to get price from the table where course name is 
#"WebServices / REST API Testing with SoapUI"
table_rows = driver.find_element(By.XPATH,table_req_data_element)
assert table_rows.text == "35"
print(table_rows.text)

driver.quit()
