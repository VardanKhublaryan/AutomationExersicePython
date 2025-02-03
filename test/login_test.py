from src.pages.login_signup_page import LoginSignupPage
from test.base_test import BaseTest


class TestLoginSignup(BaseTest):
    """Test cases for Login and Signup functionality."""

    def test_valid_login(self):
        login_page = LoginSignupPage(self.driver)
        login_page.open_page()
        login_page.log_in("testAuto@gmail.com", "test")

        assert "test" in login_page.get_account_text()

    def test_wrong_login(self):
        login_page = LoginSignupPage(self.driver)
        login_page.open_page()
        login_page.log_in("abscd@gmail.com", "4353")

        assert "Your email or password is incorrect!" in login_page.get_wrong_data_error()

    def test_signup_existing_email(self):
        login_page = LoginSignupPage(self.driver)
        login_page.open_page()
        login_page.signup('test', 'test@gmail.com')

        assert "Email Address already exist!" in login_page.get_exist_email_err()
