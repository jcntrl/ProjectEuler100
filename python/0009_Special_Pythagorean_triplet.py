"""
Special Pythagorean triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math, time

def pytrip_bruteforce(sumofabc=1000):
    for a in range(1,sumofabc):
        for b in range(1,sumofabc):
            c = (a**2 + b**2)**0.5
            if a + b + c == sumofabc and a < b:
                return [a,b,c], a*b*c

t0 = time.time()
x = pytrip_bruteforce()
t1 = time.time()
print(x, (t1-t0))

def pytrip_optimizedbymath(sumofabc=1000):
    '''
    https://en.wikipedia.org/wiki/Pythagorean_triple
    a=k\cdot (m^{2}-n^{2}),\ \,b=k\cdot (2mn),\ \,c=k\cdot (m^{2}+n^{2})
    '''
    # TODO
    pass 

# t0 = time.time()
# x = pytrip_optimizedbymath()
# t1 = time.time()
# print(x, (t1-t0))