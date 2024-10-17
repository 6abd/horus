# Imports.
import sys # System stuff.
import os # Operating System functions.

from cryptography.fernet import Fernet

from ..utils import (
    COMMAND,
    EXITED,
    NOTICE,
    PROMPT,
    QUESTION,
    SUCCESSFULLY,
    print_alert,
    print_notice
)


# Pre-run.
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def loki_keygen():
    try:
        print(f"\n{QUESTION} Do you want to back up your current key? [Y/n]")
        option = input(f"{COMMAND}")
        key_path = './src/modules/var/pipes/loki.key'
        option = option.lower()

        # Backup key
        if option == 'y':
            with open(key_path, 'r') as loki_key:
                print(f'\n{PROMPT} Previous key: {loki_key.read()}')
            os.system(f'cp {key_path} {key_path}.bk')

        # Generate new key
        with open(key_path, 'wb') as loki_key:
            key = Fernet.generate_key()
            loki_key.write(key)
            print_alert(f'New key: {key.decode("utf8")}\n')

        if option == 'n':
            print(f'\n{EXITED} {NOTICE} {SUCCESSFULLY}\n')

# Error handling.
    except KeyboardInterrupt:
        print(f"\n{EXITED} {NOTICE} {SUCCESSFULLY}")
        print_notice('You interrupted the program.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ValueError:
        print(f"\n{EXITED} {NOTICE} {SUCCESSFULLY}")
        print_notice('You entered invalid data into a field.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
    loki_keygen()
