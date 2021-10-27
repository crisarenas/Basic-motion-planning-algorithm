# Define node class (A nivel grafo/nodo)
class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x                # x and y are unique for each node
        self.y = y
        self.myId = myId          # unique identifier for each node
        self.parentId = parentId  # Id that found the current node
    def dump(self): # Dump = show node info on terminal
        print("Node info: x = "+str(self.x)+\
                         " | y = " +str(self.y)+\
                         " | id = "+str(self.myId)+\
                         " | parentId = "+str(self.parentId) + "\n______________________________________________")



# Useful info to show at the beggining
def initialCheck(cmap):
    print ("\n\nSELECTED CONFIGURATION:\n"+
                        "~~~~~~~~~~~~~~~~~~~~~~~\n"+
                        "Remember!\n"+
                         " x = down is +\n"+
                         " y = right is +\n"+
                         " id = unique node id\n"+
                         " parentId = id of the node that found the current node\n")
    printColored(cmap)




# Function that shows the charMap on terminal
def dumpMap(charMap):
    for line in charMap:
        print(line)




# Function that makes sure that the coordinates are valid (free space)
def checkPoints(cmap,sx,sy,ex,ey):
    while cmap[sx][sy] != '0' or cmap[ex][ey]!= '0' or [sx,sy] == [ex,ey]: #CHeck that the space is free and start!=goal
        print("\nPlease, make sure that you don't hit an obstacle OR start an finish at the same location.\nTry again.\n")
        sx,sy,ex,ey = inputStartEnd(cmap)





# Function that asks for start and end points
def inputStartEnd(cmap):
    y_len = len(cmap[0])-1 # lenght of a line
    x_len = len(cmap)-1    # lenght of a column
    print ("---------------------------------------------------------------------------------\n"+
           "THIS IS THE MATRIX YOU HAVE SELECTED.\n"+
           "To locate the start and goal point REMEMBER that starting from the left upper 0,"+
           "positive x goes down and positive y goes right.")
    # Show the selected matrix
    printColored(cmap)

    #START X
    START_X = input("Intro START_X coordinate:")  
    while (START_X.isnumeric() == False) or (float(START_X) not in list(range(1,x_len))): # Check that START_X is in the correct range and if it is a letter (same for the other coordinates) 
        START_X = input(f"   Posible options: {list(range(1,x_len))} ") # If not in range then help me. Show me the list of posible options
    START_X = int(START_X) # If everything ok we convert it to int

    #START Y
    START_Y = input("Intro START_Y  coordinate:")
    while (START_Y.isnumeric() == False) or (float(START_Y) not in list(range(1,y_len))):
        START_Y = input(f"   Posible options: {list(range(1,y_len))} ")
    START_Y = int(START_Y) # If everything ok we convert it to int      

    #END X
    END_X = input("Intro END_X coordinate:")
    while (END_X.isnumeric() == False) or (float(END_X) not in list(range(1,x_len))):
        END_X = input(f"   Posible options: {list(range(1,x_len))} ")
    END_X = int(END_X) # If everything ok we convert it to int      

    #END Y
    END_Y = input("Intro  END_Y coordinate:")
    while (END_Y.isnumeric() == False) or (float(END_Y) not in list(range(1,y_len))):
        END_Y = input(f"   Posible options: {list(range(1,y_len))} ")
    END_Y = int(END_Y) # If everything ok we convert it to int
    print("--------------------------------------------------------------")
    return START_X,  START_Y,  END_X,  END_Y




# Function to the select map to test
# Check that it is a number in the range
def selectMap():
    mapNum = input("What map would you like to test? (Number from 1 to 12):")  
    while (mapNum.isnumeric() == False) or (float(mapNum) not in list(range(1,13))):
        mapNum = input(f"   Posible options: {list(range(1,13))} ")
    return f"../../../../map{int(mapNum)}/map{int(mapNum)}.csv"



# Functions that set the colors for the map
def colorMap(i):
    return "\033[3{}m{}\033[0m".format(i+1, i)

import numpy as np
# Function that prints the colored Map
def printColored(charMap):
    intMap = (np.array(charMap)).astype(np.int)    # Converts charMap to numpy int matrix
    map_modified = np.vectorize(colorMap)(intMap)  # Vectorize de color Map
    print("\n".join([" ".join(["{}"]*len(charMap[0]))]*len(charMap)).format(*[x for y in map_modified.tolist() for x in y]))
