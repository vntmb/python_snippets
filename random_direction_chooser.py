#-------------------------------------------------------------------------------
# Name:        Random direction chooser
# Purpose:      Like a magic 8 ball, it tells you where to go in times when you
#                do not trust your own intuition
#
# Author:      tembov
#-------------------------------------------------------------------------------
import random
import time
import sys
def main():
    direction = ["North", "East", "South", "West"]
    choose = (str(raw_input("Do you want to choose a direction?"))).lower()
    while choose != "yes" and choose != "no":
        print ("I do not understand that. Please try again")
        choose = (str(raw_input("Do you want to choose a direction?"))).lower()
    else:
        if choose == "yes":
            go = random.choice(direction)
            print ("Go to the " + go)
        else:
            print "Sorry to see you go"
            time.sleep(2)
            sys.exit()

if __name__ == '__main__':
    main()
