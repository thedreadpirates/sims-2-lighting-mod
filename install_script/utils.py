import shutil
from pathlib import Path

# Sims 2 game installation folder paths

INPUT_DIR = Path.cwd().parent / "base_files"
OUTPUT_DIR = Path.cwd().parent / "output"

def _get_base_game_path(installation_type: str, deluxe_flag: int) -> Path:
    """
    Get base game path.

    :param installation: type of Sims 2 installation (Disc, Ultimate Collection, Legacy Edition)
    :param deluxe_flag: for disc installations - 0 for Non-Deluxe, 1 for Deluxe, 2 for Double Deluxe
    :return:
    """
    if installation_type == "ultimate":
        return OUTPUT_DIR / "Double Deluxe" / "Base"
    elif installation_type == "legacy":
        return OUTPUT_DIR / "Base"
    elif deluxe_flag == 1:
        return OUTPUT_DIR / "The Sims 2 Deluxe" / "Base"
    elif deluxe_flag == 2:
        return OUTPUT_DIR / "The Sims 2 Double Deluxe" / "Base"
    return OUTPUT_DIR / "The Sims 2"


def _get_ep2_path(installation_type: str, deluxe_flag: int) -> Path:
    """
    Get EP2 (Nightlife) path

    :param installation: type of Sims 2 installation (ultimate, disc, legacy)
    :param deluxe_flag: for disc installations - 0 for Non-Deluxe, 1 for Deluxe, 2 for Double Deluxe
    :return:
    """
    if installation_type == "ultimate":
        return OUTPUT_DIR / "Double Deluxe" / "EP2"
    elif installation_type == "legacy":
        return OUTPUT_DIR / "EP2"
    elif deluxe_flag == 1:
        return OUTPUT_DIR / "The Sims 2 Deluxe" / "EP2"
    elif deluxe_flag == 2:
        return OUTPUT_DIR / "The Sims 2 Double Deluxe" / "EP2"
    return OUTPUT_DIR / "The Sims 2 Nightlife"


def _get_sp4_path(installation_type: str, deluxe_flag: int) -> Path:
    """
    Get SP4 (Celebration Stuff) path

    :param installation:
    :param deluxe_flag:
    :return:
    """
    if installation_type == "ultimate":
        return OUTPUT_DIR / "Double Deluxe" / "SP4"
    elif installation_type == "legacy":
        return OUTPUT_DIR / "SP4"
    elif deluxe_flag == 2:
        return OUTPUT_DIR / "The Sims 2 Double Deluxe" / "SP4"
    return OUTPUT_DIR / "The Sims 2 Celebration! Stuff"


INPUT_FOLDER_PATHS = {
    "Base": INPUT_DIR / "Base",
    "EP1": INPUT_DIR / "EP1",
    "EP2": INPUT_DIR / "EP2",
    "EP3": INPUT_DIR / "EP3",
    "EP4": INPUT_DIR / "EP4",
    "EP5": INPUT_DIR / "EP5",
    "EP6": INPUT_DIR / "EP6",
    "EP7": INPUT_DIR / "EP7",
    "EP8": INPUT_DIR / "EP8",
    "EP9": INPUT_DIR / "EP9",
    "SP1": INPUT_DIR / "SP1",
    "SP2": INPUT_DIR / "SP2",
    "SP3": INPUT_DIR / "SP3",
    "SP4": INPUT_DIR / "SP4",
    "SP5": INPUT_DIR / "SP5",
    "SP6": INPUT_DIR / "SP6",
    "SP7": INPUT_DIR / "SP7",
    "SP8": INPUT_DIR / "SP8",
}

