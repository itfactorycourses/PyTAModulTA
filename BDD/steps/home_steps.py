from behave import *

@given('I am on the magento software testing homepage')
def step_impl(context):
    # atunci cand noi cream fisiere de tip pages, ele vor contine clase
    #     care vor fi populate cu atribute si metode
    #  atributele vor salva selectorii cu care vom identifica elementele, iar metodele vor
    #           reprezenta interactiunea cu acele elemente prin intermediul selectorilor
    #  Atunci cand vrem sa accesam un atribut sau o metoda dintr-o clasa, trebuie sa instantiem
    #         un obiect din acea clasa
    # acel obiect va fi folosit in fisierele de steps pentru a apela metodele din pages
    #  in cazul de mai jos, home_page va fi numele obiectului instantiat dintr-o clasa numita Home_Page
    context.home_page.navigate_to_homepage()