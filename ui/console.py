from domain.scoruri import creeaza_scoruri
from utils.validari import *
from repository.inlocuieste_scor import inlocuieste_scor
from repository.adauga_scor import adauga_scor
from repository.insereaza_scor import insert_scor
from repository.sterge_scor import sterge_scor
from repository.sterge_interval import sterge_interval
from business.tipariri_participanti import *
from business.filtrari import *
from business.operatii_subset import *
from business.copiere_lista_curenta import copiaza_lista
from business.undo import undo

def print_list(lista_participanti):
    print(lista_participanti) # o functie pt printarea listei

def ui_adauga_scor(lista_participanti, parametri, istoric):
    """
    Aceasta functie preia comanda utilizatorului, o prelucreaza cu ajutorul
    creeaza_scoruri si adauga_scor si printeaza pe ecran un mesaj sau
    ridica o eroare.
    :param lista_participanti: lista care contine scorurile participantilor
    :param parametri: lista cu 10 numere int, 10 scoruri de la tastatura
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 10:
            raise ValueError("Comanda are 10 parametri! (10 scoruri)")

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        lista_scoruri_noi = validare_scoruri(parametri)
        dict_scoruri = creeaza_scoruri(lista_scoruri_noi)
        adauga_scor(lista_participanti, dict_scoruri)
        print(f"Lista curenta este: {lista_participanti}.")
    except ValueError as error:
        print(error)

def ui_insert_scor(lista_participanti, parametri, istoric):
    """
    Aceasta functie preia comanda de la utilizator, si prelucreaza
    11 parametri: pozitia scorului unde se vor insera scorurile si
    10 scoruri ale unui participant. Apeleaza functia de
    insereaza_scor si printeaza lista dupa inserare sau ridica o
    eroare.
    :param lista_participanti: lista care contine scorurile participantilor
    :param parametri: lista cu 11 numere int, o pozitie, 10 scoruri de la tastatura
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 11:
            raise ValueError("Comanda 'insert' are nevoie de o pozitie si exact 10 scoruri!")

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        pozitie = validare_pozitie(lista_participanti, parametri[0])
        scoruri_noi = validare_scoruri(parametri[1:])
        scoruri = creeaza_scoruri(scoruri_noi)
        insert_scor(lista_participanti, pozitie, scoruri)
        print(f"Lista dupa inserare este: {lista_participanti}")
    except ValueError as error:
        print(error)

def ui_sterge_scor(lista_participanti, parametri, istoric):
    """
    Functia prelucreaza comanda primita de la utilizator care are
    un singur parametru: pozitia de unde se vor sterge scorurile.
    Apeleaza functia sterge_scor din repository si printeaza un
    mesaj sau ridica o eroare.
    :param lista_participanti: lista care contine scorurile participantilor
    :param parametri: o lista cu un int
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'sterge' are nevoie doar de o pozitie!")

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        pozitie_stergere = validare_pozitie(lista_participanti, parametri[0])
        sterge_scor(lista_participanti, pozitie_stergere)
        print(f"Lista dupa stergere este: {lista_participanti}")
    except ValueError as error:
        print(error)

def ui_sterge_interval(lista_participanti, parametri, istoric):
    """
    Functia prelucreaza comanda primita de la utilizator care are 2 parametri:
    pozitia de inceput a intervalului si pozitia de sfarsit a intervalului de
    unde se vor sterge valorile. Apeleaza functia sterge_interval din repository
    si printeaza un mesaj sau ridica o eroare.
    :param lista_participanti: lista care contine scorurile participantilor
    :param parametri: o lista cu 2 int-uri, pozitiile
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'sterge_interval' are 2 parametri: pozitia de inceput si cea de sfarsit.")

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        pozitie_inceput = validare_pozitie(lista_participanti, parametri[0])
        pozitie_sfarsit = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_inceput > pozitie_sfarsit:
            raise ValueError("Pozitia de inceput trebuie sa fie mai mica sau egala cu pozitia de sfarsit!")
        sterge_interval(lista_participanti, pozitie_inceput, pozitie_sfarsit)
        print(f"Lista dupa stergere este: {lista_participanti}.")
    except ValueError as error:
        print(error)

