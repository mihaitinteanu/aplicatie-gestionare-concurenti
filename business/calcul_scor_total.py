from domain.scoruri import get_scoruri

def calculare_scoruri_totale(lista_participanti):
    """
    Aceasta functie primeste lista cu scorurile
    participantilor si returneaza o lista cu
    scorurile totale ale acestora.
    :param lista_participanti: lista cu scorurile participantilor
    :return: lista cu scorurile totale ale acestora
    """
    lista_scoruri = []
    for participant in lista_participanti:
        scor_participant = sum(get_scoruri(participant))
        lista_scoruri.append(scor_participant)
    return lista_scoruri