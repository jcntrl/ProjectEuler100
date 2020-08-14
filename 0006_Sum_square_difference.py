"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,
    
    1^2 + 2^2 + ... + 10^2 == 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 == 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    3025 - 385 == 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_square_difference(n):
    SumSquares = 0
    Sumn = 0
    for i in range(1,n+1):
        SumSquares += i**2
        Sumn += i
    return Sumn**2 - SumSquares

assert sum_square_difference(10) == 2640, "should be 2640"

print(sum_square_difference(100))