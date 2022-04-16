from SampleProjects.POMDemo.Locators.locators import Locators

class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcomelink_id=Locators.welcomelink_id
        self.logoutlink_text=Locators.logoutlink_text

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcomelink_id).click()


    def click_logout(self):
        self.driver.find_element_by_link_text(self.logoutlink_text).click()
