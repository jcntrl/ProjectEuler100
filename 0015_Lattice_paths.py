'''
Lattice paths
Submit

 Show HTML problem content 
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''
import timeit

def LatticePathEndPath(x, y, xi=0, yi=0): 
    # not fully brute force, technically, as the end path return is a slight optimization
    # nevertheless, still a variant of the naive recursive algorithm 
    if xi == x-1 or yi == y-1:
        return 1
    else:
        return LatticePathEndPath(x, y, xi+1, yi) + LatticePathEndPath(x, y, xi, yi+1)


def LatticePathMemo(x, y, xi=0, yi=0, memo={}):
    if (xi,yi) not in memo:
        if xi == x-1 or yi == y-1:
            memo[(xi,yi)] = 1
        else:
            memo[(xi,yi)] = LatticePathMemo(x, y, xi+1, yi, memo) + LatticePathMemo(x, y, xi, yi+1, memo)
    return memo[(xi,yi)]


def LatticePathDP(x,y):
    resarr = [[1 for i in range(x)] for j in range(y)]
    for xi in range(1, x):
        for yi in range(1, y):
            resarr[xi][yi] = resarr[xi-1][yi] + resarr[xi][yi-1]
    return resarr[x-1][y-1]


# #----------------------------------------------------------------------------
# inputs for testing
# A NxM GRID in (N+1)x(M+1) NODES; path traversal is across nodes, therefore this is a nodal approach
# x,y = 2,2 #==>2
# x,y = 3,3 #==>6
# x,y = 4,4 #==>20
# x,y = 10,10 #==>48620
# x,y = 15,15 #==>40116600, epbf-->16.1 s, memo-->240 mus, itDP-->60 mus
x,y = 21,21 #==>137846528820, epbf-->TOOLONG s, memo-->449 mus, itDP-->111 mus
# #----------------------------------------------------------------------------
# t0 = timeit.default_timer()
# r = LatticePathEndPath(x,y)
# t1 = timeit.default_timer()
# dt = t1-t0
# print('----------\nNumber of paths by End Path Brute Force\n', r, round(dt*1e6), round(dt,1))
# # #----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = LatticePathMemo(x,y)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nNumber of paths by Memoization\n', r, round(dt*1e6), round(dt,1))
#----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = LatticePathDP(x,y)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nNumber of paths by IterativeDP\n', r, round(dt*1e6), round(dt,1))
#----------------------------------------------------------------------------