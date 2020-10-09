'''
Lexicographic permutations
Submit

 Show HTML problem content 
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import copy


def allnextlexperms(a):
    '''
    INPUT: Takes an iterable input (string, list, etc) and converts to sorted list.
    METHOD: as described below, from https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order. Code implementation my own work.
        1) Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
        2) Find the largest index l greater than k such that a[k] < a[l].
        3) Swap the value of a[k] with that of a[l].
        4) Reverse the sequence from a[k + 1] up to and including the final element a[n].
    OUTPUT: lexicographic sorted list of permutations (list of lists).
    '''
    a = sorted(list(a)) #assure input is a sorted list; all other steps depend on this data structure
    perms = list()
    perms.append(copy.copy(a))
    keepgoing = True
    def nextlexperm(array):
        k = len(array) - 2 # initialize search at second-to-last element
        while k >= 0:
            if array[k] < array[k + 1]: # step 1: find the largest index k such that a[k] < a[k+1]
                l = len(array) - 1
                while l > k: # step 2: find the largest index l such that a[k] < a[l]
                    if array[k] < array[l]:
                        array[k], array[l] = array[l], array[k] # step 3: swap elements
                        array[k+1:] = array[-1:k:-1] # step 4: reverse sequence in-place from a[k+1] to(incl) a[end]
                        return array
                    else:
                        l -= 1
            elif k == 0:
                return False
            else:
                k -= 1
    while keepgoing:
        prevperm = copy.copy(perms[-1])
        nextperm = nextlexperm(prevperm)
        if nextperm:
            perms.append((copy.copy(nextperm)))
        else:
            keepgoing = False
    return perms


# ~~~ DRIVER CODE ~~~

tc1 = '1234' # should return '4321'
tc2 = '0125330' # should return '5332100'
tc3 = '012' # should return 210
tc4 = '0123456789' # should return 9876543210
tc5 =  ['1','2','3','4'] # should return '1234'
x = allnextlexperms(tc4)
print(len(x))
print(''.join(x[-1]))

# Desired Output:
print(''.join(x[999_999]))