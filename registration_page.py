from variables import *
from page import Page
from page_locators import RegistrationPageLocators

class RegistrationPage(Page):

    #Automatyczne wypełnianie pół do rejestracji
    def registration(self):
        # 4. Kliknij i uzupełnij pole „Imię”
        self.driver.find_element(*RegistrationPageLocators.NAME).click()
        if sex == "male":
            self.driver.find_element(*RegistrationPageLocators.NAME).send_keys(n_ame)
        else:
            self.driver.find_element(*RegistrationPageLocators.NAME).send_keys(n_ame2)
        # 5. Kliknij i uzupełnij pole „Nazwisko”
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME).click()
        # blok warunkowy dostosowywujący zmienną z nazwiskiem do zmiennej z plcia
        if sex == "male":
            self.driver.find_element(*RegistrationPageLocators.LAST_NAME).send_keys(l_name)
        else:
            self.driver.find_element(*RegistrationPageLocators.LAST_NAME).send_keys(l_name2)
        # 7. Kliknij i błędnie uzupełnij pole „E-mail”
        self.driver.find_element(*RegistrationPageLocators.MAIL).click()
        self.driver.find_element(*RegistrationPageLocators.MAIL).send_keys(e_mail)
        # 8. Kliknij i uzupełnij „Hasło”
        self.driver.find_element(*RegistrationPageLocators.PASSWORD).click()
        self.driver.find_element(*RegistrationPageLocators.PASSWORD).send_keys(i_psswd)
        # 9. Kliknij i uzupełnij pole „Tel. komórkowy”
        self.driver.find_element(*RegistrationPageLocators.NUMBER).click()
        self.driver.find_element(*RegistrationPageLocators.NUMBER).send_keys(pho_number)
        # 10. Wybierz płeć i zaznacz odpowiednie pole
        if sex == "female":
            # Wybierz Kobieta
            self.driver.find_element(*RegistrationPageLocators.WOMAN).click()
        else:
            # Wybierz Mężczyzna
            self.driver.find_element(*RegistrationPageLocators.MAN).click()
        # 11. Zaznacz pole „Akceptuję Regulamin sklepu yves-rocher.pl oraz Politykę prywatności”
        self.driver.find_element(*RegistrationPageLocators.TERMS_OF_USE).click()
        # 12. Kliknij przycisk „Załóż konto”
        self.driver.find_element(*RegistrationPageLocators.C_ACCOUNT).click()