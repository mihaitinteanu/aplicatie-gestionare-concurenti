from tests.teste import *
from ui.console import *

def main():
    """
        Functia in care ruleaza aplicatia.
    """
    lista_participanti = [
        {1: 4, 2: 6, 3: 5, 4: 5, 5: 3, 6: 7, 7: 8, 8: 2, 9: 5, 10: 5},
        {1: 6, 2: 6, 3: 7, 4: 5, 5: 8, 6: 4, 7: 9, 8: 1, 9: 10, 10: 4}
    ] # lista de liste cu scorurile participantilor

    comenzi_care_modifica ={
        "add": ui_adauga_scor,
        "insert": ui_insert_scor,
        "sterge": ui_sterge_scor,
        "sterge_interval": ui_sterge_interval,
        "inlocuieste_scor": ui_inlocuieste_scor,
        "filtrare_multiplu": ui_filtrare_multiplu,
        "filtrare_scor_mai_mic": ui_filtrare_scor_mai_mic,
        "undo": ui_undo
    } # un dictionar separat pt comenzile care aduc modificari directe asupra listei de participanti

    istoric = [] # voi folosi aceasta lista pt undo

    comenzi = {
        "scor_mai_mic_decat": ui_participanti_sub_scor,
        "in_ordine": ui_in_ordine,
        "scor_mai_mare_decat": ui_participanti_peste_scor,
        "medie_interval": ui_medie_interval,
        "minim_interval": ui_minim_interval,
        "tiparire_multiplu_10": ui_tiparire_multiplu_10
    }
    while True:
        text_comanda = input(">>>")
        text_comanda = text_comanda.strip() # sterg caracterele albe inutile
        if text_comanda == '':
            continue
        if text_comanda == 'list':
            print_list(lista_participanti)
            continue
        if text_comanda == 'exit':
            print("Bye!")
            return
        parti_comanda = text_comanda.split(' ')
        nume_comanda = parti_comanda[0]
        parametri = parti_comanda[1:]
        if nume_comanda in comenzi:
            comenzi[nume_comanda](lista_participanti, parametri)
        elif nume_comanda in comenzi_care_modifica:
            comenzi_care_modifica[nume_comanda](lista_participanti, parametri, istoric)
        else:
            print("Comanda invalida!")

rulare_toate_testele()
main()