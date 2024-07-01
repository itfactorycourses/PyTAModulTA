import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

comanda_palasata = False

driver = Driver()
driver.get("https://magento.softwaretestingboard.com/")
input_box = driver.find_element(By.CSS_SELECTOR,'input#search')
input_box.send_keys('capri')
input_box.send_keys(Keys.ENTER)
product_element = driver.find_element(By.CLASS_NAME,"product-item-info")
hover = ActionChains(driver).move_to_element(product_element)
hover.perform()
time.sleep(2)
driver.find_element(By.XPATH,'//button[@title="Add to Cart"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//div[@id="option-label-color-93-item-50"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@option-label="28"]').click()
time.sleep(2)
purchase1 = driver.find_element(By.XPATH,'//*[@type="submit" and @title="Add to Cart"]')
apasa_buton = ActionChains(driver).move_to_element(purchase1)
apasa_buton.click().perform()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@type="submit" and @title="Add to Cart"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@class="action showcart"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="top-cart-btn-checkout"]').click()
time.sleep(3)
email_adress = driver.find_element(By.XPATH,'//div[@class="control _with-tooltip"]//input[@type="email"]')
email_adress.send_keys('testareautomata1@mailinator.com')
first_name = driver.find_element(By.XPATH,'//*[@name="firstname"]')
first_name.send_keys('Andrei-Daniel')
last_name = driver.find_element(By.XPATH,'//*[@name="lastname"]')
last_name.send_keys('Pop')
company = driver.find_element(By.XPATH,'//*[@name="company"]')
company.send_keys('IT Factory')
street_address = driver.find_element(By.XPATH,'//*[@name="street[0]"]')
street_address.send_keys('Strada Fericirii nr.7, ap 33')
city = driver.find_element(By.XPATH,'//*[@name="city"]')
city.send_keys('Cluj-Napoca')
meniu_dropdown = driver.find_element(By.CSS_SELECTOR,'select[name="region_id"]')
drp_apasat = Select(meniu_dropdown)
drp_apasat.select_by_visible_text('Alabama')
time.sleep(3)
zip_code = driver.find_element(By.XPATH,'//*[@name="postcode"]')
zip_code.send_keys('12345')
phone_number = driver.find_element(By.XPATH,'//*[@name="telephone"]')
phone_number.send_keys('0746594230')
shipping_method = driver.find_element(By.XPATH,'//*[@class="table-checkout-shipping-method"]')
select_shipping = ActionChains(driver).move_to_element(shipping_method)
select_shipping.perform()
time.sleep(5)
radio = driver.find_element(By.XPATH,'//*[@name="ko_unique_5"]')
radio.click()
driver.find_element(By.XPATH,'//*[@data-role="opc-continue"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//button[@title="Place Order"]').click()
comanda_palasata = True

assert comanda_palasata == True

time.sleep(5)
driver.quit()