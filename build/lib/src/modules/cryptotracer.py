# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.

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
with open('var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["etherscan"]
    key2 = data["bscscan"]

# Program.
def cryptotracer():
    
    # Gets the desired currency and address
    print(f'{notice} What cryptocurrency would you like to use? (Bitcoin, Ethereum, or Binance)')
    option = input(f'{command}').lower()
    address = input(f"{question} Enter an address: ")

    # Bitcoin
    if option == "bitcoin":
        
        # Gets balance through API, divides by 100,000,000 because the API data is the balance multiplied by that number.
        balance = int(requests.get(f"https://blockchain.info/rawaddr/{address}").json()["final_balance"])/100000000
        
        # Gets transaction_info base
        transaction_info = requests.get(f"https://blockchain.info/rawaddr/{address}")["txs"]
        
        print(f"{notice} The balance of this Bitcoin wallet is {balance} BTC")

        # Loops through each transaction and prints details about it (rough for now)
        for i in range(0,len(transaction_info)):
            print(f"Transaction Hash: {transaction_info['hash']}")
            print(f"Sender: {address}")
            print(f"Recipient: {transaction_info['out'][i]['addr']}")
            print(f"Value: {transaction_info['out'][i]['value']/100000000} BTC")
            print(f"Unix Timestamp: {transaction_info['time']}")
            print("-------------------------------------------------------------------")

    # Ethereum
    elif option == "ethereum":
        # Gets balance through API, divides by 1e18 because the API data is the balance multiplied by that number.
        balance = int(requests.get(f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={key}").json()["result"])/1000000000000000000
        
        # Gets transaction_info base
        transaction_info = requests.get(f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=100&sort=desc&apikey={key}").json()["result"]
        
        print(f"{notice} The balance of this Ethereum wallet is {balance} ETH")
        
        # Loops through each transaction and prints details about it (rough for now)
        for i in range(0, len(transaction_info)):
            print(f"Block Number: {transaction_info[i]['blockNumber']}")
            print(f"Transaction Hash: {transaction_info[i]['hash']}")
            print(f"Value: {int(transaction_info[i]['value'])/1000000000000000000} ETH")
            print(f"Sender: {transaction_info[i]['from']}")
            print(f"Recipient: {transaction_info[i]['to']}")
            print(f"Unix Timestamp: {transaction_info[i]['timeStamp']}")
            print("-------------------------------------------------------------------")

    elif option == "binance":
        # Gets balance through API, divides by 1e18 because the API data is the balance multiplied by that number.
        balance = int(requests.get(f"https://api.bscscan.com/api?module=account&action=balance&address={address}&apikey={key2}").json()['result'])/1000000000000000000

        # Gets transaction_info base
        transaction_info = requests.get(f"https://api.bscscan.com/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=100&sort=desc&apikey={key2}").json()["result"]
        
        print(f"{notice} The balance of this Binance wallet is {balance} BNB")
        
        # Loops through each transaction and prints details about it (rough for now)
        for i in range(0, len(transaction_info)):
            print(f"Block Number: {transaction_info[i]['blockNumber']}")
            print(f"Transaction Hash: {transaction_info[i]['hash']}")
            print(f"Value: {int(transaction_info[i]['value'])/1000000000000000000} BNB")
            print(f"Sender: {transaction_info[i]['from']}")
            print(f"Recipient: {transaction_info[i]['to']}")
            print(f"Unix Timestamp: {transaction_info[i]['timeStamp']}")
            print("-------------------------------------------------------------------")

# Run module_name module.
if __name__ == '__main__':
    cryptotracer()
