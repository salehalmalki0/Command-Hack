                            #Start Proamm,#
import os
import random
import string
from time import ctime, sleep
import socket
class Commands:
    def __init__(self):
        try:
            import requests
            import colorama
            import hashlib
            import tqdm
            import whois
            import pyfiglet as pf
            import bs4
        except:
            os.system('pip install requests')
            os.system('pip install colorama')
            os.system('pip install hashlib')
            os.system('pip install python-whois')
            os.system('pip install pyfiglet')
            os.system('pip inbstall tqdm')
            os.system('pip install bs4')
            os.system('cls')
        os.system('cls')
        import Ascii
        def commands():
            self.Username = input(colorama.Fore.RED+'[+] Enter Username : ')
            if self.Username == '':
                print('[!]~ Place Enter Username, Not Space')
                commands()
            print('-' * 50)
            def dir():
                if self.UserCommands == 'ls' or self.UserCommands == 'dir':
                    os.system('dir')
            def clear():
                if self.UserCommands == 'clear' or self.UserCommands == 'cls':
                    os.system('cls')
            def time():
                if self.UserCommands == 'date':
                    print(ctime())
            def mkdir():
                if self.UserCommands == 'mkdir':
                    try:
                        self.NameF = input('~NameF : ')
                        if self.NameF == '':
                            print('[!]~Place Enter NameF, Not Sapce')
                        os.system(f'mkdir {self.NameF}')
                    except:
                        print('[! Error]')
            def pwd():
                if self.UserCommands == 'pwd':
                    os.system('cd')
            def cat():
                if self.UserCommands == 'cat':
                    try:
                        self.doc = input('~Where : ')
                        if self.doc == '':
                            print('[!]~Place Enter Doc, Not Sapce')
                        file = open(self.doc)
                        print(file.read())
                    except:
                        print('[! Error]')
            def start_python():
                if self.UserCommands == 'python':
                    os.system('python')
            def ipcon():
                if self.UserCommands == 'ipconfig':
                    os.system('ipconfig')
            def ipsites():
                if self.UserCommands == 'ip':
                    try:
                        self.ipSites = input('~Enter Url : ')
                        if self.ipSites == '':
                            print('[!]~Place Enter Url, Not Sapce')
                        ip=socket.gethostbyname(self.ipSites)
                        print(colorama.Fore.RED+'You ip : '+ip)
                    except:
                        print('[! Error]')
            def content_page():
                if self.UserCommands == 'content':
                    try:
                        self.PageCon = input('~Enter Url -: ')
                        if self.PageCon == '':
                            print('[!]~Place Enter Url, Not Sapce')
                            content_page()
                        self.page = requests.get(self.PageCon)
                        self.soup = bs4.BeautifulSoup(self.page.content, 'html.parser')
                        print(self.soup)
                        self.saves_c = input('~Do Want to save Content ? (y - n) : ')
                        if self.saves_c == 'y':
                            with open('./content.txt','w',encoding='utf8') as self.f:
                                self.f.write(str(self.soup))
                        if self.saves_c == 'n':
                            pass
                    except:
                        print('[!] Error')
            def echo():
                if 'echo' in self.UserCommands:
                    os.system(self.UserCommands)
            def Network():
                if self.UserCommands == 'networks':
                    os.system('netstat')
            def sysinfo():
                if self.UserCommands == 'sysinfo':
                    os.system('systeminfo')
            def rm():
                if self.UserCommands == 'rm':
                    self.InputUserDoc = input('~Where : ')
                    os.system(f'rmdir {self.InputUserDoc}')
            def by():
                if self.UserCommands == 'by':
                    sleep(1)
                    os.system('cls')
                    from Ascii import By
                    print(By)
                    sleep(5)
                    os.system('cls')
            def neo():
                if self.UserCommands == 'neo':
                    from Ascii import Neo
                    print(colorama.Fore.RED+Neo)
            def infos():
                if self.UserCommands == 'infos':
                    try:
                        self.wi = input('~Url -: ')
                        if self.wi == '':
                            print('Place Enter Url, Not Space')
                            infos()
                        self.s = whois.whois(self.wi)
                        print(self.s)
                    except:
                        print('[! Error]')
            def fig():
                try:
                    if self.UserCommands == 'figlet':
                        self.fi = input('~TextF -: ')
                        if self.fi == '':
                            print('[!] Not Space')
                        self.f = pf.figlet_format(self.fi)
                        print(self.f)
                except:
                    print('[!] Error')
            def fsname():
                if self.UserCommands == 'fname':
                    try:
                        self.sn = socket.gethostname()
                        print(colorama.Fore.RED+'This is : '+self.sn)
                    except:
                        print('[!] Error')
            def listemailp():
                if self.UserCommands == 'listep':
                    try:
                        self.num = int(input('~Enter Num list email & pass -: '))
                        if self.num == '':
                            print('[!]~Enetr Num,')
                            listemailp()
                        def r_c(char):
                            return ''.join(random.choice(string.ascii_letters) for _ in range(char))
                        for i in range(self.num):
                            email = r_c(7)
                            passw = r_c(11)
                            print(colorama.Fore.RED+'=' * 20)
                            print(f'Num : {i}')
                            print(f'Email : {email}@gmail.com \npassword : {passw}')
                    except:
                        print('[!] Error')
            def hash_text():
                if self.UserCommands == 'hash':
                    try:
                        self.data = input('~Enter You Text -: ')
                        if self.data == '':
                            print('[!]~Not Space')
                        self.hash = hashlib.new('md5')
                        self.hash.update(self.data.encode('utf-8'))
                        print(self.hash.hexdigest())
                    except:
                        print('[!] Error')
            
            def help():
                if self.UserCommands.lower() == 'help':
                    print(
                        '''
                    |-------------------------------------|
                    |Command | Tariff                     |
                    |--------------------------------------
                    |dir/ls ->> Show                      |
                    |clear/cls ->> clear Command          |
                    |date ->> Show Date                   |
                    |mkdir ->> Create Folder              |
                    |pwd ->> print path                   |
                    |cat ->> start documnets              |
                    |python ->> start command python      |
                    |ifconfig ->> print info network      |
                    |ip ->> print ip sites                |
                    |content ->> print src page site      |
                    |echo ->> print string or text        |
                    |networks ->> print network stats     |
                    |sysinfo ->> print system informations|
                    |rm ->> delete folder/doc             |
                    |by ->> informations Programmer       |
                    |neo ->> print background             |
                    |infos ->> print informations websites|
                    |figlet ->> print Text Ascii          |
                    |fname ->> print name the host        |
                    |listep ->> Create Email & Pass Fake  |
                    |hash ->> encryption Text             |
                    |exit ->> quit program                |
                    |-------------------------------------|
                        '''
                    )
            while True:
                self.UserCommands = input(
                    colorama.Fore.YELLOW+f'└─{self.Username}@M7 $ '
                )
                if self.UserCommands.lower() == 'exit' or self.UserCommands.lower() == 'stop':
                    quit()
                dir()
                clear()
                time()
                mkdir()
                pwd()
                cat()
                start_python()
                ipcon()
                ipsites()
                content_page()
                echo()
                Network()
                sysinfo()
                by()
                rm()
                neo()
                infos()
                fig()
                fsname()
                listemailp()
                hash_text()
                help()
        commands()

ob = Commands()
                        #End Programm#
