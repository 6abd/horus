# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import time
import base64

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
with open('./src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["vt"]

# Program.
def vt():

     headers = {
            "accept": "application/json",
            "x-apikey": key,
            "content-type": "application/x-www-form-urlencoded"
     }

     option = input(f"{question} Would you like to scan a file or a URL? (Enter 'file' or 'url'): ").lower()

     if option == "file":

        # Obtains path then opens for reading
        path = input(f"{question} Enter a path to scan: ")
        files = {"file" : (os.path.basename(path), open(os.path.abspath(path), "rb"))}



        upload_url = "https://www.virustotal.com/api/v3/files"

        upload_request = requests.post(upload_url, headers=headers, files = files)

        # Makes sure no error code
        if upload_request.status_code == 200:
            # Resulting json data
            result = upload_request.json()
            # Virustotal ID for scanning
            scan_id = result.get("data").get("id")
            print(f"{response} Scan ID: {scan_id}")
        else:
            print(f"{failed} API Error; Request failed! Status Code: {upload_request.status_code}")
            return

        # Gives time for Virustotal to analyze the file
        print(f"{notice} Analyzing...")

        time.sleep(15)

        reports_url = requests.get(f"https://www.virustotal.com/api/v3/files/{scan_id.replace('=','')}", headers=headers)

        data = reports_url.json()


        if reports_url.status_code == 200:
            # Calls specific parts of the dictionary based on what needs to be displayed
            stats = data["data"]["attributes"]["total_votes"]
            results = data["data"]["attributes"]["last_analysis_results"]
            print(f"{alert} Detected as malicious: {stats['malicious']}")
            print(f"{notice} Detected as harmless: {stats['harmless']}")
            for result in results:
                print("----------------------------------------------")
                print(f"{response} Vendor: {results[result]['engine_name']}")
                print(f"{response} Version: {results[result]['engine_version']}")
                print(f"{response} Category: {results[result]['category']}")
                print(f"{response} Result: {results[result]['result']}")
                print(f"{response} Method: {results[result]['method']}")
                print("----------------------------------------------")
            print(f"File {successfully} analysed!")
            print(success)
        else:
            print(f"{failed} API Error; Request failed! Status Code: {reports_url.status_code}")

     elif option == "url":
        source_url = input(f"{question} Enter a url: ")
        url = "https://www.virustotal.com/api/v3/urls"

        payload = { "url": source_url }

        upload_request = requests.post(url, data=payload, headers=headers)
        # Makes sure no error code
        if upload_request.status_code == 200:
            # Resulting json data
            result = upload_request.json()
            # Virustotal ID for scanning
            link = result.get("data").get("links").get("self")
            print(f"{response} Analysis Link: {link}")
        else:
            print(f"{failed} API Error; Request failed! Status Code: {upload_request.status_code}")
            return

        # Gives time for Virustotal to analyze the URL
        print(f"{notice} Analyzing...")

        time.sleep(10)
        scan_id = base64.urlsafe_b64encode(source_url.encode()).decode().strip("=")
        reports_url = requests.get(f"https://www.virustotal.com/api/v3/urls/{scan_id}", headers=headers)

        data = reports_url.json()
        print(data)

        if reports_url.status_code == 200:
            # Calls specific parts of the dictionary based on what needs to be displayed
            stats = data["data"]["attributes"]["last_analysis_stats"]
            results = data["data"]["attributes"]["last_analysis_results"]
            for result in results:
                print("----------------------------------------------")
                print(f"{response} Vendor: {results[result]['engine_name']}")
                print(f"{response} Category: {results[result]['category']}")

                if results[result]['result'] == 'clean':
                    print(f"{response} Result: {Fore.GREEN}{results[result]['result']}")
                elif results[result]['result'] == 'unrated':
                    print(f"{notice} Result: {Fore.YELLOW}{results[result]['result']}")
                else:
                    print(f"{alert} Result: {Fore.RED}{results[result]['result']}")

                print(f"{response} Method: {results[result]['method']}")
                print("----------------------------------------------")

            print(f"\n{alert} Detected as malicious: {stats['malicious']}")
            print(f"{notice} Detected as suspicious: {stats['suspicious']}")
            print(f"{response} Detected as harmless: {stats['harmless']}")
            print(f"{question} Undetected: {stats['undetected']}")

            print(f"URL {successfully} analysed!")
            print(success)
        else:
            print(f"{failed} API Error; Request failed! Status Code: {reports_url.status_code}")

# Run module_name module.
if __name__ == '__main__':
    vt()
