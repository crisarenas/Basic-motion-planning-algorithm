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
from functions import * # functions.py with functions and the class Node

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


# First we show some info and the initial configuration    
initialCheck(charMap)  # First we show some info and the initial configuration


####################################     LET THE ALGORITHM BEGIN     ####################################  
#This algorithm is similiar to bug2, but not the same. What it does is choosing always the closer node to the cell.
start = time.time() # Start measuring the time
done = False        # classic condition for while loop
goalParentId = -1   # parentId of provisional goal point when not solved

# Priority is: up, right, down, left
while not done:
        print("Number of nodes: "+str(len(nodes))) # Print number of visited nodes
        nodes[-1].dump()                           # Print info of the last appended node
        
        
        # We save in these variables the 4 points closer to the last node. We don't consider diagonal directions.
            # UP
        tmpX_U = nodes[-1].x - 1
        tmpY_U = nodes[-1].y    
        UP = (tmpX_U,tmpY_U)
            # RIGHT 
        tmpX_R = nodes[-1].x
        tmpY_R = nodes[-1].y + 1
        RIGHT = (tmpX_R,tmpY_R)
            # DOWN
        tmpX_D = nodes[-1].x + 1
        tmpY_D = nodes[-1].y
        DOWN = (tmpX_D,tmpY_D)
            # LEFT
        tmpX_L = nodes[-1].x
        tmpY_L = nodes[-1].y - 1
        LEFT = (tmpX_L,tmpY_L)
         
        #Calculates the euclidean distance between the goal and the four new directions. Save in a list.
        distances = [pow(  pow(END_X-sx,2)+pow(END_Y-sy,2),  0.5) for sx,sy in [UP,RIGHT,DOWN,LEFT]] # List comprehension
        
        # Python dictionary containing the directions and the distance from that cell to the goal point
        distances_dict = {"UP": distances[0],"RIGHT": distances[1],"DOWN": distances[2],"LEFT": distances[3]}
        
        # Check that the moves are valid (non-visited or obstacle)
        # If it is not valid we delete that option from the dictionary.
        if  charMap[tmpX_U][tmpY_U] != '0' and charMap[tmpX_U][tmpY_U] != '4': # No free space up or goal
            del distances_dict['UP']
        if  charMap[tmpX_R][tmpY_R] != '0' and charMap[tmpX_R][tmpY_R] != '4': # No free space right or goal
            del distances_dict['RIGHT']
        if  charMap[tmpX_D][tmpY_D] != '0' and charMap[tmpX_D][tmpY_D] != '4': # No free space down or goal
            del distances_dict['DOWN']
        if  charMap[tmpX_L][tmpY_L] != '0' and charMap[tmpX_L][tmpY_L] != '4': # No free space left or goal
                del distances_dict['LEFT']    
        # Our dictionary now contains valid directions
        
        #If the dict is not empty by now 
        if len(distances_dict) > 0:
            # This calculates the direction with the minimum AVAILABLE distance to the goal.
            closer_direction = min(distances_dict, key=distances_dict.get)
        else: # The Cell has exhausted its posibilities and can't go to any direction because wall or visited
            # We search for the parent node of our last node.
            for node in nodes: 
                if nodes[-1].parentId == node.myId: # If we find a node with an id that tells me "Hey! I am the parent of the current node!"
                    print("Going backwards to...")
                    nodes.append(node)   # Then we add the that node to the end of the list
            # This will cause not all the nodes in the list nodes will be unique. 
            # That's why when we use len(set(nodes)) instead of len(nodes). That way the ids are consecutive.
        
                
        
        # Keep the tmpX and tmpY position of the cell that is closer to the goal point
        if closer_direction == 'UP':     #Going UP is closer to the goal
            tmpX = nodes[-1].x - 1
            tmpY = nodes[-1].y 
        elif closer_direction == 'RIGHT':#Going RIGHT is closer to the goal
            tmpX = nodes[-1].x
            tmpY = nodes[-1].y + 1
        elif closer_direction == 'DOWN': #Going DOWN is closer to the goal
            tmpX = nodes[-1].x + 1
            tmpY = nodes[-1].y
        else:                            #Going LEFT is closer to the goal
            tmpX = nodes[-1].x
            tmpY = nodes[-1].y - 1

            
            
        # Goal or non visited node
        if( charMap[tmpX][tmpY] == '4' ): # If habemus goal
            print(f"{closer_direction} & GOAL!")
            goalParentId = nodes[-1].myId # Change goalParentId. It was -1 but now we want it to be the id of the node
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):# If we found a free non-visited node
            print(f"{closer_direction}:    mark visited")
            newNode = Node(tmpX, tmpY, len(set(nodes)), nodes[-1].myId) # Let's save the new node we found and mark it as visited     
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
            #dumpMap(charMap) # See map
            printColored(charMap)
            continue

     

  
end = time.time()# Finish measuring the time. We have already found the goal



print("\n\n%%%%%%%%%%%%%%%%%%  FOUND PATH  %%%%%%%%%%%%%%%%%%%%%%%")
print("DFS path found, it is not the shortest path")
print("  * Time of execution :", (end-start)*1000, "ms");
print("  * Number of unique nodes in list nodes = " ,len(set(nodes)) ,"\n") # By using set, we just select the unique nodes.
print("  * Number of nodes visited (including backtracking) = " ,len(nodes) ,"\n") 
printColored(charMap)
ok = False
while not ok:
    for node in nodes:
        if( node.myId == goalParentId ):
            node.dump()
            goalParentId = node.parentId
            if( goalParentId == -2):
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                ok = True
