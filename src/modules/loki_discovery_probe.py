# Imports.
import sys
import os
from pathlib import Path
from cryptography.fernet import Fernet

from colorama import Fore # For text colour.

from ..utils import (
    print_notice,
    print_response
)

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

        print_response(f"Found file | {filePath}") # Prints when it finds an individual file.
        files.append(filePath)

    if dirs == []:
        return # No dirs

    for dirPath in dirs:
        print_notice(f"\nFound sub-dir  | {dirPath}") # Prints when it finds a sub-directory of a source.
        findFiles(dirPath)

findFiles(".") # Prints the directories, files, etc.
