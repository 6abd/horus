# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import pyshark

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

def get_packet_info(packet):
    info = ""
    if 'HTTP' in packet:
        if hasattr(packet.http, 'request_method'):
            info = f"HTTP {packet.http.request_method} {packet.http.host}{packet.http.request_uri}"
            if hasattr(packet.http, 'user_agent'):
                info += f"\nUser-Agent: {packet.http.user_agent}"
            if hasattr(packet.http, 'content_type'):
                info += f"\nContent-Type: {packet.http.content_type}"
        elif hasattr(packet.http, 'response_code'):
            info = f"HTTP {packet.http.response_code} {packet.http.response_phrase}"
            if hasattr(packet.http, 'content_type'):
                info += f"\nContent-Type: {packet.http.content_type}"
    elif 'DNS' in packet:
        if hasattr(packet.dns, 'qry_name'):
            info = f"DNS Query: {packet.dns.qry_name}"
        elif hasattr(packet.dns, 'a'):
            info = f"DNS Response: {packet.dns.a}"
    elif 'TCP' in packet:
        info = f"TCP {packet.tcp.srcport} -> {packet.tcp.dstport}"
    elif 'UDP' in packet:
        info = f"UDP {packet.udp.srcport} -> {packet.udp.dstport}"
    else:
        info = f"{packet.highest_layer} packet"
    return info

def analysis(cap):
    for pkt in cap:
        print(f"\nPacket #{pkt.number}")
        print(f"{response} Protocol: {pkt.highest_layer}")
        print(f"{response} Length: {pkt.length} bytes")
        print(f"{response} Time: {pkt.sniff_time}")

        if hasattr(pkt, 'ip'):
            print(f"{response} Source IP: {pkt.ip.src}")
            print(f"{response} Destination IP: {pkt.ip.dst}")
        else:
            print(f"{notice} Source IP: N/A")
            print(f"{notice} Destination IP: N/A")

        if hasattr(pkt, 'tcp'):
            print(f"{response} Source Port: {pkt.tcp.srcport}")
            print(f"{response} Destination Port: {pkt.tcp.dstport}")
            print(f"{response} TCP Flags: {pkt.tcp.flags}")
        elif hasattr(pkt, 'udp'):
            print(f"{response} Source Port: {pkt.udp.srcport}")
            print(f"{response} Destination Port: {pkt.udp.dstport}")
        else:
            print(f"{notice} Source Port: N/A")
            print(f"{notice} Destination Port: N/A")

        # Display additional protocol-specific information
        if hasattr(pkt, 'http'):
            if hasattr(pkt.http, 'host'):
                print(f"{response} HTTP Host: {pkt.http.host}")
        elif hasattr(pkt, 'dns'):
            if hasattr(pkt.dns, 'qry_name'):
                print(f"{response} DNS Query Name: {pkt.dns.qry_name}")

        print(f"{response} Info: {get_packet_info(pkt)}")

# Program.
def falcon():
    option = input(f"{question} (1) Sniff for packets or (2) use saved capture file: ")
    if option == "1":
        inter = input(f"{question} Enter an interface: ")
        filter = input(f"{question} Enter a BPF filter if you would like (Press enter if not): ")
        sniff_secs = int(input(f"{question} How long (secs) to sniff for packets? "))

        cap = pyshark.LiveCapture(interface=inter, bpf_filter=filter)
        cap.sniff(sniff_secs)

        analysis(cap)

    if option == "2":
        print()
        path = input(f"{question} Enter a capture file path: ")
        filter = input(f"{question} Enter a display filter if you would like (Press enter if not): ")
        cap = pyshark.FileCapture(path, display_filter=filter)

        analysis(cap)


# Run module_name module.
if __name__ == '__main__':
    falcon()
