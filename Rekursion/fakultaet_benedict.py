
def fakultaet(n):
    if n == 1:
        return 1
    else:
        return n * fakultaet(n - 1)

eingabe = int(input("Bitte eine Zahl eingeben: "))

print("Die Fakultät von", eingabe, "ist",fakultaet(eingabe))