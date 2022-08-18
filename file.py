"""
Algorithm:
***********

Step 1: Start
Step 2: Make a function: sumEvenIntegers(n)
            Declare sum = 0
            Make a for loop in range(n,0,-2)
                Assign sum = sum + i
Step 5: Make a function: fibonacci(prev,current,n)
            if(n>0)
                print(prev)
                recursively call fibonacci(current,prev+current,n-1)
Step 6: Make a function reverseArr():
            Make a list 'arr' with only integer data to represent an array
            Make another list revArr = arr[::-1]. This will traverse 'arr' from end and assign it to 'revArr'
            Print both the lists
Step 7: Display the menu using .format():
            a. Sum of positive integers
            b. Print Fibonacci series using recursion
            c. Reverse order of elements in array
Step 8: Ask for user's choice and store in variable 'choice'
Step 9: Make an if-elif-else ladder for the choices:
            if the choice is 'a', take an input value in 'n' and call sumEvenIntegers(n)
            if the choice is 'b', take an input value in 'noOfElements' and call fibonacci(0,1,noOfElements)
            if the choice is 'c', call reverseArr()
            if the three conditions fail, print "Incorrect Choice"
Step 10: Stop
"""

def sumEvenIntegers(n): #calculate the sum of the positive integers of n+(n-2)+(n-4) +. . . + 0
    sum = 0    
    for i in range(n,0,-2):
        sum = sum + i
    print("{} + {} + {} ... + 0 = {}".format(n,n-2,n-4,sum))

def fibonacci(prev,current,n): #print Fibonacci sequence using recursion for a given number of elements
    if(n>0):
        print(prev, end = " ") #Printing the series. end = " " helps in printing in same line with a space
        fibonacci(current,prev+current,n-1)

def reverseArr(): #Reverse the order of the items in the array
    arr = [2,5,3,1,6,9,4]
    revArr = arr[-1::-1] #since list index starts from -1 and decrements to the beginning, we can assign it to another list in the reverse order
    
    print("Original array: ",arr)
    print("Reversed array: ",revArr)

print("{}\n{}\n{}".format("a. Sum of positive integers", "b. Print Fibonacci series using recursion", "c. Reverse order of elements in array"))
choice = input("Enter your choice a/b/c: ")

#making an if-elif-else ladder for user's choice
if(choice=='a'):
    n = int(input("Enter the value for n: "))
    sumEvenIntegers(n)
elif(choice=='b'):
    noOfElements = int(input("Enter number of elements: "))
    fibonacci(0,1,noOfElements)
elif(choice=='c'):
    reverseArr()
else:
    print("Incorrect choice")
    
"""
Input and Output 1:
*******************
a. Sum of positive integers
b. Print Fibonacci series using recursion
c. Reverse order of elements in array
Enter your choice a/b/c: a
Enter the value for n: 10
10 + 8 + 6 ... + 0 = 30

Input and Output 2:
*******************
a. Sum of positive integers
b. Print Fibonacci series using recursion
c. Reverse order of elements in array
Enter your choice a/b/c: b
Enter number of elements: 10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 

Input and Output 3:
*******************
a. Sum of positive integers
b. Print Fibonacci series using recursion
c. Reverse order of elements in array
Enter your choice a/b/c: c
Original array:  [2, 5, 3, 1, 6, 9, 4]
Reversed array:  [4, 9, 6, 1, 3, 5, 2]
"""