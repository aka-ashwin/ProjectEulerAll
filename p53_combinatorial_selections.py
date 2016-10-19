__author__ = 'Ashwin'

#It is not until n = 23 that a value exceeds one-million: 23C10 = 1144066.
#How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

#symmetry: only need to consider, say, 1 <= r <= ceil(n/2)
#monotonicity: can start from, say, 1 and work way up to first r at which 10**6 is crossed
#better - can use previous threshold point as guess, and explore from there

#note 23c10 = 23!/(10!13!); 23c11 = 23!/(11!12!) = 23c10 * 13/11 => nC(r_0 +1) = nCr_0 * (n-r_0)/(r_0 +1) for r_0 < n/2
# 24c10 = 24!/(10!14!) => (n+1)C(r+1) = nCr * (n+1)/(n-r+1)


count = 4
thresh = 10**6

r = 10
comb = 1144066
adjcomb = 817190

for n in range(24,101):
    #adjust combinatorial factor to be equal to new nCr
    comb *= n
    comb /= (n-r)

    adjcomb *= n
    adjcomb /= (n-r-1)


    while(adjcomb >= thresh):
        comb *= (r)
        comb /= (n-(r-1))
        adjcomb *= (r-1)
        adjcomb /= (n-(r-2))
        r -= 1

    while(comb < thresh):
        comb *= (n-r)
        comb /= (r+1)
        adjcomb *= (n-(r-1))
        adjcomb /= r
        r += 1

    #when threshold r value (= first for which nCr >= 10**6) found
    #we know that all nCr' >= 10**6 for r' in [r,n-r]
    count += n - 2*r +1

print(count)