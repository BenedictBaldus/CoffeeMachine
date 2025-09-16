def fibonacci_rekursiv(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        next_value = fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)
        print(next_value)
        #fibo_array.append(next_value)  
        return next_value
summe = 0
def fibonacci_iterativ(n):
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
eingabe = int(input("Bitte eine Zahl eingeben: "))
#fibonacci_iterativ(eingabe)
print(fibonacci_iterativ(eingabe))



#fibonacci_rekursiv(eingabe) 