import subprocess


TOOL_PATH = ".\\tool_paranormasight"
EXE_TOOL = "ParanormasightChsLocalizationHelper.exe"


def create_game_assets():
    """create game assets with new data

    """
    shell_command = [
        EXE_TOOL
    ]
    subprocess.run(shell_command, shell=True, cwd=TOOL_PATH)
