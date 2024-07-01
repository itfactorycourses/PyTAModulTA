import time

from seleniumbase import Driver
from selenium.webdriver.common.by import By

driver = Driver()


driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.CSS_SELECTOR, 'header[class="page-header"] li[class="authorization-link"] > a').click()
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("test@gmail.com")
driver.find_element(By.CSS_SELECTOR, 'input[title="Password"]').send_keys("asdasdsad")
driver.find_element(By.CSS_SELECTOR,'button[class="action login primary"]').click()
# driver.find_element(By.CSS_SELECTOR,"button.login").click()
expected_error = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
actual_error = driver.find_element(By.XPATH,'//div[@data-ui-id="message-error"]//div').text
assert expected_error == actual_error, f'error : expected message : {expected_error}, actual error {actual_error}'
driver.quit()


"""
body > div.cc-window.cc-banner.cc-type-opt-in.cc-theme-block.cc-bottom.cc-color-override-688238583 > div > a.cc-btn.cc-allow

"""