from repository.sterge_scor import sterge_scor
from repository.insereaza_scor import insert_scor

def inlocuieste_scor(lista_participanti, pozitie_participant, scoruri_noi):
    """
    Aceasta functie sterge scorul participantului de pe pozitia
    'pozitie_participant' si introduce 10 scoruri noi pe acea
    pozitie.
    :param lista_participanti: lista cu scorurile participantilor
    :param pozitie_participant: int, pozitia unde se vor inlocui
    scorurile
    :param scoruri_noi: lista cu scorurile noi
    :return: None
    """
    sterge_scor(lista_participanti, pozitie_participant)
    insert_scor(lista_participanti, pozitie_participant, scoruri_noi)