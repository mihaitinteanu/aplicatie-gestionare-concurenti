def creeaza_scoruri(lista_scoruri_noi):
    """
    Aceasta functie creeaza un dictionar de 10 scoruri, in care cheia
    este nr probei si valoarea este primita prin lista_nr_intregi.
    :param lista_scoruri_noi: o lista cu 10 numere intregi
    :return: dictionar cu cele 10 scoruri
    """
    scoruri = {}
    for x in range(len(lista_scoruri_noi)):
        scoruri[x + 1] = lista_scoruri_noi[x]
    return scoruri

def get_scoruri(participant: dict) -> list:
    """
    Functie care returneaza o lista cu cele 10 scoruri ale
    unui participant preluate din dictionar.
    :param participant: dicionary cu scorurile unui participant
    :return: lista cu cele 10 scoruri
    """
    lista_scoruri = []
    for scor_participant in participant.values():
        lista_scoruri.append(scor_participant)
    return lista_scoruri
