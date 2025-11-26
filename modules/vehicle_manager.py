from prettytable import PrettyTable
from utils.file_handler import read_csv, write_csv
from utils.common import *
import questionary

VEHICLE_FILE = "data/vehicles.csv"
VEHICLE_FIELDS = ["id", "type", "brand", "model", "plate", "status", "price"]

def clear_screen():
    os.system("cls || clear")

def list_vehicles():
    vehicles = read_csv(VEHICLE_FILE)
    if not vehicles:
        print(warning + "Tidak ada kendaraan terdaftar.")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Tipe", "Merek", "Model", "Plat", "Status", "Price"]
    for v in vehicles:
        table.add_row([v["id"], v["type"], v["brand"], v["model"], v["plate"], v["status"], v["price"]])
    print(table)

def add_vehicle():
    clear_screen()
    print(menu + "=== TAMBAH KENDARAAN ===")
    vehicles = read_csv(VEHICLE_FILE)
    new_id = str(int(vehicles[-1]["id"]) + 1)
    v_type = questionary.select(
        "Tipe kendaraan: ",
        choices=["motor","mobil"]
    ).ask()
    brand = input("Merek: ").strip()
    model = input("Model: ").strip()
    plate = input("Nomor Plat: ").strip()
    price = input("Harga Sewa: ").strip()
    vehicle = {
        "id": new_id,
        "type": v_type,
        "brand": brand,
        "model": model,
        "plate": plate,
        "price": price,
        "status": "available"
    }
    vehicles.append(vehicle)
    write_csv(VEHICLE_FILE, vehicles, VEHICLE_FIELDS)
    print(done + "\nKendaraan berhasil ditambahkan!")

def update_vehicle():
    clear_screen()
    list_vehicles()
    vid = input("\nMasukkan ID kendaraan yang ingin diupdate: ").strip()
    vehicles = read_csv(VEHICLE_FILE)
    for v in vehicles:
        if v["id"] == vid:
            print(f"\nMengupdate kendaraan: {v['brand']} {v['model']} ({v['plate']})")
            v["type"] = input(f"Tipe ({v['type']}): ").strip() or v["type"]
            v["brand"] = input(f"Merek ({v['brand']}): ").strip() or v["brand"]
            v["model"] = input(f"Model ({v['model']}): ").strip() or v["model"]
            v["plate"] = input(f"Plat ({v['plate']}): ").strip() or v["plate"]
            v["price"] = input(f"Plat ({v['price']}): ").strip() or v["price"]
            write_csv(VEHICLE_FILE, vehicles, VEHICLE_FIELDS)
            print(done + "\nKendaraan berhasil diperbarui!")
            return
    print(warning + "\nKendaraan tidak ditemukan!")

def delete_vehicle():
    clear_screen()
    list_vehicles()
    vid = input("\nID kendaraan yang ingin dihapus: ").strip()
    
    if not vid:
        print(warning + "ID tidak boleh kosong!")
        return

    vehicles = read_csv(VEHICLE_FILE)
    if not any(v["id"] == vid for v in vehicles):
        print(warning + "ID kendaraan tidak ditemukan!")
        return

    vehicles = [v for v in vehicles if v["id"] != vid]
    write_csv(VEHICLE_FILE, vehicles, VEHICLE_FIELDS)
    print(done + "\nKendaraan berhasil dihapus!")