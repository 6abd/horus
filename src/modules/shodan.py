# Imports.
import shodan as shodan
import os
import sys
import json
import requests
from colorama import Fore # For text colour.

from ..utils import (
    PROMPT,
    QUESTION,
    SUCCESS,
    TEXT,
    print_notice,
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
def run_shodan():
    # Get API and base.
    direct_url = ("https://www.shodan.io/")
    extend_url = ("host/")
    key_raw = ("/raw?key=")
    # Additional API information.
    SHODAN_API_KEY = (f"{key}")
    api = shodan.Shodan(SHODAN_API_KEY)
    print("\nShodan API:")
    host_ip = input(f"{QUESTION} IP: ")
    host = api.host(f'{host_ip}')
    # Print information from API.
    print_response(f"ISP: {host.get('isp', 'n/a')}") # Get ISP.
    print_response(f"Organization: {host.get('org', 'n/a')}") # Get Org
    print_response(f"Location: {host.get('country_name', 'n/a')}, {host.get('city', 'n/a')}")
    print_response(f"Long/Lat: {host.get('longitude','n/a')} | {host.get('latitude','n/a')}") # Get Lat/Long.
    print("\nReserve API:")
    # Reserve API and base.
    reserve_direct_url = ("http://ip-api.com/")
    reserve_extend_url = ("json/")
    r = requests.get(f'{reserve_direct_url}{reserve_extend_url}{host_ip}')
    r_dict = r.json()
    # Print information from API.
    print_response(f"ISP: {r_dict['isp']}")
    print_response(f"Location: {r_dict['city']} | {r_dict['zip']}")
    # Ports check.
    print("\nPorts:")
    for item in host['data']:
        print(f"{PROMPT} {item['port']} | {item['transport']}")
        continue
    # Vuln check.
    print("\nVulns:")
    os.system(f"wget -q -O report.log {direct_url}{extend_url}{host_ip}{key_raw}{key}")
    with open('report.log') as file:
        contents = file.read()
        search_word = ("SAFE")
        if search_word in contents:
            print_notice(f' Heartbleed: {Fore.GREEN}SECURE{TEXT}\n')
        else:
            print_notice(f' Heartbleed: {Fore.RED}VULNERABLE{TEXT}\n')
    os.system("rm report.log")

    print(SUCCESS)
# Run Shodan module.
if __name__ == '__main__':
    run_shodan()
