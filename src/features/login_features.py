from src.pages.login_signup_page import LoginSignupPage
import allure

class LoginFeatures:

    @allure.step("Open login page, and log in")
    def open_login_page_and_login(self, user_name: str, password: str, driver) -> "LoginSignupPage":
        login_page = LoginSignupPage(driver)
        login_page.open_page()
        login_page.log_in(user_name, password)
        return login_page

    @allure.step("Open Login page,and sign up")
    def open_login_page_and_sign_up(self, user_name: str, password: str, driver) -> "LoginSignupPage":
        login_page = LoginSignupPage(driver)
        login_page.open_page()
        login_page.signup(user_name, password)
        return login_page
