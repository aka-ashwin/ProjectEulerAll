__author__ = 'Ashwin'

import math
import prime_testing


found = False

num = 13

while(not found):
    num += 2
    print(num)

    #check composite-ness
    if(num in prime_testing.plist):
        continue

    writeable = False
    currsq = 1
    for n in range(1, math.ceil(math.sqrt(num/2.)) ):
        currsq = 2*n*n
        remaining = num - currsq
        if(remaining in prime_testing.plist):
            writeable = True
    if(not writeable):
        found = True

print(num)


