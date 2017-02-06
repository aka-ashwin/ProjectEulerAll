__author__ = 'Ashwin'

# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

#thought - we can see that partitioning 5 = partitioning 4 + adding 1 to each unique-sized pile in each partition

#alt - sort by smallest group in partition, then by smallest group in subpartition, etc
#seems like there should be some good way to build off prev results tho

saved_values = {}



def partition(nleft, sumsofar, ub = 0):
    if(nleft==0):
        return sumsofar + 1

    else:
        delta_sum = 0
        maxposs = 0
        if(ub == 0):
            maxposs = nleft
        else:
            maxposs = min(nleft,ub)
        try:
            delta_sum = saved_values[(nleft,maxposs)]
        except:
            for i in range(1,maxposs+1):
                delta_sum = partition(nleft-i,delta_sum,ub=i)
            saved_values[(nleft, maxposs)] = delta_sum
        return sumsofar + delta_sum

million = 10**6
millmultfound = False
n = 0
a = 0

while(not millmultfound):
    if(n%10 == 0):
        print(n)
        print(a)
    n += 1
    a = 0
    a = partition(n,a)

    if(a%million == 0):
        millmultfound = True

print(n)
