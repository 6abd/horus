# Main
from asyncio import subprocess
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore

# For text colour.

# Modules
from . import apicon
# SECURITY.
# ENUMERATION.
import src.modules.recpull as recpull
# OSINT.
import src.modules.shodan as shodan
import src.modules.numlook as numlook
import src.modules.geolock as geolock
# CASE-GEN.
# SDB.
# Loki.
import src.modules.loki_keygen as loki_keygen
import src.modules.loki_discovery as loki_discovery
import src.modules.loki_encrypt as loki_encrypt
import src.modules.loki_decrypt as loki_decrypt
import src.modules.cryptotrace as cryptotrace
import src.modules.vt as vt
import src.modules.mactrace as mactrace
import src.modules.ovpn as ovpn
import src.modules.pvpn as pvpn
import src.modules.flightinfo as flightinfo
import src.modules.wigle as wigle
import src.modules.bankindex as bankindex
import src.modules.exif as exif
import src.modules.ytd as ytd
import src.modules.falcon as falcon
# FORENSICS.


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



def main_script():
        try:
            def command(col, text):
                print(f"     {col}•{Fore.RESET} {text}")
            def section(text):
                print(f"{prompt} {Fore.LIGHTRED_EX}{text}{Fore.WHITE}")
            print("\n")
            print(f"                           -=-=-=-=-COMMANDS-=-=-=-=-")
            section("SECURITY") #################
            command(Fore.RED,
                "Torshell | Drop into a Tor sub-shell, or connect to Tor.")
            command(Fore.GREEN,
                "Pvpn | Connect to a random Proton vpn.")
            command(Fore.YELLOW,
                "Ovpn | Connect to a specified open vpn.")
            section("ENUMERATION") #################
            command(Fore.YELLOW,
                "Fallenflare | Bypass cloudflare.")
            command(Fore.GREEN,
                "Recpull | Pulls a tracert, whois, dns, mx history & namp, custom-formatted.")
            command(Fore.RED,
                "Anonfile | Up/download from Anonfiles.")
            command(Fore.RED,
                "Onionshare | Up/download from Onionshare.")
            section("OSINT") #################
            command(Fore.GREEN,
                "Shodan | Pull Shodan information from API.")
            command(Fore.GREEN,
                "WiGle | Use an API for SSID/BSSIDs stat, locations, & Bluetooth data.")
            command(Fore.GREEN,
                "Numlook | Look up validity, carriers, names of phone numbers globally.")
            command(Fore.GREEN,
                "Geolock | Shodan & auxiliary API based IP tracing & tracking.")
            command(Fore.GREEN,
                "Bankindex | Search up BIN/IIN, Sort Codes, Cheque details, etc.")
            command(Fore.GREEN,
                "Mactrace | Type in an MAC address to get the vendor or device.")
            command(Fore.GREEN,
                "Flightinfo | Real-time data; global flights, military status, route, etc.")
            command(Fore.GREEN,
                "Licenseinfo | Get information from a car license plate (Currently US Only).")
            command(Fore.GREEN,
                "Cryptotrace | Transaction information, & crypto-wallet tracing.")
            command(Fore.RED,
                "Dischook | Upload or pull information from a Discord server, or webhook.")
            command(Fore.GREEN,
                "Ytd | Download Youtube videos, in crystal clear format.")
            command(Fore.RED,
                "Leverage | You can leverage a suite of tools such as; Sherlock!")
            section("CASE-GEN") ###################
            command(Fore.YELLOW,
                "Casegenerate | Build case files from skeleton docs for later population.")
            command(Fore.RED,
                "Casedelete | Delete a case from the system, & it's associated Loki key.")
            section("SDB") ###########################
            command(Fore.YELLOW,
                "Create or search through your custom horus database built in SQL.")
            section("Loki") ##########################
            command(Fore.GREEN,
                "Lokien/decrypt | En/decrypt a directory or file with Loki keys!")
            command(Fore.GREEN,
                "Lokigen | Generate a key for Loki to use for encryption.")
            command(Fore.YELLOW,
                "Lokichain | List all known Loki keys on a system, but not their directory.")
            command(Fore.GREEN,
                "Lokiprobe | Discover subdirectories and files of a chosen directory.")
            command(Fore.RED,
                "Lokivault | Access the Loki vault over terminal, move & re-arrange, etc.")
            section("FORENSICS") ######################
            command(Fore.YELLOW,
                "Autodd | Create disc images & snapshots for later analysis, or mount one!")
            command(Fore.GREEN,
                "Exif | Check exif data on a file, or wipe it clean.")
            command(Fore.GREEN,
                "Vt | Connect to the virus-total API to scan, or screen files, links, etc.")
            command(Fore.GREEN,
                "Falcon | Packet analysis; sniff for your own in the terminal or use a capture file!")
            print(f"\n{notice}  Remember; run `apicon` command to configure the API database.")

            option = input(f"{prompt} ")
            # SECURITY.
            # ENUMERATION.
            # OSINT.
            if option.lower() == "shodan":
                shodan.run_shodan()
                os._exit(0)

            if option.lower() == "numlook":
                numlook.numlook()
                os._exit(0)

            if option.lower() == "geolock":
                geolock.geolock()
                os._exit(0)

            if option.lower() == "cryptotrace":
              cryptotrace.cryptotrace()
              os._exit(0)

            if option.lower() == "vt":
              vt.vt()
              os._exit(0)

            if option.lower() == "ovpn":
                ovpn.ovpn()
                os._exit(0)

            if option.lower() == "pvpn":
              pvpn.pvpn()
              os._exit(0)

            if option.lower() == "mactrace":
              mactrace.mactrace()
              os._exit(0)

            if option.lower() == "flightinfo":
                flightinfo.flightinfo()
                os._exit(0)

            if option.lower() == "wigle":
                wigle.wigle()
                os._exit(0)

            if option.lower() == "bankindex":
                bankindex.bankindex()
                os._exit(0)

            if option.lower() == "ytd":
                ytd.ytd()
                os._exit(0)
            # CASE-GEN.
            # SDB.
            # Loki.
            # FORENSICS.

            # Loki.
            if option.lower() == "lokigen":
                loki_keygen.loki_keygen()
                os._exit(0)

            if option.lower() == "lokidiscovery":
                loki_discovery.loki_discovery()
                os._exit(0)

            if option.lower() == "lokiencrypt":
                loki_encrypt.loki_encrypt()
                os._exit(0)

            if option.lower() == "lokidecrypt":
                loki_decrypt.loki_decrypt()
                os._exit(0)
            # FORENSICS.
            # API config.
            if option.lower() == "apicon":
                apicon.apicon()
                os._exit(0)

            if option.lower() == "exif":
                exif.exif()
                os._exit(0)

            if option.lower() == "falcon":
                falcon.falcon()
                os._exit(0)

            if option.lower() == "recpull":
                recpull.recpull()
                os._exit(0)


        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
