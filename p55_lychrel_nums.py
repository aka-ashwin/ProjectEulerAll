__author__ = 'Ashwin'

import math

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
# Due to the theoretical nature of these numbers, and for the purpose of this problem,
# we shall assume that a number is Lychrel until proven otherwise.
# In addition you are given that for every number below ten-thousand,
# it will either
#   (i) become a palindrome in less than fifty iterations, or,
#   (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
#   In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
#        4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?


def nlist(n):
    ncopy = n
    currpow = 1
    npart = ncopy%(currpow*10)
    outlist = [npart]
    ncopy -= npart
    while(ncopy >0):
        currpow *= 10
        npart = int((ncopy%(currpow*10))/currpow)
        outlist.append(npart)
        ncopy -= npart*currpow
    return outlist


def rev(n):
    m = 0
    nl = nlist(n)
    nlen = len(nl)
    currpow = 10**(nlen-1)
    for i in range(0,len(nl)):
        currel = nl[i]
        m += currel*currpow
        currpow /= 10
    return int(m)


def pal(inlist):
    ispal = True
    lenlist = len(inlist)
    checkmax = int(lenlist/2)
    for i in range(0, checkmax):
        if(inlist[i] != inlist[lenlist-i-1]):
            ispal = False
            break
    return ispal

def npal(n):
    return pal(nlist(n))


ub = 10**4
lylist = []
lycount = 0
currn = 0
islych = True
for i in range(1,ub):
    currn = i
    islych = True
    for loop in range(0,50):
        currn += rev(currn)
        if(npal(currn)):
            islych = False
            break
    if(islych):
        lylist.append(i)
        lycount += 1

print(lylist)
print(lycount)
