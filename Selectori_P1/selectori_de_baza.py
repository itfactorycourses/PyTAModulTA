import time

from selenium.webdriver.common.by import By
from seleniumbase import Driver

"""

Driverul este o modalitate prin care sistemul poate interactiona cu browserul instalat local
Atunci cand vrem sa testam in mod automat un site web noi trebuie sa instruim sistemul
    sa deschida acest browser.

"""

driver = Driver() # am instantiat un obiect din clasa Driver
                        # atunci cand se instantiaza un obiect dintr-o clasa,
                            # de fapt se aloca spatiu memorie care este reprezentat de numele obiectului
                            # iar in acel spatiu de memorie se vor pastra valorile individuale pentru obiectul in scop
                            #     conform cu atributele din clasa instantiata

# Ca sa putem accesa un site web ne putem folosi de metoda get
# aceasta metoda este definita in clasa Driver si este apelabila prin intermediul obiectului instantiat din acea clasa

driver.get("https://magento.softwaretestingboard.com/")

# Pentru a putea inchide pagina web ne putem folosi de doua metode:
# a) metoda close inchide doar fereastra curenta (activa)
# b) metoda quit care inchide tot driverul

# Ca sa putem face testare automata, avem nevoie sa identificam in mod automat elementele din codul html
# un element html reprezinta o parte structurala a unei pagini web
# Ca sa accesam codul html aferent unui element din pagina, dam click dreapta pe acel element, si apoi apasam pe inspect
#     Elementul identificat este marcat cu o banderola gri sau albastra

# Identificarea in mod automat a elementelor din web se face prin intermediul selectorilor.
# Selectorii reprezinta siruri de caractere menite sa identifice in mod unic elementele din aplicatia web

"""
Exemple de elemente web:
- div -> este o modalitate prin care putem sa grupam mai multe elemente in functie de anumiti parametri
- input -> este un element web care desemneaza posibilitatea de a introduce valori de la tastatura (email, parola)
- label -> o eticheta care se poate pune peste un element web
- button -> un element care poate sa declanseze o actiune 
- span -> este o modalitate prin care putem sa definim text intr-o aplicatie web
- p -> este o modalitate prin care putem sa definim un paragraf de text
- img -> modalitate prin care putem defini imagini
- a -> vine de la ancora, si este o modalitate prin care putem sa definim linkuri catre alte pagini web
        Aceste ancore sunt compuse din urmatoarele elemente:
        - tag-ul de inceput (<a>)
        - proprietati (href -> reprezinta linkul efectiv catre care vom fi redirectionati)
        - link text (textul pe care il vedem noi in aplicatia web)
- table -> inceputul unui tabel in html
- th -> vine de la table header si reprezinta definirea headerului unui tabel (numele unei coloane)
- tr -> vine de la table row si reprezinta un rand intr-o tabela
- td -> vine de la table data si reprezinta o singura celula dintr-un tabel

Selectorii care pot fi folositi pentru testare automata sunt urmatorii:
ID
Class
Name
Tag
Link Text
Partial Link Text
XPATH
CSS Selector
"""

# Elementele web sunt particularizate de anumite atribute care pot avea o valoare.
# Atributele sunt separate de valoarea lor prin intermediul caracterului =
# Atunci cand vrem sa facem cautare dupa elemente de tip atribut = valoare, acestea trebuie puse intre paranteze patrate

# metoda find_element este folosita pentru a identifica elemente in aplicatia web
# ea primeste doua argumente: tipul selectorului si valoarea acestuia
# (La o functie / metoda:
#       - parametrii reprezinta numele variabilelor temporare care se vor aloca atunci cand se apeleaza functia
#       - argumentele reprezinta valorile efective date acelor variabile la momentul rularii)

# Variabila = spatiu de memorie unde stocam valori care se pot schimba pe parcursul executiei programului
# Constanta = spatiu de memorie unde stocam valori care nu se pot schimba pe parcursul executiei programului

# Pentru a putea sa folosim aceasta metoda este nevoie sa importam libraria By
#  Pentru a putea trimite valori pe un camp de input in browser ne putem folosi de metoda send_keys

# Pentru a trimite input pe un camp putem sa facem urmatoarele chestii:
# 1. Salvam elementul web intr-o variabila si ulterior ne folosim de acea variabila ca sa apelam metoda send_keys

driver.find_element(By.LINK_TEXT,"Sign In").click()
email_input = driver.find_element(By.ID,"email")
email_input.send_keys("test@gmail.com")
# 2. Inlantuim apelarea de metode pana cand obtinem rezultatul dorit
# email_input.clear() # goleste valoarea de pe un camp de input
driver.find_element(By.ID,"email").send_keys("test@gmail.com")

password = driver.find_element(By.NAME,"login[password]").send_keys("sdfghj")
time.sleep(3)

# In cazul in care elementul nu se afla pe pagina ne va returna eroarea: Unable to locate element: {"method":"css selector","selector":"[id="email"]"}

driver.find_element(By.XPATH,'//button[@class="action login primary"]').click()

# Partial link text identifica elementele care CONTIN textul furnizat
driver.find_element(By.PARTIAL_LINK_TEXT,"Support").click()

time.sleep(2)
driver.quit()
