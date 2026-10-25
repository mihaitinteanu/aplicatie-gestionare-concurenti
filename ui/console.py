from utils.validari import str_to_int, validare_scoruri, validare_pozitie
from domain.operatii import adauga_scor, insert_scor, sterge_scor, sterge_interval, inlocuieste_scor, calculare_scoruri_totale, participanti_sub_scor, in_ordine, participanti_peste_scor, filtrare_multiplu, medie_interval, minim_interval, tiparire_multiplu_10, filtrare_scor_mai_mic

def print_list(lista_participanti, b):
    print(lista_participanti) # o functie pt printarea listei

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

def ui_participanti_sub_scor(lista_participanti: list, parametri: list):
    """
        Aceasta functie primeste parametrii de la utilizator
        si printeaza numarul de participanti care au scorurile
        totale mai mici decat un scor dat.
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'scor_mai_mic_decat' are nevoie de un singur parametru!")
        scor_valid = str_to_int(parametri[0])
        scoruri_participanti = calculare_scoruri_totale(lista_participanti)
        rezultat = participanti_sub_scor(scoruri_participanti, scor_valid)
        print(f"Participantii care au scorurile totale mai mici decat {scor_valid} sunt {rezultat}.")
    except ValueError as error:
        print(error)

def ui_in_ordine(lista_participanti: list, parametri: list):
    """
        Aceasta functie primeste lista de participanti
        si o ordoneaza in functie de scorurile totale
        ale participantilor.
    """
    try:
        if len(parametri) != 0:
            raise ValueError("Comanda 'in_ordine' nu are parametri!")
        ordonat = in_ordine(lista_participanti)
        print(f"Participantii in ordinea scorurilor totale: {ordonat}")
    except ValueError as error:
        print(error)

def ui_participanti_peste_scor(lista_participanti: list, parametri: list):
    """
        Aceasta functie afiseaza o lista cu participantii
        care au un scor total mai mare decat un scor dat,
        in ordine.
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'scor_mai_mare_decat' are un singur parametru!")
        scor_valid = str_to_int(parametri[0])
        rezultat = participanti_peste_scor(lista_participanti, scor_valid)
        print(f"Participantii care au scorul total mai mare decat {scor_valid} sunt {rezultat} (in ordine).")
    except ValueError as error:
        print(error)

def ui_filtrare_multiplu(lista_participanti: list, parametri: list):
    """
        Aceasta functie primeste lista de participanti si o filtreaza
        in functie de parametrul primit (adica multiplul dat de utilizator)
    """
    try:
        multiplu = str_to_int(parametri[0])
        if len(parametri) != 1:
            raise ValueError("Comanda 'filtrare_multiplu' are un singur parametru!")
        rezultat = filtrare_multiplu(lista_participanti, multiplu)
        lista_participanti[:] = rezultat
        print(f"Lista dupa filtrare este: {lista_participanti}")
    except ValueError as error:
        print(error)

def ui_medie_interval(lista_participanti: list, parametri: list):
    """
        Aceasta functie primeste lista de participanti si afiseaza
        media scorurilor participantilor dintr-un interval dat de
        utilizator.
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'medie_interval' are 2 parametri!")
        pozitie_start = validare_pozitie(lista_participanti, parametri[0])
        pozitie_end = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_start > pozitie_end:
            raise ValueError("Pozitia de start nu poate fi mai mare decat pozitia de sfarsit!")
        if pozitie_end >= len(lista_participanti):
            lg = len(lista_participanti)
            raise ValueError(f"Lista are {lg} participanti!")
        rezultat = medie_interval(lista_participanti, pozitie_start, pozitie_end)
        print(f"Media scorurilor de la {pozitie_start + 1} pana la {pozitie_end + 1} este: {rezultat}!")
    except ValueError as error:
        print(error)

def ui_minim_interval(lista_participanti: list, parametri: list):
    """
        Aceasta functie se foloseste de fctia minim_interval care calculeaza
        scorul minim dintr-o lista data. aceasta functie printeaza scorul
        minim dintr-un interval dat, validand pozitiile date cu ajutorul
        fctilor de validare din pachetul utils.
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'minim_interval' are 2 parametri!")
        pozitie_start = validare_pozitie(lista_participanti, parametri[0])
        pozitie_end = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_start > pozitie_end:
            raise ValueError("Pozitia de start nu poate fi mai mare decat pozitia de sfarsit!")
        if pozitie_end >= len(lista_participanti):
            lg = len(lista_participanti)
            raise ValueError(f"Lista are {lg} participanti!")
        rezultat = minim_interval(lista_participanti, pozitie_start, pozitie_end)
        print(f"Scorul minim de la {pozitie_start + 1} pana la {pozitie_end + 1} este: {rezultat}!")
    except ValueError as error:
        print(error)

def ui_tiparire_multiplu_10(lista_participanti: list, parametri: list):
    """
        Aceasta functie se foloseste de fctia tiparire_multiplu_10 care
        pune intr-o lista totate scorurile care sunt multiplu de 10 din interval.
        Functia printeaza lista respectiva si se asigura ca nr parametrilor
        primiti din ui e corect.
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'tiparire_multiplu' are 2 parametri!")
        pozitie_start = validare_pozitie(lista_participanti, parametri[0])
        pozitie_end = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_start > pozitie_end:
            raise ValueError("Pozitia de start nu poate fi mai mare decat pozitia de sfarsit!")
        if pozitie_end >= len(lista_participanti):
            lg = len(lista_participanti)
            raise ValueError(f"Lista are {lg} participanti!")
        lista_multiplu = tiparire_multiplu_10(lista_participanti, pozitie_start, pozitie_end)
        print(f"Participantii care au scorul multiplu de 10 din interval sunt: {lista_multiplu}")
    except ValueError as error:
        print(error)

def ui_filtrare_scor_mai_mic(lista_participanti: list, parametri: list):
    """
        Aceasta functie se foloseste de fctia filtrare_scor_mai_mic care
        returneaza o lista noua cu participantii filtrati. Pentru ca
        se doreste modificarea in memorie a listei originale am
        facut slicing pe lista originala, nu am folosit metoda .copy().
        Se tipareste lista dupa modificarile facute (filtrari).
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'filtrare_scor_mai_mic' are un parametru!")
        scor_dat = str_to_int(parametri[0])
        if scor_dat < 10 or scor_dat > 100:
            raise ValueError("Scorul dat trebuie sa fie intre 10 si 100!")
        rezultat = filtrare_scor_mai_mic(lista_participanti, scor_dat)
        lista_participanti[:] = rezultat
        print(f"Lista participantilor dupa filtrare este: {lista_participanti}")
    except ValueError as error:
        print(error)