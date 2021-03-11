'''
Non-abundant sums
Submit

 Show HTML problem content 
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import timeit

def aliquotfactorize(num):
    ## PARTIAL BRUTE FORCE, SWEEP LENGTH REDUCED TO SQRT(NUM)
    # by noticing and acting that each factor found in ascending order has a mirrored factor descending from num:
        # for example: num=100: 1x100, 2x50, 4x25, 5x20, 10x10
            # can reduce a lot of computational burden this way
    aliquotfactors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0: #qualification by trial division, yay super!
            aliquotfactors.add(i)
            aliquotfactors.add(num//i)
    aliquotfactors.remove(num)
    return aliquotfactors

def isabundantnum(num):
    numfacts = aliquotfactorize(num)
    return sum(numfacts) > num

def abundantsset(num):
    setofabundants = set()
    for i in range(12, num+1, 1): #even though the vast majority of abundant nums are even, a handful are odd and divisible by 5, and there's a curveball in that set too that's odd but indivisible by 5. So, one by one we march.
        if isabundantnum(i):
            setofabundants.add(i)
    return setofabundants

def greatestabundantsum(limit=28123):
    # generate set of all abundant numbers to limit (inclusive) 
    soa = abundantsset(limit)
    # then generate set of all integers that CAN be written as the sum of two abundant numbers that are less than the limit
    canbe = set()
    for i in soa:
        for j in soa:
            tmp = i+j
            if tmp <= limit:
                canbe.add(tmp)
    # generate list of all ints up to limit
    allints = {i for i in range(limit+1)}
    # now determine the anti-intersection (difference) of sets allints and canbe
    cannotbe = allints - canbe
    return sum(cannotbe)


# #----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = greatestabundantsum()
t1 = timeit.default_timer()
dt = t1-t0
print(r, round(dt*1e6), round(dt,1))
# solution 4179871 completes in 5.1 seconds
# #----------------------------------------------------------------------------

# #----------------------------------------------------------------------------