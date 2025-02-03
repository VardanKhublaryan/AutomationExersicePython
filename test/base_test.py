import pytest
from src.utils.web_driver_singleton import WebDriverSingleton
from src.utils.wait_helper import WaitHelper


@pytest.mark.usefixtures("setup_teardown")  # Automatically applies to all derived test classes
class BaseTest:
    driver = None;
    """Base test class for driver setup and teardown"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self, request):
        """Fixture to initialize and quit the driver before and after each test."""
        self.driver = WebDriverSingleton.get_driver()
        wait = WaitHelper(self.driver)
        wait.wait_for_page_loaded()
        self.driver.get("https://automationexercise.com/")

        yield  # This makes sure tests run

        WebDriverSingleton.quit_driver()
