import requests
import os 
import colorama 
from termcolor import colored


os.system("cls")

print(colored("""


                ░▒█░░▒█░▒█▀▀▀░▒█▀▀▄░▒█░▒█░▒█▀▀▀█░▒█▀▀▀█░▒█░▄▀░░░▒█▀▀▄░▒█▀▀▀░▒█░░░░▒█▀▀▀░▀▀█▀▀░▒█▀▀▀░▒█▀▀▄
                ░▒█▒█▒█░▒█▀▀▀░▒█▀▀▄░▒█▀▀█░▒█░░▒█░▒█░░▒█░▒█▀▄░░░░▒█░▒█░▒█▀▀▀░▒█░░░░▒█▀▀▀░░▒█░░░▒█▀▀▀░▒█▄▄▀
                ░▒▀▄▀▄▀░▒█▄▄▄░▒█▄▄█░▒█░▒█░▒█▄▄▄█░▒█▄▄▄█░▒█░▒█░░░▒█▄▄█░▒█▄▄▄░▒█▄▄█░▒█▄▄▄░░▒█░░░▒█▄▄▄░▒█░▒█
""", 'green'))
print(colored("                                                            by Kazu :p", 'red'))
webhook_url = input(colored("[+] Enter your webhook url : ", 'blue'))

response = requests.delete(webhook_url)
if response.status_code == 204:
    print(colored("[+] Webhook deleted ! :p.", 'green'))
else:
    print(colored("[/] Webhook invalid !", 'red'))