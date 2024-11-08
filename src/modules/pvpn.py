# Imports.
import subprocess
import os
import sys

from ..utils import (
    COMMAND,
    PROMPT,
    print_notice
)

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def pvpn():
    # Prompt for option.
    print_notice("What would you like to do? [Config, Connect, Tor]")
    option = input(f"{COMMAND}").lower()

    # Config.
    if option == "config":
        # Obtain username and login
        user = input(f"{PROMPT} Enter your ProtonVPN username: ")
        subprocess.Popen(f"protonvpn-cli login {user}", shell=True).wait()

    # Connect.
    elif option == "connect":
        subprocess.Popen("protonvpn-cli c -r", shell=True).wait()

    # Tor.
    elif option == "tor":
        subprocess.Popen("protonvpn-cli c --tor", shell=True).wait()

if __name__ == '__main__':
    pvpn()
