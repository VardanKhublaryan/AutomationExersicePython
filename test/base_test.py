import unittest
from src.utils.web_driver_singleton import WebDriverSingleton
from src.utils.wait_helper import WaitHelper


class BaseTest(unittest.TestCase):

    def setUp(self):
        """Runs once before all test methods in a test class."""
        self.driver = WebDriverSingleton.get_driver()
        wait = WaitHelper(self.driver)
        wait.wait_for_page_loaded()
        self.driver.get("https://automationexercise.com/")


    def tearDown(self):
        """Runs once after all test methods in a test class."""
        WebDriverSingleton.quit_driver()
