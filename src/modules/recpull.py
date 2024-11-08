# Imports.
import os
import sys

from colorama import Fore # For text colour.
import whois
import dns.resolver
import nmap

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
#with open('var/pipes/api_config.json') as f:
#    data = json.load(f)
#    #{api_name} = data["{api_name}"]

# Program.
def recpull():
    domain = input(f"{QUESTION} Enter domain: ")
    w = whois.query(domain)
    print(f"\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] WHOIS:")

    if 'registrar' in w:
        print_response(f"Registrar: {w['registrar']}")
    else:
        print_notice("Registrar: Not found")

    if 'updated_date' in w:
        if len(w['updated_date']) >= 1:
            print_response(f"Last Updated: {w['updated_date'][0]}")
        else:
            print_response(f"Last Updated: {w['updated_date']}")
    else:
        print_notice("Last Updated: Not found")

    if 'creation_date' in w:
        if len(w['creation_date']) >= 1:
            print_response(f"Creation Date: {w['creation_date'][0]}")
        else:
            print_response(f"Creation Date: {w['creation_date']}")
    else:
        print_notice("Creation Date: Not found")

    if 'expiration_date' in w:
        if len(w['expiration_date']) >= 1:
            print_response(f"Expiration Date: {w['expiration_date'][0]}")
        else:
            print_response(f"Expiration Date: {w['expiration_date']}")
    else:
        print_response(f"Creation Date: {w['creation_date']}")

    try:
        for i in range(len(w['name_servers'])):
            if w['name_servers'][i][0].islower():
                print_response(f"Name Server: {w['name_servers'][i]}")
    except Exception:
        print_notice("Name Server: Not found")
    try:
        if len(w['emails']) == 1 or w['emails'] == str(w['emails']):
            print_response(f"Email: {w['emails']}")
        else:
            for i in range(len(w['emails'])):
                print_response(f"Email: {w['emails'][i]}")
    except Exception:
        print_notice("Email: Not found")

    print_response(f"Organization: {w['org']}")
    print_response(f"Name: {w['name']}")
    print_response(f"Address: {w['address']}")
    print_response(f"City: {w['city']}")
    print_response(f"State: {w['state']}")
    print_response(f"Registrant Postal Code: {w['registrant_postal_code']}")
    print_response(f"Country: {w['country']}")

    result = dns.resolver.query(domain, 'A')
    for ipval in result:
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] DNS: {ipval.to_text()}")

    print(f"\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] MX Records:")
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            print_response(x.to_text())
    except Exception:
        print_notice("No MX records found.")

    print(f"\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] NMAP:")
    nm = nmap.PortScanner()
    print_response("Scanning via nmap...")
    nm.scan(domain)
    for host in nm.all_hosts():
        print('-' * 52)
        print(f"Host : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print('-' * 10)
            print(f"Protocol : {proto}")

            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print(f"port : {port}\tstate : {nm[host][proto][port]['state']}")
    print(SUCCESS)




# Run module_name module.
if __name__ == '__main__':
    recpull()
