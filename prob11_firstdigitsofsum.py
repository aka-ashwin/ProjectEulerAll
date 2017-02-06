__author__ = 'Ashwin'


#find the first 10 digits of the sum of the following 100 50-digit numbers:
#the sum of the 14th digits on can only affect the 11th digit max
# (if all are 999.., it's about the same as adding 1 to each 13th place -> 1 to the sum of the 11th place)
#so we only need to sum the first 13 digits, and then truncate to 10


answer = 0
with open("C:/Users/Ashwin/PycharmProjects/ProjectEulerFirst30/src11_numstosum.csv") as f:
    for numstr in f.readlines():
        answer += int(numstr[0:14])

print(answer)
print(str(answer)[0:10])
