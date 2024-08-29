#To find the images in a page that are broken or in simple ways images 
# are not loaded properly.

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
images_elements = driver.find_elements(By.TAG_NAME, 'img')

for i in range(0,len(images_elements)):
    image_link = images_elements[i].get_attribute('src')
    if image_link:
        #provide the value of src attribute if present otherwise will return None
        connect = requests.get(image_link)
        if connect.status_code!=200:
            print(image_link+">>>"+connect.reason+"->"
                  +str(connect.status_code))

driver.quit()