from pages.account_page import Account_Page
from pages.home_page import Home_Page
from pages.login_page import Login_Page
from pages.search_page import Search_Page


def before_all(context):
    # context este ca o cutiuta / zona de memorie care va stoca toate obiectele instantiate
    # din clasele de tip pages
    #  atunci cand se incepe rularea se va incepe cu instantierea obiectelor din clasele de tip pages
    context.home_page = Home_Page()
    context.login_page = Login_Page()
    context.account_page = Account_Page()
    context.search_page = Search_Page()
