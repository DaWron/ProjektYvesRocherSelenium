from page import Page
from page_locators import ProductLocators

class ProductPage(Page):

    #Kliknięce przycisku dodaj do koszyka
    def add_to_cart(self):
        self.driver.find_element(*ProductLocators.ADD_CART).click()