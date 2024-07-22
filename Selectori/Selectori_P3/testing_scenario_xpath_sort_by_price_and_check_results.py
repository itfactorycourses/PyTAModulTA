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
sort_dropdown = Select(driver.find_element(By.XPATH,'//main[@id="maincontent"]//div[@class="search results"]//div[@class="toolbar toolbar-products"][1]//select[@id="sorter"]'))
sort_dropdown.select_by_visible_text('Price')

"""
Diferentele intre find_element si find_elements:
- find_element returneaza un singur element. 
    Daca sunt mai multe, il returneaza pe primul pe care il gaseste
    Daca nu este niciunul, returneaza exceptie: Unable to locate element
- find_elements returneaza o lista de elemente care respecta criteriile selectorului specificat
   Daca sunt mai multe, fiecare element va fi adaugat in lista la un index specific, in ordinea in care au fost gasite
   Daca nu este niciunul, nu va returna exceptie, ci va returna o lista goala

"""

price_list = driver.find_elements(By.XPATH,'//span[@class="price"]')
is_price_list_sorted = True
for i in range(len(price_list)-1): # 0,1,2,3,4,5,6
    if price_list[i].text.replace("$","") < price_list[i+1].text.replace("$",""): # if price_list[6]<price_list[7]
        is_price_list_sorted = False

# is_price_list_sorted = False
# for i in range(len(price_list)):
#     is_price_list_sorted = False
#     if price_list[i]>price_list[i+1]:
#         is_price_list_sorted = True

# is_price_list_sorted = True
# for i in range(len(price_list)):
#     if price_list[i]>price_list[i+1]:
#         continue
#     else:
#         is_price_list_sorted = False

assert is_price_list_sorted == True

driver.quit()