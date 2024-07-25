import requests
from environment import token


def delete_order(orderId):
    header_data = {"Authorization": token}
    header_endpoint = f"https://simple-books-api.glitch.me/orders/{orderId}/"
    return requests.delete(header_endpoint, headers=header_data)