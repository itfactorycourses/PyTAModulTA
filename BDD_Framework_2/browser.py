from seleniumbase import Driver


class Browser():

    driver = Driver()
    driver.maximize_window()
    driver.set_page_load_timeout(10) # pentru driver.get()
    driver.implicitly_wait(10) # pentru driver.find_element()

    def close_browser(self):
        self.driver.quit()