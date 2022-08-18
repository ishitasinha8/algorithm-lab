#Name: Ishita Sinha
#Reg: 202000506
import time
import random

def bubbleSort(arr,length):
    for i in range(length-1):
        for j in range(0,length-1-i):
            if(arr[j]>arr[j+1]):
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t


def insertionSort(arr,length):
    for i in range(1,length):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        print(arr)

def selectionSort(arr,length):
    for i in range(length):
        min = i
        for j in range(i+1,length):
            if(arr[j]<arr[min]):
                min = j
        t = arr[i]
        arr[i] = arr[min]
        arr[min] = t

length = 5

#values.sort(reverse=True)
#print(values)

"""
values = [random.randrange(1,50) for i in range(length)] #generate random numbers between 1 and 49
values.sort(reverse=True)
print(values)
startTime = time.time()     #Start Time
bubbleSort(values,length)
endTime = time.time()       #End Time
print(values)
print("Time: ",endTime-startTime)
"""
values = [5,4,3,2,1] #generate random numbers between 1 and 49
#values.sort(reverse=True)
print(values)
startTime = time.time()     #Start Time
insertionSort(values,length)
endTime = time.time()       #End Time
print(values)
print("Time: ",endTime-startTime)

"""
#values = [random.randrange(1,50) for i in range(length)] #generate random numbers between 1 and 49
values.sort(reverse=True)
print(values)
startTime = time.time()     #Start Time
selectionSort(values,length)
endTime = time.time()       #End Time
print(values)
print("Time: ",endTime-startTime)
"""