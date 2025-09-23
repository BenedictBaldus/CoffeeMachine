t1 = [4, 3, 2, 1]
t2 = []
t3 = []
Versuche = 0


def move(n, tower1, tower2, tower3):
    global Versuche
    Versuche += 1
    if n > 0:
        move(n-1, tower1, tower3, tower2)
        if tower1:
            tower3.append(tower1[len(tower1)-1])
            tower1.pop
        move(n-1,tower2, tower1, tower3)
    return Versuche


def move_falsch(n, tower1, tower2, tower3):
    global Versuche
    Versuche += 1

    if(n % 2 == 0):
        tower2.append(tower1[len(tower1)-1])
        tower1.pop()
        print("Bewegung", Versuche)
        print(tower1)
        print(tower2)
        print(tower3)
        print("-------------")
        print("gerade")
        
        move(len(tower1),tower1, tower3, tower2)
    else:
        tower2.append(tower1[len(tower1)-1])
        tower1.pop()
        print("Bewegung", Versuche)
        print(tower1)
        print(tower3)
        print(tower2)
        print("-------------")
        print("ungerade")
        move(len(tower1),tower1,tower3,tower2)

    return Versuche



    
      

print("Es wurden: ",move(len(t1)-1,t1,t2,t3), "Versuche benötigt")