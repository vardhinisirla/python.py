

A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not. 
Examples: 

Input: n = 15
Output: false
Divisors of 15 are 1, 3 and 5. Sum of 
divisors is 9 which is not equal to 15.

Input: n = 6
Output: true
Divisors of 6 are 1, 2 and 3. Sum of 
divisors is 6.
 

Recommended Practice
Perfect Number
Try It!
A Simple Solution is to go through every number from 1 to n-1 and check if it is a divisor. Maintain sum of all divisors. If sum becomes equal to n, then return true, else return false.
An Efficient Solution is to go through numbers till square root of n. If a number ‘i’ divides n, then add both ‘i’ and n/i to sum. 
Below is the implementation of efficient solution. 
 


