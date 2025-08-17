import pytest
from pageObjects.login_page import OrangeHRM_Login
from pageObjects.search_employee import SearchEmp
from test_data.test_data import *

@pytest.mark.usefixtures("create_multiple_employees")
class Test_SearchEmployees:

    def test_search_all_employees(self, setup, create_multiple_employees):
        self.driver = setup
        log_in_page = OrangeHRM_Login(self.driver)
        search_page = SearchEmp(self.driver)

        for emp in create_multiple_employees:
            search_page.search_employee(emp["employee_id"])
            result_id = search_page.get_employee_id_in_employee_list()
            assert emp["employee_id"] in result_id, f"Employee {emp['employee_id']} not found in results"

        log_in_page.logout_from_orange_hrm()
        assert log_in_page.get_logout_successful_message() == LOGOUT_SUCCESSFUL_TEXT, "Expected successful logout"

