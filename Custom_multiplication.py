#-------------------------------------------------------------------------------
# Name:       Custom multiplication
# Purpose:  This function provides a definition for multiplication
#
# Author:      tembov
#

#-------------------------------------------------------------------------------
def multiply(number, times):
    multiplied = number
    for i in range(times - 1):
        multiplied = multiplied + number

    return multiplied

input("Welcome to the number calculator. Press enter to start calculating")

first = int(input("What number would you like to be multiplied?"))
second = int(input("What number would you like to multiply it by?"))

print (str(first) + " x " + str(second) + " = " + str((multiply(first, second))))


