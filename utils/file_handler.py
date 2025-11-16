import csv
import os
from colorama import Fore, Style

def read_csv(filename):
    try:
        if not os.path.exists(filename):
            return []
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(Fore.RED + f"File {filename} tidak ditemukan!" + Style.RESET_ALL)
        return []
    except Exception as e:
        print(Fore.RED + f"Error membaca file: {e}" + Style.RESET_ALL)
        return []

def write_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)