#-------------------------------------------------------------------------------
# Name:        Number repetition counter
# Purpose:     Checks to see how many times, and where a number repeats in a list
#
# Author:      tembov
#
# Created:     01/02/2015
# Copyright:   (c) tembov 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
check = []
set = [1,8,11,24,33,39,41,56,71,78]
length = len(set)
ite = 0
while ite < length:
    for i in range(length):
        if ite != i:
            print str(set[ite]) + " + " + str(set[i]) + " = " + str((set[ite] + set[i]))
            check.append(set[ite] + set[i])
        else:
            pass
    ite +=1

l_length = len(check)
print check
print ("We start here")
for i in range(l_length):
    print str(check[i]) + " occurs " + str (check.count(check[i])/2) + " times."
