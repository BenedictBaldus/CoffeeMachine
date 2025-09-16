#Noch nicht ganz richtig

def fact(n):
    y=1
    if n==1:
        return 1
    else:
        for i in range(1, n+1):
            y = y*i 
            return y
            
            
                   
x = int(input("Zahl:"))
print(fact(x))