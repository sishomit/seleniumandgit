from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation tests")
        self.driver.find_element_by_name("btnK").click()

    def test_search_shomit(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("shomit")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner.run())
