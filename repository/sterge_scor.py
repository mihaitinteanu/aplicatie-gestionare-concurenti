def sterge_scor(lista_participanti, pozitie_stergere):
    """
    Aceasta functie sterge scorurile unui concurent
    de pe pozitia pozitie_stergere.
    :param lista_participanti: lista cu scorurile participantilor
    :param pozitie_stergere: int, pozitia de pe care se sterg scorurile
    :return: None
    """
    lista_participanti.pop(pozitie_stergere)