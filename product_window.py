from page import Page
from page_locators import ProductCartWindowLocators

class ProductWindow(Page):
    def click_cross_button(self):
        self.driver.find_element(*ProductCartWindowLocators.CROSS_BUTTON).click()