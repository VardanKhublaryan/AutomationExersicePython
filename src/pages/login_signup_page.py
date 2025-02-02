from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils.action_with_elements import ActionWithElements


class LoginSignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://automationexercise.com/login")
        self.__driver = driver
        self.__web_element = ActionWithElements(driver)
        self.__email_field = (By.NAME, 'email')
        self.__password_field = (By.NAME, 'password')
        self.__log_in_btn = (By.CSS_SELECTOR, '[data-qa="login-button"]')
        self.__account_text = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b')
        self.__incorrect_data_error = (By.CLASS_NAME, 'error')
        self.__forgot_password_link = (By.CSS_SELECTOR, 'href="lookup.htm')
        self.__login_error = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')
        self.__name_field = (By.NAME, 'name')
        self.__exist_email_error = (By.CSS_SELECTOR, '[action="/signup"] p')
        self.__register_btn = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
        self.__gender1_radio_btn = (By.ID,"id_gender1")
        self.__register_password_field = (By.ID,"password")
        self.__select_day_field =(By.ID,"days")
        self.__select_month_field =(By.ID,"months")
        self.__select_year_field =(By.ID,"years")
        self.__first_name_field =(By.ID,"first_name")
        self.__last_name_field =(By.ID,"last_name")
        # self.__address_field =(By.ID,"address1")


    def log_in(self, username, password):
        self.__web_element.send_key(self.__email_field, username)
        self.__web_element.send_key(self.__password_field, password)
        self.__web_element.click_to(self.__log_in_btn)

    def signup(self, name, email):
        email_field = self.__web_element.get_element_from_list(self.__email_field, 1)
        self.__web_element.send_key(self.__name_field, name)
        self.__web_element.send_key(email_field, email)
        self.__web_element.click_to(self.__register_btn)

    def get_account_text(self):
        return self.__web_element.get_text(self.__account_text)

    def get_error_text(self):
        return self.__web_element.get_text(self.__incorrect_data_error)

    def click_forgot_pass_link(self):
        self.__web_element.click_to(self.__forgot_password_link)

    def get_wrong_data_error(self):
        return self.__web_element.get_text(self.__login_error)

    def get_exist_email_err(self):
        return self.__web_element.get_text(self.__exist_email_error)
