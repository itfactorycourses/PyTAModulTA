from requests_folder.get_api_status import get_api_status

class Test_Status:

    def test_get_status(self):
        # la rularea metodei get_api_status() valoarea salvata la adresa de memorie response (din fisierul get_api_sttaus_
        #     va fi copiata la adresa de memorie response_data din fisierul curent, iar adresa de memorie get_api_status va fi eliberata
        response_data = get_api_status()
        assert response_data.json()["status"] == 'OK',f"Error: Expected status: OK, actual status: {response_data.json()['status']}"
        assert response_data.status_code == 200,f"Error: Expected status code: 200, actual status code: {response_data.status_code}"
        assert response_data.elapsed.microseconds < 4000, f"Error: Expected execution time: <4000ms, actual execution time: {response_data.elapsed}"

# Daca assertul returneaza eroare pot fi doua situatii:
# a) assertul returneaza eroare din cauza codului de testare automata -> atunci trebuie sa corectam codul de testare automata pana cand testul devine passed
# b) assertul returneaza eroare din cauza unei probleme in aplicatie -> atuncin trebuie sa cream un raport de bug catre echipa de dezvoltare care sa descrie problema pe care am identificat-o
#  dupa ce dezvoltatorul fixeaza problema noi trebuie sa facem doua lucruri:
#  - retesting -> reexecutam testul automat sa ne asiguram ca fixul a fost corect, adica sa verificam ca problema nu se mai reproduce
#  - regression testing -> reexecutam testele automate care este posibil sa fi fost afectate de modificarea adusa in urma fixarii bug-urilor pentru a ne asigura ca acestea sunt in continuare passed


