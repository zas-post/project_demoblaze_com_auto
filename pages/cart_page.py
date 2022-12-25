import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass


class CartPage(BaseClass):

    name = "Alexander"
    country = "RU"
    city = "Moscow"
    credit_card = "2025234165517564"
    month_m = "Januar"
    year_y = "2030"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    btn_place_order = "//button[@class='btn btn-success']"
    btn_purchase = "//button[@class='btn btn-primary']"

    name_locator = "//input[@id='name']"
    country_locator = "//input[@id='country']"
    city_locator = "//input[@id='city']"
    credit_card_locator = "//input[@id='card']"
    month_locator = "//input[@id='month']"
    year_locator = "//input[@id='year']"


    # Getter

    def get_btn_place_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.btn_place_order)))

    def get_name_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.name_locator)))

    def get_country_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.country_locator)))

    def get_city_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.city_locator)))

    def get_credit_card_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.credit_card_locator)))

    def get_month_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.get_month_locator())))

    def get_year_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.year_locator)))

    def get_btn_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.btn_purchase)))

    # Actions
    def click_btn_place_order(self):
        self.get_btn_place_order().click()
        print("Click Button Place Order")

    def input_name(self, name):
        self.get_name_locator().send_keys(name)
        print(f"Input Name = {name}")

    def input_country(self, country):
        self.get_country_locator().send_keys(country)
        print(f"Input Country = {country}")

    def input_city(self, city):
        self.get_city_locator().send_keys(city)
        print(f"Input City = {city}")

    def input_credit_card(self, credit_card):
        self.get_credit_card_locator().send_keys(credit_card)
        print(f"Input Credit Card = {credit_card}")

    def input_month(self, month):
        self.get_month_locator().send_keys(month)
        print(f"Input Month = {month}")

    def input_year(self, year):
        self.get_year_locator().send_keys(year)
        print(f"Input Year = {year}")

    def click_btn_purchase(self):
        self.get_btn_purchase().click()
        print("Click Button Purchase")


    # Methods
    def proucts_place_order(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        # print("---> Start Test Select Product")
        self.start_test()
        self.get_current_url()
        self.click_btn_place_order()
        self.input_name(self.name)
        self.input_country(self.country)
        self.input_city(self.city)
        self.input_credit_card(self.credit_card)
        self.input_month(self.month_m)
        self.input_year(self.year_y)
        self.click_btn_purchase()

        time.sleep(5)


        # self.click_link_sign_up(self.link_log_in)
        # self.input_user_name(self.user_name)
        # self.input_password(self.password)
        # self.click_button_sign_up(self.button_log_in)
        # self.assert_login(self.get_current_login(),"Welcome 222")

        # alert = driver.switch_to_alert()
        # alert.send_keys(Keys.ESCAPE)