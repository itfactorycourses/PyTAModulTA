from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import Base_Page


class Search_Page(Base_Page):

    SEARCH_INPUT_BOX = (By.ID,"search")
    SEARCH_RESULTS_SORT_DROPDOWN = (By.XPATH,'//main[@id="maincontent"]//div[@class="search results"]//div[@class="toolbar toolbar-products"][1]//select[@id="sorter"]')
    PRODUCT_PRICE = (By.XPATH, '//span[@class="price"]')

    def insert_input(self, product_name):
        search_input = self.driver.find_element(*self.SEARCH_INPUT_BOX)
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.ENTER)

    def sort_by(self,sort_option):
        sort_dropdown = Select(self.driver.find_element(*self.SEARCH_RESULTS_SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text(sort_option)

    def validate_sort_results_descending(self):
        price_list = self.driver.find_elements(*self.PRODUCT_PRICE)
        is_price_list_sorted = True
        for i in range(len(price_list) - 1):  # 0,1,2,3,4,5,6
            if price_list[i].text.replace("$", "") < price_list[i + 1].text.replace("$",""):  # if price_list[6]<price_list[7]
                is_price_list_sorted = False
        assert is_price_list_sorted == True, "Error, the price list is not sorted in descending order"
