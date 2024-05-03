# Imports.
import shodan as shodan
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
with open('./src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["shodan"]

# Program.
def geolock():
    # Get API and base.
    try:
        host_ip = input(f"{question} IP: ")
        # Reserve API and base.
        reserve_direct_url = ("http://ip-api.com/")
        reserve_extend_url = ("json/")
        r = requests.get(f'{reserve_direct_url}{reserve_extend_url}{host_ip}')
        r_dict = r.json()
        # Print information from API.
        print(f"{prompt}","Location:", r_dict['city'], "|", r_dict['zip'])
        print(f"{prompt}","Coordinates (Latitude | Longitude):", r_dict['lat'], "|", r_dict['lon'])
        print(f"{prompt}", "ISP:", r_dict['isp'])

    except Exception as error:
        print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
        os._exit(0)

# Run geolock module.
if __name__ == '__main__':
    geolock()
