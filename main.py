from tests.teste import rulare_toate_testele
from ui.console import print_list, ui_adauga_scor, ui_insert_scor, ui_sterge_scor, ui_sterge_interval, ui_inlocuieste_scor, ui_participanti_sub_scor, ui_in_ordine, ui_participanti_peste_scor, ui_filtrare_multiplu, ui_medie_interval, ui_minim_interval, ui_tiparire_multiplu_10, ui_filtrare_scor_mai_mic

def main():
    """
        Functia in care ruleaza aplicatia.
    """
    lista_participanti = [
        [4, 6, 5, 5, 3, 7, 8, 2, 5, 5],  
        [6, 6, 7, 5, 8, 4, 9, 1, 10, 4], 
        [7, 7, 8, 6, 9, 5, 10, 4, 7, 7], 
        [8, 8, 9, 7, 10, 6, 8, 8, 7, 9]
    ] # lista de liste cu scorurile participantilor
    comenzi = {
        "list": print_list,
        "add": ui_adauga_scor,
        "insert": ui_insert_scor,
        "sterge": ui_sterge_scor,
        "sterge_interval": ui_sterge_interval,
        "inlocuieste_scor": ui_inlocuieste_scor,
        "scor_mai_mic_decat": ui_participanti_sub_scor,
        "in_ordine": ui_in_ordine,
        "scor_mai_mare_decat": ui_participanti_peste_scor,
        "filtrare_multiplu": ui_filtrare_multiplu,
        "medie_interval": ui_medie_interval,
        "minim_interval": ui_minim_interval,
        "tiparire_multiplu_10": ui_tiparire_multiplu_10,
        "filtrare_2": ui_filtrare_scor_mai_mic
    }
    while True:
        text_comanda = input(">>>")
        text_comanda = text_comanda.strip() # sterg caracterele albe inutile
        if text_comanda == '':
            continue
        if text_comanda == 'exit':
            print("Bye!")
            return
        parti_comanda = text_comanda.split(' ')
        nume_comanda = parti_comanda[0]
        parametri = parti_comanda[1:]
        if nume_comanda in comenzi:
            comenzi[nume_comanda](lista_participanti, parametri)
        else:
            print("Comanda invalida!")

rulare_toate_testele()
main()