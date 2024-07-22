# sortare dupa pret ascending
from selenium.webdriver.support.select import Select
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = Driver()
driver.get("https://magento.softwaretestingboard.com/")
input_box = driver.find_element(By.CSS_SELECTOR,'input#search')
input_box.send_keys('capri')
input_box.send_keys(Keys.ENTER)

# am instantiat un obiect numit sort_dropdown din clasa Select
# clasa select a primit drept argument pentru constructor elementul web returnat de metoda find_element
sort_dropdown = Select(driver.find_element(By.CSS_SELECTOR,'main[id="maincontent"] div[class="search results"] div[class="toolbar toolbar-products"]:first-of-type select[id="sorter"]'))
sort_dropdown.select_by_visible_text('Price')

driver.quit()