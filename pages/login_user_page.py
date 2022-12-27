from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass


class LoginPage(BaseClass):

    url = 'https://www.demoblaze.com/'

    user_name = "222"
    password = "222"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    link_log_in = "//a[@id='login2']"
    user_name_locator = "//input[@id='loginusername']"
    password_locator = "//input[@id='loginpassword']"
    button_log_in = "//*[@id='logInModal']/div/div/div[3]/button[2]"
    main_word = "//a[@id='nameofuser']"

    # Getter
    def get_link_log_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_log_in)))

    def get_login_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_locator)))

    def get_login_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_button_log_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_log_in)))

    def get_current_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def click_link_sign_up(self, link_log_in):
        self.get_link_log_in().click()
        print("Click Link Log In")

    def input_user_name(self, user_name):
        self.get_login_user_name().send_keys(user_name)
        print(f"Input User Name = {user_name}")

    def input_password(self, password):
        self.get_login_password().send_keys(password)
        print("Input Password")

    def click_button_sign_up(self, button_log_in):
        self.get_button_log_in().click()
        print(f"Click Button Log In")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_link_sign_up(self.link_log_in)
        self.input_user_name(self.user_name)
        self.input_password(self.password)
        self.click_button_sign_up(self.button_log_in)
        self.assert_login(self.get_current_login(), "Welcome 222")
