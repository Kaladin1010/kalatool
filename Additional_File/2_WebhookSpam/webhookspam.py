import requests
import time
from colorama import Fore
import os
import ctypes
from pyfade import Fade, Colors
from pycenter import center
from os import system, mkdir, name

def clear():
    system("cls" if name == 'nt' else "clear")


clear()

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("[KalaTool] - WebHooks Spam")
    kalahome()
    print()
    print(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } URL du webhooks pour le spam: """)
    webhook = input(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } WebHooks: """)
    print(f"""\n\n{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Message a spams: """)
    message = input(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Message: """)
    print(f"""\n\n{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Temps de l'attaque (secondes): """)
    timer = input(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Montant: """)
    input(f"""\n\n\n\n{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Appuyez sur ENTER pour valider""")

    try:
        timeout = time.time() + 1 * float(timer) + 2

        while time.time() < timeout:
            response = requests.post(
                webhook,
                json = {"content" : message},
                params = {'wait' : True}
            )
            os.system('cls')
            time.sleep(1)
            if response.status_code == 204 or response.status_code == 200:
                print(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTGREEN_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Message envoyé""")
            elif response.status_code == 429:
                print(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Rate limited ({response.json()['retry_after']}ms)""")
                time.sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Error code: {response.status_code}""")
    except:
        print(f"""      {Fore.LIGHTRED_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Votre demande est invalide !""")
        time.sleep(2)
        os.system('cls')
        exit(0)
    
main()