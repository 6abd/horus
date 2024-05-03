import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
import argparse # For adding arguments.


import etc.init.banner as banner
import src.main as main

# Modules
import src.apicon as apicon
# # SECURITY.
import src.modules.pvpn as pvpn
# ENUMERATION.
# OSINT.
import src.modules.shodan as shodan
import src.modules.numlook as numlook
import src.modules.geolock as geolock
import src.modules.cryptotrace as cryptotrace
import src.modules.mactrace as mactrace
import src.modules.vt as vt
# CASE-GEN.
# SDB.
# Loki.
import src.modules.loki_decrypt as loki_decrypt
import src.modules.loki_discovery as loki_discovery
import src.modules.loki_encrypt as loki_encrypt
import src.modules.loki_keygen as loki_keygen
# FORENSICS.

# Clears screen
os.system("clear")

parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()

ap.add_argument('-apicon', help='Configure the API settings for Horus\n', action="store_true")
# SECURITY.
#ap.add_argument('-Torshell', help='\n', action="store_true")
ap.add_argument('-pvpn', help='\n', action="store_true")
#ap.add_argument('-Ovpn', help='\n', action="store_true")
# ENUMERATION.
#ap.add_argument('-Fallenflare', help='\n', action="store_true")
#ap.add_argument('-Recpull', help='\n', action="store_true")
#ap.add_argument('-Anonfile', help='\n', action="store_true")
#ap.add_argument('-Onionshare', help='\n', action="store_true")
# OSINT.
ap.add_argument('-shodan', help='Call on Loki to encrypt the home directory and pull the encryption key.\n', action="store_true")
#ap.add_argument('-wiggle', help='Use an API for SSID/BSSIDs stat, locations, & Bluetooth data.\n', action="store_true")
ap.add_argument('-numlook', help='Look up validity, carriers, names of phone numbers globally.\n', action="store_true")
ap.add_argument('-vt', help='Connect to the virus-total API to scan, or screen files, links, etc.\n', action="store_true")
ap.add_argument('-geolock', help='Shodan & auxiliary API based IP tracing & tracking.\n', action="store_true")
#ap.add_argument('-bankindex', help='Search up BIN/IIN, Sort Codes, Cheque details, etc.\n', action="store_true")
ap.add_argument('-mactrace', help='Type in an MAC address to get the vendor or device.', action="store_true")
#ap.add_argument('-Flightinfo', help='\n', action="store_true")
#ap.add_argument('-Licenseinfo', help='\n', action="store_true")
ap.add_argument('-cryptotrace', help='Transaction information, & crypto-wallet tracing.', action="store_true")
#ap.add_argument('-Dischook', help='\n', action="store_true")
#ap.add_argument('-Ytd', help='\n', action="store_true")
#ap.add_argument('-Leverage', help='\n', action="store_true")
# CASE-GEN.
#ap.add_argument('-Casegenerate', help='\n', action="store_true")
#ap.add_argument('-Casesecure', help='\n', action="store_true")
#ap.add_argument('-Casedelete', help='\n', action="store_true")
# SDB.
#ap.add_argument('-sdb', help='Create or search through your custom horus database built in SQL.\n', action="store_true")
# LOKI.


args = vars(parser.parse_args())


from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        
if args['apicon']: # Runs the apicon program.
    while True:
        try:
            apicon.apicon()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)

if args['pvpn']: # Runs the pvpn program.
    while True:
        try:
            pvpn.pvpn()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)

if args['shodan']: # Runs the shodan program.
    while True:
        try:
            shodan.run_shodan()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)

if args['numlook']: # Runs the numlook program.
    while True:
        try:
            numlook.numlook()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)

if args['geolock']: # Runs the geolock program.
    while True:
        try:
            geolock.geolock()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)

if args['mactrace']: # Runs the mactrace program.
    while True:
        try:
            mactrace.mactrace()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)

if args['cryptotrace']: # Runs the cryptotrace program.
    while True:
        try:
            cryptotrace.cryptotrace()
            os._exit(0)
        except Exception as error:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
            os._exit(0)
          
if args['vt']:
  while True:
    try:
      vt.vt()
      os._exit(0)
    except Exception as error:
      print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: {error}\n")
      os._exit(0)

if __name__ == '__main__':
    try:
        banner.banner()
        main.main_script()
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
