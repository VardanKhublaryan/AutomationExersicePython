from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WaitHelper:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_page_loaded(self):
        try:
            return self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        except Exception as e:
            print(e)

    def wait_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(e)

    def wait_element_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except Exception as e:
            print(e)

    def wait_to_url(self, url):
        try:
            return self.wait.until(lambda d: d.current_url == url)
        except Exception as e:
            print(e)

    def wait_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
