import sys
import platform

# Gestione delle importazioni in base al Sistema Operativo
if platform.system() == "Windows":
    import msvcrt
    def get_key():
        # Legge un tasto su Windows
        char = msvcrt.getch()
        if char == b'\x1b':  # ESC su Windows spesso restituisce 27
            return "ESC"
        try:
            return char.decode('utf-8').lower()
        except:
            return None
else:
    import tty
    import termios
    def get_key():
        # Legge un tasto su Linux/macOS
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        if ord(char) == 27: # Codice ASCII per ESC
            return "ESC"
        return char.lower()

def convertitore():
    print("=== CONVERTITORE UNIVERSALE (Win/Lin) ===")
    print("Premi [C] per Celsius, [F] per Fahrenheit o [ESC] per uscire.")
    
    while True:
        scelta = get_key()
        
        if scelta == "ESC":
            print("\nUscita in corso... a presto!")
            break
            
        if scelta == 'c':
            try:
                c = float(input("\nInserisci temperatura in °C: "))
                f = (c * 9/5) + 32
                res = int(f) if f.is_integer() else round(f, 2)
                print(f"Risultato: {res}°F 🌡\n")
            except ValueError:
                print("Errore: Inserisci un numero valido.")
                
        elif scelta == 'f':
            try:
                f = float(input("\nInserisci temperatura in °F: "))
                c = (f - 32) * 5/9
                res = int(c) if c.is_integer() else round(c, 2)
                print(f"Risultato: {res}°C 🌡\n")
            except ValueError:
                print("Errore: Inserisci un numero valido.")
        
        if scelta in ['c', 'f']:
            print("Premi un tasto per continuare [C/F] o ESC per uscire...")

if __name__ == "__main__":
    convertitore()