import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.test_data import *
from selenium.webdriver.common.action_chains import ActionChains


class SearchEmp:


    search_button = (By.XPATH, "//button[@type='submit']")
    Search_Result_CSS = (By.CSS_SELECTOR, "div[class='oxd-table-card'] div:nth-child(3) div:nth-child(1)")
    employee_list_button = (By.XPATH, "//a[contains(text(), 'Employee List')]")
    employee_id_input = (By.XPATH, "//label[text()='Employee Id']/following::div/input")
    employee_list_id = (By.XPATH, "//div[@role='cell']/following-sibling::div")
    result_message = (By.XPATH, "//span[contains(text(),'Record')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TIMEOUT_1)
        self.actions = ActionChains(self.driver)

    def click_on_search_button(self):
        self.wait.until(EC.visibility_of_element_located(self.search_button)).click()
        time.sleep(TIMEOUT_2) # To Load the data when searched for a particular one

    def click_on_employee_list_button(self):
        self.wait.until(EC.visibility_of_element_located(self.employee_list_button)).click()

    def enter_employee_id_to_search(self, search_id):
        self.wait.until(EC.visibility_of_element_located(self.employee_id_input)).click()
        self.driver.find_element(*self.employee_id_input).clear()
        self.driver.find_element(*self.employee_id_input).send_keys(search_id)
        self.wait.until(EC.text_to_be_present_in_element_value(self.employee_id_input, search_id))

    def get_employee_id_in_employee_list(self):
        employee_list_id = self.wait.until(EC.visibility_of_element_located(self.employee_list_id)).text
        return employee_list_id

    def search_employee(self, employee_id):
        self.click_on_employee_list_button()
        self.enter_employee_id_to_search(employee_id)
        self.click_on_search_button()