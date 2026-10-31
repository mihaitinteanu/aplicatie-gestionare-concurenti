from domain.scoruri import get_scoruri
from repository.adauga_scor import adauga_scor
from repository.inlocuieste_scor import inlocuieste_scor
from repository.insereaza_scor import insert_scor
from repository.sterge_interval import sterge_interval
from repository.sterge_scor import sterge_scor
from utils.validari import *
from business.filtrari import *
from business.operatii_subset import *
from business.tipariri_participanti import *
from business.undo import undo

def test_get_scoruri():
    assert get_scoruri({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

def test_validare_pozitie():
    # test pentru caz fericit
    assert validare_pozitie([{}], '1') == 0

    # test pentru o valoare de tip str
    try:
        validare_pozitie([], 'abc')
        assert False
    except ValueError:
        pass

    # test pentru o valoare care nu e in range
    try:
        validare_pozitie([], '10')
        assert False
    except ValueError:
        pass

def test_adauga_scor():
    lista_test = []
    scoruri_test = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    adauga_scor(lista_test, scoruri_test)
    assert len(lista_test) == 1
    assert lista_test[0] == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

    alt_scor = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}
    adauga_scor(lista_test, alt_scor)
    assert len(lista_test) == 2
    assert lista_test[1] == {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}

def test_insert_scor():
    lista_test = []
    scoruri_test = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    insert_scor(lista_test, 1, scoruri_test)
    assert len(lista_test) == 1
    assert lista_test == [{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}]

    alt_scor = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}
    insert_scor(lista_test, 2, alt_scor)
    assert len(lista_test) == 2
    assert lista_test[1] == {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}

def test_sterge_scor():
    lista_test = [{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}]
    sterge_scor(lista_test, 1)
    assert len(lista_test) == 1
    assert lista_test[0] == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

def test_sterge_interval():
    lista_test = [
        {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10},
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1},
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2},
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 9}
    ]
    sterge_interval(lista_test, 1, 2)
    assert len(lista_test) == 2
    assert lista_test[0] == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    assert lista_test[1] == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 9}

def test_inlocuieste_scor():
    lista_test = [
        {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10},
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1},
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2},
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 9}
    ]
    inlocuieste_scor(lista_test, 2, {1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5, 10: 5})
    assert len(lista_test) == 4
    assert lista_test[2] == {1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5, 10: 5}

def test_calculare_scoruri_totale():
    lista_test = [
    {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
    {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
    {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
    {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
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
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
    ]
    assert in_ordine(lista_test) == [1, 2, 3, 4]

def test_participanti_peste_scor():
    lista_test = [
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9},
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7}
    ]
    assert participanti_peste_scor(lista_test, 67) == [4, 1]

def test_medie_interval():
    lista_test = [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
    ]
    assert medie_interval(lista_test, 0, 1) == 55.0

def test_minim_interval():
    lista_test = [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
    ]
    assert minim_interval(lista_test, 0, 3) == 50

def test_tiparie_multiplu_10():
    lista_test = [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
    ]
    assert tiparire_multiplu_10(lista_test, 0, 3) == [1, 2, 3, 4]

def test_filtrare_multiplu():
    lista_test = [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 10}
    ]
    filtrare_multiplu(lista_test, 10)
    assert lista_test == [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7}
    ]

def test_filtrare_scor_mai_mic():
    lista_test = [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
        {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
    ]
    filtrare_scor_mai_mic(lista_test, 67)
    assert lista_test == [{1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
        {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}]

def test_undo():
    lista_test = []
    istoric = [
        [
            {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
            {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
            {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7},
            {1: 8, 2: 8, 3: 9, 4: 7, 5: 10, 6: 6, 7: 8, 8: 8, 9: 7, 10: 9}
        ],
        [
            {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
            {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
            {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7}
        ]
    ]
    undo(lista_test, istoric)
    assert lista_test == [
            {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
            {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4},
            {1: 7, 2: 7, 3: 8, 4: 6, 5: 9, 6: 5, 7: 10, 8: 4, 9: 7, 10: 7}
        ]
    assert len(istoric) == 1

    istoric.clear()
    try:
        undo(lista_test, istoric)
        assert False
    except ValueError:
        pass

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
    test_get_scoruri()
    test_undo()

