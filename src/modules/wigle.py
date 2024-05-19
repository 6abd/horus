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
# Example, uncomment lines 30-32 if API required.
with open('./src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    api_name = data["wigle_name"]
    api_token = data["wigle_token"]

# Program.
def wigle():
    print(f'{notice} How would you like to query WiGle: search by Bluetooth device ID ("bluetooth") or WiFi Network BSSID ("wifi")? ')
    option = input(f'{command}').lower()

    if option == 'bluetooth':
        netid = input(f"{question} Enter the Bluetooth device ID: ")
        response = requests.get(f"https://api.wigle.net/api/v2/bluetooth/detail?netid={netid}", auth=(api_name,api_token)).json()
        for i in range(0, len(response)):
            data = response[i]
            print(f"Latitude/Longitude: ({data['trilat']}, {data['trilong']})")
            print(f"QoS (0-7): {data['qos']}")
            print(f"First Seen & Last Seen: {data['firsttime']} - {data['lasttime']}")
            print(f"Device Name: {data['name']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['region']}")
            print(f"City: {data['city']}")
            print(f"Address: {data['housenumber']} {data['road']}")
            print(f"Postal Code: {data['postalcode']}")
            print("-------------------------------------------------------------------")


    if option == 'wifi':
        netid = input(f"{question} Enter the WiFi Network BSSID: ")
        response = requests.get(f"https://api.wigle.net/api/v2/network/detail?netid={netid}", auth=(api_name,api_token)).json()
        for i in range(0, len(response)):
            data = response[i]
            print(f"Latitude/Longitude: ({data['trilat']}, {data['trilong']})")
            print(f"QoS (0-7): {data['qos']}")
            print(f"First Seen & Last Seen: {data['firsttime']} - {data['lasttime']}")
            print(f"Device Name: {data['name']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['region']}")
            print(f"City: {data['city']}")
            print(f"Address: {data['housenumber']} {data['road']}")
            print(f"Postal Code: {data['postalcode']}")
            print("-------------------------------------------------------------------")

# Run module_name module.
if __name__ == '__main__':
    wigle()
