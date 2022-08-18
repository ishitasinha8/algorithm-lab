import random
import time

def swap(a,b):
    t = a
    a = b
    b = t

def partition(A, LB, UB):
    pivot = A[LB]
    pivotPos = LB
    start = LB
    end = UB
    while(start<end):
        while(A[start]<=pivot and start<(len(A)-1)):
            start = start+1
        while(A[end]>pivot and end>0):
            end = end - 1
        if(start<end):
            A[start], A[end] = A[end], A[start]
    A[end], A[pivotPos] = A[pivotPos], A[end]
    print(A)
    return end

def quicksort(A,LB,UB):
    if(LB<UB):
        location = partition(A,LB,UB)
        quicksort(A,LB,location-1)
        quicksort(A,location+1,UB)

#arr = [random.randrange(0,50) for i in range(10)]
#arr[0] = 25
arr=[1,2,3,4]
#arr.sort()
print(arr)
start = time.time()
quicksort(arr,0,len(arr)-1)
end = time.time()
print("\nSorted: ")
print(arr)
print("Time = ",end-start)