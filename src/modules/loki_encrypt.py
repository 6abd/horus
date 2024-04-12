# Imports.
import sys # System stuff.
import time
import os # Operating System functions.
from colorama import Fore # For text colour.
import prints

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def loki_encrypt():
        try:
            print(f"\n{prints.question} What directory would you like to encrypt?")
            dir_encrypt = input(f"{prints.command}")
            os.system(f"\ncp ./src/modules/loki_encryptor.py {dir_encrypt}")
            os.system(f"cp ./var/pipes/loki.key {dir_encrypt}")
            os.chdir(f"{dir_encrypt}")
            os.system(f"cd {dir_encrypt}")
            os.system(f"python3 {dir_encrypt}/loki_encryptor.py")
            os.system("rm loki_encryptor.py")
            os.system("rm loki.key")
            print(f"\n{Fore.WHITE}-! Files {Fore.RED}encrypted {Fore.WHITE}!-")
            print(f"\n{prints.exited} {prints.notice} {prints.successfully}\n")

# Error handling.
        except KeyboardInterrupt:
            print(f"\n{prints.exited} {prints.notice} {prints.successfully}\n")
            print(f'{prints.notice} You interrupted the program.\n')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except ValueError:
            print(f"\n{prints.exited} {prints.notice} {prints.successfully}")
            print(f'\n{prints.notice} You entered invalid data into a field.\n')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except FileNotFoundError as not_found:
            print("This file is missing:" + not_found.filename)
