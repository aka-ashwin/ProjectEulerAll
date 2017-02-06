__author__ = 'Ashwin'


#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumofsq(n):
    sumofsqs = 0
    for i in range(1,n+1):
        sumofsqs += i*i
    return sumofsqs

def sqofsum(n):
    sum_to_n = (n*(n+1))/2
    squareofsum = sum_to_n*sum_to_n
    return squareofsum

print(sqofsum(100) - sumofsq(100))