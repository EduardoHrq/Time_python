import os 
from time import sleep
import subprocess as s
import datetime
from tkinter.constants import TRUE

os.system('clear')

print(30*"═" + "╗")

print('''\033[1m> (D/d) ⇨ Date
> (H/h) ⇨ Time or Hours
> (F/f) ⇨ Date and Time
> (C/c) ⇨ Cronometro
> (T/t) ⇨ Timer
...''')

print(30*"═" + "╝")

print('''
\033[1;31mAo final do uso tecle ^c (Ctrl+c) para finalizar o programa e saia\033[m''')

opc = input(str('''
Selecione uma opção: '''))

if opc == "C" or opc == "c":
    horas = 0
    minut = 0
    second = 0

    while True:
        os.system('clear')
        if horas < 10:
            if minut < 10:
                if second < 10:
                    print("╔"+32*"═"+"╗")
                    print("║", 10*" ", f"0{horas}:0{minut}:0{second}", 10*" ", "║")
                    print("╚"+32*"═"+"╝")
                else:
                    print("╔"+32*"═"+"╗")
                    print("║", 10*" ", f"0{horas}:0{minut}:{second}", 10*" ", "║")
                    print("╚"+32*"═"+"╝")
            else:
                print("╔"+32*"═"+"╗")
                print("║", 10*" ", f"0{horas}:{minut}:{second}", 10*" ", "║")
                print("╚"+32*"═"+"╝")
        else:
            print("╔"+32*"═"+"╗")
            print("║", 10*" ", f"{horas}:{minut}:{second}", 10*" ", "║")
            print("╚"+32*"═"+"╝")
        second += 1
        if second == 60:
            second = 0
            minut += 1
        if minut == 60:
            minut = 0
            horas += 1
        sleep(1)       

if opc == "T" or opc == "t":
    os.system('clear')
    horas = int(input("Horas: "))
    minut = int(input("Minutos: "))
    second = int(input("Segundos: ")) 
    while True:
        os.system('clear')
        if horas == 0 and minut == 0 and second == -1:
            print("╔"+32*"═"+"╗")
            print("║", 10*" ", "\033[1;31m00:00:00\033[m", 10*" ", "║")
            print("╚"+32*"═"+"╝")   
            s.call(['notify-send','Timer','Timer Finalizado'])
            break
        if horas < 10:
            if minut < 10:
                if second < 10:
                    print("╔"+32*"═"+"╗")
                    print("║", 10*" ", f"\033[1m0{horas}:0{minut}:0{second}\033[m", 10*" ", "║")
                    print("╚"+32*"═"+"╝")
                else:
                    print("╔"+32*"═"+"╗")
                    print("║", 10*" ", f"\033[1m0{horas}:0{minut}:{second}\033[m", 10*" ", "║")
                    print("╚"+32*"═"+"╝")
            else:
                print("╔"+32*"═"+"╗")
                print("║", 10*" ", f"\033[1m0{horas}:{minut}:{second}\033[m", 10*" ", "║")
                print("╚"+32*"═"+"╝")
        else:
            print("╔"+32*"═"+"╗")
            print("║", 10*" ", f"\033[1m{horas}:{minut}:{second}\033[m", 10*" ", "║")
            print("╚"+32*"═"+"╝")
        if second == 0 and minut > 0:
            second = 60
            minut -= 1
        if minut == 0 and horas > 0:
            minut = 59
            horas -= 1
            second = 60
        second -= 1
        sleep(1)  

if opc == "H" or opc == "h":  
    while True:
        hn = datetime.datetime.now()
        os.system('clear')
        print("╔"+32*"═"+"╗")
        print("║", 10*" \033[1m", hn.strftime('%H:%M:%S'), 10*"\033[m ", "║")
        print("╚"+32*"═"+"╝")  
        sleep(1)

if opc == "D" or opc == "d":
    dt = datetime.datetime.now()
    def Semana():
        if dt.weekday() == 0:
            return "Segunda-feira"
        if dt.weekday() == 1:
            return "Terça-feira"
        if dt.weekday() == 2:
            return "Quarta-feira"
        if dt.weekday() == 3:
            return "Quinta-feira"
        if dt.weekday() == 4:
            return "Sexta-feira"
        if dt.weekday() == 5:
            return "Sábado"
        if dt.weekday() == 6:
            return "Domingo"
    os.system('clear')
    print("\033[1m", Semana() ,dt.strftime(' %d/%m/%Y'),"\033[m")

if opc == "F" or opc == "f":
    while True:
        dt = datetime.datetime.now()
        def Semana():
            if dt.weekday() == 0:
                return "Segunda-feira"
            if dt.weekday() == 1:
                return "Terça-feira"
            if dt.weekday() == 2:
                return "Quarta-feira"
            if dt.weekday() == 3:
                return "Quinta-feira"
            if dt.weekday() == 4:
                return "Sexta-feira"
            if dt.weekday() == 5:
                return "Sábado"
            if dt.weekday() == 6:
                return "Domingo"
        os.system('clear')
        print("\033[1m",Semana() ,dt.strftime(' %d/%m/%Y')," ▶ ", dt.strftime('%H:%M:%S'), "\033[m")
        sleep(1)
