from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass


class MainPage(BaseClass):

    user_name = "222"
    password = "222"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    link_phone = "//a[contains( text(),'Phones')]"
    link_laptops = "//a[contains(text(),'Laptops')]"
    link_monitor = "//a[contains( text(),'Monitors')]"

    select_product_1 = "//a[contains( text(),'Sony vaio i5')]"
    select_product_2 = "//a[contains( text(),'MacBook Pro')]"
    select_product_3 ="//a[contains( text(),'2017 Dell 15.6 Inch')]"

    add_to_cart_product_1 = "//a[@onclick='addToCart(8)']"
    add_to_cart_product_2 = "//a[@onclick='addToCart(15)']"
    add_to_cart_product_3 = "//a[@onclick='addToCart(13)']"


    # Getter
    def get_link_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_phone)))

    def get_link_laptops(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_laptops)))

    def get_link_monitor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_monitor)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))

    def get_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1)))

    def get_add_to_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_2)))

    def get_add_to_cart_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_3)))


    # Actions
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



    # Methods
    def select_proucts(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.get_current_url()
        self.click_link_laptops()
        self.click_product_1()
        self.click_add_to_cart_product_1()
        self.click_link_laptops()
        self.click_product_2()
        self.click_add_to_cart_product_2()
        self.click_link_laptops()
        self.click_product_3()
        self.click_add_to_cart_product_3()


        # self.click_link_sign_up(self.link_log_in)
        # self.input_user_name(self.user_name)
        # self.input_password(self.password)
        # self.click_button_sign_up(self.button_log_in)
        # self.assert_login(self.get_current_login(),"Welcome 222")

        # alert = driver.switch_to_alert()
        # alert.send_keys(Keys.ESCAPE)