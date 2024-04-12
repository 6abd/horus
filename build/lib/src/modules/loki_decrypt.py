# Imports.
import sys # System stuff.
import time
import os # Operating System functions.
from colorama import Fore # For text colour.

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

# Program.
def loki_decrypt():
        try:
            print(f"\n{question} What directory would you like to decrypt.\n")
            dir_encrypt = input(f"{command} ")
            os.system(f"\ncp ./src/modules/loki_decryptor.py {dir_encrypt}")
            os.system(f"cp ./var/pipes/loki.key {dir_encrypt}")
            os.chdir(f"{dir_encrypt}")
            os.system(f"cd {dir_encrypt}")
            os.system(f"python3 {dir_encrypt}/loki_decryptor.py")
            os.system("rm loki_decryptor.py")
            os.system("rm loki.key")
            print(f"\n{Fore.WHITE}-! Files {Fore.GREEN}decrypted {Fore.WHITE}!-")
            print(f"\n{exited} {notice} {successfully}\n")

# Error handling.
        except KeyboardInterrupt:
            print(f"\n{exited} {notice} {successfully}\n") # States the script ended.
            print(f'{notice} You interrupted the program.\n') # States it was interrupted.
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except ValueError:
            print(f"\n{exited} {notice} {successfully}\n")
            print(f'{notice} You entered invalid data into a field.\n')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
