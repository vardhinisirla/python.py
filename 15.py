# Python program to determine whether
# the number is Armstrong number or not
 
# Function to calculate x raised to
# the power y
def power(x, y):
     
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
         
    return x * power(x, y // 2) * power(x, y // 2)
 
# Function to calculate order of the number
def order(x):
 
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
         
    return n
 
# Function to check whether the given
# number is Armstrong number or not
def isArmstrong(x):
     
    n = order(x)
    temp = x
    sum1 = 0
     
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
 
    # If condition satisfies
    return (sum1 == x)
 
# Driver code
x = 153
print(isArmstrong(x))
 
x = 1253
print(isArmstrong(x))
Output
True
False
Time complexity: O((logn)2)

Auxiliary Space: O(1)

Method: A positive integer is called an Armstrong number if an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example, 153 is an Armstrong number because
   153 = 1*1*1 + 5*5*5 + 3*3*3
    The while loop iterates like first, it checks if the number is not equal to zero or not. if it is not equal to zero then enter into the loop and find the reminder of number ex: 153%10 gives reminder 3. In the next step add the cube of a number to the sum1(3*3*3). Then the step gives the quotient of the number (153//10=15). this loop will continue till the given number is equal to zero.
 


# python 3 program
# to check whether the given number is armstrong or not
# without using power function
 
n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
 
