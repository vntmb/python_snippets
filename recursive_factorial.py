#-------------------------------------------------------------------------------
# Name:        recursive factorial
# Purpose:      Calculate the factorial of a number using recursion
#
# Author:      tembov
#
# Created:     18/10/2014
# Copyright:   (c) tembov 2014
#-------------------------------------------------------------------------------
import sys
def recursive_factorial(number):
        if number == 1 or number == 0:
            return 1
        elif number < 0:
            return ("Factorials are not defined for numbers less than 0. Try again.")
        else:
            return number * recursive_factorial(number - 1)

recursion = recursive_factorial(-1)
print recursion
