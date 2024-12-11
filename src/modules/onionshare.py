import os
import shutil
import subprocess
import sys

from ..utils import *

PLATFORM = sys.platform


# --------------------------------
# Helper functions
# --------------------------------
def has_dependencies_installed() -> bool:
    """
    Checks if the required dependencies are installed.

    Returns:
        bool: True if all dependencies are installed AND EXECUTABLE, False otherwise.
    """
    exec_path = shutil.which("tor")
    return (exec_path and os.access(exec_path, os.X_OK)) == True


def send(config_file=None, auto_stop_seconds=None, no_autostop_sharing=None):
    files = input("Which file(s) would you like to share? ")
    args = [
        "onionshare-cli",
        files,
        "--local-only",
        f"--config {config_file}" if config_file else None,
        f"--auto-stop-timer {auto_stop_seconds}" if auto_stop_seconds else None,
        f"--no-autostop-sharing {no_autostop_sharing}" if no_autostop_sharing else None
    ]
    filtered: list[str] = list(filter(lambda x: x is not None, args))
    process = subprocess.Popen(filtered, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)

    for line in iter(process.stdout.readline, ''):
        print(line, end='')

    process.stdout.close()
    process.wait()


def receive(config_file=None, auto_stop_seconds=None):
    args = [
        "onionshare-cli",
        "--local-only",
        "--receive",
        f"--config {config_file}" if config_file else None,
        f"--auto-stop-timer {auto_stop_seconds}" if auto_stop_seconds else None
    ]

    receiving = input("Would you like to receive files, text or both (f/t/b) ")

    while receiving not in ["f", "t", "b"]:
        receiving = input(f"Sorry, {receiving} was not one of the allowed values (f, t or b)")

    if receiving == "t":
        args.append("--disable-files")
    elif receiving == "f":
        args.append("--disable-text")
    
    if receiving != "t":
        data_dir = input("Where would you like the files to be saved to? (blank for default)")
        if data_dir  != "" and data_dir is not None:
            args.append(f"--data-dir {data_dir}")
    
    filtered: list[str] = list(filter(lambda x: x is not None, args))
    print("Filtered: ", filtered)
    process = subprocess.Popen(filtered, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)

    for line in iter(process.stdout.readline, ''):
        print(line, end='')

    process.stdout.close()
    process.wait()
    


def chat(config_file=None, auto_stop_seconds=None):
    args = [
        "onionshare-cli",
        "--local-only",
        "--chat",
        f"--config {config_file}" if config_file else None,
        f"--auto-stop-timer {auto_stop_seconds}" if auto_stop_seconds else None
    ]
    filtered: list[str] = list(filter(lambda x: x is not None, args))
    process = subprocess.Popen(filtered, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
    
    for line in iter(process.stdout.readline, ''):
        print(line, end='')

    process.stdout.close()
    process.wait()
    


def onionshare(advanced=False):
    if PLATFORM == "win32":
        print_alert("Using Onionshare from the commandline is not supported on Windows. Please use the GUI which you can download from:")
        print("\t- https://onionshare.org/#download")
        print_alert("You'll also need Tor installed, which you can download from:")
        print("\t- winget install --id=TorProject.TorBrowser -e")
        print("\t- Or visit https://www.torproject.org/download/ to download directly.")
        return

    if not has_dependencies_installed():
        print("You need to have Tor installed to utilise this feature.")
        
        match PLATFORM:
            case "linux":
                print(
                    """
                    Depending on your distro, the command will something like:

                    sudo apt install tor
                    sudo pacman -S tor
                    sudo dnf install tor
                    """
                )
            case "darwin":
                print(
                    """
                    brew install tor
                    """
                )
            case _:
                print("Unknown platform")

    running = True
    config_file = None
    no_autostop_sharing = None
    auto_stop_seconds = None

    if advanced:
        config = input("Custom config file location (blank for defaults): ")
        if config and config != "":
            config_file = config

    while running:
        method = input("Are you looking to send or receive files? (send/receive/chat/q) ")

        if method == "q":
            return

        if not config_file:
            auto_stop = input("Would you like the server to stop automatically? (Y/n) ")
            if auto_stop.lower() == "y":
                auto_stop_seconds = input("How many seconds should the server run for? ")


        try:
            if method == "send":
                if not config_file:
                    no_autostop_sharing = True if input("Should the server stop after you have shared the files? (Y/n) ").lower() == 'y' else False
            
                send(config_file=config_file, no_autostop_sharing=no_autostop_sharing, auto_stop_seconds=auto_stop_seconds)
                return
            elif method == "receive":
                receive(config_file=config_file, auto_stop_seconds=auto_stop_seconds)
                return
            elif method == "chat":
                chat(config_file=config_file, auto_stop_seconds=auto_stop_seconds)
                return
            else:
                print(f"Method {method} not available or possible. Try another or exit (q)")
        except Exception as e:
            print(f"{FAILED}: {str(e)}")

if __name__ == "__main__":
    onionshare()
