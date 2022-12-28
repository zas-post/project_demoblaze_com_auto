import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass


class MainPage(BaseClass):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    link_navbar = "//a[@class='navbar-brand']"
    link_cart = "//a[@id='cartur']"

    link_phone = "//a[contains( text(),'Phones')]"
    link_laptops = "//a[contains(text(),'Laptops')]"
    link_monitor = "//a[contains( text(),'Monitors')]"

    select_product_1 = "//a[contains( text(),'Sony vaio i5')]"
    select_product_2 = "//a[contains( text(),'MacBook Pro')]"
    select_product_3 ="//a[contains( text(),'2017 Dell 15.6 Inch')]"

    add_to_cart_product_1 = "//a[@onclick='addToCart(8)']"
    add_to_cart_product_2 = "//a[@onclick='addToCart(15)']"
    add_to_cart_product_3 = "//a[@onclick='addToCart(13)']"

    price_product_1 = "//*[@id='tbodyid']/tr[2]/td[3]"
    price_product_2 = "//*[@id='tbodyid']/tr[1]/td[3]"
    price_product_3 = "//*[@id='tbodyid']/tr[3]/td[3]"

    all_price_products = "//h3[@id='totalp']"


    # Getter

    def get_link_navbar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_navbar)))

    def get_link_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_cart)))

    def get_link_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_phone)))

    def get_link_laptops(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_laptops)))

    def get_link_monitor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_monitor)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1)))

    def get_add_to_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_2)))

    def get_add_to_cart_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_3)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))

    def get_price_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_3)))

    def get_all_price_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_price_products)))

    # Actions
    def click_link_navbar(self):
        self.get_link_navbar().click()
        print("Click Link Navbar Brand")

    def click_link_cart(self):
        self.get_link_cart().click()
        print("Click Link Cart")

    def click_link_laptops(self):
        self.get_link_laptops().click()
        print("Click Link Laptops")

    def click_product_1(self):
        self.get_select_product_1().click()
        print("Click Link Product 1, Sony vaio i5")

    def click_product_2(self):
        self.get_select_product_2().click()
        print("Click Link Product 2, MacBook Pro")

    def click_product_3(self):
        self.get_select_product_3().click()
        print("Click Link Product 3, 2017 Dell 15.6 Inch")

    def click_add_to_cart_product_1(self):
        self.get_add_to_cart_product_1().click()
        print("Click Button Add To Card Product 1")

    def click_add_to_cart_product_2(self):
        self.get_add_to_cart_product_2().click()
        print("Click Button Add To Card Product 2")

    def click_add_to_cart_product_3(self):
        self.get_add_to_cart_product_3().click()
        print("Click Button Add To Card Product 3")

    def sum_three_prices(self):
        value_price_1 = self.get_price_product_1().text
        value_price_2 = self.get_price_product_2().text
        value_price_3 = self.get_price_product_3().text
        value_sum_tree_price = (int(value_price_1) + int(value_price_2) + int(value_price_3))
        return value_sum_tree_price

    # Methods
    def select_proucts(self):
        self.start_test()
        self.get_current_url()
        self.click_link_laptops()
        self.click_product_1()
        self.get_current_url()
        self.click_add_to_cart_product_1()
        self.click_link_navbar()
        self.click_link_laptops()
        self.click_product_2()
        self.get_current_url()
        self.click_add_to_cart_product_2()
        self.click_link_navbar()
        self.click_link_laptops()
        self.click_product_3()
        self.get_current_url()
        self.click_add_to_cart_product_3()
        self.click_link_navbar()
        self.click_link_cart()
        self.assert_correct_sum(self.get_all_price_products(), self.sum_three_prices())

        time.sleep(5)
