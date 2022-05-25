from selenium import webdriver
from page_locators import MainPageLocators, MyAccountLocators
from page import Page

class MainPage(Page):

    #Akceptacja plików cookie
    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIES).click()
    #Przejscie do zakładki "Dla mężczyzn"
    def going_to_for_men(self):
        self.driver.find_element(*MainPageLocators.FOR_MEN).click()
    #Przejście do koszyka
    def going_to_basket(self):
        self.driver.find_element(*MainPageLocators.BASKET).click()
    #Przejscie do zakładki moje konto
    def going_to_my_account(self):
        self.driver.find_element(*MainPageLocators.MY_ACCOUNT).click()
