__author__ = 'Ashwin'

import math
#global variable
primelist_filename = "C:/Users/Ashwin/PycharmProjects/ProjectEuler/primetest.txt"


#return list of primes from file
def read_prime_list(fname = primelist_filename):
    outlist = []
    f = open(fname, "r")
    for line in f:
        outlist.append(int(line))
    return outlist

plist = read_prime_list(primelist_filename)


def isprime_wrt_list(i, primelist = plist):
    threshold = int(math.sqrt(i))
    isprime = True
    for prime in primelist:
        if(prime > threshold):
            break
        elif(i%prime == 0):
            isprime = False
            break
    return isprime

#generate + write list of primes up to max value to file
def write_prime_list(maxval):
    #simple prime list generation:
    prevmax = max(plist)
    currprimelist = plist
    for i in range(prevmax+1,maxval):
        isprime = isprime_wrt_list(i, currprimelist)
        if(isprime):
            currprimelist.append(i)

    f = open(primelist_filename, "w")
    for prime in currprimelist:
        f.write(str(prime) + "\n")