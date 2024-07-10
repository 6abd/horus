# Imports.
import sys
import os
from pathlib import Path
from cryptography.fernet import Fernet
from colorama import Fore # For text colour

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

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Discovery.
files = [] # Creates a files array.

def findFiles(path):
    dirs = [] # Creates a directory array.
    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}*{Fore.WHITE}] source dir |", path) # Prints when it hits a source for new sub-directories.
    for file in os.listdir(path):
        filePath = path + "/" + file
        if file == "loki.py" or file == "loki.key" or file == "loki.key.bk" or file == "loki_discovery_probe.py": # Will ignore loki.py and loki.key files.
            continue

        if os.path.isdir(filePath):
            dirs.append(filePath)
            continue

        print(f"{response} Found file |", filePath) # Prints when it finds an individual file.
        files.append(filePath)

    if dirs == []:
        return # No dirs

    for dirPath in dirs:
        print(f"\n{notice} Found sub-dir  |", dirPath) # Prints when it finds a sub-directory of a source.
        findFiles(dirPath)

findFiles(".") # Prints the directories, files, etc.
