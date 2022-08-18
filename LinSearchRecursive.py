#Name: Ishita Sinha
#Reg: 202000506
import time
import random

def linearSearch(arr,x,i,arrSize):
    if(i>=arrSize):
        return -1
    if(arr[i]==x):
        return i
    else:
        return linearSearch(arr,x,i+1,arrSize)

arrSize = 10
values = [random.randrange(1,50) for i in range(arrSize)] #taking random numbers into list between 1 and 49
print(values)

searchInt = int(input("Search for element: "))

startTime = time.time()     #Start Time
pos = linearSearch(values,searchInt,0,arrSize)
if(pos==-1):
    print ("Not Found")
else:
    print("Found at: ",pos)
endTime = time.time()       #End Time

print("Time: ",endTime-startTime)