from src.pages.login_signup_page import LoginSignupPage
from test.base_test import BaseTest


class LoginSignup(BaseTest):

    def test_valid_login(self):
        login_page = LoginSignupPage(self.driver)
        login_page.open_page()
        login_page.log_in("testAuto@gmail.com","test")
        assert login_page.get_account_text() in "test"

    def test_wrong_login(self):
        login_page =LoginSignupPage(self.driver)
        login_page.open_page()
        login_page.log_in("abscd@gmail.com", "4353")
        assert login_page.get_wrong_data_error() in "Your email or password is incorrect!"

    def test_signup_existing_email(self):
        login_page = LoginSignupPage(self.driver)
        login_page.open_page()
        login_page.signup('test','test@gmail.com')
        assert login_page.get_exist_email_err() in "Email Address already exist!"




