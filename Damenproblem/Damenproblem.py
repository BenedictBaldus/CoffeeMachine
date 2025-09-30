
Brett = [[0 for _ in range(8)] for _ in range(8)]
anzahldamen = 0
gefunden = False

def prüfen(zeile, spalte):
    
    for i in range(zeile):
        if Brett[i][spalte] == 1:
            return False
    
    i = zeile - 1, 
    j = spalte - 1
    while i >= 0 and j >= 0:
        if Brett[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = zeile - 1, 
    j = spalte + 1
    while i >= 0 and j < 8:
        if Brett[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def ausgabe():
    for row in Brett:
        print(" ".join(str(x) for x in row))
    print("------------")

def setzen(zeile=0):
    global anzahldamen, gefunden
    if gefunden:
        return
    if zeile == 8:
        ausgabe()
        gefunden = True
        return
    for spalte in range(8):
        if prüfen(zeile, spalte):
            Brett[zeile][spalte] = 1
            ausgabe()  
            setzen(zeile + 1)
            if gefunden:
                return
            Brett[zeile][spalte] = 0

setzen()