__author__ = 'Ashwin'
#smallest number divisible by all numbers 1 thru 20

def getsmallestmult(upto):
    remaining_nums_thru_upto = []
    for i in range(0,upto+1):
        remaining_nums_thru_upto.append(i)
    print(remaining_nums_thru_upto)


    prod = 1
    for i in range(2,upto+1):
        currelem = remaining_nums_thru_upto[i]
        if(currelem != 1):
            prod *= currelem
            for j in range(i+1,upto+1):
                print(remaining_nums_thru_upto)
                jelem = remaining_nums_thru_upto[j]
                if(jelem%currelem == 0):
                    remaining_nums_thru_upto[j] = int(jelem/currelem)
    return prod

a = getsmallestmult(20)
print(a)