import pytest
from pageObjects.login_page import OrangeHRM_Login
from utilities.logger import LogGenerator
from utilities.read_config import Readconfig
from test_data.test_data import *

class Test_Login:
    username = Readconfig.GetUserName()
    password = Readconfig.GetPassword()
    log = LogGenerator.loggen()

    def test_login_to_orange_hrm(self, setup):
        """
        Verify Login to Orange HRM with multiple credential combinations
        """
        """
        Steps:
            - Go to Login Page for Orange HRM
            - Login with invalid user name and invalid password
            - Click on Login button
            - Verify user should not able to Login to Orange HRM
            - Login with invalid user name and valid password
            - Click on Login button
            - Verify user should not able to Login to Orange HRM
            - Login with valid user name and invalid password
            - Click on Login button
            - Verify user should not able to Login to Orange HRM
            - Login with valid user name and valid password
            - Click on Login button
            - Verify user should able to Login to Orange HRM
        """
        self.driver = setup
        log_in_page = OrangeHRM_Login(self.driver)
        # Invalid username + Invalid password
        self.log.info(f"Testing with invalid username:{INVALID_USER_NAME} & invalid password:{INVALID_PASSWORD}")
        log_in_page.login_to_orange_hrm(user_name=INVALID_USER_NAME, password=INVALID_PASSWORD)
        assert log_in_page.get_login_error_message() == INVALID_CREDENTIALS, "Expected invalid login error"
        self.driver.refresh()
        # Invalid username + Valid password
        self.log.info("Testing with invalid username & valid password")
        log_in_page.login_to_orange_hrm(user_name=INVALID_USER_NAME, password=VALID_PASSWORD)
        assert log_in_page.get_login_error_message() == INVALID_CREDENTIALS, "Expected invalid login error"
        self.driver.refresh()
        # Valid username + Invalid password
        self.log.info("Testing with valid username & invalid password")
        log_in_page.login_to_orange_hrm(user_name=VALID_USER_NAME, password=INVALID_PASSWORD)
        assert log_in_page.get_login_error_message() == INVALID_CREDENTIALS, "Expected invalid login error"
        self.driver.refresh()
        # Valid username + Valid password
        self.log.info("Testing with valid username & valid password")
        log_in_page.login_to_orange_hrm(user_name=VALID_USER_NAME, password=VALID_PASSWORD)
        assert log_in_page.get_log_in_successful_message() == LOGIN_SUCCESSFUL_TEXT, "Expected successful login"
        # Logout and verify
        self.log.info("Logging out of Orange HRM")
        log_in_page.logout_from_orange_hrm()
        assert log_in_page.get_logout_successful_message() == LOGOUT_SUCCESSFUL_TEXT, "Expected successful logout"



# pytest -v -n=2 --html=Reports/OrangeHRMreport.html --alluredir="Allure-results" --browser firefox
