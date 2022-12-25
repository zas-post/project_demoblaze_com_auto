import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.login_user_page import LoginPage
from pages.main_page import MainPage


def test_login_user():

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',[ 'enable-logging' ])
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

    print("--- Start Test ---")

    login = LoginPage(driver)
    login.authorization()
    mp = MainPage(driver)
    mp.select_proucts()
    cp = CartPage(driver)
    cp.proucts_place_order()


    # select_product = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
    # select_product.click()
    # print(f"- Click Select Product")
    #
    # enter_shopping_cart = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    # enter_shopping_cart.click()
    # print(f"- Click Enter Shopping Cart")
    #
    # success_test = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
    # value_success_test = success_test.text
    # print(value_success_test)
    # assert value_success_test == "YOUR CART"
    # print("Test Success!!! ---> Your Cart")

    print("--- Finish Test ---")
    # time.sleep(5)
    # driver.close()

# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='visibleAfter']")))



# time.sleep(5)
# driver.close()
