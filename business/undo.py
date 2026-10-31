def undo(lista_participanti, istoric):
    """
    Aceasta functie preia din ui lista de participanti curenta
    si starea inainte de modificari si modifica lista de participanti
    stergand ultima operatie facuta asupra ei.
    :param lista_participanti: lista cu scorurile participantilor
    :param istoric: lista, starea anterioara ultimei operatii efectuate
    :return: None
    """
    if len(istoric) == 0:
        raise ValueError("Nu se mai poate face 'undo'!")
    stare_anterioara = istoric.pop() # lista inainte de modificari
    lista_participanti[:] = stare_anterioara
