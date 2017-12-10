# This module calculates area using heron's formula
from math import sqrt
def askSide(n):
    """Asks for the length of a triangle side"""
    side = float(raw_input("Side " + str(n) + " : "))
    return side
    
def findS(myList):
    """Finds the value of s"""
    s = 0
    for side in myList:
        s = s + 0.5*side
    return s
    
def t_area(lengthList, s):
    """Calculates the triangle area
    Input: List with sides lengths and the value of s
    Output: The area of the triangle"""
    area = s
    for length in lengthList:
        area = area*(s-length)
    return sqrt(area)
    
def main():
    sideList = [] # Initializes list to contain side lengths
    for i in range(3): # Since this is a triangle
        sideList.append(askSide(i+1)) # +1 because python count from 0
        
    area = t_area(sideList, findS(sideList)) # Compute area
    print("The triangle has an area of " + str(area))

if __name__ == "__main__":
    main()