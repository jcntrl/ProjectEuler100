'''
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time

def SumofPrimesBelow(n):
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
            if num > n:
                keepgoing = False
                break
            Primes.append(num)
        num += 2      

    return sum(Primes)


def PrimeSieve(n): #true sieve
    sqlimit = int(n**0.5)+1
    result = 0
    Potentials = [True for i in range(0, n, 1)]
    # Base cases:
    Potentials[0], Potentials[1] = False, False
    # implement the sieve
    for i in range(2, n):
        if Potentials[i]:
            isq = i**2
            for j in range(isq, n, i):
                Potentials[j] = False
    
    for e in range(len(Potentials)):
        if Potentials[e]:
            result += e
    return result




t0 = time.time()
x = PrimeSieve(int(2e6))
t1 = time.time()
print(x, t1-t0)

t0 = time.time()
sol = SumofPrimesBelow(int(2e6))
t1 = time.time()
print(sol, t1-t0)