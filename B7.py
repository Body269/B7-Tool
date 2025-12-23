import os
import time
from termcolor import colored

def clear():
    os.system('clear')

def run_cmd(cmd, title):
    # فتح نافذة جديدة لكل أداة لضمان عملها بشكل مستقل
    print(colored(f"[+] Starting {title} in a new window...", "green"))
    os.system(f"qterminal -e 'bash -c \"{cmd}; echo; echo Press Enter to close this window...; read\"' &")

def my_heart():
    clear()
    heart = ["      ** ** ", "   * * * * ", "  * ** * ", " * /\\ /\\ /\\  /\\ /\\ /\\  * ", " * \\/ \\/ \\/  \\/ \\/ \\/  * ", "  * /\\ /\\ /\\ /\\ /\\   * ", "   * \\/ \\/ \\/ \\/    * ", "    * \\/ \\/ \\/     * ", "      * \\/      * ", "        * * "]
    print(colored("\n\n    --- ❤️ Body's Heart --- \n", "magenta"))
    for line in heart:
        print(colored(line, "magenta"))
        time.sleep(0.1)
    input(colored("\n\nPress Enter to return...", "white"))

def banner():
    print(colored("          👑 Body 👑", "red"))
    print(colored("    --- [ B7 MONSTER APOCALYPSE - v10.0 ] ---", "cyan"))
    print(colored("    --- [ 50+ TOOLS: ANDROID - IOS - WIFI - WEB ] ---", "white"))

def menu():
    print(colored("\n--- [ 📶 WiFi Warfare ] ---", "blue"))
    print("[1] Wifite (Auto)      [2] Airgeddon (Evil Twin)  [3] Fluxion (Phishing)")
    print("[4] Aircrack-ng        [5] Reaver (WPS Hack)      [6] Bully (WPS)")
    print("[7] Fern WiFi Cracker  [8] Kismet                [9] Wifiphisher")

    print(colored("\n--- [ 📱 Mobile Hacking (Android & iOS) ] ---", "magenta"))
    print("[10] PhoneSploit (ADB) [11] Ghost-Framework       [12] Ahmyth (RAT)")
    print("[13] Metasploit Mobile [14] Bettercap (MitM/SSL)  [15] Evil-Droid")
    print("[16] Quark Malware     [17] AndroRAT              [18] iOS-Sploit")

    print(colored("\n--- [ 🚀 Web Attacks & Databases ] ---", "red"))
    print("[19] SQLMap (Auto)     [20] Burp Suite (Proxy)    [21] Commix (OS Inj)")
    print("[22] WPScan (WordPress)[23] Nikto Scanner         [24] Dirb / Dirbuster")
    print("[25] XSSer (XSS Attack)[26] Admin Panel Finder    [27] Uniscan (Vuln)")
    print("[28] JoomScan (Joomla) [29] WebSploit             [30] Scan-T")

    print(colored("\n--- [ 🕵️ Social Engineering & OSINT ] ---", "green"))
    print("[31] SET (Social Tool) [32] CamPhish (Camera)     [33] Sherlock (User)")
    print("[34] Seeker (GPS/Loc)  [35] SocialFish            [36] TheHarvester")
    print("[37] Nexphisher        [38] PyPhisher             [39] BlackEye")

    print(colored("\n--- [ 🔑 Passwords & Cracking ] ---", "white"))
    print("[40] John The Ripper   [41] Hydra (Brute Force)   [42] Hashcat (GPU)")
    print("[43] Crunch (Wordlist) [44] Cupp (Custom Pass)    [45] Medusa")

    print(colored("\n--- [ 🔒 Privacy & Fun ] ---", "yellow"))
    print("[46] Enable Tor Mode   [47] Pegasus Spyware Mode  [48] ❤️ My Heart")
    print("[0] Exit")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(colored("\nB7-Monster > ", "cyan"))

        # Mapping all tools to their execution commands
        tools = {
            '1': ("sudo wifite", "Wifite"), '2': ("sudo airgeddon", "Airgeddon"), '3': ("fluxion", "Fluxion"),
            '10': ("phonesploit", "PhoneSploit"), '11': ("ghost-framework", "Ghost"), '12': ("ahmyth", "Ahmyth"),
            '14': ("bettercap", "Bettercap"), '19': ("sqlmap", "SQLMap"), '21': ("commix", "Commix"),
            '22': ("wpscan", "WPScan"), '23': ("nikto", "Nikto"), '24': ("dirb", "Dirb"),
            '31': ("sudo setoolkit", "SET"), '32': ("bash camphish.sh", "CamPhish"), '33': ("sherlock", "Sherlock"),
            '40': ("john", "John"), '41': ("hydra", "Hydra"), '47': ("msfconsole", "Metasploit")
        }

        if choice in tools:
            run_cmd(tools[choice][0], tools[choice][1])
        elif choice == '46':
            os.system("sudo service tor restart"); print(colored("[+] Tor Active!", "green")); time.sleep(2)
        elif choice == '48':
            my_heart()
        elif choice == '0':
            break
        else:
            print(colored("[!] Tool logic coming in next update...", "yellow")); time.sleep(1)

if __name__ == "__main__":
    main()
