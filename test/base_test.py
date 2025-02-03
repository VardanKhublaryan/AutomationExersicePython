import pytest
from src.utils.web_driver_singleton import WebDriverSingleton
from src.utils.wait_helper import WaitHelper

"""Base test class for driver setup and teardown"""


@pytest.mark.usefixtures("setup_teardown")
class BaseTest:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self, request):
        self.driver = WebDriverSingleton.get_driver()
        wait = WaitHelper(self.driver)
        wait.wait_for_page_loaded()
        self.driver.get("https://automationexercise.com/")

        yield  # This makes sure tests run

        WebDriverSingleton.quit_driver()
