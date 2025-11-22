import os
from colorama import *
init(autoreset=True)
def clear_screen():
    os.system("cls || clear")

info = Fore.CYAN + Style.BRIGHT
warning =  Fore.RED + Style.BRIGHT
exit = Fore.YELLOW + Style.BRIGHT
menu = Fore.BLUE + Style.BRIGHT
done = Fore.GREEN + Style.BRIGHT
