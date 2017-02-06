__author__ = 'Ashwin'

import math

#The decimal number, 585 = 1001001001 (in binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)


#I could do this without casting to string, but that's a little fiddly, so
#I'm going to cast the numbers to strings and test for palindromicity
#fn to check if input string is palindrome
def is_palindrome(instr):
    #initialize var to return
    ispal = True

    lenstr = len(instr)
    maxind = lenstr-1
    #want to check all indices up to n/2 for even-length string, or n-1/2 for odd-length string
    #so, just take half the length and truncate it to an int (ignores decimals, as we want it to)
    threshold = int (lenstr/2)

    #initialize variables to compare in loop
    currchar = "a"
    currpal = "a"
    for i in range(0, threshold):
        currchar = instr[i]
        currpal = instr[maxind-i]
        if(currchar != currpal):
            ispal = False
            break

    return ispal


#note that no leading zero allowed in binary means no final zero, means we only need to check odd numbers

#fn to convert decimal number to binary string
def decimalnum_to_binarystring(n):
    #initialize output
    outstr = ""

    #get maximum bit place involved in binary string, = len of string -1
    mpow = int(math.log(n,2))
    powval = 2**mpow
    m = n - powval
    outstr += "1"

    for i in range(0, mpow):
        powval = powval/2
        haspow = int(m/powval)
        if(haspow):
            outstr += "1"
            m -= powval
        else:
            outstr += "0"

    return outstr


#main loop

sum = 0
m = 1
strm = "1"
binm = "1"
for n in range(0,5*10**5):
    #remember, only looping over odd numbers btw 1 and 10^6 -1, inclusive
    m = 2*n + 1
    strm = str(m)
    if(is_palindrome(strm)):
        binm = decimalnum_to_binarystring(m)
        if(is_palindrome(binm)):
            sum += m

print(sum)

