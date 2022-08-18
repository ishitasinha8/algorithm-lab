#Name: Ishita Sinha
#Reg: 202000506
import time
import random

def binarySearch(arr,x,left,right):
    if(left>right):
        return -1
    else:
        mid = left+(right-left)//2
        print(arr[mid])
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            return binarySearch(arr,x,mid+1,right)
        else:
            return binarySearch(arr,x,left,mid-1)

arrSize = 20000
values = [random.randrange(1,50) for i in range(arrSize)] #generate random numbers between 1 and 49
values.sort() #Sorting the list for binary search
print(values)
#searchInt = int(input("Search for element: "))
searchInt = values[(arrSize-1)//2]
print(searchInt)
startTime = time.time()     #Start Time
pos = binarySearch(values,searchInt,0,arrSize-1)
if(pos==-1):
    print ("Not Found")
else:
    print("Found at: ",pos)
endTime = time.time()       #End Time
print("Time: ",endTime-startTime)
