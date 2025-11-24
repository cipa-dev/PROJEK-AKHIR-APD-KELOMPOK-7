from prettytable import PrettyTable
from utils.file_handler import read_csv, write_csv
from utils.common import *

CUSTOMER_FILE = "data/customers.csv"
CUSTOMER_FIELDS = ["id", "name", "phone", "license"]

def list_customers():
    customers = read_csv(CUSTOMER_FILE)
    if not customers:
        print(warning + "Tidak ada pelanggan terdaftar.")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Telepon", "SIM"]
    for c in customers:
        table.add_row([c["id"], c["name"], c["phone"], c["license"]])
    print(table)

def add_customer():
    customers = read_csv(CUSTOMER_FILE)
    new_id = str(int(customers[-1]["id"]) + 1)
    name = input("Nama: ").strip()
    phone = input("Telepon: ").strip()
    license_no = input("Nomor SIM: ").strip()
    customer = {"id": new_id, "name": name, "phone": phone, "license": license_no}
    customers.append(customer)
    write_csv(CUSTOMER_FILE, customers, CUSTOMER_FIELDS)
    print(done + "Pelanggan berhasil ditambahkan!")

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
            print(done + "Pelanggan berhasil diperbarui!")
            return
    print(warning + "Pelanggan tidak ditemukan!")

def delete_customer():
    list_customers()
    cid = input("ID pelanggan yang ingin dihapus: ").strip()
    customers = read_csv(CUSTOMER_FILE)
    customers = [c for c in customers if c["id"] != cid]
    write_csv(CUSTOMER_FILE, customers, CUSTOMER_FIELDS)
    print(done + "Pelanggan berhasil dihapus!")