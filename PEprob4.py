__author__ = 'Ashwin'

def isPal(instr):
    strlen = len(instr)
    if(strlen <= 1):
        return True

    isPalindrome = True
    for i in range(0,strlen):
        if(instr[i] != instr[strlen-1 -i]):
            isPalindrome = False
            break
    return isPalindrome

def isPalNum(num):
    return(isPal(str(num)))


pals = []
for diag in range(0,100):
    for i in range(0,int((diag+1)/2)):
        j = diag-i
        prod = (999-i)*(999-j)
        print(prod)
        if(isPalNum(prod)):
            pals.append(prod)

print(pals)
print(max(pals))