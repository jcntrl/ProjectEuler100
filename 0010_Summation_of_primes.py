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


t0 = time.time()
sol = SumofPrimesBelow(int(2e6))
t1 = time.time()
print(sol, t1-t0)