# Imports.
import os
import sys
import json
import requests

from ..utils import (
    COMMAND,
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
    api_name = data["wigle_name"]
    api_token = data["wigle_token"]

# Program.
def wigle():
    print_notice('How would you like to query WiGle: search by Bluetooth device ID ("bluetooth") or WiFi Network BSSID ("wifi")? ')
    option = input(f'{COMMAND}').lower()

    if option == 'bluetooth':
        netid = input(f"{QUESTION} Enter the Bluetooth device ID: ")
        response = requests.get(f"https://api.wigle.net/api/v2/bluetooth/detail?netid={netid}", auth=(api_name,api_token)).json()
        for i in range(0, len(response)):
            data = response[i]
            print_response(f"Latitude/Longitude: ({data['trilat']}, {data['trilong']})")
            print_response(f"QoS (0-7): {data['qos']}")
            print_response(f"First Seen & Last Seen: {data['firsttime']} - {data['lasttime']}")
            print_response(f"Device Name: {data['name']}")
            print_response(f"Country: {data['country']}")
            print_response(f"Region: {data['region']}")
            print_response(f"City: {data['city']}")
            print_response(f"Address: {data['housenumber']} {data['road']}")
            print_response(f"Postal Code: {data['postalcode']}")
            print("-" * 67)
        print(SUCCESS)

    if option == 'wifi':
        netid = input(f"{QUESTION} Enter the WiFi Network BSSID: ")
        response = requests.get(f"https://api.wigle.net/api/v2/network/detail?netid={netid}", auth=(api_name,api_token)).json()
        for i in range(0, len(response)):
            data = response[i]
            print_response(f"Latitude/Longitude: ({data['trilat']}, {data['trilong']})")
            print_response(f"QoS (0-7): {data['qos']}")
            print_response(f"First Seen & Last Seen: {data['firsttime']} - {data['lasttime']}")
            print_response(f"Device Name: {data['name']}")
            print_response(f"Country: {data['country']}")
            print_response(f"Region: {data['region']}")
            print_response(f"City: {data['city']}")
            print_response(f"Address: {data['housenumber']} {data['road']}")
            print_response(f"Postal Code: {data['postalcode']}")
            print("-" * 67)
        print(SUCCESS)
# Run module_name module.
if __name__ == '__main__':
    wigle()
