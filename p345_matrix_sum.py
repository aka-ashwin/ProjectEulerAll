__author__ = 'Ashwin'
#We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column.
#find the matrix sum of the given matrix

import random
import math

filename ="C:/Users/Ashwin/PycharmProjects/ProjectEuler/src345_matrix.tsv"

def get_matrix_from_file():
    mat = []
    #format: 3 characters for number (eg 7 = "  7"), followed by space, followed by 3 chars for next number
    #last number of line is followed by a space, so line has exactly 4 characters per number
    with open(filename) as src_file:
        for line in src_file:
            currlist = []
            num_items = int(len(line)/4)
            currind = 0
            for i in range(0,num_items):
                currlist.append(int(line[currind:currind+3]))
                currind += 4
            mat.append(currlist)
        return mat

def get_sum_from_assignment(matrix, assignment):
    sum = 0
    for i in range(0, len(assignment)):
        sum += matrix[i][assignment[i]]
    return sum



matrix = get_matrix_from_file()

msum = 0
numcycles = 10000
beta = .05

assignment = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
msum = get_sum_from_assignment(matrix, assignment)
msums = [msum]
numposns = len(assignment)

for cycle in range(0,numcycles):
    for step in range(0,numposns):
        pos1 = random.randint(0,numposns-1)
        pos2 = random.randint(0,numposns-2)
        if(pos2 == pos1):
            pos2 += 1
            pos2 = pos2%numposns

        assn1 = assignment[pos1]
        assn2 = assignment[pos2]
        delta_msum = matrix[pos1][assn2] + matrix[pos2][assn1] - (matrix[pos1][assn1] + matrix[pos2][assn2])
        #if "free energy" is increased, always accept move
        if(delta_msum > 0):
            assignment[pos1] = assn2
            assignment[pos2] = assn1
            msum += delta_msum
        #else, undergo metropolis accept step
        else:
            boltz_fac = beta*delta_msum
            boltz_rat = math.exp(boltz_fac)
            comparison = random.random()
            if(boltz_rat > comparison):
                assignment[pos1] = assn2
                assignment[pos2] = assn1
                msum += delta_msum

    #at end of each cycle, write msum to file
    with open("C:/Users/Ashwin/PycharmProjects/ProjectEuler/src345_msums.csv", "a") as outfile:
        outfile.write(str(msum) + "\n")
    msums.append(msum)
    if(cycle > 5):
        if(msum == msums[cycle-5]):
            beta -= .0001
        elif(msum > msums[cycle-5]*1.1):
            beta += .0001
    print(str(msum) + ", " + str(max(msums)) + "; " + str(beta))
    print(beta)
print(msum)
print(max(msums))