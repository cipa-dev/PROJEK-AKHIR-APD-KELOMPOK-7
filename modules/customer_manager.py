from prettytable import PrettyTable
from utils.file_handler import read_csv, write_csv
from colorama import Fore, Style

CUSTOMER_FILE = "data/customers.csv"
CUSTOMER_FIELDS = ["id", "name", "phone", "license"]

def list_customers():
    customers = read_csv(CUSTOMER_FILE)
    if not customers:
        print(Fore.YELLOW + "Tidak ada pelanggan terdaftar." + Style.RESET_ALL)
        return
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Telepon", "SIM"]
    for c in customers:
        table.add_row([c["id"], c["name"], c["phone"], c["license"]])
    print(table)

def add_customer():
    customers = read_csv(CUSTOMER_FILE)
    new_id = str(len(customers) + 1)
    name = input("Nama: ").strip()
    phone = input("Telepon: ").strip()
    license_no = input("Nomor SIM: ").strip()
    customer = {"id": new_id, "name": name, "phone": phone, "license": license_no}
    customers.append(customer)
    write_csv(CUSTOMER_FILE, customers, CUSTOMER_FIELDS)
    print(Fore.GREEN + "Pelanggan berhasil ditambahkan!" + Style.RESET_ALL)

def update_customer():
    list_customers()
    cid = input("ID pelanggan yang ingin diupdate: ").strip()
    customers = read_csv(CUSTOMER_FILE)
    for c in customers:
        if c["id"] == cid:
            c["name"] = input(f"Nama ({c['name']}): ") or c["name"]
            c["phone"] = input(f"Telepon ({c['phone']}): ") or c["phone"]
            c["license"] = input(f"SIM ({c['license']}): ") or c["license"]
            write_csv(CUSTOMER_FILE, customers, CUSTOMER_FIELDS)
            print(Fore.GREEN + "Pelanggan berhasil diperbarui!" + Style.RESET_ALL)
            return
    print(Fore.RED + "Pelanggan tidak ditemukan!" + Style.RESET_ALL)

def delete_customer():
    list_customers()
    cid = input("ID pelanggan yang ingin dihapus: ").strip()
    customers = read_csv(CUSTOMER_FILE)
    customers = [c for c in customers if c["id"] != cid]
    write_csv(CUSTOMER_FILE, customers, CUSTOMER_FIELDS)
    print(Fore.GREEN + "Pelanggan berhasil dihapus!" + Style.RESET_ALL)