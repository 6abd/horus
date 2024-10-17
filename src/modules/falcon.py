# Imports.
import os
import sys

import pyshark

from ..utils import (
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
        print_response(f"Protocol: {pkt.highest_layer}")
        print_response(f"Length: {pkt.length} bytes")
        print_response(f"Time: {pkt.sniff_time}")

        if hasattr(pkt, 'ip'):
            print_response(f"Source IP: {pkt.ip.src}")
            print_response(f"Destination IP: {pkt.ip.dst}")
        else:
            print_notice(f"Source IP: N/A")
            print_notice(f"Destination IP: N/A")

        if hasattr(pkt, 'tcp'):
            print_response(f"Source Port: {pkt.tcp.srcport}")
            print_response(f"Destination Port: {pkt.tcp.dstport}")
            print_response(f"TCP Flags: {pkt.tcp.flags}")
        elif hasattr(pkt, 'udp'):
            print_response(f"Source Port: {pkt.udp.srcport}")
            print_response(f"Destination Port: {pkt.udp.dstport}")
        else:
            print_notice(f"Source Port: N/A")
            print_notice(f"Destination Port: N/A")

        # Display additional protocol-specific information
        if hasattr(pkt, 'http'):
            if hasattr(pkt.http, 'host'):
                print_response(f"HTTP Host: {pkt.http.host}")
        elif hasattr(pkt, 'dns'):
            if hasattr(pkt.dns, 'qry_name'):
                print_response(f"DNS Query Name: {pkt.dns.qry_name}")

        print_response(f"Info: {get_packet_info(pkt)}")

# Program.
def falcon():
    option = input(f"{QUESTION} (1) Sniff for packets or (2) use saved capture file: ")
    if option == "1":
        inter = input(f"{QUESTION} Enter an interface: ")
        filter = input(f"{QUESTION} Enter a BPF filter if you would like (Press enter if not): ")
        sniff_num = int(input(f"{QUESTION} How many packets to sniff for? "))

        cap = pyshark.LiveCapture(interface=inter, bpf_filter=filter)
        cap.sniff(sniff_num)

        analysis(cap)
        print(SUCCESS)

    if option == "2":
        print()
        path = input(f"{QUESTION} Enter a capture file path: ")
        filter = input(f"{QUESTION} Enter a display filter if you would like (Press enter if not): ")
        cap = pyshark.FileCapture(path, display_filter=filter)

        analysis(cap)
        print(SUCCESS)


# Run module_name module.
if __name__ == '__main__':
    falcon()
