__author__ = 'Ashwin'


#from the source list of form "base,exponent", find the line number  of the pair with the largest base^exp value
#just doing base^exp will cause overflow; instead, compare log(base)*exp = log(base^exp)

import math

pairs = []
with open("C:/Users/Ashwin/PycharmProjects/ProjectEuler/src99_base_exp.txt") as reader:
    for line in reader.readlines():
        a = line.split(",")
        a[0] = int(a[0])
        a[1] = int(a[1])
        pairs.append(a)


bestind = 0
bestval = 0

for i in range(0, len(pairs)):
    currval = math.log(pairs[i][0])*pairs[i][1]
    if currval > bestval:
        bestval = currval
        bestind = i

print(bestind +1)