OUTPUT_FOLDER_PATHS = {
    "ultimate": {
        "Base": _get_base_game_path("ultimate", 0),
        "EP1": OUTPUT_DIR / "University Life" / "EP1",
        "EP2": _get_ep2_path("ultimate", 0),
        "EP3": OUTPUT_DIR / "Best for Business" / "EP3",
        "EP4": OUTPUT_DIR / "Fun with Pets" / "EP4",
        "EP5": OUTPUT_DIR / "Seasons",
        "EP6": OUTPUT_DIR / "Bon Voyage",
        "EP7": OUTPUT_DIR / "Free Time",
        "EP8": OUTPUT_DIR / "Apartment Life",
        "EP9": OUTPUT_DIR / "Fun with Pets" / "SP9",
        "SP1": OUTPUT_DIR / "Fun with Pets" / "SP1",
        "SP2": OUTPUT_DIR / "Glamour Life Stuff",
        "SP4": _get_sp4_path("ultimate", 0),
        "SP5": OUTPUT_DIR / "Best for Business" / "SP5",
        "SP6": OUTPUT_DIR / "University Life" / "SP6",
        "SP7": OUTPUT_DIR / "Best for Business" / "SP7",
        "SP8": OUTPUT_DIR / "University Life" / "SP8",
    },
    "disc": {
        "Base": _get_base_game_path("disc", 0),
        "EP1": OUTPUT_DIR / "The Sims 2 University",
        "EP2": _get_ep2_path("disc", 0),
        "EP3": OUTPUT_DIR / "The Sims 2 Open for Business",
        "EP4": OUTPUT_DIR / "The Sims 2 Pets",
        "EP5": OUTPUT_DIR / "The Sims 2 Seasons",
        "EP6": OUTPUT_DIR / "The Sims 2 Bon Voyage",
        "EP7": OUTPUT_DIR / "The Sims 2 Freetime",
        "EP8": OUTPUT_DIR / "The Sims 2 Apartment Life",
        "EP9": OUTPUT_DIR / "The Sims 2 Mansion and Garden Stuff",
        "SP1": OUTPUT_DIR / "The Sims 2 Family Fun Stuff",
        "SP2": OUTPUT_DIR / "The Sims 2 Glamour Life Stuff",
        "SP4": _get_sp4_path("disc", 0),
        "SP5": OUTPUT_DIR / "The Sims 2 H&M® Fashion Stuff",
        "SP6": OUTPUT_DIR / "The Sims 2 Teen Style Stuff",
        "SP7": OUTPUT_DIR / "The Sims 2 Kitchen & Bath Interior Design Stuff",
        "SP8": OUTPUT_DIR / "The Sims 2 IKEA® Home Stuff",
    },
    "legacy": {
        "Base": _get_base_game_path("legacy", 0),
        "EP1": OUTPUT_DIR / "EP1",
        "EP2": _get_ep2_path("legacy", 0),
        "EP3": OUTPUT_DIR / "EP3",
        "EP4": OUTPUT_DIR / "EP4",
        "EP5": OUTPUT_DIR / "EP5",
        "EP6": OUTPUT_DIR / "EP6",
        "EP7": OUTPUT_DIR / "EP7",
        "EP8": OUTPUT_DIR / "EP8",
        "EP9": OUTPUT_DIR / "EP9",
        "SP1": OUTPUT_DIR / "SP1",
        "SP2": OUTPUT_DIR / "SP2",
        "SP3": OUTPUT_DIR / "SP3",
        "SP4": _get_sp4_path("legacy", 0),
        "SP5": OUTPUT_DIR / "SP5",
        "SP6": OUTPUT_DIR / "SP6",
        "SP7": OUTPUT_DIR / "SP7",
        "SP8": OUTPUT_DIR / "SP8",
    },
}


def get_output_ep_path(installation_type, ep_flag="Base", deluxe_flag=0):
    if installation_type not in OUTPUT_FOLDER_PATHS:
        raise KeyError(f"Invalid installation type: {installation_type}")
    if ep_flag not in OUTPUT_FOLDER_PATHS.get(installation_type):
        raise ValueError(f"Invalid EP Flag: {ep_flag}")
    if installation_type == "disc":
        if ep_flag == "Base":
            ep_path = _get_base_game_path(installation_type, deluxe_flag)
        elif ep_flag == "EP2":
            ep_path = _get_ep2_path(installation_type, deluxe_flag)
        elif ep_flag == "SP4":
            ep_path = _get_sp4_path(installation_type, deluxe_flag)
        else:
            ep_path = OUTPUT_FOLDER_PATHS[installation_type][ep_flag]
    else:
        ep_path = OUTPUT_FOLDER_PATHS[installation_type][ep_flag]

    return ep_path


def get_input_ep_path(ep_flag="Base"):
    if ep_flag not in INPUT_FOLDER_PATHS:
        raise ValueError(f"Invalid EP Flag: {ep_flag}")
    return INPUT_FOLDER_PATHS[ep_flag]


def get_folder_path(
        installation_type: str, ep_flag: str = "Base",
        deluxe_flag: int = 0, input_flag=0
) -> Path:
    if input_flag:
        ep_path = get_input_ep_path(ep_flag)
    else:
        ep_path = get_output_ep_path(installation_type, ep_flag, deluxe_flag)
    folder = ep_path / "TSData" / "Res"
    return folder


def copy_to_output_folder(
    installation_type: str, ep_flag: str = "Base", deluxe_flag: int = 0
):
    src = get_folder_path(installation_type, ep_flag, input_flag=1)
    dst = get_folder_path(installation_type, ep_flag, input_flag=0)
    print(f"Copying {src} to {dst}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    src.copy(dst, preserve_metadata=True)
