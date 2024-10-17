# Imports.
import os
import sys
from exif import Image

from ..utils import (
    QUESTION,
    SUCCESS,
    print_alert,
    print_notice,
    print_response
)


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
    im = input(f"{QUESTION} Enter an image file path: ")

    with open(im, 'rb') as image_file:
        target = Image(image_file)

        if target.has_exif:
            print("")

            try:
                print_response(f"Camera Make: {target.make}")
            except AttributeError:
                print_notice("Camera Make: N/A")

            try:
                print_response(f"Camera Model: {target.model}")
            except AttributeError:
                print_notice("Camera Model: N/A")

            try:
                print_response(f"Lens: {target.lens_model}")
            except AttributeError:
                print_notice("Lens: N/A")

            try:
                print_response(f"Focal Length: {target.focal_length}")
            except AttributeError:
                print_notice("Focal Length: N/A")

            try:
                print_response(f"Aperture: {round(target.aperture_value, 2)}")
            except AttributeError:
                print_notice("Aperture: N/A")

            try:
                print_response(f"ISO Speed: {target.iso_speed}")
            except AttributeError:
                print_notice("ISO Speed: N/A")

            try:
                print_response("Flash: {target.flash[0]}")
            except AttributeError:
                print_notice("Flash: N/A")

            print("")

            try:
                if target.gps_altitude_ref == 0:
                    print_response(f"Altitude: {round(target.gps_altitude, 2)} meters above sea level")
                else:
                    print_response(f"Altitude: {round(target.gps_altitude, 2)} meters below sea level")
            except AttributeError:
                print_notice("Altitude: N/A")

            try:
                print_response(f"""Location: {round(target.gps_latitude[0])}°{int(target.gps_latitude[1])}'{target.gps_latitude[2]}"{target.gps_latitude_ref} {round(target.gps_longitude[0])}°{int(target.gps_longitude[1])}'{target.gps_longitude[2]}"{target.gps_longitude_ref}""")
            except AttributeError:
                print_notice("Location: N/A")

            print("")

            try:
                print_response(f"File Source: {target.file_source}")
            except AttributeError:
                print_notice("File Source: N/A")

            try:
                print_response(f" Image Size: {target.pixel_x_dimension} x {target.pixel_y_dimension}")
            except AttributeError:
                print_notice("Image Size: N/A")

            try:
                print_response(f"Datetime: {target.datetime}")
            except AttributeError:
                print_notice("Datetime: N/A")
            print("")
            print(SUCCESS)
        else:
            print_alert("Target image does not have EXIF data")

# Run module_name module.

if __name__ == '__main__':
    exif()
