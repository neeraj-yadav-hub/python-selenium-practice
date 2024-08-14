from selenium import webdriver
from selenium.webdriver.common.by import By
import time


alert_box_element = '//input[@id="name"]'
alert_button_element = '//input[@id="alertbtn"]'
alert_confirm_element = '//input[@id="confirmbtn"]'

def alert_field(value:str):
    # function to go to webelemnt of the alert box and provide value in that box
    alert_box = driver.find_element(By.XPATH, alert_box_element)
    alert_box.send_keys(value)


def alert_button(button_element):
    #function to go to webelement of different alert button
    button = driver.find_element(By.XPATH, button_element)
    button.click()
    alert_object = driver.switch_to.alert
    print(alert_object.text)
    time.sleep(2)
    return alert_object

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
alert_field('Tester')
alert_button(alert_button_element).accept()

driver.switch_to.default_content()

print('-'*40)
alert_field('Developer')
alert_button(alert_confirm_element).dismiss()
driver.quit()