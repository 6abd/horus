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
    key = data["aviationstack"]

# Program.
def flightinfo():
    print_notice("How would you like to filter flight data? (icao24, number, date, dep_iata, arr_iata or status) ")
    option = input(f"{COMMAND}").lower()

    if option == 'number':
        number = input(f"{QUESTION} Enter a flight number: ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&flight_number={number}").json()['data']
        for i in range(0,len(data)):
            print_response(f"Airline Name: {data[i]['airline']['name']}")
            print_response(f"Flight Date: {data[i]['flight_date']}")
            print_response(f"Status: {data[i]['flight_status']}")
            print_response(f"Departure Airport: {data[i]['departure']['airport']}")
            print_response(f"Departure Timezone: {data[i]['departure']['timezone']}")
            print_response(f"Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print_response(f"Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print_response(f"Estimated Departure: {data[i]['departure']['estimated']}")
            print_response(f"Actual Departure: {data[i]['departure']['actual']}")
            print_response(f"Arrival Airport: {data[i]['arrival']['airport']}")
            print_response(f"Arrival Timezone: {data[i]['arrival']['timezone']}")
            print_response(f"Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print_response(f"Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print_response(f"Estimated Arrival: {data[i]['arrival']['estimated']}")
            print_response(f"Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    if option == 'date':
        date = input(f"{QUESTION} Enter a flight date (YYYY-MM-DD): ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&date={date}").json()['data']
        for i in range(0,len(data)):
            print_response(f"Airline Name: {data[i]['airline']['name']}")
            print_response(f"Flight Date: {data[i]['flight_date']}")
            print_response(f"Status: {data[i]['flight_status']}")
            print_response(f"Departure Airport: {data[i]['departure']['airport']}")
            print_response(f"Departure Timezone: {data[i]['departure']['timezone']}")
            print_response(f"Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print_response(f"Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print_response(f"Estimated Departure: {data[i]['departure']['estimated']}")
            print_response(f"Actual Departure: {data[i]['departure']['actual']}")
            print_response(f"Arrival Airport: {data[i]['arrival']['airport']}")
            print_response(f"Arrival Timezone: {data[i]['arrival']['timezone']}")
            print_response(f"Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print_response(f"Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print_response(f"Estimated Arrival: {data[i]['arrival']['estimated']}")
            print_response(f"Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    if option == 'dep_iata':
        dep_iata = input(f"{QUESTION} Enter a flight departure IATA: ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&dep_iata={dep_iata}").json()['data']
        for i in range(0,len(data)):
            print_response(f"Airline Name: {data[i]['airline']['name']}")
            print_response(f"Flight Date: {data[i]['flight_date']}")
            print_response(f"Status: {data[i]['flight_status']}")
            print_response(f"Departure Airport: {data[i]['departure']['airport']}")
            print_response(f"Departure Timezone: {data[i]['departure']['timezone']}")
            print_response(f"Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print_response(f"Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print_response(f"Estimated Departure: {data[i]['departure']['estimated']}")
            print_response(f"Actual Departure: {data[i]['departure']['actual']}")
            print_response(f"Arrival Airport: {data[i]['arrival']['airport']}")
            print_response(f"Arrival Timezone: {data[i]['arrival']['timezone']}")
            print_response(f"Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print_response(f"Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print_response(f"Estimated Arrival: {data[i]['arrival']['estimated']}")
            print_response(f"Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    if option == 'arr_iata':
        arr_iata = input(f"{QUESTION} Enter a flight arrival IATA: ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&arr_iata={arr_iata}").json()['data']
        for i in range(0,len(data)):
            print_response(f"Airline Name: {data[i]['airline']['name']}")
            print_response(f"Flight Date: {data[i]['flight_date']}")
            print_response(f"Status: {data[i]['flight_status']}")
            print_response(f"Departure Airport: {data[i]['departure']['airport']}")
            print_response(f"Departure Timezone: {data[i]['departure']['timezone']}")
            print_response(f"Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print_response(f"Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print_response(f"Estimated Departure: {data[i]['departure']['estimated']}")
            print_response(f"Actual Departure: {data[i]['departure']['actual']}")
            print_response(f"Arrival Airport: {data[i]['arrival']['airport']}")
            print_response(f"Arrival Timezone: {data[i]['arrival']['timezone']}")
            print_response(f"Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print_response(f"Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print_response(f"Estimated Arrival: {data[i]['arrival']['estimated']}")
            print_response(f"Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    if option == 'status':
        status = input(f"{QUESTION} Enter a flight status (scheduled, active, landed, cancelled, incident, diverted): ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&status={status}").json()['data']
        for i in range(0,len(data)):
            print_response(f"Airline Name: {data[i]['airline']['name']}")
            print_response(f"Flight Date: {data[i]['flight_date']}")
            print_response(f"Status: {data[i]['flight_status']}")
            print_response(f"Departure Airport: {data[i]['departure']['airport']}")
            print_response(f"Departure Timezone: {data[i]['departure']['timezone']}")
            print_response(f"Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print_response(f"Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print_response(f"Estimated Departure: {data[i]['departure']['estimated']}")
            print_response(f"Actual Departure: {data[i]['departure']['actual']}")
            print_response(f"Arrival Airport: {data[i]['arrival']['airport']}")
            print_response(f"Arrival Timezone: {data[i]['arrival']['timezone']}")
            print_response(f"Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print_response(f"Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print_response(f"Estimated Arrival: {data[i]['arrival']['estimated']}")
            print_response(f"Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
    if option == 'icao24':
        icao24 = input(f"{QUESTION} Enter a plane icao24: ")
        begin = input(f"{QUESTION} Enter a begin Unix timestamp for the flights interval: ")
        end = input(f"{QUESTION} Enter an end Unix timestamp for the flights interval: ")
        data = requests.get(f"https://opensky-network.org/api/flights/aircraft?icao24={icao24}&begin={begin}&end={end}").json()
        for i in range(0,len(data)):
            print_response(f"Aircraft Callsign: {data[i]['callsign']}")
            print_response(f"Departure Airport (Estimated): {data[i]['estDepartureAirport']}")
            print_response(f"Arrival Airport (Estimated): {data[i]['estArrivalAirport']}")
            print_response(f"Arrival Airport (Estimated): {data[i]['estArrivalAirport']}")
            print_response(f"First Seen: {data[i]['firstSeen']}")
            print_response(f"Last Seen: {data[i]['lastSeen']}")
            print("-------------------------------------------------------------------")
        print(SUCCESS)
# Run module_name module.
if __name__ == '__main__':
    flightinfo()
