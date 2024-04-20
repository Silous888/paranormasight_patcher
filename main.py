from fileFolderUI import FileFolderUI
import utils
import drive_to_local
from API import steam_game_api
import paranormasight_tools_api

import os

# pyinstaller --onefile --name Paranormasight_Patch_Automatique --icon=./ressource/DreamteamLogo.ico main.py

utils.import_names_files()


def process(instance_worker):

    drive_to_local.replace_text_in_hazy(instance_worker)
    drive_to_local.replace_text_in_hazy_localization(instance_worker)

    # drive_to_local.replace_en_json(instance_worker)
    drive_to_local.update_texte_progression(instance_worker, "recompilation")

    paranormasight_tools_api.create_game_assets()

    output_folder = drive_to_local.TOOL_FOLDER + "\\out\\Windows\\"
    for file in os.listdir(output_folder):
        path_file = os.path.join(output_folder, file)
        steam_game_api.copy_data_in_steam_game_folder_paranormasight("PARANORMASIGHT", path_file)


# -------------------- Main code -------------------
if __name__ == "__main__":
    var = FileFolderUI()
    var.process_func = lambda: process(var.get_worker())
    var.has_progressbar = True
    var.has_lineedit = False
    var.run()
