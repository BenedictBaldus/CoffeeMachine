def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
        


eingabe =int(input("Zahl:"))
for i in range (0,eingabe+1):
    print(f(i))