from faker import Faker
import random
# biblioteka faker do generacji losowych danych
tested_page = 'https://www.yves-rocher.pl/'
fake = Faker("pl_PL") #generuje polskie dane
#funkcja losująca liczby z zakresu 1-2 i przypisująca odpowiednią płeć
def sex():
    s = random.randint(1,2)
    if s == 1:
        return 'male'
    else:
        return 'female'
sex = sex() #przypisanie wylosowanej płci do zmiennej
e_mail = fake.email() + "lll"  # niepoprawnie podany email
n_ame = fake.first_name_male() # imię męskie
n_ame2 = fake.first_name_female() #imie zenskie
l_name = fake.last_name_male() # nazwisko męskie
l_name2 = fake.last_name_female() # nazwisko zenskie
pho_number = fake.msisdn()[:-4]  # format telefonu bez "-"
i_psswd = fake.password() #generuje losowe haslo
product = "Hoggar woda toaletowa 50 ml" #szukana fraza
errors_msg_exp = 'Wpisz poprawny adres email'  #zmienna do testu rejestracji przy uzyciu złego maila