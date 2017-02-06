__author__ = 'Ashwin'

import helper_fibonacci

fibstil4mil = helper_fibonacci.fibos_til_value(4000000)

evenfibsum = 0
for fib in fibstil4mil:
    if(fib%2 == 0):
        evenfibsum += fib

print(evenfibsum)
