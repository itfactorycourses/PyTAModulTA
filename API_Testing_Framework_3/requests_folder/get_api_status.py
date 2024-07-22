import requests


def get_api_status():
    response = requests.get('https://simple-books-api.glitch.me/status')
    # variabila response este o variabila locala, adica o adresa de memorie accesibila doar
    #         in interiorul metodei get_api_status
    return response
