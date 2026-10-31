def insert_scor(lista_participanti, pozitie_inserare, scoruri_inserare):
    """
    Aceasta functie preia parametri valizi si insereaza
    la pozitia dorita scorurile participantului.
    :param lista_participanti: lista de participanti
    :param pozitie_inserare: pozitie unde se insereaza scorurile
    :param scoruri_inserare: scorurile care se insereaza
    :return: None
    """
    lista_participanti.insert(pozitie_inserare, scoruri_inserare)