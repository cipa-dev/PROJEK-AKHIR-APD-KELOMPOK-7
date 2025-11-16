import os
from prettytable import PrettyTable
from utils.file_handler import read_csv, write_csv
from colorama import Fore, Style

VEHICLE_FILE = "data/vehicles.csv"
VEHICLE_FIELDS = ["id", "type", "brand", "model", "plate", "status"]

def clear_screen():
    os.system("cls || clear")

def list_vehicles():
    vehicles = read_csv(VEHICLE_FILE)
    if not vehicles:
        print(Fore.YELLOW + "Tidak ada kendaraan terdaftar." + Style.RESET_ALL)
        return
    table = PrettyTable()
    table.field_names = ["ID", "Tipe", "Merek", "Model", "Plat", "Status"]
    for v in vehicles:
        table.add_row([v["id"], v["type"], v["brand"], v["model"], v["plate"], v["status"]])
    print(table)

def add_vehicle():
    clear_screen()
    print(Fore.BLUE + "=== TAMBAH KENDARAAN ===" + Style.RESET_ALL)
    vehicles = read_csv(VEHICLE_FILE)
    new_id = str(len(vehicles) + 1)
    v_type = input("Tipe kendaraan (motor/mobil): ").strip()
    brand = input("Merek: ").strip()
    model = input("Model: ").strip()
    plate = input("Nomor Plat: ").strip()
    vehicle = {
        "id": new_id,
        "type": v_type,
        "brand": brand,
        "model": model,
        "plate": plate,
        "status": "available"
    }
    vehicles.append(vehicle)
    write_csv(VEHICLE_FILE, vehicles, VEHICLE_FIELDS)
    print(Fore.GREEN + "\nKendaraan berhasil ditambahkan!" + Style.RESET_ALL)

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
            write_csv(VEHICLE_FILE, vehicles, VEHICLE_FIELDS)
            print(Fore.GREEN + "\nKendaraan berhasil diperbarui!" + Style.RESET_ALL)
            return
    print(Fore.RED + "\nKendaraan tidak ditemukan!" + Style.RESET_ALL)

def delete_vehicle():
    clear_screen()
    list_vehicles()
    vid = input("\nID kendaraan yang ingin dihapus: ").strip()
    
    if not vid:
        print(Fore.RED + "❌ ID tidak boleh kosong!" + Style.RESET_ALL)
        return

    vehicles = read_csv(VEHICLE_FILE)
    if not any(v["id"] == vid for v in vehicles):
        print(Fore.RED + "❌ ID kendaraan tidak ditemukan!" + Style.RESET_ALL)
        return

    vehicles = [v for v in vehicles if v["id"] != vid]
    write_csv(VEHICLE_FILE, vehicles, VEHICLE_FIELDS)
    print(Fore.GREEN + "\n✅ Kendaraan berhasil dihapus!" + Style.RESET_ALL)