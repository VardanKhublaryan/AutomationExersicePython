from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils.action_with_elements import ActionWithElements


class CardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://automationexercise.com/view_cart")
        self.driver = driver
        self.__web_element = ActionWithElements(driver)
        self.__click_here_btn = (By.CSS_SELECTOR, '[href="/products"]')
        self.__item_description = (By.CLASS_NAME, 'cart_description')

    def click_to_here_btn(self):
        self.__web_element.click_to(self.__click_here_btn)

    def is_card_visible(self) -> bool:
        return self.__web_element.is_displayed(self.__item_description)
