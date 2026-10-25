def str_to_int(text: str) -> int:
    """
        O functie care transforma un string intr-un numar intreg
        si arunca o eroare de tip ValueError daca nu se poate
    """
    try:
        return int(text)
    except ValueError:
        raise ValueError("Numarul trebuie sa fie intreg!")

def validare_scoruri(parametri: list) -> list:
    """
        Aceasta functie transforma lista cu string-uri
        intr-o lista cu numere intregi. Also, se valideaza
        datele introduse.
    """
    if len(parametri) != 10:
        raise ValueError("Lista trebuie sa contina exact 10 scoruri!")
    scoruri = []
    for x in range(len(parametri)):
        numar = str_to_int(parametri[x])
        if numar < 1 or numar > 10:
            raise ValueError("Elementele listei trebuie sa fie numere intre 1 si 10!")
        scoruri.append(numar)
    return scoruri

def validare_pozitie(lista_participanti: list, pozitie: str) -> int:
    """
        Aceasta functie transforma pozitia dintr-un
        string intr-un int si se asigura ca este
        posibila aceasta transformare, in acelasi timp
        asigurand faptul ca pozitia exista in lista.
    """
    pozitie = str_to_int(pozitie)
    if pozitie < 1 or pozitie > len(lista_participanti) + 1:
        raise ValueError(f"Pozitia trebuie sa fie intre 1 si {len(lista_participanti)}!")
    return pozitie - 1