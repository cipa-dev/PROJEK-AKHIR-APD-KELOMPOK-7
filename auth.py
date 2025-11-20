import os
from colorama import Fore, Style

def clear_screen():
    os.system("cls || clear")

def login():
    clear_screen()
    print(Fore.CYAN + "\n=== Go Rent - Login ===" + Style.RESET_ALL)
    print(Fore.YELLOW + "Ketik 'exit' sebagai username untuk keluar.\n" + Style.RESET_ALL)
    
    username = input("Username: ").strip()
    if username.lower() == "exit":
        return "exit"
    
    # Validasi username tidak boleh kosong
    if not username:
        print(Fore.RED + "❌ Username tidak boleh kosong!" + Style.RESET_ALL)
        input("Tekan Enter...")
        return None

    password = input("Password: ").strip()
    if not password:
        print(Fore.RED + "❌ Password tidak boleh kosong!" + Style.RESET_ALL)
        input("Tekan Enter...")
        return None
    
    # perbaiki Login nya
    if username == "admin" and password == "admin123":
        return "admin"
    elif username == "staff" and password == "staff123":
        return "staff"
    else:
        return None