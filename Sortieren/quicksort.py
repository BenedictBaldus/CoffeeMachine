import random

list=[]
for i in range (0,10):
    list.append(random.randint(1,100))
print(list)

def quicksort(arr,start,ende):
    pivot =arr[0]
    i= start
    j= ende-1
    if i == j:
        
    while i<=j:
        if arr[i]>=arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
        i +=1
        j -=1
    
    print(arr)
    quicksort(arr,0,i)
    quicksort(arr,i+1,len(arr))

quicksort(list,0,len(list))

