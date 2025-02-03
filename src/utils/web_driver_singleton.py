from selenium import webdriver


class WebDriverSingleton:
    _instance = None  # Private class variable to store the WebDriver instance

    @staticmethod
    def get_driver():
        if WebDriverSingleton._instance is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-ads")
            chrome_options.add_argument("--disable-javascript")
            chrome_options.add_argument("--incognito")  # Open in incognito mode (ads might not be stored)
            WebDriverSingleton._instance = webdriver.Chrome(chrome_options)  # Initialize only once
        return WebDriverSingleton._instance

    @staticmethod
    def quit_driver():
        if WebDriverSingleton._instance:
            WebDriverSingleton._instance.quit()
            WebDriverSingleton._instance = None
