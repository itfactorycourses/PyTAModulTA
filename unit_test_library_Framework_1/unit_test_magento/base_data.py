import unittest

from selenium.webdriver.common.by import By
from seleniumbase import Driver

class Base_Data():

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.XPATH, '//input[@title="Password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="action login primary"]')
    UNEXISTING_CREDENTIALS_ERROR_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    INVALID_EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, 'div[for="email"]')
    SEARCH_INPUT_BOX = (By.CSS_SELECTOR, 'input#search')
    SEARCH_RESULTS_SORT_DROPDOWN = (By.XPATH,'//main[@id="maincontent"]//div[@class="search results"]//div[@class="toolbar toolbar-products"][1]//select[@id="sorter"]')
    PRODUCT_PRICE = (By.XPATH, '//span[@class="price"]')

    def setup_actions(self):
        self.driver = Driver()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window() # prin intermediul driverului instantiat din clasa Driver am apelat metoda maximize_window
                                # ea maximizeaza fereastra de web pentru a asigura vizibilitatea elementelor
        self.driver.implicitly_wait(10) # este un wait global care instruieste sistemul ca de fiecare data
                            #  cand vede ca un element nu este gasit, sa nu returneze eroare imediat
                            #  ci sa incerce sa mai caute elementul timp de x secunde (specificate intre paranteze inainte sa dea eroare)
                            #   Avantajul de a folosi un wait in loc de sleep este acela ca daca elementul a fost gasit, se trece instant mai departe
                             # la sleep se asteapta numarul specificat de secunde indiferent daca elementul a fost gasit sau nu
        return self.driver

    def insert_login_actions(self,username, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def evaluate_error_message(self, expected_message, selector):
        expected_error_message = expected_message
        actual_error_message = self.driver.find_element(*selector).text
        assert expected_error_message == actual_error_message, f"Error: expected message: {expected_error_message}, actual message: {actual_error_message}"
