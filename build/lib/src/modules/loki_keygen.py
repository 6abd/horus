# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
from pathlib import Path
from cryptography.fernet import Fernet
import prints

# Pre-run.
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def loki_keygen():
    try:
        print(f"\n{prints.question} Do you want to back up your current key? [Y/n]")
        option = input(f"{prints.command}")
        key_path = './var/pipes/loki.key'
        option = option.lower()

        # Backup key
        if option == 'y':
            with open(key_path, 'r') as loki_key:
                print(f'\n{prints.prompt} Pevious key: {loki_key.read()}')
            os.system(f'cp {key_path} {key_path}.bk')

        # Generate new key
        with open(key_path, 'wb') as loki_key:
            key = Fernet.generate_key()
            loki_key.write(key)
            print(f'\n{prints.alert} New key: {key.decode("utf8")}\n')

        if option == 'n':
            print(f'\n{prints.exited} {prints.notice} {prints.successfully}\n')

# Error handling.
    except KeyboardInterrupt:
        print(f"\n{prints.exited} {prints.notice} {prints.successfully}")
        print(f'{prints.notice} You interrupted the program.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ValueError:
        print(f"\n{prints.exited} {prints.notice} {prints.successfully}")
        print(f'{prints.notice} You entered invalid data into a field.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
