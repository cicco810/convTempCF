import sys
import tty
import termios

def getch():
    """Legge un singolo tasto su Linux senza aspettare l'Invio."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def convertitore():
    print("=== CONVERTITORE LINUX ===")
    print("Premi ESC per uscire, C per Celsius, F per Fahrenheit")

    while True:
        # Cattura il tasto
        tasto = getch()

        # Gestione con MATCH
        match tasto:
            case '\x1b': # Tasto ESC
                print("\nUscita... a presto!")
                break
            
            case 'c' | 'C':
                try:
                    celsius = float(input("\nInserisci °C: "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"Risultato: {fahrenheit:g} °F 🌡")
                except ValueError:
                    print("Errore: inserisci un numero valido!")

            case 'f' | 'F':
                try:
                    fahrenheit = float(input("\nInserisci °F: "))
                    celsius = (fahrenheit - 32) * 5/9
                    print(f"Risultato: {celsius:g} °C 🌡")
                except ValueError:
                    print("Errore: inserisci un numero valido!")
            
            case _: # Qualsiasi altro tasto
                try:
                    celsius = float(input("\nInserisci °C: "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"Risultato: {fahrenheit:g} °F 🌡")
                except ValueError:
                    print("Errore: inserisci un numero valido!")
    
convertitore_linux()