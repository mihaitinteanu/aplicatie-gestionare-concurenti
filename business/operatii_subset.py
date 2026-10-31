from business.calcul_scor_total import calculare_scoruri_totale

def medie_interval(lista_participanti, pozitie_start, pozitie_end):
    """
    Aceasta functie returneaza media scorurilor pt un interval dat
    folosind indecsii de pozitie primiti din ui.
    :param lista_participanti: lista cu scorurile participantilor
    :param pozitie_start: int, pozitia de start a intervalului
    :param pozitie_end: int, pozitia de end a intervalului
    :return: float, medie
    """
    scoruri_participanti = calculare_scoruri_totale(lista_participanti)
    total = 0
    for x in range(pozitie_start, pozitie_end + 1):
        total += scoruri_participanti[x]
    medie = total / (pozitie_end - pozitie_start + 1)
    return medie

def minim_interval(lista_participanti, pozitie_start, pozitie_end):
    """
    Aceasta functie returneaza cel mai mic scor dintr-un
    interval dat, intervalul fiind dat de indecsii de pozitie
    primiti din ui.
    :param lista_participanti: lista cu scorurile participantilor
    :param pozitie_start: int, pozitia de start a intervalului
    :param pozitie_end: int, pozitia de end a intervalului
    :return: int, scorul minim din interval
    """
    scoruri_participanti = calculare_scoruri_totale(lista_participanti)
    minim = scoruri_participanti[pozitie_start]
    for x in range(pozitie_start + 1, pozitie_end + 1):
        if scoruri_participanti[x] < minim:
            minim = scoruri_participanti[x]
    return minim

def tiparire_multiplu_10(lista_participanti, pozitie_start, pozitie_end):
    """
    Aceasta functie returneaza o lista cu toti participantii care
    au scorurile un multiplu al lui 10 dintr-un interval dat.
    lista returnata contine nr de concurs ale participantilor.
    :param lista_participanti: lista cu scorurile participantilor
    :param pozitie_start: int, pozitia de start a intervalului
    :param pozitie_end: int, pozitia de end a intervalului
    :return: list, lista cu nr de concurs ale participantilor
    """
    participanti_ok = []
    scoruri = calculare_scoruri_totale(lista_participanti)
    for x in range(pozitie_start, pozitie_end + 1):
        if scoruri[x] % 10 == 0:
            participanti_ok.append(x + 1)
    return participanti_ok