def ui_inlocuieste_scor(lista_participanti, parametri, istoric):
    """
    Aceasta functie este apelata in main(), primeste parametrii
    de la utilizator si apeleaza functiile auxiliare pt a
    prelucra lista pe care o afiseaza la final, dupa modificari.
    Primul parametru este pozitia participantului in lista, iar
    urmatorii 10 sunt scorurile noi.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: o lista 11 int-uri, pozitia de unde se
    inlocuiesc scorurile si 10 scoruri noi
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 11:
            raise ValueError("Comanda 'inlocuieste_scor' are nevoie de 11 parametri!")

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        pozitie_participant = validare_pozitie(lista_participanti, parametri[0])
        scoruri_noi = validare_scoruri(parametri[1:])
        inlocuieste_scor(lista_participanti, pozitie_participant, scoruri_noi)
        print(f"Lista participantilor dupa modificare este: {lista_participanti}")
    except ValueError as error:
        print(error)

def ui_participanti_sub_scor(lista_participanti, parametri):
    """
    Functie care prelucreaza comanda utilizatorului, comanda avand ca
    parametru un scor dat. Apeleaza functiile calculare_scoruri_totale
    si participanti_sub_scor din business si printeaza un mesaj sau
    ridica o eroare.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: o lista cu un int, un scor dat
    :return: None
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'scor_mai_mic_decat' are nevoie de un singur parametru!")
        scor_valid = str_to_int(parametri[0])
        if scor_valid < 10 or scor_valid > 100:
            raise ValueError("Scorul dat este un numar intre 10 si 100!")
        scoruri_participanti = calculare_scoruri_totale(lista_participanti)
        rezultat = participanti_sub_scor(scoruri_participanti, scor_valid)
        print(f"Participantii care au scorurile totale mai mici decat {scor_valid} sunt {rezultat}.")
    except ValueError as error:
        print(error)

def ui_in_ordine(lista_participanti, parametri):
    """
    Functia preia comanda de la utilizator si o prelucreaza cu
    ajutorul functiei in_ordine din pachetul business. Comanda
    nu are parametri, iar functia printeaza un mesaj sau arunca
    o eroare.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: o lista, goala in acest caz
    :return: None
    """
    try:
        if len(parametri) != 0:
            raise ValueError("Comanda 'in_ordine' nu are parametri!")
        ordonat = in_ordine(lista_participanti)
        print(f"Participantii in ordinea scorurilor totale: {ordonat}")
    except ValueError as error:
        print(error)

def ui_participanti_peste_scor(lista_participanti, parametri):
    """
    Functia preia comanda de la utilizator si apeleaza functia
    participanti_peste_scor din business. Printeaza un mesaj
    sau arunca o eroare.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: o lista, contine un int cu un scor total dat
    :return: None
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'scor_mai_mare_decat' are un singur parametru!")
        scor_valid = str_to_int(parametri[0])
        if scor_valid < 10 or scor_valid > 100:
            raise ValueError("Scorul dat este un numar intre 10 si 100!")
        rezultat = participanti_peste_scor(lista_participanti, scor_valid)
        print(f"Participantii care au scorul total mai mare decat {scor_valid} sunt {rezultat} (in ordine).")
    except ValueError as error:
        print(error)

def ui_medie_interval(lista_participanti, parametri):
    """
    Functia preia comanda de la utilizator si apeleaza functia
    medie_interval din pachetul de business. Printeaza un mesaj
    sau arunca o eroare.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: o lista, cu 2 pozitii care definesc intervalul
    :return: None
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'medie_interval' are 2 parametri!")
        pozitie_start = validare_pozitie(lista_participanti, parametri[0])
        pozitie_end = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_start > pozitie_end:
            raise ValueError("Pozitia de start nu poate fi mai mare decat pozitia de sfarsit!")
        rezultat = medie_interval(lista_participanti, pozitie_start, pozitie_end)
        print(f"Media scorurilor de la {pozitie_start + 1} pana la {pozitie_end + 1} este: {rezultat}!")
    except ValueError as error:
        print(error)

