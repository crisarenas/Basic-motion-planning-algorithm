import time
#from functions import *
start = time.time()

# Initial values are hard coded
MAP_PATH = "../../../../map1/map1.csv"
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2


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

# List nodes: contains the graph nodes
nodes = []

# Create first node: parentId = -2 since it's start node
init = Node(START_X, START_Y, 0, -2) # Node class object

# Add the first node (start node) to the list nodes
nodes.append(init)


# 2D list containing the characters of the map (our drawing)
charMap = [] 


# Function that shows the map on terminal
def dumpMap():
    for line in charMap:
        print(line)



# Map creation from csv file
with open(MAP_PATH) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()



# Add the references to the start and goal point
charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

# Info + Show map with the start and goal points placed
def initialCheck():
    print ("INITIAL CONFIGURATION:\n"+
                        "~~~~~~~~~~~~~~~~~~~~~\n"+
                         "x = down is +\n"+
                         "y = right is +\n"+
                         "id = unique node id\n"+
                         "parentId = id of the node that found the current node\n")
    dumpMap()

initialCheck()

####################################     LET THE ALGORITHM BEGIN     ####################################  
done = False        # classic condition for while loop
goalParentId = -1   # parentId of provisional goal point when not solved

# Priority is: up, right, down, left
while not done:
        # Print number of visited nodes + node info
        print("Number of nodes: "+str(len(nodes))) 
        nodes[-1].dump()
        
        # UP
        tmpX = nodes[-1].x - 1
        tmpY = nodes[-1].y
        if( charMap[tmpX][tmpY] == '4' ): # Habemus goal
            print("UP & GOAL!")
            goalParentId = nodes[-1].myId # change goalParentId=1 for node real unique id
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("up:    mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), nodes[-1].myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            dumpMap() # See map
            continue
            print(str(nodes[0].x+nodes[0].y)+ "  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        
        #RIGHT 
        tmpX = nodes[-1].x
        tmpY = nodes[-1].y + 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("RIGHT & GOAL!")
            goalParentId = nodes[-1].myId 
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("right: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), nodes[-1].myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            dumpMap() # See map
            continue

        # DOWN
        tmpX = nodes[-1].x + 1
        tmpY = nodes[-1].y
        if( charMap[tmpX][tmpY] == '4' ):
            print("DOWN & GOAL!")
            goalParentId = nodes[-1].myId
            done = True
            break 
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("down:  mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), nodes[-1].myId) # tempX e Y son valores temporales con el incremento sumado
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            dumpMap() # See mapv
            continue

        # LEFT
        tmpX = nodes[-1].x
        tmpY = nodes[-1].y - 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("LEFT & GOAL!")
            goalParentId = nodes[-1].myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("left:  mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), nodes[-1].myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            dumpMap() # See map
            continue

        
print("\n\n___________________________\n\n")
ok = False
while not ok:
    for node in nodes:
        if( node.myId == goalParentId ):
            node.dump()
            goalParentId = node.parentId
            if( goalParentId == -2):
                print("%%%%%%%%%%%%%%%%%2")
                ok = True

end = time.time()
print("Time of execution :", (end-start)*1000, "ms")