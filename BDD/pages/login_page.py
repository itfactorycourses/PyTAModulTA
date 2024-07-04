import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import Base_Page


class Login_Page(Base_Page):

    USERNAME = (By.ID,'email')
    PASSWORD = (By.XPATH,'//*[@name="login[password]"]')
    LOGIN_BUTTON = (By.XPATH,'//button[@class="action login primary"]')
    LOGIN_ERROR_MESSAGE_INCORRECT_CREDENTIALS = (By.XPATH, '//div[@class="message-error error message"]//div')
    INVALID_EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR,'div[for="email"]')
    REQUIRED_DATA_ERROR_MESSAGE = (By.XPATH,'//div[@class="mage-error"]')

    def insert_username(self,username):
        if username == "N/A":
            pass
        else:
            self.driver.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self,password):
        if password == "N/A":
            pass
        else:
            self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def check_login_error_message(self, error_message):
        is_error_message_correct = True
        actual_text = ""
        if "required" in error_message:
            # mai jos am aplicat explicit wait
            # visibility_of_element_located primeste drept argument un tuplu, deci nu mai punem * in fata elementului
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.REQUIRED_DATA_ERROR_MESSAGE))
            # time.sleep(10)
            error_message_list = self.driver.find_elements(*self.REQUIRED_DATA_ERROR_MESSAGE)
            for i in range(len(error_message_list)):
                actual_text = error_message_list[i].text
                if not self.check_error_message(error_message, actual_text):
                    is_error_message_correct = False
                    break
        elif "valid email" in error_message:
            if not self.check_error_message(error_message, selector = self.INVALID_EMAIL_ERROR_MESSAGE):
                actual_text = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE_INCORRECT_CREDENTIALS).text
                is_error_message_correct = False
        else:
            if not self.check_error_message(error_message, selector = self.LOGIN_ERROR_MESSAGE_INCORRECT_CREDENTIALS):
                actual_text = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE_INCORRECT_CREDENTIALS).text
                is_error_message_correct = False
        assert is_error_message_correct == True, (f"Error: expected message: {error_message}, "
                                                  f"actual message: {actual_text}")



