from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from src.utils.wait_helper import WaitHelper


class ActionWithElements(WaitHelper):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.wait_halper = WaitHelper(driver)

    def send_key(self, locator, text):
        if not isinstance(locator, WebElement):
            locator = self.wait_element_visible(locator)
        try:
            locator.clear()
            locator.send_keys(text)
        except Exception as e:
            print(e)

    def click_to(self, locator):
        element = self.wait_element_clickable(locator)
        try:
            element.click()
        except Exception as e:
            print(e)

    def get_text(self, locator):
        element = self.wait_element_visible(locator)
        try:
            return element.text
        except Exception as e:
            print(e)

    def get_element_from_list(self, locator, index):
        elements = self.wait_all_elements(locator)
        return elements[index]

    def select_element(self,locator,value):
        element = self.wait_element_visible(locator)
        select = Select(element)
        select.select_by_value(value)



