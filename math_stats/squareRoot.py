# This function finds the square root of a number to within 0.0001
# This does not use anything imported from math
import sys
def toBRooted():
    """
    This function takes the number to be square rooted from the user
    Input: None
    Output: User defined number and whether it is positive or negative
    """
    try:
        number = float(raw_input("What number do you want the square root of? "))
    except ValueError:
        print("That is not a valid input. Bye. ")
        sys.exit()
    if number < 0:
        return number, "neg"
        
    return number, "pos"

def root(number, epsilon):
    """
    This function finds the square root of a number
    Input: Number whose square root is to be found and tolerance
    Output: Square root correct to 0.0001
    """
    lowerLimit = 0
    upperLimit = number
    root = float(0.5*(lowerLimit+upperLimit)) # root starts off as midway point
    while True: # True is used here because this method always converges
        square = root*root
        if square >= number:
            if square - number < epsilon:
                return round(root, 4) # Rounds it to desired accuracy
            else:
                upperLimit = root 
                root = float(0.5*(lowerLimit+upperLimit)) # Find new midway
        else:
            if number - square < epsilon:
                return round(root, 4)
            else:
                lowerLimit = root
                root = float(0.5*(lowerLimit+upperLimit)) # Find new midway
    
def main():
    epsilon = 0.000001 # This determines convergence condition
    number = toBRooted()
    
    # If the number is positive, find the square root of the positive part
    # Then tack on a '0i' as the imaginary part is 0
    if number[1] == "pos":
        sroot = root(number[0], epsilon)
        print("The answer is: " + str(sroot) + " + 0 i" + "\n... Bye")
        
    # If the number is negative, strip the positive part and find its squareroot
    # Then tack on an 'i' for imaginary with the real part being 0
    else:
        sroot = root(-1*number[0], epsilon)
        print("The answer is: " + "0 + " + str(sroot) + " i" + "\n... Bye")

if __name__ == "__main__":
    main()