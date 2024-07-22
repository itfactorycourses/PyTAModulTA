from selenium.webdriver.common.by import By

from base_page import Base_Page
from browser import Browser

class Home_Page(Base_Page):

    SIGN_IN_LINK = (By.LINK_TEXT,'Sign In')

    def navigate_to_homepage(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

    def click_sign_in_link(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()

