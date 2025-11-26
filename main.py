# Local modules
from auth import *
from utils.common import *
from modules.vehicle_manager import list_vehicles, add_vehicle, update_vehicle, delete_vehicle, clear_screen
from modules.customer_manager import list_customers, add_customer, update_customer, delete_customer
from modules.transaction_manager import list_transactions, rent_vehicle, return_vehicle
import questionary

# Inisialisasi Colorama
init(autoreset=True)

def admin_menu():
    while True:
        clear_screen()
        print(menu + "=== MENU ADMIN ===")
        print("1. Kelola Kendaraan")
        print("2. Kelola Pelanggan")
        print("3. Lihat Semua Transaksi")
        print("4. Kembali ke Login")
        choice = input("\nPilih menu (1-4): ").strip()

        if choice == "1":
            manage_vehicles()
        elif choice == "2":
            manage_customers()
        elif choice == "3":
            clear_screen()
            list_transactions()
            input("\nTekan Enter untuk kembali...")
        elif choice == "4":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")

def manage_vehicles():
    while True:
        clear_screen()
        print(menu + "=== KELOLA KENDARAAN ===")
        print("1. Lihat Semua Kendaraan")
        print("2. Tambah Kendaraan")
        print("3. Update Kendaraan")
        print("4. Hapus Kendaraan")
        print("5. Kembali")
        choice = input("\nPilih (1-5): ").strip()

        if choice == "1":
            list_vehicles()
            input("\nTekan Enter untuk kembali...")
        elif choice == "2":
            add_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "3":
            update_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "4":
            delete_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "5":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")

def manage_customers():
    while True:
        clear_screen()
        print(menu + "=== KELOLA PELANGGAN ===")
        print("1. Lihat Semua Pelanggan")
        print("2. Tambah Pelanggan")
        print("3. Update Pelanggan")
        print("4. Hapus Pelanggan")
        print("5. Kembali")
        choice = input("\nPilih (1-5): ").strip()

        if choice == "1":
            list_customers()
            input("\nTekan Enter untuk kembali...")
        elif choice == "2":
            add_customer()
            input("\nTekan Enter untuk kembali...")
        elif choice == "3":
            update_customer()
            input("\nTekan Enter untuk kembali...")
        elif choice == "4":
            delete_customer()
            input("\nTekan Enter untuk kembali...")
        elif choice == "5":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")

def staff_menu():
    while True:
        clear_screen()
        print(menu + "=== MENU STAFF ===")
        print("1. Sewa Kendaraan")
        print("2. Kembalikan Kendaraan")
        print("3. Lihat Transaksi")
        print("4. Kembali ke Login")
        choice = input("\nPilih menu (1-4): ").strip()

        if choice == "1":
            rent_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "2":
            return_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "3":
            clear_screen()
            list_transactions()
            input("\nTekan Enter untuk kembali...")
        elif choice == "4":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")

def main():
    while True:
        clear_screen()
        print(exit + "=== SELAMAT DATANG DI GO RENT ===")
        print("Sistem Penyewaan Kendaraan di Terminal")

        pilihan = questionary.select(
            "pilihan: ",
        choices= ["login", "register", "exit"]
        ).ask()
        
        if pilihan == "login": 
            print("menu login")
            role = login()
            if role == "admin":
                admin_menu()
            elif role == "staff":
                staff_menu()
            else:
                print("kamu bukan siapa siapa")
        elif pilihan == "register":
            register()
        elif pilihan == "exit":
            break

if __name__ == "__main__":
    main()