# Name: Ishita Sinha
# Registration: 202000506

"""
Algorithm
**********

Step 1: Start
Step 2: Make a method: calculator()
Step 3: Print the Operations of calculator using string method .format()
Step 4: Take user's choice into variable 'choice'
Step 5: Now, take the numbers into variables 'a' and 'b'
Step 6: Make an if-elif ladder to perform the operations and print them as follows:
            if choice==1, perform a+b and print it
            elif choice==2, perform a-b and print it
            elif choice==3, perform a*b and print it
            elif choice==4, perform a/b and print it
            else, print that choice is invalid
Step 7: Now, make a method: checkLeapYear()
Step 8: Take user's input into variable 'year'
Step 9: Check if year is leap as follows:
            if((year%400==0) or ((year%4==0) and (year%100!=0)))
                print "year is leap"
            otherwise, print "year is not leap"
Step 10: Define a dictionary variable 'switch' with the choices: 1: "Calculator"  and   2:"Check leap year". Print the dictionary
Step 11: Take user's choice into variable 'i'
Step 12: Call the respective functions based on user's choice using if-elif-else
Step 13: Stop

"""
#Function for basic calculator
def calculator():
    print(" 1:{}\n 2:{}\n 3:{}\n 4:{}".format("Add","Subtract","Multiply","Divide"))    #Display menu using string method .format()
    choice = int(input("Enter your choice (1/2/3/4): "))    #Ask for user's choice
    a = float(input("Enter the first number: "))            
    b = float(input("Enter the second number: "))
    
    #Perform Calculations based on user's choice
    if choice==1:
        print("{} + {} = {}".format(a,b,a+b))
    elif choice==2:
        print("{} - {} = {}".format(a,b,a-b))
    elif choice==3:
        print("{} * {} = {}".format(a,b,a*b))
    elif choice==4:
        print("{} / {} = {}".format(a,b,a/b))
    else:
        print("Invalid Choice")

#Function to check if a year is leap
def checkLeapYear():
    year = int(input("Enter a year: "))
    if((year%400==0) or ((year%4==0) and (year%100!=0))):   #if the year is divisible by 400, it is leap. Also, it is leap if it is divisible by 4 and not a century year
        print("It is a leap year")
    else:
        print("It is not a leap year")

#Switch implemented using dictionary
switch = {1: "Calculator",2:"Check leap year"}
print(switch)
i = int(input("Enter your choice: "))   #Asking for user's choice between calculator() and checkLeapYear()
#Calling the functions based on user's choice        
if i==1:
    calculator()
elif i==2:
    checkLeapYear()
else:
    print("Invalid Choice")
    
"""
Expected Input/Output 1:
************************

{1: 'Calculator', 2: 'Check leap year'}
Enter your choice: 1
 1:Add
 2:Subtract
 3:Multiply
 4:Divide
Enter your choice (1/2/3/4): 1 2
Enter the first number: 29.3
Enter the second number: 18.6
29.3 - 18.6 = 10.7


Expected Input/Output 2:
************************

{1: 'Calculator', 2: 'Check leap year'}
Enter your choice: 2
Enter a year: 1 2017
It is not a leap year

"""