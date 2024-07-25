from requests_folder.submit_order import submit_order


class Test_Submit_Order():

    def test_submit_order_valid_data(self):
        response_data = submit_order(4,"John")
        assert response_data.status_code == 201, f"Error, expected status: 201, actual status: {response_data.status_code}"
        assert response_data.json()["created"] == True
        assert len(response_data.json()["orderId"]) == 21, "Error, invalid length order"


    def test_submit_order_missing_customer_name(self):
        response_data = submit_order(4)
        assert response_data.status_code == 400, f"Error, invalid status code returned. Expected status code: 400, actual status code: {response_data.status_code}"
        assert response_data.json()["error"] == "Invalid or missing customerName."

"""

Dupa identificarea unui bug, el trebuie raportat.
Componentele unui bug:
Titlu 
Preconditii
Pasi de reproducere
Rezultate asteptate
Rezultate actuale

Raportarea bug-ului de mai sus: 
Titlu: Submit order request can be sent without mandatory customer name field
Preconditions: A valid token must be generated in order to be able to send the request
Steps to reproduce: 
Send the submit order request with the following payload:
curl --location 'https://simple-books-api.glitch.me/orders' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{

  "bookId": 1
}'

Expected results: 
1. The request should not go through
2. Status code 400 should be returned
3. An error should be displayed announcing that the customer name field is mandatory

Actual results:
The request is executed successfuly and the order is created

"""