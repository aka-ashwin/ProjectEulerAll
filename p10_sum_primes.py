__author__ = 'Ashwin'

import prime_testing as pt

pt.write_prime_list(2*10**6)

primesum = 0
for i in range(2,2*10**6):
    if(pt.isprime_wrt_list(i)): primesum += i
print(primesum)
