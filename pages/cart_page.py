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
    mmonth = "07"
    yyear = "2030"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    btn_place_order = "//button[@class='btn btn-success']"
    btn_purchase = "//button[contains( text(),'Purchase')]"

    name_locator = "//input[@id='name']"
    country_locator = "//input[@id='country']"
    city_locator = "//input[@id='city']"
    credit_card_locator = "//input[@id='card']"
    month_locator = "//input[@id='month']"
    year_locator = "//input[@id='year']"

    end_shop = "//div[contains(@class,'sweet-alert')]//h2"

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
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.month_locator)))

    def get_year_locator(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.year_locator)))

    def get_btn_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.btn_purchase)))

    def get_correct_shoping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.end_shop)))

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

    def input_month(self,mmonth):
        self.get_month_locator().send_keys(mmonth)
        print(f"Input Month = {mmonth}")

    def input_year(self,yyear):
        self.get_year_locator().send_keys(yyear)
        print(f"Input Year = {yyear}")

    def click_btn_purchase(self):
        self.get_btn_purchase().click()
        print("Click Button Purchase")

    # Methods
    def products_place_order(self):
        self.start_test()
        self.get_current_url()
        self.click_btn_place_order()
        self.input_name(self.name)
        self.input_country(self.country)
        self.input_city(self.city)
        self.input_credit_card(self.credit_card)
        self.input_month(self.mmonth)
        self.input_year(self.yyear)
        self.click_btn_purchase()
        self.take_screenshot()
        self.assert_finish_shopping(self.get_correct_shoping(), "Thank you for your purchase!")

        time.sleep(5)
