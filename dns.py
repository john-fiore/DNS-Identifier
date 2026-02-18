from colorama import Fore as col
import socket as sock
import os, sys

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_dns(ip: str):
    try:
        hostinfo = sock.gethostbyaddr(ip)
        hostname = hostinfo[0]
        print(f"{col.CYAN}IP Address: {col.RESET}{ip}")
        if hostname == sock.gethostname():
            print(f"{col.YELLOW}Hostname: {col.RESET}{hostname} {col.GREEN}(that's you!){col.RESET}")
        else:
            print(f"{col.YELLOW}Hostname: {col.RESET}{hostname}")
    except sock.herror as ex:
        print(f"{col.RED}Error: {col.RESET}Could not resolve name for IP Address '{ip}' - {ex}")
        print()
        input(f"Press {col.YELLOW}[ENTER]{col.RESET} to continue...")
        main()
    except Exception as ex:
        print(f"{col.RED}An unexpected error has occurred: {col.RESET}{ex}")
        print()
        input(f"Press {col.YELLOW}[ENTER]{col.RESET} to continue...")
        main()

def main():
    clear()
    print("Welcome to DNS Identifier.")
    print("*" * 53)
    print("Simply enter an IP Address, and you will recieve")
    print("the inputted IP address and it's hostname.")
    print("*" * 53)
    entered_ip = input("Enter an IP: ")
    
    clear()
    get_dns(entered_ip)
    print("*" * 53)
    restart = input("Would you like to go again? (y/n): ").lower()
    
    if restart == "y":
        main()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()