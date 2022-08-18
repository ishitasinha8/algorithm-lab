#Name: Ishita Sinha
#Reg: 202000506
"""
Algorithm:
**********

Step 1: Start
Step 2: Make a function: merge(arr,l,m,r)
            Here 'arr' is a list, 'l' is lower index of first subarray, 'm' is the upper index of the same and 'r' is upper index of second subarray
Step 3: Initialise the sizes of the subarrays:
            n1 = m - l + 1
            n2 = r - m
        Make the subarrays arr1 and arr2 of sizes 'n1' and 'n2' respectively:
        arr1 = [0]*(n1)
        arr2 = [0]*(n2)
Step 4: Assign values into the two subarrays:
            Make a for loop from 0 to n1.
                In each iteration, assign: arr1[i] = arr[l+i]
            Make a for loop from 0 to n2.
                In each iteration, assign: arr2[j] = arr[m+1+j]
Step 5: Initialise:
            i = 0
            j = 0
            k = l
Step 6: Make a while loop:  while (i<n1 and j<n2)
Step 7: Check if(arr1[i]<=arr2[j])
            If yes, assign: arr[k] = arr1[i]. Increment i by 1
            Otherwise assign: arr[k] = arr2[j]. Increment j by 1
Step 8: Increment k by 1. Go to step 6
Step 9: Now copy remaining elements if any from arr1[] or arr2[] into arr[] as follows:
            Make a while loop: while i<n1
                Assign arr[k] = arr1[i]. Increment i by 1 and k by 1.
            Make a while loop: while j<n2
                Assign arr[k] = arr2[j]. Increment j by 1 and k by 1.

Step 10: Make a recursive function to divide the array till size is 1: def mergesort(arr,l,r)
Step 11: Check if l<r.
            if yes, do the following:
                m = l+ (r-l)//2
                mergesort(arr,l,m)
                mergesort(arr,m+1,r)
                merge(arr,l,m,r)

Step 12: Assign length to a variable 'length'
Step 13: Make a list with random numbers in the range 0 and 50 for size length.
Step 14: starttime = time.time()
         Now, call mergesort(arr,0,len(arr)-1)
         endtime = time.time()
         Print endtime-starttime
Step 15: Stop
"""

import random
import time

def merge(arr,l,m,r):  #Merges two subarrays of arr[] in a sorted manner - namely arr1[l..m] and arr2[m+1..r]
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
    
def mergesort(arr,l,r): #// Recursively divide array into two halves till the size becomes 1.
    if l<r:
        m = l+ (r-l)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)

length = 1000
arr = [random.randrange(0,50) for i in range(length)]
print(arr)
starttime = time.time()
mergesort(arr,0,len(arr)-1)
endtime = time.time()
print(arr)
print(endtime - starttime)