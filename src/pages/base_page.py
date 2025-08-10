from typing import Self

from selenium.webdriver.remote.webdriver import WebDriver

from src.utils.wait_helper import WaitHelper

class BasePage:
    def __init__(self, driver: WebDriver, page_url: str):
        self.driver = driver
        self.page_url = page_url

    def open_page(self) -> Self:
        self.driver.get(self.page_url)
        return self

    def is_loaded(self):
        wait_helper = WaitHelper(self.driver)
        wait_helper.wait_for_page_loaded()
        wait_helper.wait_to_url(self.page_url)
