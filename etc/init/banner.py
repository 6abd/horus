import secrets
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
import random # For tagline.

version = ("1.2.6") # Major.Minor.Rev/Build
motd = (f"{Fore.LIGHTRED_EX}Are you worried yet?{Fore.LIGHTRED_EX}") # Always use 20 char max.
tag = ['                                Access the matrix', '                                Break the system'] # Use spaces to centre the tag to the divider bar.

def banner():
    try:
        # Logo has been disabled in this version, if you want to re-enable un-comment lines 14-32, and 40.
        print("")
        print("                                  ,,,,,,,%%%%%,,,,,,,,,,,")
        print("                          ,,,,,,,,,,,,*%%%%%%%%%%%%%,,,,,,")
        print("                  .,,,,,,%%%%%%%%%%%%%%*,,,,,,,%%%%%%%%%%%,****")
        print("              ,,,,%%%%%%%%%%,,,,,,,,           ,,,,,%%%%%%%%%%#****")
        print("         ..,.,&&&&&&%%,,,,,,         ,,,,,,,,,,,    ,,,,,%%%%%%%%%(***,")
        print(f"      ....&&&&&&&&,,,,.              ,,,,{Fore.RED}%%%%%%{Fore.LIGHTRED_EX}*{Fore.RESET},,,     .,,,*%%%%%%%%%***,")
        print(f"    ...&&&&&&&,,.,            .,,,      ,,{Fore.RED}%%%%%%%%{Fore.RESET},,        ,*,*%%%%%%%%%***")
        print(f" ...&&&&&&&....               ,,{Fore.LIGHTRED_EX}%,,.   ,,,{Fore.RED}%%%%%%%%{Fore.LIGHTRED_EX}%{Fore.RESET},,          ,,,,%%%%%%%%(***")
        print(f"..&&&&&&(...                 ,,{Fore.LIGHTRED_EX}#{Fore.RED}%%%,,,,{Fore.RED}%%%%%%%%%%%%{Fore.RESET},,             ,,,*%%%%%%%%**")
        print(f" ...&&&&&&&....               ,,{Fore.RED}%%%%%%%%%%%%%%%%%%{Fore.LIGHTRED_EX}%{Fore.RESET},,          ,,,,%%%%%%%%***.")
        print(f"   ....&&&&&&&....            ,,,{Fore.LIGHTRED_EX}&&{Fore.RED}%%%%%%%%%%%%%%{Fore.LIGHTRED_EX}#{Fore.RESET},,        ,,,,%%%%%%%%%,,*")
        print(f"      ....&&&&&&&&....          ,,,{Fore.LIGHTRED_EX}&&{Fore.RED}%%%%%%%%%%{Fore.RESET},,,,     ,,,,#%%%%%%%%%,,,.")
        print("          ....&&&&&&&&......       ,,,,,,,,,,,,,    ,,,,(%%%%%%%%%#,,,.")
        print("              .....&&&&&&&&&........           ,,,,,%%%%%%%%%%%,,,,")
        print("                   ........&&&&&&&&&&,..,,,,,,(%%%%%%%%%%%,,,,,")
        print("                       ...............&&&&&&&&&%%%%%%,,,,,.")
        print("                       .....(&&&&&&&&&&&&&&&,,,,,,,,.")
        print("                              ............")
        print("")
        print(f"                            {Fore.RED}Horus{Fore.WHITE} - {motd}{Fore.RESET}")
        print(f"                                       {version}")
        print("                                                                                ")
        print(f"{Fore.RED}  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.   .{Fore.WHITE}")
        print(f"{Fore.WHITE}:::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}:::")
        print(f"{Fore.RED}'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `.'{Fore.WHITE}")
        # print(random.choice(tag))

    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
banner()
