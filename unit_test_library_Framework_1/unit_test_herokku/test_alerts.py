import unittest

from selenium.webdriver.common.by import By
from seleniumbase import Driver


class Test_Alerts(unittest.TestCase):

    JS_ALERT_BUTTON = (By.XPATH,'//button[contains(text(),"Click for JS Alert")]')
    JS_ALERT_CONFIRM_MESSAGE = (By.ID, "result")
    JS_CONFIRM_BUTTON = (By.XPATH,'//button[contains(text(),"Click for JS Confirm")]')
    JS_PROMPT_BUTTON = (By.XPATH,'//button[contains(text(),"Click for JS Prompt")]')


    def setUp(self):
        self.driver = Driver()
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()


    def test_js_alert(self):
        self.driver.find_element(*self.JS_ALERT_BUTTON).click()
        js_alert = self.driver.switch_to.alert
        js_alert.accept()
        expected_result = "You successfully clicked an alert"
        actual_result = self.driver.find_element(*self.JS_ALERT_CONFIRM_MESSAGE).text
        self.assertEqual(expected_result,actual_result,f"Error: Expected message: {expected_result}, actual message: {actual_result}")

    def test_js_confirm_accept(self):
        self.driver.find_element(*self.JS_CONFIRM_BUTTON).click()
        js_confirm_alert = self.driver.switch_to.alert
        js_confirm_alert.accept()
        expected_result = "You clicked: Ok"
        actual_result = self.driver.find_element(*self.JS_ALERT_CONFIRM_MESSAGE).text
        self.assertEqual(expected_result, actual_result,f"Error: Expected message: {expected_result}, actual message: {actual_result}")


    def test_js_confirm_cancel(self):
        self.driver.find_element(*self.JS_CONFIRM_BUTTON).click()
        js_confirm_alert = self.driver.switch_to.alert
        js_confirm_alert.dismiss()
        expected_result = "You clicked: Cancel"
        actual_result = self.driver.find_element(*self.JS_ALERT_CONFIRM_MESSAGE).text
        self.assertEqual(expected_result, actual_result,
                         f"Error: Expected message: {expected_result}, actual message: {actual_result}")


    def test_js_prompt_insert_text_accept(self):
        self.driver.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt_alert = self.driver.switch_to.alert
        js_prompt_alert.send_keys("text")
        js_prompt_alert.accept()
        expected_result = "You entered: text"
        actual_result = self.driver.find_element(*self.JS_ALERT_CONFIRM_MESSAGE).text
        self.assertEqual(expected_result,actual_result,f"Error: Expected message: {expected_result}, actual message: {actual_result}")


    """
    
    Scenarii JS Prompt
    
    - ok + text
    - ok fara text
    - cancel fara text
    - cancel cu text
    
    """

    def tearDown(self):
        self.driver.quit()
