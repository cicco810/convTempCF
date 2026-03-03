import msvcrt
import sys
import math

def convertitore():#definisco il convertitore da celsius a fahrenheit
    print("CONVERTIORE TEMPERATURA")
    cond = True
    while cond:
        print("inserisci formato di conversione [Celsius/Fahrenheit]:")
        tasto = msvcrt.getch()
        if ord(tasto) == 27:
            print("\nUscita in corso... a presto!")
            break
        scelta = tasto.decode('utf-8').lower()
        scelta = input()
        match scelta:
            case "c":
                try:
                    celsius = float(input("inserisci la temperatura °C: "))
                    fahrenheit = (celsius*9/5)+32
                    if fahrenheit.is_integer():
                        fahrenheit = int(fahrenheit)
                        print(fahrenheit,"°F",'🌡')
                    else:
                         print(fahrenheit,"°F",'🌡')
                except ValueError:
                    print("Valore non valido")
            case "f":
                try:
                    fahrenheit = float(input("inserisci la temperatura °F: "))
                    celsius = (fahrenheit-32)*5/9
                    celsius = round(celsius, 2)
                    if celsius.is_integer():
                        celsius = int(celsius)
                        print(celsius, "°C 🌡")
                    else:
                        print(celsius, "°C 🌡")
                except ValueError:
                    print("Valore non valido")   
            case _:
                try:
                    celsius = float(input("inserisci la temperatura °C: "))
                    fahrenheit = (celsius*9/5)+32
                    if fahrenheit.is_integer():
                        fahrenheit = int(fahrenheit)
                        print(fahrenheit,"°F",'🌡')
                    else:
                         print(fahrenheit,"°F",'🌡')
                except ValueError:
                    print("Valore non valido")
convertitore()