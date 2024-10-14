# Imports.
import ctypes
import glob
import multiprocessing
import os
import shutil
import signal
import subprocess
import sys
import time

from colorama import Fore  # For text colour.
from pathlib import Path

# Config (Prints).
text = (f"{Fore.WHITE}")  # Change the colour of text output in the client side
# Changes the [], | and : in the client side
dividers = (f"{Fore.LIGHTRED_EX}")
# Success output.
success = (f"\n{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] Program executed successfully.")
response = (f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]")
# Successfully output.
successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]")
# Failed output.
failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]")
prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")  # Prompt output.
notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]")  # Notice output.
question = (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]")  # Alert output.
alert = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]")  # Alert output.
# Execited output.
exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]")
# Disconnected output.
disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]")
# Always asks for a command on a new line.
command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ")

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Program.

PROC_ID = multiprocessing.Value('i', 0)
PLATFORM = sys.platform


# --------------------------------
# Helper functions
# --------------------------------
def has_dependencies_installed() -> bool:
    exec_path = shutil.which("openvpn")
    return exec_path and os.access(exec_path, os.X_OK)


def get_links_by_platform() -> (str, str, str, str):
    global PLATFORM

    openvpn = ''
    proton = ''
    nord = ''
    mullvad = ''

    if PLATFORM.startswith("linux"):
        openvpn = "https://openvpn.net/openvpn-client-for-linux/"
        nord = "https://support.nordvpn.com/hc/en-us/articles/20164827795345-Connect-to-NordVPN-using-Linux-Terminal"
        proton = "https://protonvpn.com/support/linux-openvpn/"
        mullvad = "https://mullvad.net/en/help/linux-openvpn-installation"
    elif PLATFORM == "win32":
        openvpn = "https://openvpn.net/connect-docs/installation-guide-windows.html"
        nord = "https://support.nordvpn.com/hc/en-us/articles/19749554331793-How-to-set-up-a-manual-connection-on-Windows-using-OpenVPN"
        proton = "https://protonvpn.com/support/openvpn-windows-setup/"
        mullvad = "https://mullvad.net/en/help/windows-openvpn-installation"
    elif PLATFORM == "darwin":
        openvpn = "https://openvpn.net/connect-docs/connect-for-macos.html"
        proton = "https://protonvpn.com/support/mac-vpn-setup/"
        nord = "https://support.nordvpn.com/hc/en-us/articles/19924903986961-Manual-connection-setup-with-Tunnelblick-on-macOS"
        mullvad = "https://mullvad.net/en/help/tunnelblick-mac"
    else:
        raise Exception("Unsupported platform")

    return openvpn, proton, nord, mullvad


def has_files_in_dir(directory: str, pattern: str) -> bool:
    """
    Checks if a directory contains any file that matches the given pattern
    """
    files = glob.glob(os.path.join(directory, pattern))
    return files and len(files) > 0


def list_files_in_dir(directory: str):
    """
    Lists all the files in a directory
    """
    files = glob.glob(os.path.join(directory, "*"))
    [print(file) for file in files]


def is_admin():
    try:
        admin = os.getuid() == 0
    except AttributeError:
        admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return admin
# --------------------------------


def get_windows_command_and_path(config_file_path: str) -> (list, str):
    """
    Handle Windows specific config and setup.

    The Windows method requires that the *.ovpn config file is placed inside the config directory.
    This function checks for its existence there and moves it if it does not exist.

    Args:
        config_file_path (str): The path to the OpenVPN configuration file.

    Returns:
        list: The command to execute.
        str: The path to the config directory.
    """
    command = []
    windows_path = "C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe"
    config_path = "C:\\Program Files\\OpenVPN\\config\\"
    config_file_name = config_file_path.split("\\")[-1]

    command = [windows_path, "--connect", config_file_name]
    if not has_files_in_dir(Path(config_path).resolve(), config_file_name):
        print(f"{notice} Moving config file to {config_path}")
        moved = subprocess.run(f"copy {config_file_path} {config_path + config_file_name}", shell=True, check=True)
        print(f"{response} Config file moved to {config_path}: {moved.returncode == 0}")
    else:
        print(f"{notice} Config file already exists in {config_path}. Executing...")

    return command, config_path


