# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
from exif import Image

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
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# API.
# Example, uncomment lines 30-32 if API required.
#with open('var/pipes/api_config.json') as f:
#    data = json.load(f)
#    #{api_name} = data["{api_name}"]

# Program.
def exif():
    im = input(f"{question} Enter an image file path: ")

    with open(im, 'rb') as image_file:
        target = Image(image_file)

        if target.has_exif:
            print("")

            try:
                print(f"{response} Camera Make: {target.make}")
            except AttributeError:
                print(f"{notice} Camera Make: N/A")

            try:
                print(f"{response} Camera Model: {target.model}")
            except AttributeError:
                print(f"{notice} Camera Model: N/A")

            try:
                print(f"{response} Lens: {target.lens_model}")
            except AttributeError:
                print(f"{notice} Lens: N/A")

            try:
                print(f"{response} Focal Length: {target.focal_length}")
            except AttributeError:
                print(f"{notice} Focal Length: N/A")

            try:
                print(f"{response} Aperture: {round(target.aperture_value, 2)}")
            except AttributeError:
                print(f"{notice} Aperture: N/A")

            try:
                print(f"{response} ISO Speed: {target.iso_speed}")
            except AttributeError:
                print(f"{notice} ISO Speed: N/A")

            try:
                print(f"{response} Flash: {target.flash[0]}")
            except AttributeError:
                print(f"{notice} Flash: N/A")

            print("")

            try:
                if target.gps_altitude_ref == 0:
                    print(f"{response} Altitude: {round(target.gps_altitude, 2)} meters above sea level")
                else:
                    print(f"{response} Altitude: {round(target.gps_altitude, 2)} meters below sea level")
            except AttributeError:
                print(f"{notice} Altitude: N/A")

            try:
                print(f"""{response} Location: {round(target.gps_latitude[0])}°{int(target.gps_latitude[1])}'{target.gps_latitude[2]}"{target.gps_latitude_ref} {round(target.gps_longitude[0])}°{int(target.gps_longitude[1])}'{target.gps_longitude[2]}"{target.gps_longitude_ref}""")
            except AttributeError:
                print(f"{notice} Location: N/A")

            print("")

            try:
                print(f"{response} File Source: {target.file_source}")
            except AttributeError:
                print(f"{notice} File Source: N/A")

            try:
                print(f"{response} Image Size: {target.pixel_x_dimension} x {target.pixel_y_dimension}")
            except AttributeError:
                print(f"{notice} Image Size: N/A")

            try:
                print(f"{response} Datetime: {target.datetime}")
            except AttributeError:
                print(f"{notice} Datetime: N/A")
            print("")
            print(success)
        else:
            print(f"{alert} Target image does not have EXIF data")

# Run module_name module.

if __name__ == '__main__':
    exif()
