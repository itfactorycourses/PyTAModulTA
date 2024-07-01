import time

from selenium.webdriver.common.by import By

from browser import Browser


class Login_Page(Browser):

    USERNAME = (By.ID,'email')
    PASSWORD = (By.XPATH,'//*[@name="login[password]"]')
    LOGIN_BUTTON = (By.XPATH,'//button[@class="action login primary"]')
    LOGIN_ERROR_MESSAGE = (By.XPATH,'//div[@class="message-error error message"]//div')

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


    def check_error_message(self,expected_error_message):
         actual_error_message = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE).text
         assert expected_error_message == actual_error_message, f"Error: expected message: {expected_error_message}, actual message: {actual_error_message}"

