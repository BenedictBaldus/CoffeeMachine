def f(n):
    temp = 1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
            a=0
            b=1
            temp = b
            b = b+a
            return temp
        


eingabe =int(input("Zahl:"))
for i in range (0,eingabe+1):
    print(f(i))