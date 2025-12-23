import os
import time
import random
import sys
from termcolor import colored

def clear():
    os.system('clear')

def run_cmd(cmd, title):
    # استخدام exec bash للتحكم الكامل في النافذة الجديدة
    print(colored(f"[+] Starting {title} in a new window...", "green"))
    os.system(f"qterminal -e 'bash -c \"{cmd}; exec bash\"' &")

def matrix_effect():
    # الأداة الجديدة: كلام ملون يركض بسرعة ولا يتوقف
    clear()
    print(colored("[!] Press Ctrl+C to stop the Matrix...", "yellow"))
    time.sleep(2)
    colors = ['red', 'blue', 'green', 'white', 'magenta', 'cyan']
    chars = "ABCDEFGHIKLMNOPQRSTUVWXYZ1234567890@#$%^&*()_+"
    try:
        while True:
            line = "".join(random.choice(chars) for _ in range(80))
            print(colored(line, random.choice(colors)))
            time.sleep(0.01)
    except KeyboardInterrupt:
        print(colored("\n[!] Matrix Stopped.", "yellow"))
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
    print(colored("          👑 Body 👑", "red"))
    print(colored("    --- [ B7 MONSTER APOCALYPSE - v11.0 ] ---", "cyan"))
    print(colored("    --- [ 50+ TOOLS: ANDROID - WIFI - WEB - MATRIX ] ---", "white"))

def menu():
    print(colored("\n--- [ 📶 WiFi Warfare ] ---", "blue"))
    print("[1] Wifite (Auto)      [2] Airgeddon (Evil Twin)  [3] Fluxion (Phishing)")
    
    print(colored("\n--- [ 📱 Mobile Hacking ] ---", "magenta"))
    print("[10] PhoneSploit (ADB) [11] Ghost-Framework       [12] Ahmyth (RAT)")
    
    print(colored("\n--- [ 🚀 Web Attacks ] ---", "red"))
    print("[19] SQLMap (Auto)     [21] Commix (OS Inj)       [22] WPScan (WordPress)")
    
    print(colored("\n--- [ 🕵️ Social & OSINT ] ---", "green"))
    print("[31] SET (Social Tool) [33] Sherlock (User)       [35] SocialFish")
    
    print(colored("\n--- [ 🔑 Cracking ] ---", "white"))
    print("[40] John The Ripper   [41] Hydra (Brute Force)   [42] Hashcat (GPU)")
    
    print(colored("\n--- [ 🔒 Privacy & Fun ] ---", "yellow"))
    print("[46] Enable Tor Mode   [47] ⚡ Matrix Rain (NEW)   [48] ❤️ My Heart")
    print("[0] Exit")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(colored("\nB7-Monster > ", "cyan"))

        tools = {
            '1': ("sudo wifite", "Wifite"), '2': ("sudo airgeddon", "Airgeddon"), '3': ("fluxion", "Fluxion"),
            '10': ("sudo adb devices", "ADB-Check"), '11': ("ghost-framework", "Ghost"), '12': ("ahmyth", "Ahmyth"),
            '19': ("sqlmap", "SQLMap"), '21': ("commix", "Commix"), '22': ("wpscan", "WPScan"),
            '31': ("sudo set", "SET"), '33': ("sherlock", "Sherlock"), '40': ("john", "John"),
            '41': ("hydra", "Hydra"), '42': ("hashcat", "Hashcat")
        }

        if choice in tools:
            run_cmd(tools[choice][0], tools[choice][1])
        elif choice == '46':
            os.system("sudo service tor restart"); print(colored("[+] Tor Active!", "green")); time.sleep(2)
        elif choice == '47':
            matrix_effect()
        elif choice == '48':
            my_heart()
        elif choice == '0':
            break
        else:
            print(colored("[!] Invalid choice or Tool logic coming soon...", "yellow")); time.sleep(1)

if __name__ == "__main__":
    main()
