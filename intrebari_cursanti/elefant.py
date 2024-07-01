from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumbase import Driver


driver = Driver()
driver.get('https://www.elefant.ro/')
input_search_box = driver.find_element(By.XPATH,'//input[@type="text"]')
input_search_box.send_keys("iphone")
input_search_box.send_keys(Keys.ENTER)
product_list = driver.find_elements(By.CLASS_NAME,'product-image-container')