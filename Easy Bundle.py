#-*- coding: utf-8 -*-
import sys
import os
class col:
    head = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warn = '\033[93m'
    fail = '\033[91m'
    none = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

while True:
    try:
        print(col.warn +" ")
        os.system("sudo apt-get install figlet toilet")
        os.system("clear")
        os.system("figlet Easy Bundle")
        print("PRO-TIP: running info in this window opens some interesting Information :)")
        print(col.green + "CTRL + C to exit")
        print(" "+ col.none)
        print("     MsfVenomGenerator (1) ")
        print("     YourShell (2) ")
        print("Enter a Number:")
        print(col.head + "| " + col.none)
        easy = input(col.warn + "--» " + col.none)

        if str(easy) == "1":
            os.system("sudo python3 msfvenomgenerator.py")

        elif str(easy) == "2":
            os.system("sudo python3 YourShell.py")
        elif str(easy) == "info":
            os.system("cat info.txt")
            exit()
        else:
            print("Uknown error! Make sure to enter 1 or 2. CTRL + C to exit")
    except KeyboardInterrupt:
        print("")
        print(col.blue + "Shutdown... Cya ;)" + col.none)
        exit("")
