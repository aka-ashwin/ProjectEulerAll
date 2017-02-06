__author__ = 'Ashwin'


#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#(where fibo numbers F_n are defined such that F_1 = 1, F_2 = 1, F_3 = F_1 + F_2, etc)



currind = 2

currnum = 1
pastnum = 1

holder = 1

#smallest thousand-digit number = 10^999; want first fibo number above this
threshold = 10**999

#loop until we get our current fibo number greater than the threshold
while(currnum < threshold):
    #need a separate holder variable to hold the current number
    #since next fibo number = curr + past
    #and we also need to update past fibo to current fibo
    holder = currnum
    currnum += pastnum
    pastnum = holder

    #update index
    currind += 1

print(currind)


