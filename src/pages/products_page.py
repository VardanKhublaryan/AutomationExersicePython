from typing import Self

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils.action_with_elements import ActionWithElements


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://automationexercise.com/products")
        self.__web_element = ActionWithElements(driver)
        self.__buttons = self.driver.find_elements(By.CLASS_NAME, "add-to-cart")
        self.__continue_shopping_btn = self.driver.find_element(By.CLASS_NAME,'close-modal')

    def click_add_to_card_button(self)-> Self:
        self.__web_element.click_to(self.__buttons[0])
        return self

    def click_continue_shop_btn(self):
        self.__web_element.click_to(self.__continue_shopping_btn)
        from src.pages.card_page import CardPage
        return CardPage(self.driver)
