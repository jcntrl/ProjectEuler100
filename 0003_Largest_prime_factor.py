'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600_851_475_143 ?
'''

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
            primes.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return primes

    
def maxPrimeFactor(n):
    return max(PrimeFactors(n))


# test case
print(PrimeFactors(int(13195))) # = [5, 7, 13, 29] OK

# do the thing:
print(maxPrimeFactor(int(600_851_475_143)))