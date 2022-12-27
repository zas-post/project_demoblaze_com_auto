from selenium import webdriver
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
    cp.products_place_order()

    print("--- Finish Test ---")
    # time.sleep(5)
    # driver.close()
