from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OrangeHRM_Login:

    # Locators
    login_user_name = (By.NAME, "username")
    login_password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]")
    profile_drop_down = (By.XPATH, "//span[contains(@class,'userdropdown')]")
    logout_button = (By.XPATH, "//ul[contains(@class,'dropdown-menu')]//a[text()='Logout']")
    login_error_message = (By.XPATH, '//div[@class="orangehrm-login-error"]/div')
    dashboard_header = (By.XPATH, '//h6')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_user_name(self, username):
        self.wait.until(EC.visibility_of_element_located(self.login_user_name)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.login_password)).send_keys(password)

    def click_on_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def click_on_profile_drop_down(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_drop_down)).click()

    def click_on_logout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()

    def login_to_orange_hrm(self, user_name, password):
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.click_on_login_button()

    def logout_from_orange_hrm(self):
        self.click_on_profile_drop_down()
        self.click_on_logout_button()

    def get_login_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.login_error_message)).text

    def get_log_in_successful_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_header)).text

    def get_logout_successful_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.login_button)).text