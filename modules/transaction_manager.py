from prettytable import PrettyTable
from utils.file_handler import read_csv, write_csv
from utils.common import *
from datetime import datetime, timedelta
from utils.hitung import hitung_hari_sewa, hitung_hari_telat, hitung_denda

TRANSACTION_FILE = "data/transactions.csv"
TRANSACTION_FIELDS = ["id", "customer_id", "vehicle_id", "rent_date", "return_date", "status", "price"]  # status: rented/returned
VEHICLE_FILE = "data/vehicles.csv"
CUSTOMER_FILE = "data/customers.csv"

def list_transactions():
    transactions = read_csv(TRANSACTION_FILE)
    if not transactions:
        print(warning + "Tidak ada transaksi.")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Pelanggan ID", "Kendaraan ID", "Sewa", "Kembali", "Status"]
    for t in transactions:
        table.add_row([t["id"], t["customer_id"], t["vehicle_id"], t["rent_date"], t["return_date"] or "-", t["status"]])
    print(table)

def rent_vehicle():
    from modules.vehicle_manager import VEHICLE_FILE
    from modules.customer_manager import CUSTOMER_FILE

    vehicles = read_csv(VEHICLE_FILE)
    customers = read_csv(CUSTOMER_FILE)

    print(menu + "\n--- Daftar Kendaraan Tersedia ---")
    available = [v for v in vehicles if v["status"] == "available"]
    if not available:
        print(warning + "Tidak ada kendaraan tersedia!")
        return

    v_table = PrettyTable()
    v_table.field_names = ["ID", "Tipe", "Merek", "Plat","Price"]
    for v in available:
        v_table.add_row([v["id"], v["type"], v["brand"], v["plate"], v["price"]])
    print(v_table)

    vid = input("Pilih ID kendaraan: ").strip()
    selected_vehicle = next((v for v in available if v["id"] == vid), None)
    if not selected_vehicle:
        print(Fore.RED + "Kendaraan tidak valid atau tidak tersedia!" + Style.RESET_ALL)
        return

    print(menu + "\n--- Daftar Pelanggan ---")
    list_customers()
    cid = input("Masukkan ID pelanggan: ").strip()
    if not any(c["id"] == cid for c in customers):
        print(warning + "Pelanggan tidak ditemukan!")
        return

    transactions = read_csv(TRANSACTION_FILE)
    new_id = str(len(transactions) + 1)
    rent_date = datetime.now().strftime("%Y-%m-%d")

    # Update status kendaraan
    for v in vehicles:
        if v["id"] == vid:
            v["status"] = "rented"
    from utils.file_handler import write_csv as write_csv_util
    write_csv_util(VEHICLE_FILE, vehicles, ["id", "type", "brand", "model", "plate", "status","price"])

    transaction = {
        "id": new_id,
        "customer_id": cid,
        "vehicle_id": vid,
        "rent_date": rent_date,
        "return_date": "",
        "status": "rented"
    }
    transactions.append(transaction)
    write_csv(TRANSACTION_FILE, transactions, TRANSACTION_FIELDS)
    print(done + "Kendaraan berhasil disewa!")

def return_vehicle():
    transactions = read_csv(TRANSACTION_FILE)
    vehicles = read_csv(VEHICLE_FILE)

    rented = [t for t in transactions if t["status"] == "rented"]
    if not rented:
        print(warning + "Tidak ada kendaraan yang sedang disewa.")
        return

    print(menu + "\n--- Kendaraan yang Sedang Disewa ---")
    table = PrettyTable()
    table.field_names = ["Transaksi ID", "Pelanggan ID", "Kendaraan ID"]
    for t in rented:
        table.add_row([t["id"], t["customer_id"], t["vehicle_id"]])
    print(table)

    tid = input("Masukkan ID transaksi untuk pengembalian: ").strip()
    selected = next((t for t in rented if t["id"] == tid), None)
    if not selected:
        print(warning + "Transaksi tidak ditemukan!")
        return

    

    hari_sewa = hitung_hari_sewa(selected["rent_date"], return_date) 
    hari_telat = hitung_hari_telat(tgl_batasSewa_str, return_date) 
    denda = hitung_denda(hari_telat)

    kendaraan = next((v for v in vehicles if v["id"] == selected["vehicle_id"]), None)
    if not kendaraan:
        print(Fore.RED + "Data kendaraan tidak ditemukan!" + Style.RESET_ALL)
        return
    
    price_per_hari = int(kendaraan["price"])
    biaya_sewa = hari_sewa * price_per_hari
    total = biaya_sewa + denda

    # Struk
    table = PrettyTable()
    table.field_names = ["Rincian", "Detail"]
    table.align = "l" 
    table.add_row(["Tanggal Sewa", selected["rent_date"]])
    table.add_row(["Tanggal Kembali", return_date])
    table.add_row(["Batas Sewa (3 hari)", tgl_batasSewa_str])
    table.add_row(["Harga / Hari", f"Rp {price_per_hari:,}"])
    table.add_row(["Total Hari Sewa", f"{hari_sewa} hari"])
    table.add_row(["Hari Telat Kembali", f"{hari_telat} hari"])
    table.add_row(["Denda", f"Rp {denda:,}"])
    table.add_row(["Biaya Sewa", f"Rp {biaya_sewa:,}"])
    table.add_row(["TOTAL", f"Rp {total:,}"])
    print(table)

    # Update status kendaraan
    for v in vehicles:
        if v["id"] == selected["vehicle_id"]:
            v["status"] = "available"

    # Update transaksi
    for t in transactions:
        if t["id"] == tid:
            t["return_date"] = return_date
            t["status"] = "returned"

    # Simpan ke CSV
    write_csv(TRANSACTION_FILE, transactions, TRANSACTION_FIELDS)
    write_csv(VEHICLE_FILE, vehicles, ["id", "type", "brand", "model", "plate", "status", "price"])

    print(done + "Kendaraan berhasil dikembalikan!" + Style.RESET_ALL)
    
# Aliases untuk reuse
def list_customers():
    from modules.customer_manager import list_customers as lc
    lc()
