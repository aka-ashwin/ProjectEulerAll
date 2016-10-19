__author__ = 'Ashwin'
#
# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random,
#  it can be seen that the probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2.
#
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
# is a box containing eighty-five blue discs and thirty-five red discs.
#
# By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total,
#  determine the number of blue discs that the box would contain.


#denote total number by n, numble blue by m
#for large n, we will have m very close to n/sqrt(2)
#rather than being fancy, we will just start with n = 10^12, guess m = int(sqrt(2) * n)
#adjust m until it's the lowest m that gives probability p(n,m) >= .5
#if p(n,m) != .5, increase n and repeat process

import math

def p(n,m):
    # = m/n * (m-1)/(n-1)
    return (m*m - m)/(n*n - n)

def pstatus(n,m):
    mterm = m*m -m
    nterm = n*n -n
    if(2*mterm == nterm):
        return "equal"
    elif(2*mterm > nterm):
        return "greater"
    else:
        return "less"


n = 10**12
m = int(n/math.sqrt(2))
found = False


while(not found):
    if(n%1000 == 0):
        print(n)
    n += 1
    while(pstatus(n,m-1) == "greater"):
        m -= 1
    while(pstatus(n,m) == "lesser"):
        m += 1
    if(pstatus(n,m) == "equal"):
        found = True
        print(m)
        print(p(n,m))

print(m)