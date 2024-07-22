"""

Un css selector permite identificarea elementelor web folosindu-ne de mai multe
        proprietati ale elementelor, sau chiar pe baza succesiunii elementelor web
        intr-o pagina

Unul din avantajele folosirii unui CSS selector este ca este destul de rapid,
        dar are ca si dezavantaj faptul ca permite doar cautarea elementelor
        din parinte in copil (sau din frate anterior in frate ulterior),
        nu si din copil in parinte (sau din frate ulterior in frate anterior)

        Consideram ca un element este parinte daca are in subcomponenta sau unul sau mai multe elemente.
        Concomitent, considetam ca un element este copil daca se afla in subcomponenta unui alt element.
        De regula cea mai usoara modalitate prin care ne putem da seama de legatura intre doua elemente
        este de a verifica sagetuta din stanga elementului (daca aceasta exista).
        Atunci cand inchidem sagetuta unui element, toate elementele copil ar trebui sa devina ascunse

        Alta modalitate prin care putem decide daca un element este copil al altui element este de a verifica
        daca acesta se afla intre tag-ul de inceput (<tag>) al elementului si tag-ul ed sfarsit
        al elementului (</tag>)

        Consideram ca un element este frate cu un alt element daca daca cele doua elemente au acelasi
                parinte direct.
        Consideram ca un element este frate anterior pentru un alt element daca se afla inaintea acestuia
                in structura html.
        Concomitent, putem considera ca un element este frate ulterior pentru un alt element
                daca se afla dupa acesta in structura html


- id -> daca facem cautare in css selector dupa id, precedam acel id de caracterul # (exemplu: #search)
- clasa -> daca facem cautare in css selector dupa clasa, precedam acea clasa de caracterul . (exemplu: .label)
- tag + atribut / valoare -> la fel ca la mentiunea de la cursul anterior,
            atunci cand facem cautare dupa atribut = valoare trebuie sa incadram aceasta cautare intre []
            (exemplu: input[title="Email"], input[id="email"])
- tag + id / clasa (exemplu: input#email, button.login)
- primul copil al elementului (>) sau first-of-type
        (exemplu: fieldset > div -> returneaza toti copiii directi de tip div ai elementului fieldset
                  fieldset > div:first-of-type -> returneaza DOAR PRIMUL COPIL DIRECT al elementului fieldset)
- orice copil al elementului (" ") -> returneaza toti urmasii (directi sau indirecti ai elementului cautat
                    (exemplu: fieldset div -> returneaza 8 rezultate:
                                    - patru copii directi de tip div ai lui fieldset
                                    - un copil de tip div al celui de-al doilea div (cinci)
                                    - un copil de tip div al celui de-al treilea div (sase)
                                    - doi copii de tip div al celui de-al patrulea div (opt)
- ultimul copil al elementului (last-of-type) -> returneaza DOAR ULTIMUL COPIL DIRECT al elementului cautat
                    (exemplu: fieldset > div:last-of-type -> returneaza un singur rezultat
                                        - ultimul copil de tip div al elementului fieldset)
- copil specific (nth-of-type(x)) -> returneaza elementul cu numarul specificat intre paranteze;
                    (exemplu: fieldset div:nth-of-type(3) -> returneaza al treilea copil DIRECT al elementului fieldset)

- frate ulterior (+) -> returneaza primul frate cu tag-ul specificat
                    (exemplu: footer[class="page-footer"] + div + small
                                -> gasim elementul cu tag-ul footer reprezentat de
                                        o pereche atribut = valoare (atributul este class si valoarea este page-footer)
                                 dupa ce l-am identificat cautam urmatorul frate al lui cu tag-ul div
                                 dupa ce div-ul a fost identificat, se cauta urmatorul frate AL ACESTUI DIV cu tag-ul small

"""

