# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour
import src.modules.prints as prints

# Pre-run.
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def loki_discovery():
        try: # Launches the probe.
            print(f"\n{prints.question} What directory would you like to probe?")
            dir_probe = input(f"{prints.command}")
            os.system(f"cp src/modules/loki_discovery_probe.py {dir_probe}")
            os.chdir(f"{dir_probe}")
            os.system(f"cd {dir_probe}")
            os.system(f"python3 {dir_probe}/loki_discovery_probe.py")
            os.system("rm loki_discovery_probe.py")
            print(f"\n{prints.exited} {prints.notice} {prints.successfully}\n")


# Error handling.
        except KeyboardInterrupt:
            print(f"\n{prints.exited} {prints.notice} {prints.successfully}\n")
            print(f'{prints.notice} You interrupted the program.\n')
            try:
                sys.exit(0) # Attempts to exit.
            except SystemExit:
                os._exit(0) # Attempts to exit.
        except ValueError:
            print(f"\n{prints.exited} {print.snotice} {prints.successfully}\n")
            print(f'{prints.notice} You entered invalid data into a field.\n')
            try:
                sys.exit(0) # Attempts to exit.
            except SystemExit:
                os._exit(0) # Attempts to exit.
