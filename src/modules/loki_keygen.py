# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
from pathlib import Path
from cryptography.fernet import Fernet

# Config (Prints).
text = (f"{Fore.WHITE}") # Change the colour of text output in the client side
dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side
success = (f"\n{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] Program executed sucessfully.") # Success output.
response = (f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]")
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
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.
def loki_keygen():
    try:
        print(f"\n{question} Do you want to back up your current key? [Y/n]")
        option = input(f"{command}")
        key_path = './src/modules/var/pipes/loki.key'
        option = option.lower()

        # Backup key
        if option == 'y':
            with open(key_path, 'r') as loki_key:
                print(f'\n{prompt} Previous key: {loki_key.read()}')
            os.system(f'cp {key_path} {key_path}.bk')

        # Generate new key
        with open(key_path, 'wb') as loki_key:
            key = Fernet.generate_key()
            loki_key.write(key)
            print(f'\n{alert} New key: {key.decode("utf8")}\n')

        if option == 'n':
            print(f'\n{exited} {notice} {successfully}\n')

# Error handling.
    except KeyboardInterrupt:
        print(f"\n{exited} {notice} {successfully}")
        print(f'{notice} You interrupted the program.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ValueError:
        print(f"\n{exited} {notice} {successfully}")
        print(f'{notice} You entered invalid data into a field.\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
    loki_keygen()
