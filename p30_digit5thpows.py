__author__ = 'Ashwin'


#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#let x = n 9s = 9...9 has 5thpow sum n*9^5 < n * 10^5; for n = 6, value of x ~ 10^7 > 6 * 10^5
                                #specifically, crossover should happen btw n = 5 and 6 -> x ~ 10^6, vs digsum = 5 9^5


def dig5thsum(n):
    output = 0
    strn = str(n)
    for char in strn:
        output += int(char)**5
    return output


dif5thtable = []
for i in range(1,10):
    dif5thtable.append(i**5 - (i-1)**5)

def dig5thincrto(n, currsum):
    incr = currsum

    # pow = 10
    # remainder = n%pow
    # while(remainder == 0):
    #     pow *= 10
    #     remainder = n%pow

    a = n%10
    if(a != 0):
        incr += dif5thtable[a-1]

    else:
        incr = dig5thsum(n)

    return incr

n = 2
dig5th = 2**5
dig5thsumval = 0
dig5thlist = []
done = False
while(not done):
    if(n%100 == 0):
        print(n)
        print(dig5thlist)
    n += 1
    dig5th = dig5thincrto(n,dig5th)
    if(n > 10**6):
        done = True
    elif(n == dig5th):
        dig5thsumval += dig5th
        dig5thlist.append(n)

print(dig5thsumval)
print(dig5thlist)