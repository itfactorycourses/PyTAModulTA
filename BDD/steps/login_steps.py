from behave import *


# pasii din steps trebuie sa coincida pana la ultima virgula cu pasii din feature
# chiar daca acelasi pas este folosit de mai multe ori in mai multe scenarii sau features
#     el va fi implementat in steps O SINGURA DATA
# atunci cand se face rularea, sistemul va lua textul din pasul din feature file si il va cauta
#        pe rand in toate fisierele de steps pana cand il va gasi
#  daca va gasi doi pasi implementati in steps cu exact acelasi text, ne va returna eroare:
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

@when('I click on the sign in link')
def step_impl(context):
    context.home_page.click_sign_in_link()

@when('I insert username "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.login_page.insert_username(username)
    context.login_page.insert_password(password)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I am logged into the application')
def step_impl(context):
    context.account_page.check_if_logged_in()
    context.account_page.logout()

@then('I receive error message: "{error_message}"')
def step_impl(context,error_message):
    context.login_page.check_error_message(error_message)


