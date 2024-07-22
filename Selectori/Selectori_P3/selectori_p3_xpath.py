"""
XPATH este un selector care are rolul de a identifica elementul pe baza pozitiei lui in
        structura codului html

Exista doua tipuri de xpath-uri:
a) XPATH absolut -> cauta elementul din aproape in aproape de la inceputul paginii HTML pana la identificarea acestuia
b) XPATH relativ -> cauta elementul pe baza unor elmente de filtrare care ne ajuta sa cautam
        fie direct elementul care ne intereseaza fie pleacand de la un element apropiat si apoi
        navigand la elementul care ne intereseaza

NICIODATA nu se va folosi XPATH absolut pentru ca daca se schimba structura codului, adresa elementului
        nostru se schimba, iar el nu va mai fi gasit
Exemplu:
XPATH absolut initial: /html/body/div[2]/div/a[2]
Modificare: Dupa body s-a mai adaugat un div ca si copil direct in pozitia a doua (deci dupa primul copil direct de tip div)
Consecinta: XPATH-ul /html/body/div[2]/div/a[2] se va transforma in /html/body/div[3]/div/a[2]

In general exista si posibilitatea de a copia valoarea xpath-ului direct din codul html (copy xpath)
        dar nu avem garantia ca ni se va returna un xpath reliable
Exemplu: //*[@id="post-34269"]/div/div/section[1]/div[3]/div[1]/div/div[4]/div/div/a
                -> chiar daca el este inceput ca fiind xpath relativ,
                    el se finalizeaza tot ca xpath absolut

Cum se poate identifica un xpath relativ si unul absolut?
- In general atunci cand navigam direct la elementul care ne intereseaza (adica la orice urmas)
            ne folosim de caracterele //
- atunci cand navigam la copilul direct ne folosim de caracterul /

Exemplu: /html/body/div[2]/div/a[2] => din html navigam in body, apoi in al doilea copil de tip div
            apoi in primul copil de tip div al div-ului identificat, apoi in al doilea copil de tip ancora
Daca scriu html/body/div[2]/div/a[2] => elementul va fi identificat
Daca scriu html/a[2] -> elementul nu va fi identificat pentru ca nu exista un copil direct de tip ancora al elementului cu tag-ul html
Daca scriu html//a[2] -> elementul poate fi identificat pentru ca se cauta orice urmas care respecta criteriul

// este obligatoriu la XPATH indiferent ce fel de filtrare facem

Asa cum am discutat la sesiunea anterioara, un CSS selector are avantajul fata de XPATH ca este mai rapid
Avantajul XPATH-ului in fata unui CSS este acela ca poate sa caute un element
si de jos in sus (din copil in parinte sau din frate posterior in frate anterior),
nu doar de sus in jos (din parinte in copil sau din frate anterior in frate posterior)
"""


# Modalitati de identificare a elementelor prin xpath:
# a) pe baza de tag: -> la xpath relativ tag-urile sunt precedate de caracterel //
# exemplu: //input
# b) dupa tag + atribut=valoare => atentie!!!! atunci cand facem cautare dupa atribut=valoare in xpath,
#             atributul trebuie precedat de caracterul @
# exemplu: //select[@class="sorter-options"]
# c) dupa atribut=valoare indiferent de tag => in acest caz, tag-ul va fi inlocuit de caracterul *
# //*[@class="content"]
# d) cautare din parinte in copil: => de regula se face cu tag-ul direct: /
# exemplu: //select/option => nu este recomandat
# e) cautare din copil in parinte: => se face prin specificarea keyword-ului //parent urmat de :: si tag-ul parintelui la care trebuie sa ajungem
# exemplu: //button[@class="btn btn_primary btn_small btn_inventory "]//parent::div
#             am plecat de la elementul cu tag-ul button identificat prin clasa btn btn_primary btn_small btn_inventory
#             de la acel al buton am plecat si am identificat parintele de tip div
# Se poate face si cautare cu index, caz in care elementele se vor returna in ordinea proximitatii de sus in jos
# f) cautare din frate anterior in frate posterior: se face prin specificarea keyword-ului //following-sibling urmat de :: si tag-ul fratelui la care trebuie sa ajungem
# - daca nu dam index, se va returna primul element identificat in proximitatea parintelui
# - daca dam index, se va returna primul element identificat in proximitatea elementului curent
# exemplu: //select/option[@value="12"]//following-sibling::option
# g) cautare din frate posterior in frate anterior: se face prin specificarea keyword-ului //preceding-sibling urmat de :: si tag-ul fratelui la care trebuie sa ajungem
# exemplu: //div[@class="actions-toolbar"]//preceding-sibling::div[3]
# h) cautare dupa un text care apare peste element (intre tag-ul de deschidere <tag> si tag-ul de inchidere </tag>
# - contains text - (//div[contains(text(),"If you have an account, sign in")])
# Daca facem cautare dupa text, nu o sa facem assert pe acelasi text dupa care am cautat (exemplu de asa nu mai jos)
# expected_text = '//div[contains(text(),"If you have an account, sign in with your email address.")]'
# actual_text = driver.find_element(By.XPATH('//div[contains(text(),"If you have an account, sign in with your email address.")]')).text
# assert expected_text == actual_text
# - text is (//div[text()="If you have an account, sign in with your email address."])
# i) Cautare dupa criterii multiple, indeplinibile in acelasi timp (ex: doua perechi de tip atribut=valoare)
# exemplu 1: //select[@id="sorter" and @data-role="sorter" and @class="sorter-options"]
#  => in situatia de mai sus elementul cu tag-ul select trebuie sa indeplineasca concomitent toate regulile specificate intre paranteze patrate
# exemplu 2: //main[@id="maincontent"]//div[@class="search results"]//div[@class="toolbar toolbar-products"][1]//select[@id="sorter"]//option[@value="name" and contains(text(),"Product Name")]
# j) Cautare dupa criterii multiple care pot fi indeplinite separat (adica ori unul ori altul)
# exemplu: //option[@value="name" or @value="price"]
