def sterge_interval(lista_participanti, pozitie_inceput, pozitie_sfarsit) :
    """
    Aceasta functie sterge scorurile unui concurent
    de la pozitie_inceput pana la pozitie_sfarsit.
    :param lista_participanti: lista cu scorurile participantilor
    :param pozitie_inceput: int, pozitia de unde incepe stergerea
    :param pozitie_sfarsit: int, pozitia unde se sfarseste stergerea
    :return: None
    """
    del lista_participanti[pozitie_inceput:pozitie_sfarsit + 1]