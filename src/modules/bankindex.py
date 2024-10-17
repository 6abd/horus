# Imports.
import os
import sys
import json
import requests

from ..utils import (
    QUESTION,
    SUCCESS,
    print_notice,
    print_response
)

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

    bin_num = input(f"{QUESTION} Enter a BIN/IIN number: ")

    request = requests.get(f"https://neutrinoapi.net/bin-lookup?bin-number={bin_num}", headers = {"User-ID": user, "API-Key": key}).json()

    print("")

    print_notice(f"Checking BIN/IIN number: {bin_num}")
    print_response(f"Card Brand: {request['card-brand']}")
    print_response(f"Card Category: {request['card-category']}")
    print_response(f"Card Type: {request['card-type']}")
    print_response(f"Country: {request['country']}")
    print_response(f"Commercial: {request['is-commercial']}")
    print_response(f"Prepaid: {request['is-prepaid']}")
    print_response(f"Issuer: {request['issuer']}")
    print_response(f"Validity: {request['valid']}")

    print(SUCCESS)
# Run module_name module.
if __name__ == '__main__':
    bankindex()
