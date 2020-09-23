'''
Maximum path sum I
Submit

 Show HTML problem content 
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''
'''
   3
  7 4
 2 4 6
8 5 9 3
    transforms into
3
7 4
2 4 6
8 5 9 3

    coordinate representation:

           (0,0)
        (1,0),(1,1)
     (2,0),(2,1),(2,2)
  (3,0),(3,1),(3,2),(3,3)
    is read as
(0,0)
(1,0),(1,1)
(2,0),(2,1),(2,2)
(3,0),(3,1),(3,2),(3,3)

valid paths are always either (i+1, j) or (i+1, j+1)
'''

import timeit

def loadfile(filename):
    with open(filename) as matrix:
        grid = matrix.readlines()
        matrix = []
        for line in grid:
            x = map(int, line.split())
            intlist = list(x)
            matrix.append(intlist)
    return matrix


def maxpath_naive(data):
    '''
    Input: data from loadfile func., or data structured as a matrix/ list-of-lists: [[]]
        ASSUMES INPUT DATA IS 1:1 TRIANGULAR
    Method: recurses through every path
    Output: sum of maximum value path through the triangular array
    '''
    imax = len(data)-1
    def recurse(data, i=0, j=0):
        if i == imax:
            return data[i][j]
        else:
            cdata = data[i][j]
            nextleft = recurse(data, i = i+1, j = j+0)
            nextrigt = recurse(data, i = i+1, j = j+1)
            return max( (cdata+nextleft), (cdata+nextrigt) )
    return recurse(data)


def maxpath_tdmemo(data):
    '''
    Input: data from loadfile func., or data structured as a matrix/ list-of-lists: [[]]
        ASSUMES INPUT DATA IS 1:1 TRIANGULAR
    Method: recurses through every path, returning memoized results if possible
    Output: sum of maximum value path through the triangular array
    '''
    imax = len(data)-1
    def recurse(data, i=0, j=0, memo={}):
        if (i,j) not in memo:
            if i == imax:
                memo[(i,j)] = data[i][j]
            else:
                cdata = data[i][j]
                nextleft = recurse(data, i = i+1, j = j+0, memo=memo)
                nextrigt = recurse(data, i = i+1, j = j+1, memo=memo)
                memo[(i,j)] = max( (cdata+nextleft), (cdata+nextrigt) )
            return memo[(i,j)]
        else:
            return memo[(i,j)]
    return recurse(data)


def maxpath_bottomup(data):
    x = len(data)
    rvt = [ [0 for i in range(x)] for j in range(x)] #initialize result value table
    rvt[0][0] = data[0][0] 
    for i in range(1,x):
        jmax = len(data[i])
        for j in range(0, jmax):
            rvt[i][j] = max(
                data[i][j] + rvt[i-1][j],
                data[i][j] + rvt[i-1][j-1]
            )
    return max(rvt[x-1])


#----------------------------------------------------------------------------
# data = loadfile('0018_testsource.txt')
data = loadfile('0018_triangle.txt')
# data = loadfile('0067_triangle.txt')
#----------------------------------------------------------------------------
# t0 = timeit.default_timer()
# r = maxpath_naive(data)
# t1 = timeit.default_timer()
# dt = t1-t0
# print('----------\nMaximum Path by simple recursion\n', r, round(dt*1e6), round(dt,1))
# # result: 1074, approx 11600 mus using 0018_triangle.txt
#----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = maxpath_tdmemo(data)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nMaximum Path by memoized recursion\n', r, round(dt*1e6), round(dt,1))
# result: 1074, approx 140 mus using 0018_triangle.txt
# result: 7273, approx 6098 mus using 0067_triangle.txt
#----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = maxpath_bottomup(data)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nMaximum Path by iterative dynamic programming\n', r, round(dt*1e6), round(dt,1))
# result: 1074, approx 96 mus using 0018_triangle.txt
# result: 7273, approx 3201 mus using 0067_triangle.txt
#----------------------------------------------------------------------------
