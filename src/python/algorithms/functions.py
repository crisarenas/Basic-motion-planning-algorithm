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


# Useful info & Show map with the start and goal points placed
def initialCheck():
    print ("SELECTED CONFIGURATION:\n"+
                        "~~~~~~~~~~~~~~~~~~~~~~~\n"+
                        "Remember!\n"+
                         " x = down is +\n"+
                         " y = right is +\n"+
                         " id = unique node id\n"+
                         " parentId = id of the node that found the current node\n")
    dumpMap()


def inputStartEnd(cmap):
    y_len = len(cmap[0])-1
    x_len = len(cmap)-1
    print ("THIS IS THE MATRIX YOU HAVE SELECTED.\n"+
           "To locate the start and goal point REMEMBER that starting from the left upper 0,"+
           "positive x goes down and positive y goes right.")
    for line in cmap:
        print(line)
    #START X
    START_X = input("Intro START_X coordinate:")  
    while (int(START_X) not in list(range(1,x_len))):
        print(f"   Posible options: {list(range(1,x_len))} ")
        START_X = input()
    #START Y
    START_Y = input("Intro START_Y  coordinate:")
    while (int(START_Y) not in list(range(1,y_len))):
        print(f"   Posible options: {list(range(1,y_len))} ")
        START_Y = input()    
    #END X
    END_X = input("Intro END_X coordinate:")
    while (int(END_X) not in list(range(1,x_len))):
        print(f"   Posible options: {list(range(1,x_len))} ")
        END_X = input()    
    #END Y
    END_Y = input("Intro  END_Y coordinate:")
    while (int(END_Y) not in list(range(1,y_len))):
        print(f"   Posible options: {list(range(1,y_len))} ")
        END_Y = input()  
    return int(START_X),int(START_Y),int(END_X),int(END_Y) 

