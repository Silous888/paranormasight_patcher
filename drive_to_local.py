"""Module providing function to write Google sheets texts in local text files"""
# from API import google_sheet_api
# from API import google_drive_api

import utils
import googleSheetAPI

HAZY_SCRIPT_DRIVE = "1hOkZotQQ_5-W3C4KY2lxLtdouIUjiloG"

CREDIT_DRIVE = "1T-paeQY2RIRX5imkFFnHP6sSfyBcw9uY4Wg9rYfg7CI"

HAZY_LOCALIZATION_DRIVE = "1KCjqV9Gkcsyhy3OmCZgt02W8lH0QlKI9g9r0O3xWLbE"


TOOL_FOLDER = ".\\tool_paranormasight"

TEXTS_FOLDER = TOOL_FOLDER + "\\texts\\zh_Hans"


progression_actuelle: int = 0


def replace_text_in_hazy(instance_worker):
    """replace text in hazy script

    Args:
        instance_worker (_type_): _description_
    """
    first_sheet_not_yet: bool = True
    for i in range(len(utils.files_names)):
        sheet = utils.files_names[i]
        if instance_worker.liste_choix_fichiers[i]:
            incrementer_progression(instance_worker)
            update_texte_progression(instance_worker, sheet)
            list_value_sheet = googleSheetAPI.get_matrice_sheet(sheet)
            with open(TEXTS_FOLDER + "\\Hazy_Script.txt", 'r', encoding='utf-8') as file:
                lines = file.readlines()

            with open(TEXTS_FOLDER + "\\Hazy_Script.txt", 'w', encoding='utf-8') as file:
                found_id = False
                len_text_replaced = 0
                # print(lines[0])
                for line in lines:
                    line = line.rstrip()
                    if len_text_replaced > 0:
                        len_text_replaced -= 1
                        continue
                    if ',' in line:
                        id_, text = line.split(',', 1)
                        if found_id:
                            print("ça traduit " + sheet)
                            for new_text in list_value_sheet[2:]:
                                if len(new_text) >= 5:
                                    file.write(f"{new_text[0]},{new_text[4]}\n")
                                else:
                                    file.write(f"{new_text[0]},{new_text[2]}\n")
                            found_id = False
                            len_text_replaced = len(list_value_sheet[3:])
                            continue
                        if id_ == list_value_sheet[1][0] or (list_value_sheet[1][0] == "a0_010_0001" and first_sheet_not_yet):
                            first_sheet_not_yet = False
                            found_id = True
                            if len(list_value_sheet[1]) >= 5:
                                file.write(f"{list_value_sheet[1][0]},{list_value_sheet[1][4]}\n")
                            else:
                                file.write(f"{list_value_sheet[1][0]},{list_value_sheet[1][2]}\n")
                        else:
                            file.write(line + '\n')
                    else:
                        file.write(line + '\n')


def replace_text_in_hazy_localization(instance_worker):
    sheet = "Hazy_Localization"
    update_texte_progression(instance_worker, sheet)
    list_value_sheet = googleSheetAPI.get_matrice_sheet(sheet)
    with open(TEXTS_FOLDER + "\\Hazy_Localization.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(TEXTS_FOLDER + "\\Hazy_Localization.txt", 'w', encoding='utf-8') as file:
        found_id = False
        len_text_replaced = 0
        for line in lines:
            line = line.rstrip()
            if len_text_replaced > 0:
                len_text_replaced -= 1
                continue
            if ',' in line:
                id_, text = line.split(',', 1)
                if found_id:
                    for new_text in list_value_sheet[2:]:
                        if len(new_text) >= 4:
                            file.write(f"{new_text[0]},{new_text[3]}\n")
                        else:
                            file.write(f"{new_text[0]},{new_text[1]}\n")
                    found_id = False
                    len_text_replaced = len(list_value_sheet[3:])
                    continue
                if id_ == list_value_sheet[1][0]:
                    found_id = True
                    if len(list_value_sheet[1]) >= 4:
                        file.write(f"{list_value_sheet[1][0]},{list_value_sheet[1][3]}\n")
                    else:
                        file.write(f"{list_value_sheet[1][0]},{list_value_sheet[1][1]}\n")
                else:
                    file.write(line + '\n')
            else:
                file.write(line + '\n')


def incrementer_progression(instance_worker, valeur=1):
    """incrémente la barre de progression

    Args:
        instance_worker (worker): sert à accéder à la barre de progression
        valeur (int, optional): de combien on incrémente. Defaults to 1.
    """
    global progression_actuelle
    progression_actuelle = progression_actuelle + valeur
    instance_worker.set_value_progressbar(
        utils.get_valeur_progression(progression_actuelle, utils.total_progress)
    )


def update_texte_progression(instance_worker, message):
    """change le texte de progression

    Args:
        instance_worker (worker): sert à accéder à au label du texte
        message (str): texte à afficher
    """
    instance_worker.set_text_progress(message)
