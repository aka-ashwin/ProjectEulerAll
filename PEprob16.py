__author__ = 'Ashwin'

#find the sum of the decimal digits of 2**1000

def digitsum(num):
    strnum = str(num)
    sumofdigits = 0
    for digit in strnum:
        sumofdigits += int(digit)
    return sumofdigits

ans = digitsum(2**1000)
print(ans)