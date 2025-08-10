
from src.features.login_features import LoginFeatures
from test.base_test import BaseTest


class TestLoginSignup(BaseTest):

    def setup_method(self):
        self.__login_feature = LoginFeatures()

    def test_valid_login(self):
        assert ("test" in
                self.__login_feature.open_login_page_and_login("testAuto@gmail.com",
                                                               "test",
                                                               self.driver)
                .get_account_text())

    def test_wrong_login(self):
        assert ("Your email or password is incorrect!" in
                self.__login_feature.open_login_page_and_login("abscd@gmail.com",
                                                               "4353",
                                                               self.driver)
                .get_wrong_data_error())

    def test_signup_existing_email(self):
        assert ("Email Address already exist!" in
                self.__login_feature.open_login_page_and_sign_up('test',
                                                                 'test@gmail.com',
                                                                 self.driver)
                .get_exist_email_err())
