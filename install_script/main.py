from utils import copy_to_output_folder

EP_LIST = [
    "Base", "EP1", "EP2", "EP3", "EP4", "EP5", "EP6", "EP7", "EP8", "EP9",
    "SP1", "SP2", "SP4", "SP5", "SP6", "SP7", "SP8"
]

def create_lighting_mod_files(installation_type, deluxe_flag=0):
    for ep in EP_LIST:
        copy_to_output_folder(installation_type, ep, deluxe_flag)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_lighting_mod_files(installation_type="ultimate")
