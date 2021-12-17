from random import seed
from random import random
from twilio.rest import Client
import random , string
import csv
import string
from time import sleep
import os
import getpass
from discord_webhook import DiscordWebhook

print('''                                                                                                                          
      _____        _____           _____     ____    ____   ____      ______        ______  _______          ____         _____    
 ___|\     \   ___|\    \     ____|\    \   |    |  |    | |    | ___|\     \      |      \/       \    ____|\   \    ___|\    \   
|    |\     \ |    |\    \   /     /\    \  |    |  |    | |    ||     \     \    /          /\     \  /    /\    \  /    /\    \  
|    | |     ||    | |    | /     /  \    \ |    | /    // |    ||     ,_____/|  /     /\   / /\     ||    |  |    ||    |  |____| 
|    | /_ _ / |    |/____/ |     |    |    ||    |/ _ _//  |    ||     \--'\_|/ /     /\ \_/ / /    /||    |__|    ||    |    ____ 
|    |\    \  |    |\    \ |     |    |    ||    |\    \'  |    ||     /___/|  |     |  \|_|/ /    / ||    .--.    ||    |   |    |
|    | |    | |    | |    ||\     \  /    /||    | \    \  |    ||     \____|\ |     |       |    |  ||    |  |    ||    |   |_,  |
|____|/____/| |____| |____|| \_____\/____/ ||____|  \____\ |____||____ '     /||\____\       |____|  /|____|  |____||\ ___\___/  /|
|    /     || |    | |    | \ |    ||    | /|    |   |    ||    ||    /_____/ || |    |      |    | / |    |  |    || |   /____ / |
|____|_____|/ |____| |____|  \|____||____|/ |____|   |____||____||____|     | / \|____|      |____|/  |____|  |____| \|___|    | / 
  \(    )/      \(     )/       \(    )/      \(       )/    \(    \( |_____|/     \(          )/       \(      )/     \( |____|/  
   '    '        '     '         '    '        '       '      '     '    )/         '          '         '      '       '   )/     
\--------------------------------------------------------------------------------------------------------------------------------NFT's''')
series = input("Which Series do you want? (X,W,U,M):- ")
password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
if "X" in series or "x" in series:
        print('''
███████╗███████╗██████╗ ██╗███████╗███████╗██╗  ██╗
██╔════╝██╔════╝██╔══██╗██║██╔════╝██╔════╝╚██╗██╔╝
███████╗█████╗  ██████╔╝██║█████╗  ███████╗ ╚███╔╝ 
╚════██║██╔══╝  ██╔══██╗██║██╔══╝  ╚════██║ ██╔██╗ 
███████║███████╗██║  ██║██║███████╗███████║██╔╝ ██╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
 \-------------------------------------------------brokiemag''')
        with open("password.txt") as file:
            contents = file.read()
            webhook = DiscordWebhook(url='<your webhook>', rate_limit_retry=True,
                            content=f'Your SAT PASS is "{password}" please do not share the password')
            response = webhook.execute()
            pass_verification = getpass.getpass(prompt = "Please Verify Your Satellite Generated Password:- ")
        if pass_verification == password:
            print ('Satellite Generated Password Found')
            sleep(1)
            choice = input(f"Do you want to open the series {series} in your system or on cloud ('S' or 'C'):-")
            if "C" in series or "c" in choice:
                print("not available")
            if "S" in series or "s" in choice:
                print ('Redirecting to Authorized page...')
                os.startfile("<file loction>")
                print (f"Redirecting to Series {series}'s system page...")
            else:
                exit()
        else:
            print ('Satellite Generated Password Error')
else:
        print(f"Series {series}'s not found")
