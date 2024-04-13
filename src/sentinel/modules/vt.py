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
success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
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
with open('./sentinel/src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["vt"]

# Program.
def vt():
     headers = {
                    "X-Apikey" : key,
                    "User-Agent" : "Sentinel v.1.0",
                    "Accept-Encoding" : "gzip, deflate",
                }
    
     option = input("Would you like to scan a file or a URL? (Enter 'file' or 'url')>> ").lower()

     if option == "file":
        
        # Obtains path then opens for reading
        path = input("Enter a path to scan: ")
        files = {"file" : (os.path.basename(path), open(os.path.abspath(path), "rb"))}

       

        upload_url = "https://www.virustotal.com/api/v3/files"

        upload_request = requests.post(upload_url, headers=headers, files = files)
        
        # Makes sure no error code
        if upload_request.status_code == 200:
            # Resulting json data
            result = upload_request.json()
            # Virustotal ID for scanning
            scan_id = result.get("data").get("id")
            print(scan_id)
        else:
            print("API Error; Request failed!")

        # Gives time for Virustotal to analyze the file
        print("Analyzing...")

        time.sleep(30)

        reports_url = requests.get(f"https://www.virustotal.com/api/v3/files/{scan_id.replace('=','')}", headers=headers)

        data = reports_url.json()
        

        if reports_url.status_code == 200:
            # Calls specific parts of the dictionary based on what needs to be displayed
            stats = data["data"]["attributes"]["total_votes"]
            results = data["data"]["attributes"]["last_analysis_results"]
            print(f"Detected as malicious: {stats['malicious']}")
            print(f"Detected as harmless: {stats['harmless']}")
            for result in results:
                print("----------------------------------------------")
                print(f"Vendor: {results[result]['engine_name']}")
                print(f"Version: {results[result]['engine_version']}")
                print(f"Category: {results[result]['category']}")
                print(f"Result: {results[result]['result']}")
                print(f"Method: {results[result]['method']}")
                print("----------------------------------------------")
            print("File successfully analysed!")
        else:
            print(f"API Error; Request failed! Status Code: {reports_url.status_code}")

     elif option == "url":
        url = input("Enter a url: ")
        # Vt uses base64 encoding, and the API said to do this.
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        
        reports_url = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers)
        data = reports_url.json()

        # Same as for the file section, just for the URL
        if reports_url.status_code == 200:
            stats = data["data"]["last_analysis_stats"]
            results = data["data"]["last_analysis_results"]
            print(f"Detected as malicious: {stats['malicious']}")
            print(f"Detected as harmless: {stats['harmless']}")
            print(f"Undetected: {stats['undetected']}")
            for result in results:
                print("----------------------------------------------")
                print(f"Vendor: {results[result]['engine_name']}")
                print(f"Version: {results[result]['engine_version']}")
                print(f"Category: {results[result]['category']}")
                print(f"Result: {results[result]['result']}")
                print(f"Method: {results[result]['method']}")
                print("----------------------------------------------")
            print("URL successfully analysed!")
        else:
            print(f"API Error; Request failed! Status Code: {reports_url.status_code}")
# Run module_name module.
if __name__ == '__main__':
    vt()
