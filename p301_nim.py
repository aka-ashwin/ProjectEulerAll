__author__ = 'Ashwin'

# Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.
#
# We'll consider the three-heap normal-play version of Nim, which works as follows:
# - At the start of the game there are three heaps of stones.
# - On his turn the player removes any positive number of stones from any single heap.
# - The first player unable to move (because no stones remain) loses.
#
# If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and n3 then there is a simple function X(n1,n2,n3) - that you may look up or attempt to deduce for yourself - that returns:
#
# zero if, with perfect strategy, the player about to move will eventually lose; or
# non-zero if, with perfect strategy, the player about to move will eventually win.
# For example X(1,2,3) = 0 because, no matter what the current player does, his opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by his opponent until no stones remain; so the current player loses. To illustrate:
# - current player moves to (1,2,1)
# - opponent moves to (1,0,1)
# - current player moves to (0,0,1)
# - opponent moves to (0,0,0), and so wins.
#
# For how many positive integers n???230 does X(n,2n,3n) = 0 ?
#
# X(n1,n2,n3):
    #for each bit place, sum the binary digits of n1,n2,n3, modulo 2 (eg 1 + 1 + 0 = 0, 1 + 1 + 1 = 1)
    #if any bit place has sum != 0, the current player will win given perfect play
    #if all bit places have sum = 0, the current player will lose
    #exa: (1,2,3) -> (1, 10, 11) -> placewise sums = 1+1 = 0; game is lost for current player


import binary_conversions_manipulations

def charbitsum(chars):
    output = 0
    for char in chars:
        if(char != "0"):
            output += 1
    return output

#assumes a <= b <= c
def nimsumiszero(stra, strb, strc):
    #initialize output
    sumiszero = True

    #get maximum bit place to check
    alen = len(stra)
    blen = len(strb)
    clen = len(strc)

    currsum = 0

    #if clen is > blen, then assuming no leading 0s are used, the sum must be nonzero
    if(clen > blen):
        sumiszero = False


    else:
        #blen and clen are same, >= alen
        #compare values where they differ first
        ind = 0
        for i in range(alen, clen):
            ind = clen -1 - i
            if(strb[ind] != strc[ind]):
                sumiszero = False
                break

        if(sumiszero):
            for i in range(0, alen):
                aind = alen-1 - i
                bcind = clen-1 - i
                currsum = charbitsum([stra[aind], strb[bcind], strc[bcind]])
                currsum = currsum %2
                if(currsum != 0):
                    sumiszero = False
                    break

    return sumiszero

threshold = 2**30
count = 0

nstr = ""
n2str = ""
n3str = ""

lb = 1
ub = 2
for pow2 in range(1,31):
    for n in range(lb,ub):
        nstr = binary_conversions_manipulations.decimalnum_to_binarystring(n)
        n2str = nstr
        n2str += "0"
        n3str = binary_conversions_manipulations.decimalnum_to_binarystring(3*n)

        losing = nimsumiszero(nstr,n2str,n3str)
        if(losing):
            count += 1

    print(str(lb) + ", " + str(ub) + ": " + str(count))

    lb*=2
    ub*=2