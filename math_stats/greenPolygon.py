# This takes in points of a polygon, one after another, counterclockwise
### and uses Green's theorem to calculate the area of the polygon
import sys
import time

def setup():
    """This function figures out what polygon is being dealt with
    Input: None
    Output: Number of polygon size, if the polygon is valid 
    """
    
    try:
        polySize = int(raw_input("How many sides does your polygon have? "))
    except ValueError:
        print("Only input numeric values. Bye. ")
        sys.exit()
    
    if polySize > 2:
        print("Thank you! ")
        return polySize
    else:
        print("That was not a valid input. Bye. ")
        sys.exit()

def message(sides):
    """
    This only serves to instruct the user what to do 
    """
    time.sleep(2)
    print("You mentioned that your polygon has " + str(sides) + " sides. ")
    time.sleep(2)
    print("Pick a vertex... ")
    time.sleep(2)
    print("And then input the x-y values separated by a comma... e.g. '2,3' (no spaces) ")
    time.sleep(2)
    print("And do the same for the next vertex, one point after another, in a counterclockwise direction until the last. ")
    
def vertexAssert(vertexValue):
    """Makes sure that the user input numbers for points
    Input: User input for x/y value
    Output: Integer value of input if the input is a numbers
    """
    try:
        value = int(vertexValue)
    except ValueError:
        print("You did not type in your values correctly. Bye. ")
        sys.exit()
    return value
    
def getVertex():
    """
    Takes in the user coordinates for vertext
    """
    vertex = raw_input("Enter your vertex: ")
    
    # Find out where the , is
    commaPos = vertex.find(',')
    
    #The return makes sure the x and y points are in the right position
    return (vertexAssert(vertex[:commaPos]), vertexAssert(vertex[commaPos+1:]))
    
def makeVertexList(sides):
    """
    Takes the user input point and adds it to the list of vertices
    Input: number of sides in the polygon
    """
    
    vertexSet = []
    for i in range(sides):
        vertexSet.append(getVertex())
    return vertexSet
        
def areaCalculation(vertexList):
    """
    This function uses green's theorem to calculate the area of a polygon
    Input: A list of polygon vertices in counterclockwise order
    Output: Area of the polygon
    """
    area = 0
    # Calculates until the last step because of wrap around issue
    for i in range(len(vertexList) - 1):
        area = area + ((vertexList[i][0]*vertexList[i+1][1])-(vertexList[i][1]*vertexList[i+1][0]))
        
    # Completes the addition to area by wrapping around and multiplying by half
    area = (area + ((vertexList[-1][0]*vertexList[0][1])-(vertexList[-1][1]*vertexList[0][0])))*0.5
    
    return area
        
def main():
    sides = setup() # Start with number of polygon sides
    message(sides) # Instructs user
    vertices = makeVertexList(sides) #Gets user to input polygon vertices
    area = areaCalculation(vertices) 
    print(area)

if __name__ == "__main__":
    main()