# sortare dupa pret ascending
import time

from selenium.webdriver import ActionChains
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = Driver()
driver.get("https://magento.softwaretestingboard.com/")
input_box = driver.find_element(By.CSS_SELECTOR,'input#search')
input_box.send_keys('capri')
input_box.send_keys(Keys.ENTER)
product_element = driver.find_element(By.CLASS_NAME,"product-item-info")
hover = ActionChains(driver).move_to_element(product_element)
hover.perform()
driver.find_element(By.XPATH,'//button[@title="Add to Cart"]').click()
time.sleep(5)
driver.quit()
