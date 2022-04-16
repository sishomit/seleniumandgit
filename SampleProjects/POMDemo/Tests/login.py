import HtmlTestRunner
from selenium import webdriver
import time
import unittest
from SampleProjects.POMDemo.Pages.loginpage import Loginpage
from SampleProjects.POMDemo.Pages.homepage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Shomit/PycharmProjects/Firstselenium/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logout()
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)
        cls.driver.quit()
        print("Test OK")
if __name__ == '__main__':
    unittest.main(HtmlTestRunner.HTMLTestRunner(output="C:/Users/Shomit/PycharmProjects/Firstselenium/reports"))
