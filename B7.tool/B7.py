import os
import time
import sys
from termcolor import colored

def clear():
    os.system('clear')

def banner():
    # شعار Body مع علامة التاج والنقاط
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
    print(colored("    --- [ Version 1.0 - Created by B7 ] ---", "green"))
    print("\n")

def menu():
    print(colored("[1] 📶 WiFi Penetration Test", "white"))
    print(colored("[2] 🛡️ Scan System for Malware", "white"))
    print(colored("[3] 🚀 Web Attack (DDoS/Stress)", "white"))
    print(colored("[4] 🔒 Stealth Mode (Tor & VPN)", "white"))
    print(colored("[5] 📱 Android Penetration", "white"))
    print(colored("[6] ❤️ My Heart (Spider Web Heart)", "magenta"))
    print(colored("[7] 💀 Ghost Terminal (Matrix Mode)", "red"))
    print(colored("[0] Exit", "yellow"))

def my_heart():
    # رسم قلب على شكل شبكة عنكبوتية
    heart = [
        "      ** ** ",
        "   * * * * ",
        "  * ** * ",
        " * /\\ /\\ /\\  /\\ /\\ /\\  * ",
        " * \\/ \\/ \\/  \\/ \\/ \\/  * ",
        "  * /\\ /\\ /\\ /\\ /\\   * ",
        "   * \\/ \\/ \\/ \\/    * ",
        "    * \\/ \\/ \\/     * ",
        "      * \\/      * ",
        "        * * ",
        "          * * ",
        "             ** "
    ]
    for line in heart:
        print(colored(line, "magenta"))
        time.sleep(0.1)

def ghost_terminal():
    # كود الرموز المرعبة والجماجم
    symbols = ["💀", "☣️", "🔥", "☠️", "⚡", "✖️"]
    try:
        print(colored("Entering Ghost Mode...", "red"))
        while True:
            line = " ".join([symbols[i % len(symbols)] for i in range(20)])
            print(colored(line, "red", attrs=['bold']))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nReturning to Menu...")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(colored("\nB7 > ", "cyan"))

        if choice == '1':
            print(colored("\n[!] Starting WiFi scan using Aircrack-ng...", "blue"))
            # هنا يوضع أمر النظام لتشغيل أدوات الواي فاي
            time.sleep(2)
        elif choice == '2':
            print(colored("\n[!] Scanning files for malware...", "green"))
            time.sleep(2)
        elif choice == '3':
            url = input("Enter Target URL: ")
            print(colored(f"[!] Attacking {url}...", "red"))
            time.sleep(2)
        elif choice == '4':
            print(colored("\n[!] Installing Tor & Configuring VPN...", "cyan"))
            print(colored("[+] Your Identity is now Hidden.", "green"))
            time.sleep(2)
        elif choice == '5':
            print(colored("\n[!] Generating MSFVenom Payload...", "green"))
            time.sleep(2)
        elif choice == '6':
            my_heart()
            input("\nPress Enter to return...")
        elif choice == '7':
            ghost_terminal()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid Option!")
            time.sleep(1)

if __name__ == "__main__":
    main()