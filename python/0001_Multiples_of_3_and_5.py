# Multiples of 3 and 5
# Problem 1

def Sum_of_multiples_of(n=1000, mult=[3,5]):
    '''
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.
    Input: n = 1000, or input other desired upper limit (integer)
    Input: mult = [3,5], or list of other integer multiples
    Output: integer sum of these multiples beneath (exclusive) upper bound
    
    O(n*mult) time complexity
    '''

    resultarr = []
    for i in mult:
        for j in range(n):
            tmp = j % i
            if tmp == 0 and j not in resultarr:
                resultarr.append(j)
    return sum(resultarr)

# test cases
assert Sum_of_multiples_of(10) == 23, "should be 23"
assert Sum_of_multiples_of(15) == 45, "should be 45"
assert Sum_of_multiples_of(24, [2,3,4]) == 180, "should be 180"

# output
print(Sum_of_multiples_of())