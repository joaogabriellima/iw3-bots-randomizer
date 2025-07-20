import json
import random
import zipfile
import os
import shutil

JSON_PATH = "names.json"
IWD_PATH = "{Your z_svr_bots.iwd directory}"

BOTS_TXT_NAME = "bots.txt"

def randomize_nicks(json_path, quantity=18):
    with open(json_path, "r", encoding="utf-8") as f:
        all_nicks = json.load(f)

    return random.sample(all_nicks, quantity)

def save_bots_txt(nicks, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for nick in nicks:
            f.write(nick + "\n")

def replace_bots_on_iwd(iwd_path, new_bots_txt):
    temp_zip = iwd_path + ".tmp"

    with zipfile.ZipFile(iwd_path, "r") as original:
        with zipfile.ZipFile(temp_zip, "w") as newfile:
            for item in original.infolist():
                if item.filename != BOTS_TXT_NAME:
                    newfile.writestr(item, original.read(item.filename))
            newfile.write(new_bots_txt, arcname=BOTS_TXT_NAME)

    shutil.move(temp_zip, iwd_path)

def main():
    print("Randomizing nicks...")
    nicks = randomize_nicks(JSON_PATH)

    print("Saving bots.txt...")
    save_bots_txt(nicks, BOTS_TXT_NAME)

    print("Updating z_svr_bots.iwd...")
    replace_bots_on_iwd(IWD_PATH, BOTS_TXT_NAME)

    print("Ready! Happy gaming 🍻")

if __name__ == "__main__":
    main()
