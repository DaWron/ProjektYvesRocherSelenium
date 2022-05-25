from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIES = (By.ID, 'onetrust-accept-btn-handler')
    MY_ACCOUNT = (By.XPATH, '/html/body/header/div[9]/account-mini')
    SEARCH = (By.XPATH, '/html/body/header/div[4]/form/input')
    SEARCH_ICON = (By.XPATH, '/html/body/header/div[4]/form/button[1]')
    FOR_MEN = (By.XPATH, '/html/body/div[2]/nav/ul/li[9]')
    BASKET = (By.XPATH, '/html/body/header/div[10]')
class MyAccountLocators:
    CREATE_ACCOUNT = (By.XPATH, '/html/body/main/div[1]/div/div/div[2]/div[1]/a')
class RegistrationPageLocators:
    NAME = (By.XPATH,'//*[@id="page-register-form"]/div[1]/div[3]/span/div[1]/div[1]/span/input')
    LAST_NAME = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[1]/div[2]/span/input')
    MAIL = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[1]/div[3]/span/input')
    PASSWORD = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[1]/div[4]/span/input')
    NUMBER = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[1]/div[5]/span/input')
    WOMAN = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[3]/div[1]/label')
    MAN = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[3]/div[2]/label')
    TERMS_OF_USE = (By.XPATH,'//*[@id="page-register-form"]/div[1]/div[3]/span/div[4]/div[2]/span/div/label/span[1]')
    C_ACCOUNT = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/div[3]/div/button')
    ERROR_MSG = (By.XPATH, '//*[@id="page-register-form"]/div[1]/div[3]/span/div[1]/div[3]/span/span')
class ProductsForMenLocators:
    BALM = (By.LINK_TEXT, 'Balsam po goleniu')
    FOAM = (By.LINK_TEXT, 'Pianka do golenia')
class ProductLocators:
    ADD_CART = (By.XPATH, '/html/body/main/article/div/div[2]/aside/div[1]/div[5]/cart-add[1]/div')
class ProductCartWindowLocators:
    CROSS_BUTTON = (By.XPATH, '//*[@id="micromodal-root"]/div/div/div[1]/button')
class CartLocators:
    BALM_PRICE = (By.XPATH, '/html/body/main/div/table/tbody/tr[1]/td[4]')
    FOAM_PRICE = (By.XPATH, '/html/body/main/div/table/tbody/tr[2]/td[4]')
    TOTAL_PRICE = (By.XPATH, '/html/body/main/div/table/tfoot/tr/td[2]')
class FoundProductsLocators:
    FOUND_NUMBER = (By.XPATH, '/html/body/main/article/div/div[3]/span[2]')
    FOUND_PRODUCT = (By.LINK_TEXT, 'Hoggar woda toaletowa 50 ml')