def adauga_scor(lista_participanti: list, parametri: list):
    """
        Aceasta functie adauga efectiv la finalul
        listei de participanti scorul noului concurent.
    """
    lista_participanti.append(parametri)

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

def sterge_scor(lista_participanti: list, pozitie_stergere: int) -> list:
    """
        Aceasta functie sterge scorurile unui concurent
        de pe pozitia pozitie_stergere.
    """
    lista_participanti.pop(pozitie_stergere)
    return lista_participanti

def sterge_interval(lista_participanti: list, pozitie_inceput: int, pozitie_sfarsit: int) -> list:
    """
        Aceasta functie sterge scorurile unui concurent
        de la pozitie_inceput pana la pozitie_sfarsit.
    """
    del lista_participanti[pozitie_inceput:pozitie_sfarsit + 1]
    return lista_participanti

def inlocuieste_scor(lista_participanti: list, pozitie_participant: int, scoruri_noi: list) -> list:
    """
        Aceasta functie sterge scorul curent al concurentului
        adauga unul nou si returneaza lista modificata.
    """
    sterge_scor(lista_participanti, pozitie_participant)
    insert_scor(lista_participanti, pozitie_participant, scoruri_noi)
    return lista_participanti

def calculare_scoruri_totale(lista_participanti: list) -> list:
    """
        Aceasta functie primeste lista cu scorurile
        participantilor si returneaza o lista cu
        scorurile totale ale acestora.
    """
    lista_scoruri = []
    for x in lista_participanti:
        scor_participant = sum(x)
        lista_scoruri.append(scor_participant)
    return lista_scoruri

def participanti_sub_scor(scoruri_participanti: list, scor_target: int) -> list:
    """
        Aceasta functie preia lista cu scoruri din functia
        calculare_scoruri_totale() si afla care participanti au
        scorul sub un scor dat.
    """
    participanti_ok = []
    index_participant = 1
    for scor_participant in scoruri_participanti:
        if scor_participant < scor_target:
            participanti_ok.append(index_participant)
        index_participant += 1
    return participanti_ok

def in_ordine(lista_participanti: list) -> list:
    """
        Aceasta functie sorteaza participantii in ordine
        cresc. in functie de scorurile lor. Am optat pt
        sortarea manuala pt a nu pierde indecsii
        participantilor in timpul sortarii. Folosirea
        metodei sort() ar fi pierdut indecsii.
    """
    scoruri = calculare_scoruri_totale(lista_participanti)
    lista_indici = []
    for i in range(len(scoruri)):
        lista_indici.append(i + 1)
    for i in range(len(scoruri) - 1):
        for j in range(i + 1, len(scoruri)):
            if scoruri[i] > scoruri[j]:
                aux_scoruri = scoruri[i]
                scoruri[i] = scoruri[j]
                scoruri[j] = aux_scoruri

                aux_index = lista_indici[i]
                lista_indici[i] = lista_indici[j]
                lista_indici[j] = aux_index
    return lista_indici

def participanti_peste_scor(lista_participanti: list, scor_target: int) ->list:
    """
        Aceasta functie returneaza o lista cu participantii
        care au un scor total mai mare decat un numar dat, participantii
        fiind sortati in ordine crescatoare.
    """
    participanti_sortati = in_ordine(lista_participanti)
    scoruri = calculare_scoruri_totale(lista_participanti)
    rezultat = []
    for participant in participanti_sortati:
        scor_participant = scoruri[participant - 1]
        if scor_participant > scor_target:
            rezultat.append(participant)
    return rezultat

def filtrare_multiplu(lista_participanti: list, multiplu: int) -> list:
    """
        Aceasta functie returneaza o lista cu participantii
        care au scorul un multiplu al unui nr dat.
    """
    lista_participanti_filtrati = []
    scoruri = calculare_scoruri_totale(lista_participanti)
    index = 0
    for scor in scoruri:
        if scor % multiplu == 0:
            lista_participanti_filtrati.append(lista_participanti[index])
        index += 1
    return lista_participanti_filtrati

def medie_interval(lista_participanti: list, pozitie_start: int, pozitie_end: int) -> float:
    """
        Aceasta functie returneaza media scorurilor pt un interval dat
        folosind indecsii de pozitie primiti din ui.
    """
    scoruri_participanti = calculare_scoruri_totale(lista_participanti)
    total = 0
    for x in range(pozitie_start, pozitie_end + 1):
        total += scoruri_participanti[x]
    medie = total / (pozitie_end - pozitie_start + 1)
    return medie

def minim_interval(lista_participanti: list, pozitie_start: int, pozitie_end: int) -> int:
    """
        Aceasta functie returneaza cel mai mic scor dintr-un
        interval dat, intervalul fiind dat de indecsii de pozitie
        primiti din ui.
    """
    scoruri_participanti = calculare_scoruri_totale(lista_participanti)
    minim = scoruri_participanti[pozitie_start]
    for x in range(pozitie_start + 1, pozitie_end + 1):
        if scoruri_participanti[x] < minim:
            minim = scoruri_participanti[x]
    return minim

def tiparire_multiplu_10(lista_participanti: list, pozitie_start: int, pozitie_end: int) -> list:
    """
        Aceasta functie returneaza o list cu toti participantii care
        au scorurile un multiplu al lui 10 dintr-un interval dat.
         lista returnata contine nr de concurs ale participantilor.
    """
    participanti_ok = []
    scoruri = calculare_scoruri_totale(lista_participanti)
    for x in range(pozitie_start, pozitie_end + 1):
        if scoruri[x] % 10 == 0:
            participanti_ok.append(x + 1)
    return participanti_ok

def filtrare_scor_mai_mic(lista_participanti: list, scor_dat: int) -> list:
    """
        Aceasta functie filtreaza lista de participanti in functie de
        un scor dat, punand scorurile conform cerintei intr-o lista
        noua si returnand-o la final. sunt returnate toate scorurile
        participantilor de la toate probele (adica 10 probe).
    """
    scoruri = calculare_scoruri_totale(lista_participanti)
    rezultat = []
    for x in range(len(scoruri)):
        if scoruri[x] >= scor_dat:
            rezultat.append(lista_participanti[x])
    return rezultat