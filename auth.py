import os
from utils.common import *
from colorama import Fore, Style
from utils.file_handler import read_csv

USER_FILE = "data/users.csv"

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
    
    data = read_csv(USER_FILE)
    if not data:
        print("list kosong!")
    else:
        for user in data:
            if user["username"] == username and user["password"] == password:
                return user["role"]
            else:
                print("login gagal")