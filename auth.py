from utils.common import *
from utils.file_handler import read_csv

USER_FILE = "data/users.csv"

def login():
    clear_screen()
    print(info + "\n=== Go Rent - Login ===")
    print(exit + "Ketik 'exit' sebagai username untuk keluar.\n")
    
    username = input("Username: ").strip()
    if username.lower() == "exit":
        return "exit"
    
    if not username:
        print(warning + "❌ Username tidak boleh kosong!")
        input("Tekan Enter...")
        return None

    password = input("Password: ").strip()
    if not password:
        print(warning + "❌ Password tidak boleh kosong!")
        input("Tekan Enter...")
        return None
    
    data = read_csv(USER_FILE)
    if not data:
        print(warning + "list kosong!")
    else:
        for user in data:
            if user["username"] == username and user["password"] == password:
                return user["role"]
            else:
                print(warning + "login gagal")