def str_to_int(text):
    """
    O functie care transforma un string intr-un numar intreg
    si arunca o eroare de tip ValueError daca nu se poate
    :param text: string
    :return: numarul intreg
    """
    try:
        return int(text)
    except ValueError:
        raise ValueError("Numarul trebuie sa fie intreg!")

def validare_scoruri(parametri):
    """
    Aceasta functie primeste o lista cu 10 scoruri si le valideaza.
    Se returneaza o lista de 10 scoruri.
    :param parametri: lista de string-uri
    :return: lista de 10 int-uri
    """
    lista_scoruri = []
    for scor in parametri:
        scor = str_to_int(scor)
        if scor < 1 or scor > 10:
            raise ValueError("Scorul trebuie sa fie un numar intre 1 si 10")
        lista_scoruri.append(scor)
    return lista_scoruri

def validare_pozitie(lista_participanti, pozitie):
    """
    Functia preia lista de participanti si o pozitie pe care o valideaza
    in functie de lungimea listei de participanti. Se returneaza pozitie - 1
    pentru ca indexarea din python incepe de la 0.
    :param lista_participanti: lista de participanti
    :param pozitie: string, o pozitie
    :return: int, pozitia validata
    """
    pozitie = str_to_int(pozitie)
    if pozitie < 1 or pozitie > len(lista_participanti) + 1:
        raise ValueError(f"Pozitia trebuie sa fie intre 1 si {len(lista_participanti)}!")
    return pozitie - 1