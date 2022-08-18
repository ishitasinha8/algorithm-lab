# Method 1: Finding the maximum p/w whose corresponding solution is not 1 and then finding the capacity left
"""def findMax(A, sol):
    pos = 0
    max = A[0]
    for i in range(0,len(A)):
        if (sol[pos]==1):
            pos+=1
            max = A[pos]
        elif (max<A[i] and sol[i]!=1):
            pos = i
            max = A[i]
    return pos

def knapsack(o,p,w,sol,capacity):
    profByWeight = [0]*len(o)
    for i in range(len(o)):
        profByWeight[i] = p[i]/w[i]
    print(profByWeight)
    maxPos = 0
    while (capacity!=0):
        maxPos = findMax(profByWeight,sol)
        print(maxPos)
        if(w[maxPos]<=capacity):
            sol[maxPos] = 1
            capacity -= w[maxPos]
        else:
            sol[maxPos] = capacity/w[maxPos]
            capacity -= capacity

    totalProf = 0
    for i in range(len(o)):
        totalProf += (p[i] * sol[i])
    print(sol)
    print(totalProf)
"""


noOfObject = int(input("Enter number of objects: "))
profit = [0]*noOfObject
weight = [0]*noOfObject
sol = [0]*noOfObject
object = [0]*noOfObject

for i in range(noOfObject):
    object[i] = i
    profit[i] = int(input("Enter profit of object: "))
    weight[i] = int(input("Enter weight of object: "))

capacity = int(input("Enter the capacity of the sack: "))

print(object)    
print(profit)   
print(weight)   
print(sol)   
print(capacity)   



# Method 2: sorting the list in decreasing order of p/w and then finding the solution

def knapsack(o,p,w,sol,capacity):
    profByWeight = [0]*len(o)
    for i in range(len(o)):
        profByWeight[i] = p[i]/w[i]
    print(profByWeight)
    for i in range(len(o)):
        for j in range(len(o)-i-1):
            if(profByWeight[j]<profByWeight[j+1]):
                profByWeight[j], profByWeight[j+1] = profByWeight[j+1], profByWeight[j]
                p[j], p[j+1] = p[j+1], p[j]
                w[j], w[j+1] = w[j+1], w[j]
    i = 0
    while (capacity!=0):
        if(w[i]<=capacity):
            sol[i] = 1
            capacity -= w[i]
        else:
            sol[i] = capacity/w[i]
            capacity -= capacity
        i+=1

    totalProf = 0
    for i in range(len(o)):
        totalProf += (p[i] * sol[i])
    print(sol)
    print(totalProf)

knapsack(object,profit,weight,sol,capacity)

#Test Case 1
"""object  = [1,2,3,4]
sizeOfArr = len(object)
profit = [24,18,18,10]
weight = [24,10,10,7]
sol = [0]*sizeOfArr
capacity = 25"""

#Test Case 2
"""object  = [1,2,3,4,5]
sizeOfArr = len(object)
profit = [8,5,10,15,9]
weight = [1,1,3,5,3]
sol = [0]*sizeOfArr
capacity = 12"""

#Test Case 3
"""object  = [1,2,3,4,5,6,7]
sizeOfArr = len(object)
profit = [12,7,17,9,8,20,5]
weight = [4,5,7,9,3,6,3]
sol = [0]*sizeOfArr
capacity = 22"""

#Test Case 4
"""object  = [1,2,3]
sizeOfArr = len(object)
profit = [60,100,120]
weight = [10,20,30]
sol = [0]*sizeOfArr
capacity = 50"""