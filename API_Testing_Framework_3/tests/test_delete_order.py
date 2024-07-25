from requests_folder.delete_order import delete_order
from requests_folder.submit_order import submit_order


class Test_Delete_Order:

    def test_delete_order_valid_order_id(self):
        order_id = submit_order(3,"John").json()["orderId"]
        response_data = delete_order(order_id)
        assert response_data.status_code == 204, f"Error, invalid status code returned. Expected: 204, actual {response_data.status_code}"
