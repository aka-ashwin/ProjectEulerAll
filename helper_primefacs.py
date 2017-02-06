__author__ = 'Ashwin'
import math
#note: current implementation is v shitty. ideally, have txt file of generated primes (up to some fairly high number) that you load to get the primestlist vector

def genprimeslist(maxN):
    primeslist = [2,3,5,7]
    for currposs in range(11,maxN+1,2):
        isprime = True
        for prime in primeslist:
            if(currposs%prime == 0):
                isprime = False
                break
        if(isprime):
            primeslist.append(currposs)
        if(currposs == maxN/100):
            print(currposs)
    return primeslist

defaultplist = genprimeslist(1000)


def checkfac(num,possfac):
    return(num%possfac == 0)

def checkprime(num, primeslist = defaultplist):
    return(num in primeslist)




def highestprimefac(num):
    currtry = num-1
    facfound = False
    while(not facfound):
        print(currtry)
        if(checkfac(num,currtry)):
            if(checkprime(currtry)):
                facfound = True
        else:
            currtry -= 1

    return currtry

def getlowestprimefac(num, primeslist = defaultplist):
    try:
        for currtry in primeslist:
            if(checkfac(num, currtry)):
                lowestfac = currtry
                break

        return lowestfac
    except:
        print("number " + str(num) + " too big to get its lowest prime factor; need to generate a larger prime list to compare it to.")

def getprimefacs(num):
    primefacs = []
    currnum = num
    while(currnum > 1):
        nextfac = getlowestprimefac(currnum)
        primefacs.append(nextfac)
        currnum = currnum/nextfac
    return primefacs
