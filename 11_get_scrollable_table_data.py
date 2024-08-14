from selenium import webdriver
from selenium.webdriver.common.by import By

table_element = '//div[@class="tableFixHead"]/table'
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#Get full table data
table = driver.find_element(By.XPATH, table_element)
print(table.text)

#check if Smith data is there or not
table_req_data_element = '//div[@class="tableFixHead"]/table/tbody/tr[9]/td[1]'
table_data = driver.find_element(By.XPATH, table_req_data_element)
assert table_data.text == "Smith"
print(table_data.text)
driver.quit()