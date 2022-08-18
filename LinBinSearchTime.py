"""
1. Write a Python program to implement recursive Linear Search on a given set of elements and determine the time required to perform the same.  Plot a graph (on a graph paper) of number of elements versus time taken. Specify the time efficiency class of this algorithm. Follow the sample observation table given in the Lab Manual in Page No. 46.

2. Write a Python program to implement recursive Binary Search on a given set of elements and determine the time required to perform the same. Plot a graph (on a graph paper) of number of elements versus time taken. Specify the time efficiency class of this algorithm. Follow the sample observation table given in the Lab Manual in Page No. 46.

NOTE: Solutions to both problems has to be saved in a single pdf file. Rename the file with your registration number. Eg: 202011111.pdf
"""

from re import search
import time
import random
import sys
import resource

#resource.setrlimit(resource.RLIMIT_STACK,(2**29,-1))
sys.setrecursionlimit(1000000)

#segmentation fault for larger lists
"""def linearSearch(arr,x,i,arrSize):
    if(i>=arrSize):
        return -1
    if(arr[i]==x):
        pos = i+1
        return pos
    else:
        return linearSearch(arr,x,i+1,arrSize)"""

"""def linearSearch(arr,x,i,arrSize):
    if(i>arrSize):
        return -1
    if(arr[i]==x):
        return i
    if(arr[arrSize]==x):
        return arrSize
    return linearSearch(arr,x,i+1,arrSize-1)"""

#runs error-free
def linearSearch(arr,x,i,arrSize):
    for i in range(0,arrSize):
        if(arr[i]==x):
            return i
    return -1

def binarySearch(arr,x,left,right):
    if(left>right):
        return -1
    else:
        mid = left+(right-left)//2
        #print(arr[mid])
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            return binarySearch(arr,x,mid+1,right)
        else:
            return binarySearch(arr,x,left,mid-1)



arrSize = 1000000
values = [random.randrange(1,50) for i in range(arrSize)] #between 1 and 49, random numbers
values.sort() #sorting them
print(values)

"""searchInt = int(input("Search for element: "))

startTime = time.time()
found = linearSearch(values,searchInt,0,arrSize)
if(found==-1):
    print ("Not Found")
else:
    print("Found at: ",found)
endTime = time.time()
print("Time: ",endTime-startTime)"""

searchInt = values[arrSize//4]
print(searchInt)
startTime = time.time()
found = binarySearch(values,searchInt,0,arrSize-1)
if(found==-1):
    print ("Not Found")
else:
    print("Found at: ",found)
endTime = time.time()
print("Time: ",endTime-startTime)

"""
10: 
Time:  0.9317631721496582
Time:  1.984605073928833
Time:  1.9873030185699463

100:
Time:  1.2302446365356445
Time:  1.4876008033752441
Time:  1.7413649559020996

500:
Time:  1.2960858345031738
Time:  1.90621399879455575
Time:  1.2049388885498047

10000:
Time:  1.6959290504455566
Time:  1.4686992168426514
Time:  1.9359931945800781

20000:
Time:  1.4369111061096191
Time:  1.7255070209503174
Time:  1.2378618717193604

50000:
Time:  1.052250862121582

"""
