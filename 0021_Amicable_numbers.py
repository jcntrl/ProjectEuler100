'''
Amicable numbers
Submit

 Show HTML problem content 
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def aliquotfactorize(num):
    ## PARTIAL BRUTE FORCE, SWEEP LENGTH REDUCED TO SQRT(NUM)
    # by noticing and acting that each factor found in ascending order has a mirrored factor descending from num:
        # for example: num=100: 1x100, 2x50, 4x25, 5x20, 10x10
            # can reduce a lot of computational burden this way
    aliquotfactors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0: #qualification by trial division, yay super!
            if i == num//i: #don't double-list the middle-solution factor if it exists
                aliquotfactors.append(i)
            else: #list the factor and its mirror
                aliquotfactors.append(i)
                aliquotfactors.append(num//i)
    aliquotfactors.remove(num)
    return aliquotfactors


def testifamicable(a):
    afactors = aliquotfactorize(a)
    b = sum(afactors)
    bfactors = aliquotfactorize(b)
    sumofbfactors = sum(bfactors)
    if sumofbfactors == a and a != b:
        return True, a, b
    else:
        return False, a, b

def sum_of_amicable_nums_to_n(n):
    listofamicablenums = []
    for num in range(2, n):
        if num not in listofamicablenums:
            x = testifamicable(num)
            if x[0]:
                listofamicablenums.append(x[1])
                listofamicablenums.append(x[2])
    return sum(listofamicablenums)


print(sum_of_amicable_nums_to_n(10000))