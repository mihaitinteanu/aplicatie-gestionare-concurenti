from business.calcul_scor_total import calculare_scoruri_totale

def participanti_sub_scor(scoruri_participanti, scor_valid):
    """
    Aceasta functie preia lista cu scoruri totale din functia
    calculare_scoruri_totale() si returneaza participantii
    care au un scor mai mic decat 'scor_valid'.
    :param scoruri_participanti: lista cu scorurile TOTALE ale
    participantilor
    :param scor_valid: int, un scor intre 10-100
    :return: lista cu numarul de concurs al participantilor cu
    un scor mai mic decat 'scor_valid'.
    """
    participanti_ok = []
    index_participant = 1
    for scor_participant in scoruri_participanti:
        if scor_participant < scor_valid:
            participanti_ok.append(index_participant)
        index_participant += 1
    return participanti_ok

def in_ordine(lista_participanti):
    """
    Aceasta functie sorteaza participantii in ordine
    cresc. in functie de scorurile lor. Am optat pt
    sortarea manuala pt a nu pierde indecsii
    participantilor in timpul sortarii. Folosirea
    metodei sort() ar fi pierdut indecsii.
    :param lista_participanti: lista cu scorurile participantilor
    :return: o lista cu nr de concurs ale participantilor
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

def participanti_peste_scor(lista_participanti, scor_target):
    """
    Aceasta functie returneaza o lista cu participantii
    care au un scor total mai mare decat un scor total
    dat, participantii fiind sortati in ordine crescatoare.
    :param lista_participanti: lista cu scorurile participantilor
    :param scor_target: int, un scor intre 10-100
    """
    participanti_sortati = in_ordine(lista_participanti)
    scoruri = calculare_scoruri_totale(lista_participanti)
    rezultat = []
    for participant in participanti_sortati:
        scor_participant = scoruri[participant - 1]
        if scor_participant > scor_target:
            rezultat.append(participant)
    return rezultat