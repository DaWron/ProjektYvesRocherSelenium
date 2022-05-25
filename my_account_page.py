from page import Page
from page_locators import MyAccountLocators

class MyAccountPage(Page):

    #Przejscie do podstrony z rejestracją
    def going_to_registration(self):
        self.driver.find_element(*MyAccountLocators.CREATE_ACCOUNT).click()