#Importowanie bibliotek

from variables import * #pobiera zmienne z pliku variables
import unittest
from time import sleep
from selenium import webdriver
from main_page import MainPage
from for_men_page import ForMenPage
from product_page import ProductPage
from product_window import ProductWindow
from my_account_page import MyAccountPage
from registration_page import RegistrationPage
from page_locators import *

class YvesRocherTests(unittest.TestCase):
    def setUp(self):
        # Warunki wstepne
        print("Przygotowanie testu")
        #Cztery poniższe linie kodu mają na celu zezwolenie na powiadomienia na stronie-w ten sposób podczas testów nie pojawia się okno które mogło doprowadzić do ich przerwania
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 1}
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.get(tested_page)
        self.home_page = MainPage(self.driver)
        self.men_page = ForMenPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.product_window = ProductWindow(self.driver)
        self.regi_page = MyAccountPage(self.driver)
        self.new_regi_page = RegistrationPage(self.driver)
        self.driver.maximize_window()
        #Maksymalny czas kiedy webdriver ma na znalezeieni elementu
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # Zakonczenie testow
        print("Zakonczenie testu")
        self.driver.quit()

    def test_registration_with_wrong_email(self):
        # 1. Wejdź na stronę www.yves-rocher.pl (krok realizuje sie w metodzie setUp)
        # 2. Zaakceptuj cookies
        self.home_page.accept_cookies()
        # 3. Kliknij w zakładkę „Moje konto”
        self.home_page.going_to_my_account()
        # 4. Kliknij przycisk „Załóż konto”
        self.regi_page.going_to_registration()
        # W tej funkcji realizuja się punkty 5-12 - rejestracja uzytkownika (z blednym mailem)
        self.new_regi_page.registration()
        sleep(3)

        ###Oczekiwany rezultat###

        #Sprawdzenie czy pojawia sie odpowiedni komunikat o niepoprawnym mailu
        errors_msg = self.driver.find_element(*RegistrationPageLocators.ERROR_MSG).text
        self.assertEqual(errors_msg_exp, errors_msg)

    def test_searching_for_product(self):
        # 1. Wejdź na stronę www.yves-rocher.pl (krok realizuje sie w metodzie setUp)
        # 2. Zaakceptuj cookies
        self.home_page.accept_cookies()
        # 3.Kliknij i uzupełnij pole „Nazwa lub kod produktu…” dokładną nazwą szukanego produktu
        self.driver.find_element(*MainPageLocators.SEARCH).click()
        self.driver.find_element(*MainPageLocators.SEARCH).send_keys(product)
        # 4.Kliknij ikonę lupki - „Szukaj”
        self.driver.find_element(*MainPageLocators.SEARCH_ICON).click()

        ###Oczekiwany rezultat###

        #Porównanie czy liczba znalezionych produktów jest różna od 0
        searched_element = self.driver.find_element(*FoundProductsLocators.FOUND_NUMBER).text
        searched_element = int(searched_element)
        self.assertNotEqual(0, searched_element)
        #Porównanie czy nazwa szukanego produktu jest dokładnie taka sama jak znalezionego
        searched_product = self.driver.find_element(*FoundProductsLocators.FOUND_PRODUCT).text
        self.assertEqual(searched_product, product)

    def test_is_the_price_correct(self):
        # 1. Wejdź na stronę www.yves-rocher.pl (krok realizuje sie w metodzie setUp)
        # 2. Zaakceptuj cookies
        self.home_page.accept_cookies()
        sleep(1)
        # 3. Kliknij w pole „Dla mężczyzn”
        self.home_page.going_to_for_men()
        sleep(1)
        # 4. Kliknij w pole produktu "Balsam po goleniu"
        self.men_page.balm_click()
        sleep(1)
        # 5. Kliknij w pole "Dodaj do koszyka"
        self.product_page.add_to_cart()
        sleep(1)
        # 6. Kliknij w pole „X” aby zamknąć okno „Produkt został dodany do Twojego koszyka.”
        self.product_window.click_cross_button()
        sleep(1)
        # 7. Kliknij w pole „Dla mężczyzn”
        self.home_page.going_to_for_men()
        sleep(1)
        # 8. Kliknij w pole produktu "Pianka do golenia"
        self.men_page.foam_click()
        sleep(1)
        # 9. Kliknij w pole "Dodaj do koszyka"
        self.product_page.add_to_cart()
        sleep(1)
        # 10. Kliknij w pole „X” aby zamknąć okno „Produkt został dodany do Twojego koszyka.”
        self.product_window.click_cross_button()
        sleep(1)
        # 11. Kliknij w ikonę koszyka w prawym górnym pasku strony
        self.home_page.going_to_basket()


        ###Oczekiwany rezultat###

        #Zamiana tekstu na liczbę zmiennoprzecinkową, usunięcie pustego znaku oraz liter "zł"
        price1 = float(self.driver.find_element(*CartLocators.BALM_PRICE).text[:-3])
        price2 = float(self.driver.find_element(*CartLocators.FOAM_PRICE).text[:-3])
        sum_of_prices = float(self.driver.find_element(*CartLocators.TOTAL_PRICE).text[:-3])
        #Sprawdzenie poprawności naliczonej ceny
        self.assertEqual(price1 + price2, sum_of_prices)

if __name__ == '__main__' :
    unittest.main()
