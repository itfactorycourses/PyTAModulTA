import requests
import faker
from faker import Faker


def get_api_status():
    response = requests.get('https://simple-books-api.glitch.me/status')
    # variabila response este o variabila locala, adica o adresa de memorie accesibila doar
    #         in interiorul metodei get_api_status
    return response


def generate_token(name="", email=""):
    faker_object = Faker()
    if name == "" and email != "":
        name = faker_object.name()
    elif name != "" and email == "":
        email = faker_object.email()
    elif name == "" and email == "":
        name = faker_object.name()
        email = faker_object.email()
    else:
        name = name
        email = email
    request_body = {
        "clientName": name,
        "clientEmail": email
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=request_body)
    return response.json()["accessToken"]

