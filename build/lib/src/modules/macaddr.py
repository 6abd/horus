# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import json

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
#with open('var/pipes/api_config.json') as f:
#    data = json.load(f)
#    #{api_name} = data["{api_name}"]

# Program.
def macaddr():
   addr = input("Enter a MAC address: ")

   r = requests.get(f"https://www.macvendorlookup.com/oui.php?mac={addr}")

   if r.status_code == 200:
       try:
           results = r.json()
       except json.decoder.JSONDecodeError:
           print(f"{failed} Address not found in database!")
       else:
           print(f"Company: {results[0]['company']}")
           print(f"Country: {results[0]['country']}")
           print(f"Address: {results[0]['addressL1']}, {results[0]['addressL3']}")
   elif r.status_code == 204:
       print(f"{failed} Address not found in database!")
   elif r.status_code == 404:
       print(f"{failed} Status Code 404: Page not found!")
   else:
       print(f"{failed} An error has occurred! Status Code: {r.status_code}")
# Run module_name module.

if __name__ == '__main__':
    macaddr()
