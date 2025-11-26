from utils.common import *
from utils.file_handler import read_csv,write_csv

USER_FILE = "data/users.csv"
USER_FIELD = ["id", "username", "password", "role"]

def login():
    clear_screen()
    print(info + "\n=== Go Rent - Login ===")
    
    username = input("Username: ").strip()
    
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

def register():
    nama = input("masukkan username: ").strip()
    pw = input("masukkan password: ").strip()
    if not nama:
        print(warning + "Username Tidak Boleh Kosong!")
        input("Tekan Enter...")
        return
    if not pw:
        print("Password Tidak Boleh Kosong!")
        input("Tekan Enter...")
        return
    users = read_csv("data/users.csv")
    newusers = {
        "id": str(int(users[-1]["id"]) + 1),
        "username": nama, 
        "password": pw,
        "role": "staff"
        }
    users.append(newusers)
    write_csv(USER_FILE, users, USER_FIELD )
    print(done + "Akun Berhasil Dibuat!")
    input("Tekan Enter...")
