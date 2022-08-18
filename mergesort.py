from re import M
import random

def merge(arr,l,m,r):
    n1 = m - l + 1
    n2 = r - m

    arr1 = [0]*(n1)
    arr2 = [0]*(n2)
    for i in range(0,n1):
        arr1[i] = arr[l+i]
    for j in range(0,n2):
        arr2[j] = arr[m+1+j]

    i = 0
    j = 0
    k = l
    while (i<n1 and j<n2):
        if(arr1[i]<=arr2[j]):
            arr[k] = arr1[i]
            i = i+1
        else:
            arr[k] = arr2[j]
            j = j+1
        k = k+1
    
    while i<n1:
        arr[k] = arr1[i]
        i = i+1
        k = k+1
    while j<n2:
        arr[k] = arr2[j]
        j = j+1
        k = k+1
    
def mergesort(arr,l,r):
    if l<r:
        m = l+ (r-l)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)

arr = [random.randrange(0,100) for i in range(120)]
print(arr)
mergesort(arr,0,len(arr)-1)
print(arr)