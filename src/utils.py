from colorama import Fore
from colorama.ansi import AnsiCodes

# Config (Prints).
TEXT = f"{Fore.WHITE}" # Change the colour of text output in the client side
DIVIDERS = f"{Fore.LIGHTRED_EX}" # Changes the [], | and : in the client side
SUCCESS = f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]" # Success output.
RESPONSE = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]"
SUCCESSFULLY = f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]" # Successfully output.
FAILED = f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]" # Failed output.
PROMPT = f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]" # Prompt output.
NOTICE = f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]" # Notice output.
QUESTION =  f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]" # Alert output.
ALERT =  f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]" # Alert output.
EXITED = f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]" # Exited output.
DISCONNECTED = f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]" # Disconnected output.
COMMAND = f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: " # Always asks for a command on a new line.


def print_command(statement: str, *values: object):
    """
    Used to print command statements with the COMMAND visual prefix.

    Args:
        statement (str): The statement to print after the COMMAND prefix.
    """
    print(f"{COMMAND} {statement}", *values)


def print_alert(statement: str, *values: object):
    """
    Used to print alert statements with the ALERT visual prefix.

    Args:
        statement (str): The statement to print after the ALERT prefix.
    """
    print(f"{ALERT} {statement}", *values)


def print_response(statement: str, *values: object):
    """
    Used to print a statement with the RESPONSE visual prefix.

    Args:
        statement (str): THe statement to print after the RESPONSE prefix.
    """
    print(f"{RESPONSE} {statement}", *values)


def print_notice(statement: str, *values: object):
    """
    Used to print a statement with the NOTICE visual prefix.

    Args:
        statement (str): THe statement to print after the NOTICE prefix.
    """
    print(f"{NOTICE} {statement}", *values)


def command(col: AnsiCodes, text: str):
    """
    Used to print the program commands and their support status

    Args:
        col (colorama.ansi.AnsiCodes): The colour of the command.
        text (str): The text of the command.
    """
    print(f"     {col}•{Fore.RESET} {text}")


def section(text):
    """
    Used to print hero section headers
    """
    print(f"{PROMPT} {Fore.LIGHTRED_EX}{text}{Fore.WHITE}")


def print_hero():
    """
    Used to print the logo of the program as well as information about what tools it has and their state of implementation
    """
    print("\n")
    print("                           -=-=-=-=-COMMANDS-=-=-=-=-")
    section("SECURITY") 
    command(Fore.RED, "Torshell | Drop into a Tor sub-shell, or connect to Tor.")
    command(Fore.GREEN,"Pvpn | Connect to a random Proton vpn.")
    command(Fore.YELLOW,"Ovpn | Connect to a specified open vpn.")
    section("ENUMERATION") 
    command(Fore.YELLOW, "Fallenflare | Bypass cloudflare.")
    command(Fore.GREEN,"Recpull | Pulls a tracert, whois, dns, mx history & namp, custom-formatted.")
    command(Fore.RED,"Anonfile | Up/download from Anonfiles.")
    command(Fore.RED,"Onionshare | Up/download from Onionshare.")
    section("OSINT") 
    command(Fore.GREEN,"Shodan | Pull Shodan information from API.")
    command(Fore.GREEN,"WiGle | Use an API for SSID/BSSIDs stat, locations, & Bluetooth data.")
    command(Fore.GREEN,"Numlook | Look up validity, carriers, names of phone numbers globally.")
    command(Fore.GREEN,"Geolock | Shodan & auxiliary API based IP tracing & tracking.")
    command(Fore.GREEN,"Bankindex | Search up BIN/IIN, Sort Codes, Cheque details, etc.")
    command(Fore.GREEN,"Mactrace | Type in an MAC address to get the vendor or device.")
    command(Fore.GREEN,"Flightinfo | Real-time data; global flights, military status, route, etc.")
    command(Fore.GREEN,"Licenseinfo | Get information from a car license plate (Currently US Only).")
    command(Fore.GREEN,"Cryptotrace | Transaction information, & crypto-wallet tracing.")
    command(Fore.RED,"Dischook | Upload or pull information from a Discord server, or webhook.")
    command(Fore.GREEN,"Ytd | Download Youtube videos, in crystal clear format.")
    command(Fore.RED,"Leverage | You can leverage a suite of tools such as; Sherlock!")
    section("CASE-GEN") ##
    command(Fore.YELLOW,"Casegenerate | Build case files from skeleton docs for later population.")
    command(Fore.RED,"Casedelete | Delete a case from the system, & it's associated Loki key.")
    section("SDB") ##########
    command(Fore.YELLOW,"Create or search through your custom horus database built in SQL.")
    section("Loki") #########
    command(Fore.GREEN,"Lokien/decrypt | En/decrypt a directory or file with Loki keys!")
    command(Fore.GREEN,"Lokigen | Generate a key for Loki to use for encryption.")
    command(Fore.YELLOW,"Lokichain | List all known Loki keys on a system, but not their directory.")
    command(Fore.GREEN,"Lokiprobe | Discover subdirectories and files of a chosen directory.")
    command(Fore.RED,"Lokivault | Access the Loki vault over terminal, move & re-arrange, etc.")
    section("FORENSICS") #####
    command(Fore.YELLOW,"Autodd | Create disc images & snapshots for later analysis, or mount one!")
    command(Fore.GREEN,"Exif | Check exif data on a file, or wipe it clean.")
    command(Fore.GREEN,"Vt | Connect to the virus-total API to scan, or screen files, links, etc.")
    command(Fore.GREEN,"Falcon | Packet analysis; sniff for your own in the terminal or use a capture file!")
    print(f"\n{NOTICE}  Remember; run `apicon` command to configure the API database.")