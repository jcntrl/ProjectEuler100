'''
Factorial digit sum
Submit

 Show HTML problem content 
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import math

def FactorialSum(n):
    N = math.factorial(n)
    Nstr = str(N)
    Nsum = 0
    for i in Nstr:
        Nsum += int(i)
    return Nsum

print(FactorialSum(100))
