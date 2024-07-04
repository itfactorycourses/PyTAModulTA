from browser import Browser


class Base_Page(Browser):

    def check_error_message(self, expected_error_message, actual_error_message = "", selector=""):
        if selector != "":
            actual_error_message = self.driver.find_element(*selector).text
        is_error_message_correct = expected_error_message == actual_error_message
        return is_error_message_correct
