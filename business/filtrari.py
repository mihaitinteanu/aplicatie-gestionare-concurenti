from business.calcul_scor_total import calculare_scoruri_totale

def filtrare_multiplu(lista_participanti, multiplu):
    """
    Aceasta functie returneaza o lista cu participantii
    care au scorul un multiplu al unui nr dat.
    :param lista_participanti: lista cu scorurile participantilor
    :param multiplu: int, un numar primit din ui
    :return: None
    """
    lista_participanti_filtrati = []
    scoruri = calculare_scoruri_totale(lista_participanti)
    index = 0
    for scor in scoruri:
        if scor % multiplu == 0:
            lista_participanti_filtrati.append(lista_participanti[index])
        index += 1
    lista_participanti[:] = lista_participanti_filtrati

def filtrare_scor_mai_mic(lista_participanti, scor_dat):
    """
    Aceasta functie filtreaza lista de participanti in functie de
    un scor dat. Se foloseste o lista noua care retine doar
    scorurile care au un scor mai mare sau egal cu un scor
    dat si se modifica lista originala.
    :param lista_participanti: lista cu scorurile participantilor
    :param scor_dat: int, un scor dat din ui
    :return: None
    """
    scoruri = calculare_scoruri_totale(lista_participanti)
    rezultat = []
    for x in range(len(scoruri)):
        if scoruri[x] >= scor_dat:
            rezultat.append(lista_participanti[x])
    lista_participanti[:] = rezultat