# BY VIKO
# pip install requests
# pip install colorama

import requests
from colorama import init, Fore, Back, Style
init(autoreset=True)

chate = raw_input("Kirim pesan kesimi : ")

response = requests.get('https://viko-api.herokuapp.com/api/f/simi?apikey=rxking&query=' + chate)
viko = response

print(Back.YELLOW + Fore.YELLOW + viko.json()["result"])
