from unittest import TestCase
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from base_data import Base_Data

class Test_Search(TestCase,Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()

    def test_search_and_sort_by_price_descending(self):
        input_box = self.driver.find_element(*self.SEARCH_INPUT_BOX)
        input_box.send_keys('capri')
        input_box.send_keys(Keys.ENTER)
        sort_dropdown = Select(self.driver.find_element(*self.SEARCH_RESULTS_SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text('Price')
        price_list = self.driver.find_elements(*self.PRODUCT_PRICE)
        is_price_list_sorted = True
        for i in range(len(price_list) - 1):  # 0,1,2,3,4,5,6
            if price_list[i].text.replace("$", "") < price_list[i + 1].text.replace("$",""):  # if price_list[6]<price_list[7]
                is_price_list_sorted = False
        self.assertTrue(is_price_list_sorted,"Error, the price list is not sorted in descending order")

    def tearDown(self):
        self.driver.quit()