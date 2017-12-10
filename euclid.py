__author__ = 'tembov'

def euclid (M, N):
    R = 0
    if (M<1 or N<1):
        return

    if (M<N):
        temp = 0
        temp = M
        M = N
        N = temp
    else:
        pass

    R = M % N

    if (R != 0):
        return euclid(N,R)
    else:
        return N

first = int(input("Type in your first number: "))
second = int(input("Type in your second number: "))

answer = euclid(first, second)
if (answer != None):
    print ("The GCD of " + str(first) + " and " + str(second) + " is " + str(answer))
else:
    print ("Due to problems with your input, the GCD could not be computed.\n")



