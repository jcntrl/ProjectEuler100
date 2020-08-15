"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def nPrimes(n):
    Primes = [2, 3]
    keepgoing = True
    num = 3
    while keepgoing:
        prmflag = True
        for prm in Primes:
            if num % prm == 0:
                prmflag = False
                break #no need to keep checking when a nonprime is found
        if prmflag:
            Primes.append(num)
            if len(Primes) == n:
                keepgoing = False
        num += 2      

    return Primes

print(nPrimes(10_001))
