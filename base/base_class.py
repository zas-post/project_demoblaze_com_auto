class BaseClass:

    def __init__(self, driver):
        self.driver = driver


    """ Method get current URL """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL = {get_url}")


    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert  value_word == result
        print("Good Value Word")
