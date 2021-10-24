'''
**Original map**
* 0: free
* 1: wall or obstacle

**Our states**
* 2: visited point
* 3: start
* 4: goal

**A nivel grafo (nosotros):**
* -2: parentId start node
* -1: parentId goal node when not solved yet

'''

import time
from functions import *

# First we choose a map (functions file)
MAP_PATH = selectMap()

# List nodes: contains the graph nodes
nodes = []

# 2D list containing the characters of the map (our drawing)
charMap = [] 

# Map creation from csv file
with open(MAP_PATH) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()
        
# Let's ask for the start an goal points
START_X,START_Y,END_X,END_Y = inputStartEnd(charMap) # in functions folder

# Let's make sure that those coordinates are valid (free space)
checkPoints(charMap,START_X,START_Y,END_X,END_Y)     # in functions folder
    
# Add the references to the start and goal points once they are valid
charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

# Now we can create the first node: parentId = -2 since it's start node
init = Node(START_X, START_Y, 0, -2) # Node class object defined in functions.py

# Add the first node (start node) to the list nodes
nodes.append(init)


# Function that shows the map on terminal
def dumpMap():
    for line in charMap:
        print(line)

    
initialCheck()      # First we show some info 
dumpMap()           # Then we show the initial map
####################################     LET THE ALGORITHM BEGIN     ####################################  
start = time.time() # Start measuring the time
done = False        # classic condition for while loop
goalParentId = -1   # parentId of provisional goal point when not solved

# Priority is: up, right, down, left
while not done:
        print("Number of nodes: "+str(len(nodes))) # Print number of visited nodes
        nodes[-1].dump()                           # Print info of the last appended node
        
        # UP
        tmpX = nodes[-1].x - 1
        tmpY = nodes[-1].y
        if( charMap[tmpX][tmpY] == '4' ): # If habemus goal
            print("UP & GOAL!")
            goalParentId = nodes[-1].myId # Change goalParentId. It was -1 but now we want it to be the id of the node
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):# If we found a free non-visited node
            print("up:    mark visited")
            # At the end of the while loop we will understand why we use len(set(nodes) instead if len(nodes)
            newNode = Node(tmpX, tmpY, len(set(nodes)), nodes[-1].myId) # Let's save the new node we found and mark it as visited     
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            dumpMap() # See map
            continue
        # Same logic for right, down and left
                    
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
            newNode = Node(tmpX, tmpY, len(set(nodes)), nodes[-1].myId)
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
            newNode = Node(tmpX, tmpY, len(set(nodes)), nodes[-1].myId) # tempX e Y son valores temporales con el incremento sumado
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
            newNode = Node(tmpX, tmpY, len(set(nodes)), nodes[-1].myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            dumpMap() # See map
            continue
            
        # When the Cell has exhausted its posibilities and can't go to any direction because wall or visited
        # We search for the parent node of our last node.
        for node in nodes: # We check every node in nodes
            if nodes[-1].parentId == node.myId: # If we find a node with an id that tells me "Hey! I am the parent of the current node!"
                print("Going backwards to...")
                nodes.append(node)   # Then we add the that node to the end of the list
        # This will cause not all the nodes in the list nodes will be unique. 
        # That's why when we use len(set(nodes)) instead of len(nodes). That way the ids are consecutive.
        
        
end = time.time()# Finish measuring the time. We have already found the goal



print("\n\n%%%%%%%%%%%%%%%%%%  FOUND PATH  %%%%%%%%%%%%%%%%%%%%%%%")
print("DFS path found, it is not the shortest path")
print("  * Time of execution :", (end-start)*1000, "ms");
print("  * Number of unique nodes in list nodes = " ,len(set(nodes)) ,"\n") # By using set, we just select the unique nodes.
ok = False
while not ok:
    for node in nodes:
        if( node.myId == goalParentId ):
            node.dump()
            goalParentId = node.parentId
            if( goalParentId == -2):
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                ok = True