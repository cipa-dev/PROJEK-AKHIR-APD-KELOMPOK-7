# Local modules
from utils.auth import *
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
        choice = questionary.select(
            "Apa pilihan ?",
            choices=[
                "Kelola Kendaraan",
                "Kelola Pelanggan",
                "Lihat Semua Transaksi",
                "Kembali ke Login"
            ]
        ).ask()

        if choice == "Kelola Kendaraan":
            manage_vehicles()
        elif choice == "Kelola Pelanggan":
            manage_customers()
        elif choice == "Lihat Semua Transaksi":
            clear_screen()
            list_transactions()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Kembali ke Login":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")


def manage_vehicles():
    while True:
        clear_screen()
        print(menu + "=== KELOLA KENDARAAN ===")
        choice = questionary.select(
            "Apa pilihan ?",
            choices=[
                "Lihat Semua Kendaraan",
                "Tambah Kendaraan",
                "Update Kendaraan",
                "Hapus Kendaraan",
                "Kembali",
            ]
        ).ask()

        if choice == "Lihat Semua Kendaraan":
            list_vehicles()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Tambah Kendaraan":
            add_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Update Kendaraan":
            update_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Hapus Kendaraan":
            delete_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Kembali":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")


def manage_customers():
    while True:
        clear_screen()
        print(menu + "=== KELOLA PELANGGAN ===")
        choice = questionary.select(
            "Apa pilihan ?",
            choices=[
                "Lihat Semua Pelanggan",
                "Tambah Pelanggan",
                "Update Pelanggan",
                "Hapus Pelanggan",
                "Kembali",
            ]
        ).ask()
        if choice == "Lihat Semua Pelanggan":
            list_customers()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Tambah Pelanggan":
            add_customer()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Update Pelanggan":
            update_customer()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Hapus Pelanggan":
            delete_customer()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Kembali":
            break
        else:
            print(warning + "Pilihan tidak valid!")
            input("Tekan Enter...")


def staff_menu():
    while True:
        clear_screen()
        print(menu + "=== MENU STAFF ===")
        choice = questionary.select(
            "Apa pilihan ?",
            choices=[
                "Sewa Kendaraan",
                "Kembalikan Kendaraan",
                "Lihat Transaksi",
                "Kembali ke Login",
            ]
        ).ask()

        if choice == "Sewa Kendaraan":
            rent_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Kembalikan Kendaraan":
            return_vehicle()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Lihat Transaksi":
            clear_screen()
            list_transactions()
            input("\nTekan Enter untuk kembali...")
        elif choice == "Kembali ke Login":
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
            choices=["login", "register", "exit"]
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
