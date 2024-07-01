from unittest import TestCase
from selenium.webdriver.common.by import By
from base_data import Base_Data


# import unittest

# class TestLogin(unittest.TestCase)
class Test_Login(TestCase,Base_Data):

    # self-ul dintre paranteze are rolul de a marca metoda ca apartinand clasei (defineste legatura intre metoda si clasa)
    # atunci cand accesam in interiorul metodei un atribut definit la nivel de clasa, acesta trebuie sa fie precedat de keyword-ul self
    # daca nu ii punem self in fata, sistemul il va cauta printre parametrii metodei
    def setUp(self):
        self.driver = self.setup_actions()
        self.driver.find_element(By.LINK_TEXT,"Sign In").click()

    # atunci cand definim o metoda de test, numele metodei de test trebuie sa fie cat mai clar, astfel incat sa nu trebuiasca
    #         sa citim tot codul atunci cand vrem sa intelegem ce s-a intamplat

    def test_login_unexisting_email_and_password(self):
        # incorect:
        # self.driver.find_element(self.EMAIL_INPUT).send_keys("unexisting_email@gmail.com")
        # self.driver.find_element((By.ID,"email")).send_keys("unexisting_email@gmail.com")

        # corect
        # Atunci cand am pus * in fata elementului am facut ceea ce se numeste despachetare a tuplului
        # practic am extras valorile din tuplu in mod individual
        self.insert_login_actions("unexisting_email@gmail.com","unexisting_password")
        self.evaluate_error_message("The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later",self.UNEXISTING_CREDENTIALS_ERROR_MESSAGE)
        # test@gmail.com -> valid
        # test -> invalid

    def test_login_invalid_email(self):
        self.insert_login_actions("invalid_email","invalid_password")
        self.evaluate_error_message("Please enter a valid email address (Ex: johndoe@domain.com).",self.INVALID_EMAIL_ERROR_MESSAGE)

    def tearDown(self):
        self.driver.quit()

"""

Elemente din programare care au nevoie de un corp (bloc de cod):
- if
- for / foreach / while
- clase
- functii

In python blocurile de cod sunt marcate prin indentare (in java se marcheaza prin acolade {})

"""




