from utils import copy_to_output_folder
import argparse

INSTALL_MODES = ["ultimate", "legacy", "disc"]

EP_LIST = [
    "Base", "EP1", "EP2", "EP3", "EP4", "EP5", "EP6", "EP7", "EP8", "EP9",
    "SP1", "SP2", "SP4", "SP5", "SP6", "SP7", "SP8"
]

def create_lighting_mod_files(installation_type, deluxe_flag=0):
    for ep in EP_LIST:
        copy_to_output_folder(installation_type, ep, deluxe_flag)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--installation-type", choices=["ultimate", "disc", "legacy", "all"], help="Sims 2 installation type (UC, Legacy, or Disk)", default="all")
    parser.add_argument("--deluxe", help="Deluxe mode (for DISC or ALL installation mode only)", action="store_true")
    parser.add_argument("--double-deluxe", help="Double Deluxe mode (for DISC or ALL installation mode only)", action="store_true")
    args = parser.parse_args()
    deluxe_flag = 0
    if args.double_deluxe:
        deluxe_flag = 2
    elif args.deluxe:
        deluxe_flag = 1

    print(f"Creating lighting mod files in {args.installation_type} mode.")
    if args.installation_type == "all":
        for mode in INSTALL_MODES:
            create_lighting_mod_files(installation_type=mode, deluxe_flag=deluxe_flag)
    else:
        create_lighting_mod_files(installation_type=args.installation_type, deluxe_flag=deluxe_flag)
