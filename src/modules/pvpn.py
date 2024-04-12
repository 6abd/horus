# Imports.
import subprocess
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import src.modules.prints as prints

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def pvpn():
    # Prompt for option.
    print(f"\n{prints.notice} What would you like to do? [Config, Connect, Tor]")
    option = input(f"{prints.command}").lower()

    # Config.
    if option == "config":
        # Obtain username and login
        user = input(f"{prints.prompt} Enter your ProtonVPN username: ")
        subprocess.Popen(f"protonvpn-cli login {user}", shell=True).wait()

    # Connect.
    elif option == "connect":
        subprocess.Popen("protonvpn-cli c -r", shell=True).wait()
        
    # Tor.
    elif option == "tor":
        subprocess.Popen("protonvpn-cli c --tor", shell=True).wait()

if __name__ == '__main__':
    pvpn()
