"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
def nPrimes(n):
    Primes = [2, 3]
    keepgoing = True
    num = 3
    while keepgoing:
        prmflag = True
        for prm in Primes:
            if prm > 9 and prm ** 2 > num:
                break #potential prime must be less than the square root of the num, has some false negatives in small numbers though
            elif num % prm == 0:
                prmflag = False
                break #no need to keep checking when a nonprime is found
        if prmflag:
            Primes.append(num)
            if len(Primes) == n:
                keepgoing = False
        num += 2      

    return Primes

n = 10_001
t0= time.time()
x = nPrimes(n)
t1 = time.time()
useroutput = "{}'th prime: {}. Computation completed in {} seconds."
print(useroutput.format(n, x[-1], t1-t0))
