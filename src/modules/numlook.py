# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import src.modules.prints as prints

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# API.
with open('./var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["numlook"]

# Program.
def numlook():
    # Get API and base.
    direct_url = ("https://api.numlookupapi.com/")
    extend_url = ("v1/validate/")
    key_raw = ("?apikey=")
    ndc = input(f"\n{prints.question} National code (+44): ")
    number = input(f"{prints.question} Number: ")
    # Get information from API.
    r = requests.get(f'{direct_url}{extend_url}{ndc}{number}{key_raw}{key}')
    r_dict = r.json()
    # Print information from API.
    print(f"{prints.prompt}","Live:", r_dict['valid'])
    print(f"{prints.prompt}","Country:", r_dict['country_name'], "|", r_dict['country_code'])
    convert = lambda inp : inp if len(inp) > 0 else "n/a"
    print(f"{prints.prompt}","Location:", convert(r_dict['location']))
    print(f"{prints.prompt}","Carrier:", r_dict['carrier'])
    print(f"{prints.prompt}","Line type:", r_dict['line_type'], "\n")
# Run numlook module.
if __name__ == '__main__':
    numlook()
