from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AddEmployee:

    # Locators
    left_panel_pim = (By.XPATH, "//span[text()='PIM']/parent::a")
    add_employee_button = (By.XPATH, "//a[contains(text(), 'Add Employee')]")
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    middle_name = (By.XPATH, "//input[@placeholder='Middle Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    employee_id_field = (By.XPATH, "")
    save_button = (By.XPATH, "//button[@type='submit']")
    employee_id_input = (By.XPATH, "//label[text()='Employee Id']/following::div/input")
    success_message = (By.XPATH, "//div[contains(@class, 'content--success')]/p")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def click_on_left_panel_pim(self):
        pim_element = self.wait.until(EC.element_to_be_clickable(self.left_panel_pim))
        self.actions.move_to_element(pim_element).click().perform()

    def click_on_add_employee_button(self):
        add_btn = self.wait.until(EC.element_to_be_clickable(self.add_employee_button))
        add_btn.click()

    def enter_first_name(self, first_name):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first_name)
        return first_name

    def enter_middle_name(self, middle_name):
        self.wait.until(EC.visibility_of_element_located(self.middle_name)).send_keys(middle_name)

    def enter_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys(last_name)
        return last_name

    def enter_employee_id(self, emp_id):
        emp_id_input = self.wait.until(EC.visibility_of_element_located(self.employee_id_input))
        emp_id_input.clear()
        emp_id_input.send_keys(emp_id)

    def click_on_save_button(self):
        save_btn = self.wait.until(EC.element_to_be_clickable(self.save_button))
        save_btn.click()

    def get_employee_id(self):
        return self.wait.until(EC.visibility_of_element_located(self.employee_id_input)).get_attribute("value")

    def get_employee_successfully_created_message(self):
        self.wait.until(EC.visibility_of_element_located(self.success_message))
        messages = self.driver.find_elements(*self.success_message)
        all_text = [msg.text for msg in messages]
        self.wait.until(EC.invisibility_of_element_located(self.success_message))
        return all_text