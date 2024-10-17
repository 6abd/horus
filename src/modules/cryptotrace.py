# Imports.
import os
import sys
import json
import requests

from ..utils import (
    COMMAND,
    QUESTION,
    SUCCESS,
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
    key = data["etherscan"]
    key2 = data["bscscan"]

# Program.
def cryptotrace():

    # Gets the desired currency and address
    print_notice('What cryptocurrency would you like to use? (Bitcoin, Ethereum, or Binance)')
    option = input(f'{COMMAND}').lower()
    address = input(f"{QUESTION} Enter an address: ")

    # Bitcoin
    if option == "bitcoin":

        # Gets balance through API, divides by 100,000,000 because the API data is the balance multiplied by that number.
        balance = int(requests.get(f"https://blockchain.info/rawaddr/{address}").json()["final_balance"])/100000000

        # Gets transaction_info base
        transaction_info = requests.get(f"https://blockchain.info/rawaddr/{address}").json()["txs"]

        print_notice(f"The balance of this Bitcoin wallet is {balance} BTC")

        # Loops through each transaction and prints details about it (rough for now)
        for i in range(0,len(transaction_info)):
            print_response(f"Transaction Hash: {transaction_info['hash']}")
            print_response(f"Sender: {address}")
            print_response(f"Recipient: {transaction_info['out'][i]['addr']}")
            print_response(f"Value: {transaction_info['out'][i]['value']/100000000} BTC")
            print_response(f"Unix Timestamp: {transaction_info['time']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    # Ethereum
    elif option == "ethereum":
        # Gets balance through API, divides by 1e18 because the API data is the balance multiplied by that number.
        balance = int(requests.get(f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={key}").json()["result"])/1000000000000000000

        # Gets transaction_info base
        transaction_info = requests.get(f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=100&sort=desc&apikey={key}").json()["result"]

        print_notice(f"The balance of this Ethereum wallet is {balance} ETH")

        # Loops through each transaction and prints details about it (rough for now)
        for i in range(0, len(transaction_info)):
            print_response(f"Block Number: {transaction_info[i]['blockNumber']}")
            print_response(f"Transaction Hash: {transaction_info[i]['hash']}")
            print_response(f"Value: {int(transaction_info[i]['value'])/1000000000000000000} ETH")
            print_response(f"Sender: {transaction_info[i]['from']}")
            print_response(f"Recipient: {transaction_info[i]['to']}")
            print_response(f"Unix Timestamp: {transaction_info[i]['timeStamp']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    elif option == "binance":
        # Gets balance through API, divides by 1e18 because the API data is the balance multiplied by that number.
        balance = int(requests.get(f"https://api.bscscan.com/api?module=account&action=balance&address={address}&apikey={key2}").json()['result'])/1000000000000000000

        # Gets transaction_info base
        transaction_info = requests.get(f"https://api.bscscan.com/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=100&sort=desc&apikey={key2}").json()["result"]

        print_notice(f"The balance of this Binance wallet is {balance} BNB")

        # Loops through each transaction and prints details about it (rough for now)
        for i in range(0, len(transaction_info)):
            print_response(f"Block Number: {transaction_info[i]['blockNumber']}")
            print_response(f"Transaction Hash: {transaction_info[i]['hash']}")
            print_response(f"Value: {int(transaction_info[i]['value'])/1000000000000000000} BNB")
            print_response(f"Sender: {transaction_info[i]['from']}")
            print_response(f"Recipient: {transaction_info[i]['to']}")
            print_response(f"Unix Timestamp: {transaction_info[i]['timeStamp']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
# Run module_name module.
if __name__ == '__main__':
    cryptotrace()
