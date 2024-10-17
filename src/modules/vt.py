# Imports.
import base64
import json
import os
import sys
import time
import requests
from colorama import Fore # For text colour.

from ..utils import (
    FAILED,
    QUESTION,
    SUCCESS,
    SUCCESSFULLY,
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

     option = input(f"{QUESTION} Would you like to scan a file or a URL? (Enter 'file' or 'url'): ").lower()

     if option == "file":

        # Obtains path then opens for reading
        path = input(f"{QUESTION} Enter a path to scan: ")
        files = {"file" : (os.path.basename(path), open(os.path.abspath(path), "rb"))}



        upload_url = "https://www.virustotal.com/api/v3/files"

        upload_request = requests.post(upload_url, headers=headers, files = files)

        # Makes sure no error code
        if upload_request.status_code == 200:
            # Resulting json data
            result = upload_request.json()
            # Virustotal ID for scanning
            scan_id = result.get("data").get("id")
            print_response(f"Scan ID: {scan_id}")
        else:
            print(f"{FAILED} API Error; Request FAILED! Status Code: {upload_request.status_code}")
            return

        # Gives time for Virustotal to analyze the file
        print_notice("Analyzing...")

        time.sleep(15)

        reports_url = requests.get(f"https://www.virustotal.com/api/v3/files/{scan_id.replace('=','')}", headers=headers)

        data = reports_url.json()


        if reports_url.status_code == 200:
            # Calls specific parts of the dictionary based on what needs to be displayed
            stats = data["data"]["attributes"]["total_votes"]
            results = data["data"]["attributes"]["last_analysis_results"]
            print_alert(f"Detected as malicious: {stats['malicious']}")
            print_notice(f"Detected as harmless: {stats['harmless']}")
            for result in results:
                print("-" * 46)
                print_response(f"Vendor: {results[result]['engine_name']}")
                print_response(f"Version: {results[result]['engine_version']}")
                print_response(f"Category: {results[result]['category']}")
                print_response(f"Result: {results[result]['result']}")
                print_response(f"Method: {results[result]['method']}")
                print("-" * 46)
            print(f"File {SUCCESSFULLY} analysed!")
            print(SUCCESS)
        else:
            print(f"{FAILED} API Error; Request FAILED! Status Code: {reports_url.status_code}")

     elif option == "url":
        source_url = input(f"{QUESTION} Enter a url: ")
        url = "https://www.virustotal.com/api/v3/urls"

        payload = { "url": source_url }

        upload_request = requests.post(url, data=payload, headers=headers)
        # Makes sure no error code
        if upload_request.status_code == 200:
            # Resulting json data
            result = upload_request.json()
            # Virustotal ID for scanning
            link = result.get("data").get("links").get("self")
            print_response(f"Analysis Link: {link}")
        else:
            print(f"{FAILED} API Error; Request FAILED! Status Code: {upload_request.status_code}")
            return

        # Gives time for Virustotal to analyze the URL
        print_notice("Analyzing...")

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
                print("-" * 46)
                print_response(f"Vendor: {results[result]['engine_name']}")
                print_response(f"Category: {results[result]['category']}")

                if results[result]['result'] == 'clean':
                    print_response(f"Result: {Fore.GREEN}{results[result]['result']}")
                elif results[result]['result'] == 'unrated':
                    print_notice(f"Result: {Fore.YELLOW}{results[result]['result']}")
                else:
                    print_alert(f"Result: {Fore.RED}{results[result]['result']}")

                print_response(f"Method: {results[result]['method']}")
                print("-" * 46)

            print_alert(f"Detected as malicious: {stats['malicious']}")
            print_notice(f"Detected as suspicious: {stats['suspicious']}")
            print_response(f"Detected as harmless: {stats['harmless']}")
            print(f"{QUESTION} Undetected: {stats['undetected']}")

            print(f"URL {SUCCESSFULLY} analysed!")
            print(SUCCESS)
        else:
            print(f"{FAILED} API Error; Request FAILED! Status Code: {reports_url.status_code}")

# Run module_name module.
if __name__ == '__main__':
    vt()
