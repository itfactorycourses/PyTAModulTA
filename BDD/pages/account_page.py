from selenium.webdriver.common.by import By
from base_page import Base_Page

class Account_Page(Base_Page):

    MY_ACCOUNT_ARROW = (By.XPATH,'//header[@class="page-header"]//button[@class="action switch"]')
    MY_ACCOUNT_LINK = (By.LINK_TEXT,'My Account')
    SIGN_OUT_LINK = (By.LINK_TEXT,'Sign Out')

    def check_if_logged_in(self):
        self.driver.find_element(*self.MY_ACCOUNT_ARROW).click()
        self.driver.find_element(*self.MY_ACCOUNT_LINK).click()
        expected_url = "https://magento.softwaretestingboard.com/customer/account/"
        actual_url = self.driver.current_url
        assert expected_url == actual_url,f"Error: expected url: {expected_url}, actual url: {actual_url}"

    def logout(self):
        self.driver.find_element(*self.MY_ACCOUNT_ARROW).click()
        self.driver.find_element(*self.SIGN_OUT_LINK).click()