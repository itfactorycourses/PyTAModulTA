import requests
from environment import token

"""

Testul de submit_order este conditionat de existenta unui token valid care sa autorizeze
        crearea unei comenzi noi in baza de date

In termeni de testare acest lucru se numeste preconditie

Atentie!!!

preconditie = criteriu care trebuie indeplinit pentru ca un test case sa fie executat
test condition = criteriu care trebuie indeplinit pentru ca un test case sa fie considerat passed dupa executie

Exemple de test conditions:
Verify that the user can submit order when using valid data -> positive functional testing
Verify that the user cannot submit order without a valid bookid -> negative functional testing
Verify that the user cannot submit order without a valid customer name -> negative functional testing

"""

def submit_order(book_id="", customer_name=""):
    header_data = {"Authorization": token}
    if book_id == "" and customer_name !="":
            request_body = {
                "customerName": customer_name
              }
    elif book_id != "" and customer_name == "":
        request_body = {
            "bookId": book_id
        }
    elif book_id == "" and customer_name == "":
        request_body = {

        }
    else:
        request_body = {

            "bookId":book_id,
            "customerName":customer_name
        }

    response = requests.post('https://simple-books-api.glitch.me/orders/', json=request_body, headers=header_data)
    return response
