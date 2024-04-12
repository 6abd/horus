# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.

# Config (Prints).
text = (f"{Fore.WHITE}") # Change the colour of text output in the client side 
dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side 
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

# API.
with open('var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["numlook"]

# Program.
def numlook():
    # Get API and base.
    direct_url = ("https://api.numlookupapi.com/")
    extend_url = ("v1/validate/")
    key_raw = ("?apikey=")
    ndc = input(f"\n{question} National code (+44): ")
    number = input(f"{question} Number: ")
    # Get information from API.
    r = requests.get(f'{direct_url}{extend_url}{ndc}{number}{key_raw}{key}')
    r_dict = r.json()
    # Print information from API.
    print(f"{prompt}","Live:", r_dict['valid'])
    print(f"{prompt}","Country:", r_dict['country_name'], "|", r_dict['country_code'])
    convert = lambda inp : inp if len(inp) > 0 else "n/a"
    print(f"{prompt}","Location:", convert(r_dict['location']))
    print(f"{prompt}","Carrier:", r_dict['carrier'])
    print(f"{prompt}","Line type:", r_dict['line_type'], "\n")
# Run numlook module.
if __name__ == '__main__':
    numlook()
