def countingsort(array, maxwert):
    array_index = []
    array_sort = []
    for i in range(maxwert):
        array_index.append(0)

    for i in range(maxwert):
        if i in array:
            array_index[i] +=1

    for i in range(maxwert):
        if (array_index[i]>0):
            array_sort.append(i) 

    
    print("Aufsteigend Sortiert:",array_sort)
    array_sort.reverse()
    print("Absteigend Sortiert:", array_sort)



array = [44,55,12,42,94,18,6,67]
maxwert = 94

countingsort(array, maxwert+1)