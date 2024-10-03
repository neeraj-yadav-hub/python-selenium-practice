from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

#Web elements list
website = 'https://student.nielit.gov.in/'
home_declaration = '//img[@alt="close"]'
iframe_home_element = '//iframe[@name="ifHome" and @src="Home.aspx"]'
apply_online_element = '//*[@id="cthRightPannel_Sidelink_divLinks"]/table/tbody/tr[6]/td/input'
ccc_plus_element = '//a[text()="CCC Plus (CCCP)"]'
open_form_checkbox = '//input[@id="chk1"]'
agree_proceed_btn = '//input[@value="I Agree & Proceed"]'
#driver initialise
driver =  webdriver.Chrome()
driver.maximize_window()
driver.get(website)
wait = WebDriverWait(driver, 10)

#close home page declartion
close_pop = wait.until(EC.presence_of_element_located((By.XPATH,home_declaration)))
close_pop.click()
time.sleep(2)

#click on "Apply Online" by entering iframe
iframe_home = driver.find_element(By.XPATH, iframe_home_element)
driver.switch_to.frame(iframe_home)
apply_online = driver.find_element(By.XPATH, apply_online_element)
apply_online.click()
time.sleep(2)

#click on "CCC Plus (CCCP)" in IT literacy program
ccc_plus = driver.find_element(By.XPATH, ccc_plus_element)
ccc_plus.click()
time.sleep(2)

#click declaration and click 'I Agree and Proceed' button to open form
form_checkbox = driver.find_element(By.XPATH, open_form_checkbox)
form_checkbox.click()
agree_and_proceed = driver.find_element(By.XPATH, agree_proceed_btn)
agree_and_proceed.click()
time.sleep(2)

#Quit driver instance
driver.quit()