# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour

from ..utils import (
    COMMAND,
    EXITED,
    FAILED,
    NOTICE,
    QUESTION,
    SUCCESSFULLY,
    print_notice
)

# Pre-run.
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def loki_discovery():
        try: # Launches the probe.
            print(f"\n{QUESTION} What directory would you like to probe?")
            dir_probe = input(f"{COMMAND}")
            os.system(f"cp src/modules/loki_discovery_probe.py {dir_probe}")
            os.chdir(f"{dir_probe}")
            os.system(f"cd {dir_probe}")
            os.system(f"python3 {dir_probe}/loki_discovery_probe.py")
            os.system("rm loki_discovery_probe.py")
            print(f"\n{EXITED} {NOTICE} {SUCCESSFULLY}\n")


# Error handling.
        except KeyboardInterrupt:
            print(f"\n{EXITED} {NOTICE} {FAILED}\n")
            print_notice('You interrupted the program.\n')
            try:
                sys.exit(0) # Attempts to exit.
            except SystemExit:
                os._exit(0) # Attempts to exit.
        except ValueError:
            print(f"\n{EXITED} {NOTICE} {FAILED}\n")
            print_notice('You entered invalid data into a field.\n')
            try:
                sys.exit(0) # Attempts to exit.
            except SystemExit:
                os._exit(0) # Attempts to exit.
