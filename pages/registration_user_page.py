from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass


class RegistrationPage(BaseClass):

    url = 'https://www.demoblaze.com/'

    user_name = "alex"
    password = "qw12!!"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    link_sign_up = "//a[@id='signin2']"
    user_name_locator = "//input[@id='sign-username']"
    password_locator = "//input[@id='sign-password']"
    button_sign_up = "//*[@id='signInModal']/div/div/div[3]/button[2]"


    # Getter

    def get_link_sign_up(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_sign_up)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_button_sign_up(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sign_up)))


    # Actions

    def click_link_sign_up(self, link_sign_up):
        self.get_link_sign_up().click()
        print("Click Link Sign Up")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print(f"Input User Name = {user_name}")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_button_sign_up(self, button_sign_up):
        self.get_user_name().send_keys()
        print(f"Click Button Sign Up")


    # Methods

    def registration(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_link_sign_up(self.link_sign_up)
        self.input_user_name(self.user_name)
        self.input_password(self.password)
        self.click_button_sign_up(self.button_sign_up)

        # alert = driver.switch_to_alert()
        # alert.send_keys(Keys.ESCAPE)
