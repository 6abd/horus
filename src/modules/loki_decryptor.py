# Imports.
import sys
import os
from pathlib import Path
from cryptography.fernet import Fernet

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Recursive Path Traversal.
def findFiles(path):
    files = []
    for f in os.listdir(path):
        new_path = f"{path}/{f}"
        # Is Directory.
        if os.path.isdir(new_path):
            # Recursion
            files += findFiles(new_path)
        # Is File.
        else:
            # Add file to list.
            files.append(new_path)
    return files

# Encrypt/Decrypt handler.
def handleFile(filePath, key, action):
    with open(filePath, "rb") as file:
        contents = file.read()

    if action.lower() == "e":
        contents = Fernet(key).encrypt(contents)
        message = "Encrypted"
    elif action.lower() == "d":
        contents = Fernet(key).decrypt(contents)
        message = "Decrypted"
    else:
        print(f"{action} is not a valid file action")
        return

    with open(filePath, "wb") as file:
        file.write(contents)
        print(message, "|", filePath)

# Functions.
def decrypt(files):
    # Get the key.
    with open("loki.key", "rb") as loki_key:
        key = loki_key.read()

    # decrypt files.
    for path in files:
        # Skip self.
        if '.py' in path:
            continue
        # Skip key.
        if 'loki.key' in path:
            continue
        
        # Handle file.
        handleFile(path, key, "d")

        # Rename.
        new_path = path
        ext = '.loki'
        # if end of path is ext and the whole filename isn't the ext.
        if path[-len(ext):] == ext and path.split('/')[-1] != ext:
            new_path = new_path[:-len(ext)]
        # Do the actual renaming
        os.rename(path, new_path)

def loki_decryptor():
    # Find files in current dir, and sub dirs.
    files = findFiles(".")
    decrypt(files)
    return

if __name__ == '__main__':
    loki_decryptor()