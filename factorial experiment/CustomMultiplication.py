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




