import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumbase import Driver

driver = Driver()
driver.maximize_window()
driver.get("https://www.elefant.ro/")

time.sleep(5)
driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
time.sleep(10)
driver.find_element(By.XPATH,'//div[@class="top-header mf-header-min-height"]//form//input[@name="SearchTerm"]').send_keys("iphone")
driver.find_element(By.XPATH,'//div[@class="top-header mf-header-min-height"]//form//input[@name="SearchTerm"]').send_keys(Keys.ENTER)

# de aici incepe numaratoarea elementelor
item_count = driver.find_elements(By.XPATH, '//div[@class="lazy inventory-item"]')

if len(item_count) < 14:
    print("Search results are less than 14!")
else:
    print(f'Search result item count passed {len(item_count)}')

item_prices = driver.find_elements(By.XPATH, '//div[@data-testing-id="current-price"]')
print(len(item_prices))

driver.quit()