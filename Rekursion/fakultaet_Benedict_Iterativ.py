def fakultaet(n):
    temp = 1
    for x in range(1, n + 1):
        temp = temp * x
    return temp


eingabe = int(input("Bitte eine Zahl eingeben: "))
print("Die Fakultät von", eingabe, "ist",fakultaet(eingabe))