import csv
import os
from colorama import Fore, Style
from utils.common import*

def read_csv(filename):
    try:
        if not os.path.exists(filename):
            return []
        with open(file=filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(warning + f"File {filename} tidak ditemukan!")
        return []
    except Exception as e:
        print(warning + f"Error membaca file: {e}")
        return []

def write_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)