# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import whois
import dns.resolver
import nmap

# Config (Prints).
text = (f"{Fore.WHITE}") # Change the colour of text output in the client side
dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side
success = (f"\n{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] Program executed sucessfully.") # Success output.
response = (f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]")
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
def recpull():
    domain = input(f"{question} Enter domain: ")
    w = whois.whois(domain)
    print(f"\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] WHOIS:")
    try:
        print(f"{response} Registrar: {w['registrar']}")
    except:
        print(f"{notice} Registrar: Not found")
    try:
        print(f"{response} Last Updated: {w['updated_date'][0]}")
    except:
        print(f"{response} Last Updated: {w['updated_date']}")
    try:
        print(f"{response} Creation Date: {w['creation_date'][0]}")
    except:
        print(f"{response} Creation Date: {w['creation_date']}")
    try:
        print(f"{response} Expiration Date: {w['expiration_date'][0]}")
    except:
        print(f"{response} Creation Date: {w['creation_date']}")
    try:
        for i in range(len(w['name_servers'])):
            if w['name_servers'][i][0].islower():
                print(f"{response} Name Server: {w['name_servers'][i]}")
    except:
        print(f"{notice} Name Server: Not found")
    try:
        if len(w['emails']) == 1 or w['emails'] == str(w['emails']):
            print(f"{response} Email: {w['emails']}")
        else:
            for i in range(len(w['emails'])):
                print(f"{response} Email: {w['emails'][i]}")
    except:
        print(f"{notice} Email: Not found")
    print(f"{response} Organization: {w['org']}")
    print(f"{response} Name: {w['name']}")
    print(f"{response} Address: {w['address']}")
    print(f"{response} City: {w['city']}")
    print(f"{response} State: {w['state']}")
    print(f"{response} Registrant Postal Code: {w['registrant_postal_code']}")
    print(f"{response} Country: {w['country']}")

    result = dns.resolver.query(domain, 'A')
    print()
    for ipval in result:
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] DNS: {ipval.to_text()}")

    print(f"\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] MX Records:")
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            print(f"{response} " + x.to_text())
    except:
        print(f"{notice} No MX records found.")

    print(f"\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] NMAP:")
    nm = nmap.PortScanner()
    print(f"{response} Scanning via nmap...")
    nm.scan(domain)
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
    print(success)




# Run module_name module.
if __name__ == '__main__':
    recpull()
