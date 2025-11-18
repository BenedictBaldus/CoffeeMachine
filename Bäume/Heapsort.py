def Heapsort(array,n):
    
    parent= array[round(n/2)-1]
    
    child_left= array[n-2]
    child_right= array[n-1]
    print(parent,child_left,child_right)

    if child_left>parent:
        #print("größer")
        array[round(n/2)-1], array[n-2] = array[n-2],array[round(n/2)-1]
        #child_left,parent = parent,child_left
    parent= array[round(n/2)-1]
    if child_right>parent:
        array[round(n/2)-1], array[n-1] = array[n-1],array[round(n/2)-1]
        #child_right,parent = parent,child_right

    
    print(array)
    if n>2:
        if n%2==0:
            Heapsort(array,n/2)
        else:
            Heapsort(array,int((n/2)+0.5))
    else:
        array[0],array[len(array)-1] = array[len(array)-1],array[0]
        print(array)
        global sortiert
        sortiert.insert(0,array[len(array)-1])
        array.pop()
        print("sort",sortiert)
        if n%2==0:
            Heapsort(array,int(n-1))
        else:
            Heapsort(array,int(n-1.5))

        #Heapsort(array,len(array)-1)


werte =[ 57, 16, 62, 30, 80, 7, 21, 78, 41]
sortiert=[]
laenge=len(werte)
print(werte)

Heapsort(werte, laenge)
