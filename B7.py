import os
import time
import random
import sys
from termcolor import colored

def clear():
    os.system('clear')

def run_cmd(cmd, title):
    # السطر المعدل للتحكم الكامل
    print(colored(f"[+] Starting {title} in a new window...", "green"))
    os.system(f"qterminal -e 'bash -c \"{cmd}; exec bash\"' &")

def matrix_effect():
    # تأثير هكر واقعي: حروف وأطوال وسرعات عشوائية
    clear()
    print(colored("[!] SYSTEM BREACH IN PROGRESS... Press Ctrl+C to abort", "red", attrs=['bold']))
    time.sleep(1.5)
    
    colors = ['green', 'green', 'cyan', 'white', 'red', 'blue']
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()+-={}[]|;:,.<>?"
    
    try:
        while True:
            # عشوائية في طول السطر وكمية الفراغات لتبدو واقعية
            length = random.randint(20, 100)
            line = "".join(random.choice(chars) for _ in range(length))
            
            # اختيار لون عشوائي مع غلبة للأخضر
            color = random.choice(colors)
            
            # طباعة السطر مع سرعة عشوائية جداً
            print(colored(line.center(100), color))
            time.sleep(random.uniform(0.01, 0.1))
            
    except KeyboardInterrupt:
        print(colored("\n[!] ACCESS TERMINATED BY USER.", "yellow"))
        time.sleep(1)

def my_heart():
    clear()
    heart = ["      ** ** ", "   * * * * ", "  * ** * ", " * /\\ /\\ /\\  /\\ /\\ /\\  * ", " * \\/ \\/ \\/  \\/ \\/ \\/  * ", "  * /\\ /\\ /\\ /\\ /\\   * ", "   * \\/ \\/ \\/ \\/    * ", "    * \\/ \\/ \\/     * ", "      * \\/      * ", "        * * "]
    print(colored("\n\n    --- ❤️ Body's Heart --- \n", "magenta"))
    for line in heart:
        print(colored(line, "magenta"))
        time.sleep(0.1)
    input(colored("\n\nPress Enter to return...", "white"))

def banner():
    # كلمة B7 كبيرة واحترافية
    b7_logo = """
    ██████╗ ███████╗
    ██╔══██╗╚════██║
    ██████╔╝    ██╔╝
    ██╔══██╗   ██╔╝ 
    ██████╔╝   ██║  
    ╚═════╝    ╚═╝  
    """
    print(colored(b7_logo, "red", attrs=['bold']))
    print(colored("          👑 Body 👑", "yellow"))
    print(colored("    --- [ B7 MONSTER APOCALYPSE - v11.3 ] ---", "cyan"))
    print(colored("    --- [ 50+ TOOLS: THE REAL HACKER EXPERIENCE ] ---", "white"))

def menu():
    print(colored("\n--- [ 📶 WiFi Warfare ] ---", "blue"))
    print("[1] Wifite (Auto)      [2] Airgeddon (Twin)   [3] Fluxion (Phish)")
    print("[4] Aircrack-ng        [5] Reaver (WPS)       [6] Bully (WPS)")
    print("[7] Fern WiFi          [8] Kismet             [9] Wifiphisher")

    print(colored("\n--- [ 📱 Mobile Hacking ] ---", "magenta"))
    print("[10] PhoneSploit (ADB) [11] Ghost-Framework   [12] Ahmyth (RAT)")
    print("[13] Metasploit Mobile [14] Bettercap (MitM)  [15] Evil-Droid")
    print("[16] Quark Malware     [17] AndroRAT          [18] iOS-Sploit")

    print(colored("\n--- [ 🚀 Web Attacks ] ---", "red"))
    print("[19] SQLMap (Auto)     [20] Burp Suite        [21] Commix (Inj)")
    print("[22] WPScan            [23] Nikto             [24] Dirb / Buster")
    print("[25] XSSer             [26] Admin Finder      [27] Uniscan")
    print("[28] JoomScan          [29] WebSploit         [30] Scan-T")

    print(colored("\n--- [ 🕵️ Social & OSINT ] ---", "green"))
    print("[31] SET (Social Tool) [32] CamPhish (Cam)     [33] Sherlock (User)")
    print("[34] Seeker (GPS)      [35] SocialFish        [36] TheHarvester")
    print("[37] Nexphisher        [38] PyPhisher         [39] BlackEye")

    print(colored("\n--- [ 🔑 Cracking ] ---", "white"))
    print("[40] John The Ripper   [41] Hydra (Brute)     [42] Hashcat (GPU)")
    print("[43] Crunch (Wordlist) [44] Cupp (Custom)     [45] Medusa")

    print(colored("\n--- [ 🔒 Privacy & Fun ] ---", "yellow"))
    print("[46] Enable Tor Mode   [47] ⚡ Real Hacker Matrix [48] ❤️ My Heart")
    print("[0] Exit")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(colored("\nB7-Monster > ", "cyan"))

        tools = {
            '1': ("sudo wifite", "Wifite"), '2': ("sudo airgeddon", "Airgeddon"), '3': ("sudo fluxion", "Fluxion"),
            '10': ("sudo adb devices", "ADB-Check"), '11': ("ghost-framework", "Ghost"), '12': ("ahmyth", "Ahmyth"),
            '19': ("sqlmap", "SQLMap"), '21': ("commix", "Commix"), '22': ("wpscan", "WPScan"),
            '31': ("sudo set", "SET"), '33': ("sherlock", "Sherlock"), '40': ("john", "John"),
            '41': ("hydra", "Hydra"), '42': ("hashcat", "Hashcat")
        }

        if choice == '47':
            matrix_effect()
        elif choice in tools:
            run_cmd(tools[choice][0], tools[choice][1])
        elif choice == '46':
            os.system("sudo service tor restart"); print(colored("[+] Tor Active!", "green")); time.sleep(2)
        elif choice == '48':
            my_heart()
        elif choice == '0':
            break
        else:
            print(colored("[!] Starting tool or invalid choice...", "yellow")); time.sleep(1)

if __name__ == "__main__":
    main()
