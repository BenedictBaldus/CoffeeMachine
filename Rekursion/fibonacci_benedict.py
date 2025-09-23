def fibonacci_rekursiv(n):
    """Berechnet die Fibonacci-Zahlen rekursiv"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #fibonacci_array = [0, 1]
        #next_value = fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)
        #print(next_value)
        #fibonacci_array.append(next_value)  
        return fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)


summe = 0
def fibonacci_iterativ_summe(n):
    """Berechnet die Fibonacci-Zahlen iterativ und gibt die Summe der geraden Zahlen zurück"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #print(0)
        #print(1)

        a = 0
        b = 1
        for x in range(2, n+1):
            temp = b
            b = a + b
            a = temp
            
            if b % 2 == 0:
                global summe
                summe = summe + b
                print(b)
                
        return summe
def fibonacci_iterativ(n):
    """Berechnet die Fibonacci-Zahlen iterativ"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(0)
        print(1)

        a = 0
        b = 1
        for x in range(2, n+1):
            temp = b
            b = a + b
            a = temp
            print(b)
        return b



print("Welche Methode möchten Sie aufrufen?\n 1: Summe der geraden Fibonacci-Zahlen\n 2: Fibonacci Zahlen Iterativ\n 3: Fibonacci Zahlen Rekursiv")
wahl = input()
eingabe = int(input("Bitte eine Zahl eingeben: "))
match wahl:
    case "1":
        print("Summe der geraden Fibonacci-Zahlen")
        print(fibonacci_iterativ_summe(eingabe))
    case "2":
        print("Fibonacci Zahlen Iterativ")
        fibonacci_iterativ(eingabe)
    case "3":
        print("Fibonacci Zahlen Rekursiv")
        print(fibonacci_rekursiv(eingabe))
    case _:
        print("Ungültige Eingabe")
