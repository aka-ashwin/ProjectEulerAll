__author__ = 'Ashwin'

import math

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

