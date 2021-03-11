"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math

def PrimeFactors(n):
    '''
    Input: integer to prime factorize
    Method: trial division (NON-OPTIMIZED)
    Output: list of prime factors
    '''
    primes = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            if divisor not in primes:
                primes.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return primes

def Smallest_Multiple(m=10):
    '''
    Input: maximum of range of integer multiples, ex: 4 --> [1,2,3,4]
    Output: integer smallest multiple that is perfectly divisible by all factors
    '''
    m = [ i for i in range(2, m+1) ]
    simplestmultiple = math.prod(m)
    primefactors = PrimeFactors(simplestmultiple)
    result = math.prod(primefactors)
    for element in primefactors:
        m.remove(element)
    for i in m:
        if result % i != 0:
            iprimes = PrimeFactors(i)
            result = result*min(iprimes)
    
    return result


x = int(input("All integer factors up to:"))
print(Smallest_Multiple(x))