def str_to_int(text: str, mesaj_eroare: str) -> int:
    """
        O functie care transforma un string intr-un numar intreg
        si arunca o eroare de tip ValueError daca nu se poate
    """
    try:
        return int(text)
    except ValueError:
        raise ValueError(mesaj_eroare)

def test_str_to_int():
    assert str_to_int('2', 'mesaj') == 2
    assert str_to_int('10', 'mesaj') == 10
    assert str_to_int('0', 'mesaj') == 0
    assert str_to_int('-1', 'mesaj') == -1
    try:
        str_to_int('a', 'mesaj')
        assert False
    except ValueError:
        pass


def validare_scoruri(parametri: list) -> list:
    """
        Aceasta functie transforma lista cu string-uri 
        intr-o lista cu numere intregi. Also, se valideaza
        datele introduse.
    """
    if len(parametri) != 10:
        raise ValueError("Lista trebuie sa contina exact 10 scoruri!")
    scoruri = []
    for x in range(len(parametri)):
        numar = str_to_int(parametri[x],"Elementele listei trebuie sa fie numere intre 1 si 10!")
        if numar < 1 or numar > 10:
            raise ValueError("Elementele listei trebuie sa fie numere intre 1 si 10!")
        scoruri.append(numar)

    return scoruri

def test_validare_scoruri():
    """
        Functie de test pentru validare_scoruri()
    """
    # test in caz fericit
    assert validare_scoruri(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # test in cazul in care lista nu are 10 elemente
    try:
        validare_scoruri(['1', '2', '3'])
        assert False
    except ValueError:
        pass

    # test pentru valori string in cadrul listei
    try:
        validare_scoruri(['abc', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        assert False
    except ValueError:
        pass

    # test pentru valori care nu sunt intre 1 si 10
    try:
        validare_scoruri(['100', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        assert False
    except ValueError:
        pass

def adauga_scor(lista_participanti: list, parametri: list) -> list:
    """
        Aceasta functie adauga efectiv la finalul
        listei de participanti scorul noului concurent.
    """
    lista_participanti.append(parametri)

def test_adauga_scor():
    """
        Functia care testeaza adauga_scor()
    """
    lista_test = []
    scoruri_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    adauga_scor(lista_test, scoruri_test)
    assert len(lista_test) == 1
    assert lista_test[0] == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    alt_scor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    adauga_scor(lista_test, alt_scor)
    assert len(lista_test) == 2
    assert lista_test[1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
def ui_adauga_scor(lista_participanti: list, parametri: list):
    """
        Aceasta e functia apelata in main(), ea 
        primeste parametrii de la utilizator si lista de
        participanti.
    """

    try:
        scoruri_valide = validare_scoruri(parametri)
        adauga_scor(lista_participanti, scoruri_valide)
        print(f"Lista curenta este: {lista_participanti}.")
    except ValueError as error:
        print(error)



def validare_pozitie(lista_participanti: list, pozitie: str) -> int:
    """
        Aceasta functie transforma pozitia dintr-un
        string intr-un int si se asigura ca este
        posibila aceasta transformare, in acelasi timp 
        asigurand faptul ca pozitia exista in lista.
    """
    pozitie = str_to_int(pozitie, "Pozitia trebuie sa fie un nr intreg!")
    if pozitie < 1 or pozitie > len(lista_participanti) + 1:
        raise ValueError(f"Pozitia trebuie sa fie intre 1 si {len(lista_participanti)}!")
    return pozitie - 1

def test_validare_pozitie():
    """
        Aceasta functie testeaza functionarea corecta a 
        functiei validare_pozitie() prin intermediul assert
    """
    # test pentru caz fericit
    assert validare_pozitie([[]], 1) == 0

    # test pentru o valoare de tip str
    try:
        validare_pozitie([], 'abc')
        assert False
    except ValueError:
        pass

    # test pentru o valoare care nu e in range
    try:
        validare_pozitie([], 10)
        assert False
    except ValueError:
        pass



def insert_scor(lista_participanti: list, pozitie_inserare: int, scoruri_inserare: list) -> list:
    """
        Aceasta functie preia parametri valizi si insereaza
        la pozitia dorita scorurile participantului.
    """
    lista_participanti.append([]) # se face loc pentru elementul nou
    for i in range(len(lista_participanti) - 2, pozitie_inserare - 1, -1):
        lista_participanti[i+1] = lista_participanti[i]
    lista_participanti[pozitie_inserare] = scoruri_inserare
    return lista_participanti

def test_insert_scor():
    """
        Aceasta functie testeaza functionarea corecta a 
        functiei insert_scor() prin intermediul assert
    """
    assert insert_scor([], 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    lista_test = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    insert_scor(lista_test, 0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert len(lista_test) == 2
    assert lista_test[0] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert lista_test[1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ui_insert_scor(lista_participanti: list, parametri: list):
    """
        Aceasta functie este apelata in main(), primeste parametrii
        de la utilizator si apeleaza functiile auxiliare pt a 
        prelucra lista pe care o afiseaza la final, dupa modificari
    """
    try:
        if len(parametri) != 11:
            raise ValueError("Comanda 'insert' are nevoie de o pozitie si exact 10 scoruri!")
        pozitie_inserare = validare_pozitie(lista_participanti, parametri[0])
        scoruri_inserare = validare_scoruri(parametri[1:])
        insert_scor(lista_participanti, pozitie_inserare, scoruri_inserare)
        print(f"Lista dupa inserare este: {lista_participanti}")
    except ValueError as error:
        print(error)



def sterge_scor(lista_participanti: list, pozitie_stergere: int) -> list:
    """
        Aceasta functie sterge scorurile unui concurent
        de pe pozitia pozitie_stergere.
    """
    lista_participanti.pop(pozitie_stergere)
    return lista_participanti

def test_sterge_scor():
    """
        Aceasta functie testeaza functionarea corecta a 
        functiei sterge_scor() prin intermediul assert
    """
    assert sterge_scor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 0) == []
    lista_test = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    sterge_scor(lista_test, 1)
    assert len(lista_test) == 1
    assert lista_test[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ui_sterge_scor(lista_participanti: list, parametri: list):
    """
        Aceasta functie este apelata in main(), primeste parametrii
        de la utilizator si apeleaza functiile auxiliare pt a 
        prelucra lista pe care o afiseaza la final, dupa modificari.
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'sterge' are nevoie doar de o pozitie!")
        pozitie_stergere = validare_pozitie(lista_participanti, parametri[0])
        sterge_scor(lista_participanti, pozitie_stergere)
        print(f"Lista dupa stergere este: {lista_participanti}")
    except ValueError as error:
        print(error)



def sterge_interval(lista_participanti: list, pozitie_inceput: int, pozitie_sfarsit: int) -> list:
    """
        Aceasta functie sterge scorurile unui concurent
        de la pozitie_inceput pana la pozitie_sfarsit.
    """
    del lista_participanti[pozitie_inceput:pozitie_sfarsit + 1]
    return lista_participanti

def test_sterge_interval():
    """
        Aceasta functie testeaza functionarea corecta a 
        functiei sterge_interval() prin intermediul assert
    """
    lista_test = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
    ]
    sterge_interval(lista_test, 1, 2)
    assert len(lista_test) == 2
    assert lista_test[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert lista_test[1] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]

def ui_sterge_interval(lista_participanti: list, parametri: list):
    """
        Aceasta functie este apelata in main(), primeste parametrii
        de la utilizator si apeleaza functiile auxiliare pt a 
        prelucra lista pe care o afiseaza la final, dupa modificari.
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'sterge_interval' are 2 parametri: pozitia de inceput si cea de sfarsit.")
        pozitie_inceput = validare_pozitie(lista_participanti, parametri[0])
        pozitie_sfarsit = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_inceput > pozitie_sfarsit:
            raise ValueError("Pozitia de inceput trebuie sa fie mai mica sau egala cu pozitia de sfarsit!")
        sterge_interval(lista_participanti, pozitie_inceput, pozitie_sfarsit)
        print(f"Lista dupa stergere este: {lista_participanti}.")
    except ValueError as error:
        print(error)



def inlocuieste_scor(lista_participanti: list, pozitie_participant: int, scoruri_noi: list) -> list:
    """
        Aceasta functie sterge scorul curent al concurentului
        adauga unul nou si returneaza lista modificata.
    """
    sterge_scor(lista_participanti, pozitie_participant)
    insert_scor(lista_participanti, pozitie_participant, scoruri_noi)
    return lista_participanti

def test_inlocuieste_scor():
    lista_test = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
    ]
    inlocuieste_scor(lista_test, 2, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    assert len(lista_test) == 4
    assert lista_test[2] == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

def ui_inlocuieste_scor(lista_participanti: list, parametri: list):
    """
        Aceasta functie este apelata in main(), primeste parametrii
        de la utilizator si apeleaza functiile auxiliare pt a 
        prelucra lista pe care o afiseaza la final, dupa modificari.
        Primul parametru este pozitia participantului in lista, iar
        urmatorii 10 sunt scorurile noi.
    """
    try:
        if len(parametri) != 11:
            raise ValueError("Comanda 'inlocuieste_scor' are nevoie de 11 parametri!")
        pozitie_participant = validare_pozitie(lista_participanti, parametri[0])
        scoruri_noi = validare_scoruri(parametri[1:])
        inlocuieste_scor(lista_participanti, pozitie_participant, scoruri_noi)
        print(f"Lista participantilor dupa modificare este: {lista_participanti}")
    except ValueError as error:
        print(error)



def validare_medie(medie: str) -> float:
    """
        Aceasta functie primeste media in tip string
        si o transforma in tip float, daca este posibila
        transformarea.
    """
    try:
        return float(medie)
    except ValueError:
        raise ValueError("Media trebuie sa fie un numar real!")

def test_validare_medie():
    """
        functie de test pt validare_medie()
    """
    assert validare_medie('8.0') == 8.0
    assert validare_medie('8.55') == 8.55
    assert validare_medie('9.25') == 9.25
    try:
        validare_medie('abc')
        assert False
    except ValueError:
        pass

def calculare_medii(lista_participanti: list) -> list:
    """
        Aceasta functie primeste lista cu scorurile
        participantilor si returneaza o lista cu
        mediile acestora.
    """
    lista_medii = []
    for x in lista_participanti:
        medie_participant = sum(x) / len(x)
        lista_medii.append(medie_participant)
    return lista_medii

def test_calculare_medii():
    """
        functie de test pt calculare_medie()
    """
    lista_test = [
    [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],  
    [6, 6, 7, 5, 8, 4, 9, 1, 10, 4], 
    [7, 7, 8, 6, 9, 5, 10, 4, 7, 7], 
    [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]  
]
    assert calculare_medii(lista_test) == [5.0, 6.0, 7.0, 8.0]
    assert len(calculare_medii(lista_test)) == 4

def participanti_sub_medie(medii_participanti: list, medie_target: float) -> list:
    """
        Aceasta functie preia lista cu medii din functia
        calculare_medii() si afla care participanti au
        media sub o medie data.
    """
    participanti_ok = []
    index_participant = 1
    for medie_participant in medii_participanti:
        if medie_participant < medie_target:
            participanti_ok.append(index_participant)
        index_participant += 1
    return participanti_ok

def test_participanti_sub_medie():
    medii_test = [5.0, 6.0, 7.0, 8.0]
    medie_target_test = 6.5
    assert participanti_sub_medie(medii_test, medie_target_test) == [1,2]
    assert len(participanti_sub_medie(medii_test, medie_target_test)) == 2
    assert participanti_sub_medie([], 10) == []

def ui_participanti_sub_medie(lista_participanti: list, parametri: list):
    """
        Aceasta functie primeste parametrii de la utilizator
        si printeaza numarul de participanti care au o medie 
        a scorurilor mai mica decat o medie data.
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'medie_mai_mica_decat' are nevoie de un singur parametru!")
        medie_valida = validare_medie(parametri[0]) 
        medii_participanti = calculare_medii(lista_participanti)     
        rezultat = participanti_sub_medie(medii_participanti, medie_valida)
        print(f"Participantii care au o medie a scorurilor mai mica decat {medie_valida} sunt {rezultat}.")
    except ValueError as error:
        print(error)



def in_ordine(lista_participanti: list) -> list:
    """
        Aceasta functie sorteaza participantii in ordine
        cresc. in functie de media lor. Am optat pt 
        sortarea manuala pt a nu pierde indecsii 
        participantilor in timpul sortarii. Folosirea
        metodei sort() ar fi pierdut indecsii.
    """
    medii = calculare_medii(lista_participanti)
    lista_indici = []
    for i in range(len(medii)):
        lista_indici.append(i + 1)
    for i in range(len(medii) - 1):
        for j in range(i + 1, len(medii)):
            if medii[i] > medii[j]:
                aux_medie = medii[i]
                medii[i] = medii[j]
                medii[j] = aux_medie

                aux_index = lista_indici[i]
                lista_indici[i] = lista_indici[j]
                lista_indici[j] = aux_index
    return lista_indici          

def test_in_ordine():
    lista_test = [
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9], # media 8
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],  # media 5
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4], # media 6
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7]  # media 7
    ]
    assert in_ordine(lista_test) == [2, 3, 4, 1]

def ui_in_ordine(lista_participanti: list, parametri: list):
    try:
        if len(parametri) != 0:
            raise ValueError("Comanda 'in_ordine' nu are parametri!")
        ordonat = in_ordine(lista_participanti)
        print(f"Participantii in ordinea mediilor: {ordonat}")
    except ValueError as error:
        print(error)



def participanti_peste_medie(lista_participanti: list, medie_target: float) ->list:
    """
        Aceasta functie returneaza o lista cu participantii
        care au o medie mai mare decat un numar dat, participantii
        fiind sortati in ordine crescatoare.
    """
    participanti_sortati = in_ordine(lista_participanti)
    medii = calculare_medii(lista_participanti)
    rezultat = []
    for participant in participanti_sortati:
        medie_participant = medii[participant - 1]
        if medie_participant > medie_target:
            rezultat.append(participant)
    return rezultat

def test_participanti_peste_medie():
    """
        functie de test pt participanti_peste_medie.
    """
    lista_test = [
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9], # media 8
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],  # media 5
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4], # media 6
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7]  # media 7
    ]
    assert participanti_peste_medie(lista_test, 6.7) == [4, 1]

def ui_participanti_peste_medie(lista_participanti: list, parametri: list):
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'medie_mai_mare_decat' are un singur parametru!")
        medie_valida = validare_medie(parametri[0])
        rezultat = participanti_peste_medie(lista_participanti, medie_valida)
        print(f"Participantii care au o medie a scorurilor mai mare decat {medie_valida} sunt {rezultat} (in ordine).")     
    except ValueError as error:
        print(error)

def rulare_toate_testele():
    """
        Aceasta functie are rolul de a cuprinde
        toate functiile de tip test si de a rula inainte
        de functia main()
    """
    test_str_to_int()
    test_validare_scoruri()
    test_adauga_scor()
    test_validare_pozitie()
    test_insert_scor()
    test_sterge_scor()
    test_sterge_interval()
    test_inlocuieste_scor()
    test_validare_medie()
    test_calculare_medii()
    test_participanti_sub_medie()
    test_in_ordine()
    test_participanti_peste_medie()

def print_list(lista_participanti, b):
    print(lista_participanti) # o functie pt printarea listei

def main():
    """
        Functia in care ruleaza codul.
    """
    lista_participanti = [
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9], # media 8
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],  # media 5
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4], # media 6
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7]  # media 7
    ] # lista de liste cu scorurile participantilor
    comenzi = {
        "list": print_list,
        "add": ui_adauga_scor,
        "insert": ui_insert_scor,
        "sterge": ui_sterge_scor,
        "sterge_interval": ui_sterge_interval,
        "inlocuieste_scor": ui_inlocuieste_scor,
        "medie_mai_mica_decat": ui_participanti_sub_medie,
        "in_ordine": ui_in_ordine,
        "medie_mai_mare_decat": ui_participanti_peste_medie
    }
    while True:
        text_comanda = input(">>>")
        text_comanda = text_comanda.strip() # sterg caracterele albe inutile
        if text_comanda == '':
            continue
        if text_comanda == 'exit':
            print("Bye!")
            return
        parti_comanda = text_comanda.split(' ')
        nume_comanda = parti_comanda[0]
        parametri = parti_comanda[1:]
        if nume_comanda in comenzi:
            comenzi[nume_comanda](lista_participanti, parametri)
        else:
            print("Comanda invalida!")

rulare_toate_testele()
main()