def connect(config_file_path: str, move=False) -> subprocess.Popen:
    """
    Call the underlying openvpn command to connect to the VPN server.

    If run on Windows, move the config file to the OpenVPN config directory to make running the program easier.

    Linux and MacOS do not need the config file to be moved.

    Args:
        config_path (str): Path to the OpenVPN configuration file.
        move (bool, optional): Move into the directory of the config file before connecting. Defaults to False.

    Returns:
        None
    """
    global PROC_ID
    global PLATFORM

    command = []

    if PLATFORM == "win32":
        command, config_path = get_windows_command_and_path(config_file_path)
    else:
        config_path = "/etc/openvpn/"
        command = ["sudo", "openvpn", "--config", config_file_path]

    if move:
        os.chdir(os.path.dirname(config_path))

    try:
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
        )

        # On Windows we're using the GUI as the CLI isn't compiled with support for compression and this breaks many
        # config files. The GUI doesn't return any data to our process so we can't read the output _but_ as the GUI
        # opens up, it should be obvious if it starts or are any issues.
        if PLATFORM == "win32":
            print(f"{response} OpenVPN initialized. Check the GUI for any errors or the taskbar for the OpenVPN GUI icon.")
            return proc

        while True:
            line = proc.stdout.readline()
            if 'Initialization Sequence Completed' in line.decode():
                print(f"{response} OpenVPN initialized")
                PROC_ID.value = proc.pid
                break
            else:
                print(line.decode().strip())

        return proc
    except subprocess.CalledProcessError as e:
        print(f"{alert} Error executing command: {e}")
    except Exception as e:
        print(f"{alert} An error occurred: {e}")


def process(config_path: str, move=False) -> (multiprocessing.Process, int):
    """
    This function is the main entry point of the program. It takes a config file path and an optional 'move' flag.

    The 'move' flag is determined by whether there are "authentication" files in the same folder as the config file. Some
    providers include the authentication and certs in the config file itself, others include them in separate files and
    then refer to those in the config file using relative paths.

    Args:
        config_path (str): The path to the OpenVPN configuration file.
        move (bool): If True, the program will change directory to the same as the config file before execution.

    Returns:
        None
    """

    global PLATFORM
    global PROC_ID

    proc_id = None
    running = True

    while running:
        try:
            if not PROC_ID.value or PROC_ID.value == 0:

                # On Windows, multiprocessing imports the main script and executes it, causing all of the intro text to display
                # again. It doesn't break anything but it looks bad and confusing.
                if PLATFORM != "win32":
                    print(f"{alert} openvpn requires admin permissions. You might be asked to enter your password")
                    proc = multiprocessing.Process(target=connect, args=(config_path, move,))
                    proc.start()
                else:
                    connect(config_path, move)
                    return None, None

                while not PROC_ID.value or PROC_ID.value == 0:
                    time.sleep(1)

                if not proc:
                    print(f"{alert} Error connecting to VPN")
                    running = False

            proc_id = PROC_ID.value
            print(f"{response} VPN is connected using process {proc_id}")
            break
        except KeyboardInterrupt:
            proc.terminate()
            running = False

            if PROC_ID and PROC_ID.value != 0:
                os.kill(PROC_ID.value, signal.SIGTERM)
            PROC_ID.value = 0

    if proc_id and proc_id != 0:
        print(f"{notice} VPN process is running as process ID {proc_id}. If you wish to stop it, run: sudo kill -9 {proc_id} or restarting the computer will end it.")

    return proc, proc_id


def ovpn():
    global PLATFORM

    openvpn, proton, nord, mullvad = get_links_by_platform()

    if not has_dependencies_installed():
        print(f"{alert} OpenVPN is required but is not installed.")
        print(f"Please install it using your package manager or by following the instructions here: {openvpn}")

    while True:
        # Prompt for option.
        print(f"\n{prompt} What would you like to do? [Connect, Config]")
        option = input(f"{command}").lower()

        if option == "connect":
            if PLATFORM == "win32" and not is_admin():
                print(f"{alert} This program does support Windows but you will need to run in Administrator Mode.")
                return

            path = input(
                f"{prompt} Enter the filepath to your OpenVPN connection profile (*.ovpn file): "
            )
            move = input(f"{prompt} Are there any auth files in the same folder as your ovpn profile? Such as a *.crt and *_userpass.txt [y/n/unsure] ").lower()

            if not path.startswith("\\") and not path.startswith("C:\\"):
                path = os.path.abspath(path)

            if move == 'unsure':
                if (
                    has_files_in_dir(Path(path).resolve(), "*.crt")
                    or has_files_in_dir(Path(path).resolve(), "*_userpass.txt")
                ):
                    move = "y"

            if Path(path).is_file():
                proc, proc_id = process(path, move == 'y')
                return proc
            else:
                print(f"{alert} Supplied config file does not exist, is not a file or is not accessible, please try again.")
        elif option == "config":
            print(f"{alert} We can't set up the OpenVPN config file for any particular provider, but here are some helpful links for how to get started:")
            print(f"\tProton VPN: {proton}")
            print(f"\tNord VPN: {nord}")
            print(f"\tMullvad: {mullvad}")
        else:
            print(f"{alert} Invalid option. Exiting.")
            return None


if __name__ == '__main__':
    ovpn()
