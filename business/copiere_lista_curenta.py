def copiaza_lista(lista_participanti):
    """
    Functie care primeste lista curenta cu participantii
    si returneaza o lista noua care e o copie completa a
    acesteia.
    :param lista_participanti: lista cu scorurile participantilor
    :return: list, copie a listei cu participanti
    """
    copie = []
    for participant in lista_participanti:
        copie_scoruri = {}
        for cheie in participant:
            copie_scoruri[cheie] = participant[cheie]
        copie.append(copie_scoruri)
    return copie