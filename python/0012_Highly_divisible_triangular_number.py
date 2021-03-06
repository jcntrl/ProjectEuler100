'''
Highly divisible triangular number

Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

'''
some background reading on the purely mathematical solution: The Tao Function. This will lead to an interesting alternative approach!
    https://en.wikipedia.org/wiki/Divisor_function
    https://mathschallenge.net/library/number/number_of_divisors
    https://primes.utm.edu/glossary/page.php?sort=Tau
'''
import time

def factorize(num):
    factors = []
    ## BRUTE FORCE WITH 50% REDUCED SWEEP LENGTH
        # this wouldn't even converge within the limit of my patience (walkaway 10 minutes to do laundry) to find a TrNum with >500 factors
    # for i in range(1, num//2 + 1):
    #     if num%i == 0:
    #         factors.append(i)
    # factors.append(num)
    ##
    
    ## PARTIAL BRUTE FORCE, SWEEP LENGTH REDUCED TO SQRT(NUM)
    # by noticing and acting that each factor found in ascending order has a mirrored factor descending from num:
        # for example: num=100: 1x100, 2x50, 4x25, 5x20, 10x10
            # can reduce a lot of computational burden this way
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0: #qualification by trial division, yay super!
            if i == num//i: #don't double-list the middle-solution factor if it exists
                factors.append(i)
            else: #list the factor and its mirror
                factors.append(i)
                factors.append(num//i)
    return factors

def highlyDivisibleTriangleNums(n):
    '''
    input: n = minimum num of divisors to qualify solution
    output: returns the first triangle number which contains > n divisors
    '''
    # initialize for while loop
    TNum = 0
    i = 0
    divisors = []
    while len(divisors) < n:
        # while loop simply calls factorize function on each iteration. That is where the real meat of the solution is. Look there!
        i += 1
        TNum += i
        divisors = factorize(TNum)
    return TNum, len(divisors)


# execute functions and prints the answer, and computation time for your/my local device. 
n = 500
t0 = time.time()
result = highlyDivisibleTriangleNums(n)
t1 = time.time()
answer = "\n-------------------\nTriangle Number: {}\nnum of divisors: {}\nexecuted in {} seconds.\n-------------------\n"
print(answer.format(result[0],result[1],t1-t0))
# for n = 500, solution is returned in ~3.5s on my device. Slow for what I want, but well within satisfactory Project Euler requirement.


