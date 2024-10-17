# Imports.
import os
import sys
import json
import requests

from ..utils import (
    QUESTION,
    SUCCESS,
    print_response
)



# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# API.
with open('./src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["numlook"]

# Program.
def numlook():
    # Get API and base.
    direct_url = ("https://api.numlookupapi.com/")
    extend_url = ("v1/validate/")
    key_raw = ("?apikey=")
    ndc = input(f"\n{QUESTION} National code (+44): ")
    number = input(f"{QUESTION} Number: ")
    # Get information from API.
    r = requests.get(f'{direct_url}{extend_url}{ndc}{number}{key_raw}{key}')
    r_dict = r.json()
    # Print information from API.
    print_response(f"Live: {r_dict['valid']}")
    print_response(f"Country: {r_dict['country_name']} | {r_dict['country_code']}")
    convert = lambda inp : inp if len(inp) > 0 else "n/a"
    print_response(f"Location: {convert(r_dict['location'])}")
    print_response(f"Carrier: {r_dict['carrier']}")
    print_response(f"Line type: {r_dict['line_type']}\n")
    print(SUCCESS)
# Run numlook module.
if __name__ == '__main__':
    numlook()
