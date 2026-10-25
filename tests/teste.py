from utils.validari import str_to_int, validare_scoruri, validare_pozitie
from domain.operatii import adauga_scor, insert_scor, sterge_scor, sterge_interval, inlocuieste_scor, calculare_scoruri_totale, participanti_sub_scor, in_ordine, participanti_peste_scor, filtrare_multiplu, medie_interval, minim_interval, tiparire_multiplu_10, filtrare_scor_mai_mic

def test_str_to_int():
    assert str_to_int('2') == 2
    assert str_to_int('10') == 10
    assert str_to_int('0') == 0
    assert str_to_int('-1') == -1
    try:
        str_to_int('a')
        assert False
    except ValueError:
        pass

def test_validare_scoruri():
    # test in caz fericit
    assert validare_scoruri(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # test in cazul in care lista nu are 10 elemente
    try:
        validare_scoruri(['1', '2', '3'])
        assert False
    except ValueError:
        pass

    # test pentru valori string in cadrul listei
    try:
        validare_scoruri(['abc', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        assert False
    except ValueError:
        pass

    # test pentru valori care nu sunt intre 1 si 10
    try:
        validare_scoruri(['100', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        assert False
    except ValueError:
        pass

def test_adauga_scor():
    lista_test = []
    scoruri_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    adauga_scor(lista_test, scoruri_test)
    assert len(lista_test) == 1
    assert lista_test[0] == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    alt_scor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    adauga_scor(lista_test, alt_scor)
    assert len(lista_test) == 2
    assert lista_test[1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_validare_pozitie():
    # test pentru caz fericit
    assert validare_pozitie([[]], 1) == 0

    # test pentru o valoare de tip str
    try:
        validare_pozitie([], 'abc')
        assert False
    except ValueError:
        pass

    # test pentru o valoare care nu e in range
    try:
        validare_pozitie([], 10)
        assert False
    except ValueError:
        pass

def test_insert_scor():
    assert insert_scor([], 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    lista_test = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    insert_scor(lista_test, 0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert len(lista_test) == 2
    assert lista_test[0] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert lista_test[1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_sterge_scor():
    assert sterge_scor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 0) == []
    lista_test = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    sterge_scor(lista_test, 1)
    assert len(lista_test) == 1
    assert lista_test[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_sterge_interval():
    lista_test = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
    ]
    sterge_interval(lista_test, 1, 2)
    assert len(lista_test) == 2
    assert lista_test[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert lista_test[1] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]

def test_inlocuieste_scor():
    lista_test = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
    ]
    inlocuieste_scor(lista_test, 2, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    assert len(lista_test) == 4
    assert lista_test[2] == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

def test_calculare_scoruri_totale():
    lista_test = [
    [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
    [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
    [7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
    [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]
]
    assert calculare_scoruri_totale(lista_test) == [50, 60, 70, 80]
    assert len(calculare_scoruri_totale(lista_test)) == 4

def test_participanti_sub_scor():
    scoruri_test = [50, 60, 70, 80]
    scor_target_test = 65
    assert participanti_sub_scor(scoruri_test, scor_target_test) == [1,2]
    assert len(participanti_sub_scor(scoruri_test, scor_target_test)) == 2
    assert participanti_sub_scor([], 10) == []

def test_in_ordine():
    lista_test = [
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9], # media 8
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],  # media 5
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4], # media 6
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7]  # media 7
    ]
    assert in_ordine(lista_test) == [2, 3, 4, 1]

def test_participanti_peste_scor():
    lista_test = [
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9],
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7]
    ]
    assert participanti_peste_scor(lista_test, 67) == [4, 1]

def test_medie_interval():
    lista_test = [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]
    ]
    assert medie_interval(lista_test, 0, 1) == 55.0

def test_filtrare_multiplu():
    lista_test = [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 10]
    ]
    assert filtrare_multiplu(lista_test, 10) == [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7]
    ]

def test_minim_interval():
    lista_test = [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]
    ]
    assert minim_interval(lista_test, 0, 3) == 50

def test_tiparie_multiplu_10():
    lista_test = [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]
    ]
    assert tiparire_multiplu_10(lista_test, 0, 3) == [1, 2, 3, 4]

def test_filtrare_scor_mai_mic():
    lista_test = [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4],
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]
    ]
    assert filtrare_scor_mai_mic(lista_test, 67) == [[7, 7, 8, 6, 9, 5, 10, 4, 7, 7],
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]]

def rulare_toate_testele():
    """
        Aceasta functie are rolul de a cuprinde
        toate functiile de tip test si de a rula inainte
        de functia main()
    """
    test_str_to_int()
    test_validare_scoruri()
    test_adauga_scor()
    test_validare_pozitie()
    test_insert_scor()
    test_sterge_scor()
    test_sterge_interval()
    test_inlocuieste_scor()
    test_calculare_scoruri_totale()
    test_participanti_sub_scor()
    test_in_ordine()
    test_participanti_peste_scor()
    test_filtrare_multiplu()
    test_medie_interval()
    test_minim_interval()
    test_tiparie_multiplu_10()
    test_filtrare_scor_mai_mic()


