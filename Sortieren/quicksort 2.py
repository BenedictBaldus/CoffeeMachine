import random


data_list = []
for i in range(10):
    data_list.append(random.randint(1, 100))

print("Unsortierte Liste:", data_list)

def quicksort(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]
    
    i = start + 1  # Zeiger für Elemente, die größer als der Pivot sind
    j = end        # Zeiger für Elemente, die kleiner oder gleich dem Pivot sind
    
    while i <= j:
        
        while i <= j and arr[i] <= pivot:
            i += 1
            
        while i <= j and arr[j] > pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]

    quicksort(arr, start, j - 1) # Sortiere die linke Seite (Elemente <= Pivot)
    quicksort(arr, j + 1, end)   # Sortiere die rechte Seite (Elemente > Pivot)


quicksort(data_list, 0, len(data_list) - 1)

print("Sortierte Liste:", data_list)
