# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.

# Config (Prints).
text = (f"{Fore.WHITE}") # Change the colour of text output in the client side
dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side
success = (f"\n{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] Program executed sucessfully.") # Success output.
successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
response = (f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]")
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

# API.
# Example, uncomment lines 30-32 if API required.
with open('./src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    user = data["bankindex_i"]
    key = data["bankindex_ii"]
# Program.
def bankindex():

    bin = input(f"{question} Enter a BIN/IIN number: ")

    request = requests.get(f"https://neutrinoapi.net/bin-lookup?bin-number={bin}", headers = {"User-ID": user, "API-Key": key}).json()

    print("")

    print(f"{notice} Checking BIN/IIN number: {bin}")

    print(f"{response} Card Brand: {request['card-brand']}")
    print(f"{response} Card Category: {request['card-category']}")
    print(f"{response} Card Type: {request['card-type']}")
    print(f"{response} Country: {request['country']}")
    print(f"{response} Commercial: {request['is-commercial']}")
    print(f"{response} Prepaid: {request['is-prepaid']}")
    print(f"{response} Issuer: {request['issuer']}")
    print(f"{response} Validity: {request['valid']}")

    print(success)
# Run module_name module.
if __name__ == '__main__':
    bankindex()
