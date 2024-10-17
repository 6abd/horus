# Imports.
import os
import sys

from pytube import YouTube
from pytube.cli import on_progress

from ..utils import (
    QUESTION,
    SUCCESS,
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
def ytd():
    link = input(f"{QUESTION} Enter a YouTube video link: ")
    print("")
    print_response("Downloading...")

    yt = YouTube(link, on_progress_callback=on_progress)
    yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path="videos")
    print(SUCCESS)

# Run module_name module.
if __name__ == '__main__':
    ytd()
