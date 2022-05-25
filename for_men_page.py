from page import Page
from page_locators import ProductsForMenLocators

class ForMenPage(Page):

    #Przjescie do podstron wybranych produktów
    def balm_click(self):
        self.driver.find_element(*ProductsForMenLocators.BALM).click()
    def foam_click(self):
        self.driver.find_element(*ProductsForMenLocators.FOAM).click()