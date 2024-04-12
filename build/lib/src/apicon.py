# Imports.
import os
import sys
import json
from colorama import Fore # For text colour.
import modules.prints

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

def apicon():
    confirmation = input(f"\n{prints.alert} Do you want to continue, this will overwrite previous keys [y/n]: ")
    if confirmation == "y" or confirmation == "Y":
        # Requests API keys for configuration file.
        print(f"\n{prints.notice} If you don't have an API key, just press ENTER.")
        shodan = input(f"\n{prints.question} Shodan API key: ")
        numlook = input(f"{prints.question} Numlookup API key: ")
        bankindex_i = input(f"{prints.question} iBAN API key: ")
        bankindex_ii = ("n/a")
        # bankindex_ii = input(f"{prints.question} bankindex_ii API key: ")
        virustotal = input(f"{prints.question} VirusTotal API key: ")
        WiGle = input(f"{prints.question} WiGle API key: ")
        # Don't touch this, it works for some reason.
        api_keys = {
            "update": "verified",
            "shodan": shodan,
            "numlook": numlook,
            "bankindex_i": bankindex_i,
            "bankindex_ii": bankindex_ii,
            "vt": virustotal,
            "WiGle": WiGle,
        }
        # open, not save? outputs to apicon.json and moval to var/pipes file.
        with open("apicon.json", "w") as outfile:
            json.dump(api_keys, outfile)
        os.system("mv ./apicon.json ./var/pipes/api_config.json")
        # Checks for update valid.
        with open('./var/pipes/api_config.json') as f:
            data = json.load(f)
            validity = ("update")
            if validity in data:
                print(f"\n{prints.notice} API Keys have been", api_keys[validity], f"{prints.successfully}!")
            else:
                print(f"\n{prints.alert} API Keys have not been verified successfully.")
    # Simply quits if not wanting to update.
    if confirmation == "n" or confirmation == "N":
        print(f"\n{prints.notice} Quitting program for safety reasons.")
# Run apicon.
if __name__ == '__main__':
    apicon()
