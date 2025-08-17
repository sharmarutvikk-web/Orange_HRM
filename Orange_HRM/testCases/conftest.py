import random
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pageObjects.add_employee import AddEmployee
from pageObjects.login_page import OrangeHRM_Login
from test_data.test_data import *


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        options = Options()
        options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(URL)
    yield driver
    driver.quit()

@pytest.fixture()
def create_multiple_employees(setup):
    driver = setup
    login_page = OrangeHRM_Login(driver)
    login_page.login_to_orange_hrm(user_name=VALID_USER_NAME, password=VALID_PASSWORD)

    employees = []

    for i in range(NUMBER_OF_EMPLOYEES):
        add_employee = AddEmployee(driver)
        add_employee.click_on_left_panel_pim()
        add_employee.click_on_add_employee_button()

        # Generate unique data for each employee
        emp_id = str(random.randint(10000, 99999))
        first_name = f"{FIRST_NAME}{i}"
        middle_name = f"{MIDDLE_NAME}{i}"
        last_name = f"{LAST_NAME}{i}"

        add_employee.enter_first_name(first_name)
        add_employee.enter_middle_name(middle_name)
        add_employee.enter_last_name(last_name)
        add_employee.enter_employee_id(emp_id)

        add_employee.click_on_save_button()
        success_message = add_employee.get_employee_successfully_created_message()
        employee_id = add_employee.get_employee_id()

        employees.append({
            "first_name": first_name,
            "last_name": last_name,
            "employee_id": employee_id,
            "success_message": success_message
        })

    return employees