def ui_minim_interval(lista_participanti, parametri):
    """
    Aceasta functie se foloseste de fctia minim_interval care calculeaza
    scorul minim dintr-o lista data. aceasta functie printeaza scorul
    minim dintr-un interval dat, validand pozitiile date cu ajutorul
    fctilor de validare din pachetul utils.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: o lista, contine 2 pozitii care definesc intervalul
    :return: None
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'minim_interval' are 2 parametri!")
        pozitie_start = validare_pozitie(lista_participanti, parametri[0])
        pozitie_end = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_start > pozitie_end:
            raise ValueError("Pozitia de start nu poate fi mai mare decat pozitia de sfarsit!")
        rezultat = minim_interval(lista_participanti, pozitie_start, pozitie_end)
        print(f"Scorul minim de la {pozitie_start + 1} pana la {pozitie_end + 1} este: {rezultat}!")
    except ValueError as error:
        print(error)

def ui_tiparire_multiplu_10(lista_participanti, parametri):
    """
        Aceasta functie se foloseste de fctia tiparire_multiplu_10 din
        pachetul business si printeaza rezultatul modificat sau arunca
        o eroare.
        :param lista_participanti: lista cu scorurile participantilor
        :param parametri: o lista, cu 2 pozitii care definesc intervalul
        :return: None
    """
    try:
        if len(parametri) != 2:
            raise ValueError("Comanda 'tiparire_multiplu' are 2 parametri!")
        pozitie_start = validare_pozitie(lista_participanti, parametri[0])
        pozitie_end = validare_pozitie(lista_participanti, parametri[1])
        if pozitie_start > pozitie_end:
            raise ValueError("Pozitia de start nu poate fi mai mare decat pozitia de sfarsit!")
        lista_multiplu = tiparire_multiplu_10(lista_participanti, pozitie_start, pozitie_end)
        print(f"Participantii care au scorul multiplu de 10 din interval sunt: {lista_multiplu}")
    except ValueError as error:
        print(error)

def ui_filtrare_multiplu(lista_participanti, parametri, istoric):
    """
    Functia preia comanda de la utilizator si o prelucreaza cu
    ajutorul validarilor din pachetul utils. Apeleaza functia
    filtrare_multiplu din business si printeaza un mesaj sau
    arunca o eroare.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: un scor dat
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'filrare_multiplu' are un parametru!")
        multiplu = str_to_int(parametri[0])

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        filtrare_multiplu(lista_participanti, multiplu)
        print(f"Lista dupa filtrare este: {lista_participanti}")
    except ValueError as error:
        print(error)


def ui_filtrare_scor_mai_mic(lista_participanti, parametri, istoric):
    """
    Aceasta functie se foloseste de fctia filtrare_scor_mai_mic care
    returneaza o lista noua cu participantii filtrati. Pentru ca
     se doreste modificarea in memorie a listei originale am
    facut slicing pe lista originala, nu am folosit metoda .copy().
    Se tipareste lista dupa modificarile facute (filtrari) sau
    se arunca o eroare.
    :param lista_participanti: lista cu scorurile participantilor
    :param parametri: un scor dat
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 1:
            raise ValueError("Comanda 'filtrare_scor_mai_mic' are un parametru!")
        scor_dat = str_to_int(parametri[0])
        if scor_dat < 10 or scor_dat > 100:
            raise ValueError("Scorul dat trebuie sa fie intre 10 si 100!")

        before = copiaza_lista(lista_participanti)
        istoric.append(before)

        filtrare_scor_mai_mic(lista_participanti, scor_dat)
        print(f"Lista participantilor dupa filtrare este: {lista_participanti}")
    except ValueError as error:
        print(error)

def ui_undo(lista_participanti, parametri, istoric):
    """
    Functia preia comanda de la utilizator si se foloseste de istoric
    si apelarea functiei undo din business pentru a printa un mesaj
    sau a arunca o eroare.
    :param lista_participanti: lista cu scorul participantilor
    :param parametri: o lista, goala in acest caz
    :param istoric: lista cu participanti inainte de modificari
    :return: None
    """
    try:
        if len(parametri) != 0:
            raise ValueError("Comanda 'undo' nu are parametri!")
        undo(lista_participanti, istoric)
        print(f"Lista participantilor dupa undo: {lista_participanti}")
    except ValueError as error:
        print(error)