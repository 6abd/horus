# Imports.
import os
import sys
import json
import requests

import shodan as shodan

from ..utils import (
    COMMAND,
    FAILED,
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
    key = data["shodan"]

# Program.
def geolock():
    # Get API and base.
    try:
        host_ip = input(f"{QUESTION} IP: ")
        # Reserve API and base.
        reserve_direct_url = ("http://ip-api.com/")
        reserve_extend_url = ("json/")
        r = requests.get(f'{reserve_direct_url}{reserve_extend_url}{host_ip}')
        r_dict = r.json()
        # Print information from API.
        print_response(f"Location: {r_dict['city']} | {r_dict['zip']}")
        print_response(f"Coordinates (Latitude | Longitude): {r_dict['lat']}|{r_dict['lon']}")
        print_response(f"ISP: {r_dict['isp']}")
        print(SUCCESS)
    except Exception as error:
        print(f"{COMMAND} {FAILED}: {error}\n")
        os._exit(0)

# Run geolock module.
if __name__ == '__main__':
    geolock()
