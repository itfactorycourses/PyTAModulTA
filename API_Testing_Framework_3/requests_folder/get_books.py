import requests

def get_all_books(type="",limit=""):
    # atunci cand facem requesturi cu parametri endpointul o sa fie influentat in felul urmator:
    # - in momentul in care incepe lista de parametri, aceasta va fi precedata de caracterul "?"
    # - parametrii sunt separati intre ei de caracterul "&"
    # - fiecare parametru va fi reprezentat de cheie=valoare

    #  Scenarii:
    # 1. Type gol, limita goala
    # 2. Type populat, limita goala
    # 3. Type gol, limita populata
    # 4. Type populat, limita populata

    if type == "" and limit == "":
        return requests.get('https://simple-books-api.glitch.me/books')
    elif type != "" and limit == "":
        return requests.get(f'https://simple-books-api.glitch.me/books?type={type}')
    elif type == "" and limit != "":
        return requests.get(f'https://simple-books-api.glitch.me/books?limit={limit}')
    else:
        return requests.get(f'https://simple-books-api.glitch.me/books?type={type}&limit={limit}')