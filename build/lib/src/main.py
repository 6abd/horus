# Main
from asyncio import subprocess
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.



import prints


# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Modules
import apicon
# # SECURITY.
# ENUMERATION.
# OSINT.
import modules.shodan as shodan
import modules.numlook as numlook
import modules.geolock as geolock
# CASE-GEN.
# SDB.
# Loki.
import modules.loki_keygen as loki_keygen
import modules.loki_discovery as loki_discovery
import modules.loki_encrypt as loki_encrypt
import modules.loki_decrypt as loki_decrypt
# FORENSICS.

def main_script():
        try:
            def command(col, text):
                print(f"     {col}•{Fore.RESET} {text}")
            def section(text):
                print(f"{prints.prompt} {Fore.LIGHTRED_EX}{text}{Fore.WHITE}")
            print("\n")
            print(f"                           -=-=-=-=-COMMANDS-=-=-=-=-")
            section("SECURITY") #################
            command(Fore.RED,    
                "Torshell | Drop into a Tor sub-shell, or connect to Tor.")
            command(Fore.RED,    
                "Pvpn | Connect to a random Proton vpn.")
            command(Fore.RED,    
                "Ovpn | Connect to a specified open vpn.")
            section("ENUMERATION") #################
            command(Fore.YELLOW, 
                "Fallenflare | Bypass cloudflare.")
            command(Fore.RED,    
                "Recpull | Pulls a tracert, whois, dns, mx history & namp, custom-formatted.")
            command(Fore.RED,    
                "Anonfile | Up/download from Anonfiles.")
            command(Fore.RED,    
                "Onionshare | Up/download from Onionshare.")
            section("OSINT") #################
            command(Fore.GREEN, 
                "Shodan | Pull Shodan information from API.")
            command(Fore.YELLOW, 
                "WiGle | Use an API for SSID/BSSIDs stat, locations, & Bluetooth data.")
            command(Fore.GREEN, 
                "Numlook | Look up validity, carriers, names of phone numbers globally.")
            command(Fore.GREEN, 
                "Geolock | Shodan & auxiliary API based IP tracing & tracking.")
            command(Fore.RED, 
                "Bankindex | Search up BIN/IIN, Sort Codes, Cheque details, etc.")
            command(Fore.RED, 
                "Mactrace | Type in an MAC address to get the vender or device.")
            command(Fore.RED, 
                "Flightinfo | Real-time data; global flights, military status, route, etc.")
            command(Fore.RED, 
                "Licenseinfo | Get information from a car license plate.")
            command(Fore.RED, 
                "Cryptotrace | Transaction information, & crypto-wallet tracing.")
            command(Fore.RED, 
                "Dischook | Upload or pull information from a Discord server, or webhook.")
            command(Fore.RED, 
                "Ytd | Download Youtube videos, in crystal clear format.")
            command(Fore.RED, 
                "Leverage | You can leverage a suite of tools such as; Sherlock!")
            section("CASE-GEN") ###################
            command(Fore.RED, 
                "Casegenerate | Build case files from skeleton docs for later population.")
            command(Fore.RED, 
                "Casesecure | Use Loki to secure a case-file with it's associated Loki key!")
            print("         (this also prints out the check_sum & hash for validation)")
            command(Fore.RED, 
                "Casedelete | Delete a case from the system, & it's associated Loki key.")
            section("SDB") ###########################
            command(Fore.YELLOW, 
                "Create or search through your custom sentinel database built in SQL.")
            section("Loki") ##########################
            command(Fore.YELLOW, 
                "Lokien/decrypt | En/decrypt a directory or file with Loki keys!")
            command(Fore.YELLOW, 
                "Lokizip | Create zips further secured with Loki, & an optional password.")
            command(Fore.YELLOW, 
                "Lokichain | List all known Loki keys on a system, but not their directory.")
            command(Fore.YELLOW, 
                "Lokivault | Access the Loki vault over terminal, move & re-arrange, etc.")
            section("FORENSICS") ######################
            command(Fore.RED, 
                "Autodd | Create disc images & snapshots for later analysis, or mount one!")
            command(Fore.RED, 
                "Exif | Check exif data on a file, or wipe it clean.")
            command(Fore.RED, 
                "Geo | Geo-locate an IP, or exif & meta data.")
            command(Fore.RED, 
                "Vt | Connect to the virus-total API to scan, or screen files, links, etc.")
            command(Fore.RED, 
                "Netjack | Crack a capture file using Netjack!")
            print(f"\n{prints.notice}  Remember; run `apicon` command to configure the API database.")

            option = input(f"{prints.command}")
            # SECURITY.
            # ENUMERATION.
            # OSINT.
            if option == "shodan".lower():
                shodan.run_shodan()
                os._exit(0)

            if option == "numlook".lower():
                numlook.numlook()
                os._exit(0)

            if option == "geolock".lower():
                geolock.geolock()
                os._exit(0)
            # CASE-GEN.
            # SDB.
            # Loki.
            # FORENSICS.
            # API config.
            if option == "apicon" or option == "Apicon":
                apicon.apicon()
                os._exit(0)


            # Loki.
            if option == "lokigen".lower():
                loki_keygen.loki_keygen()
                os._exit(0)
                
            if option == "lokidiscovery".lower():
                loki_discovery.loki_discovery()
                os._exit(0)
                
            if option == "lokiencrypt".lower():
                loki_encrypt.loki_encrypt()
                os._exit(0)
                
            if option == "lokidecrypt".lower():
                loki_decrypt.loki_decrypt()
                os._exit(0)
            # FORENSICS.
            # API config.
            if option == "apicon".lower():
                apicon.apicon()
                os._exit(0)
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
