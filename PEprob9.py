__author__ = 'Ashwin'

# There exists exactly one Pythagorean triplet (a,b,c with a**2 + b**2 = c**2) for which a + b + c = 1000.
# Find the product abc.




found = False
for a in range(1,499):
    if(found):
        break
    asquared = a**2
    #c > a,b, so 1000 - (a+b) > a, 1000 - (a+b) > b, 1000 > 2a +b, 1000 > 2b + a; b <= (1000-a)/2, b <= 1000-2a
    maxb = int((1000-a)/2) +1
    for b in range(1,maxb):
        c = 1000 - (a+b)
        if(asquared + b**2 == c**2):
            prod = a*b*c
            trio = [a,b,c]
            found = True
if(found):
    print(prod)
    print(trio)

