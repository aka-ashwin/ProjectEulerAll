__author__ = 'Ashwin'
import math

#Problem 63: The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#How many n-digit positive integers exist which are also an nth power?


#thought process: must drop off at some point to be calculable..what's the maximum?
#ln(.1)/ln(.9) = 21.something; .9^22 is the first integer power of .9 less than .1
#QED 21 is the max power m such that any m-digit integer n can be written as a^m for some integer a
#(since numbers a >= 10 will always have a^m more than m digits, we only need consider 1 <= a < 10)

#further, for 1 < a' < a < 10, (a')^m being m-digit implies a^m is m-digit
#thus, we only need to figure out which single-digit integer a* is the lower one to have its power a*^m be m-digit
    #(for each m in [1,21])


minint = 1
count = 0
threshold = math.log(.1)

minintlegit = False
for m in range(1, 22):
    while(not minintlegit):
        if(math.log(minint/10.)*m >= threshold):
            break
        else:
            minint += 1

    count += (10-minint)

print(count)