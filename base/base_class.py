import datetime

class BaseClass:

    def __init__(self, driver):
        self.driver = driver


    """ Method get current URL """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL = {get_url}")


    """ Method assert word """

    def assert_login(self, word, result):
        value_current_login = word.text
        assert value_current_login == result
        print(f"Entered Valid User ---> {value_current_login}")

    def assert_finish_shopping(self, str, end_str):
        value_current_word = str.text
        print(value_current_word)
        assert value_current_word == end_str
        print(f"Entered Valid Word ---> {value_current_word}")

    def start_test(self):
        print("---> Start Test")

    def take_screenshot(self):
        new_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot1_{new_date}.png'
        self.driver.save_screenshot('.\\screenshot\\' + name_screenshot)
