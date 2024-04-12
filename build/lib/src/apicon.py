# Imports.
import os
import sys
import json
from colorama import Fore # For text colour.


# Config (Prints).
text = (f"{Fore.WHITE}") # Change the colour of text output in the client side prints.
dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side prints.
success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

def apicon():
    confirmation = input(f"\n{alert} Do you want to continue, this will overwrite previous keys [y/n]: ")
    if confirmation == "y" or confirmation == "Y":
        # Requests API keys for configuration file.
        print(f"\n{notice} If you don't have an API key, just press ENTER.")
        shodan = input(f"\n{question} Shodan API key: ")
        numlook = input(f"{question} Numlookup API key: ")
        bankindex_i = input(f"{question} iBAN API key: ")
        bankindex_ii = ("n/a")
        # bankindex_ii = input(f"{question} bankindex_ii API key: ")
        virustotal = input(f"{question} VirusTotal API key: ")
        WiGle = input(f"{question} WiGle API key: ")
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
                print(f"\n{notice} API Keys have been", api_keys[validity], f"{successfully}!")
            else:
                print(f"\n{alert} API Keys have not been verified successfully.")
    # Simply quits if not wanting to update.
    if confirmation == "n" or confirmation == "N":
        print(f"\n{notice} Quitting program for safety reasons.")
# Run apicon.
if __name__ == '__main__':
    apicon()
