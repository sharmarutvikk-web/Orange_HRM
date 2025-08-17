import pytest
from test_data.test_data import *

@pytest.mark.usefixtures("create_multiple_employees")
class Test_CreateEmployees:


    def test_verify_employees_created(self, create_multiple_employees):
        assert len(create_multiple_employees) == NUMBER_OF_EMPLOYEES
        for emp in create_multiple_employees:
            assert emp["success_message"][0] == SUCCESS_POP_UP_MESSAGE
            assert emp["success_message"][1] == SUCCESSFULLY_SAVE_POP_UP_MESSAGE
