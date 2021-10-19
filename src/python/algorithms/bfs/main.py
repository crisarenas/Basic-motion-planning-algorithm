import time
start = time.time()

#! /usr/bin/env python
'''
Mapa original:
* 0:libre
* 1: ocupado por muro u obstaculo

Nosotros:
* 2: visitados
* 3: start
* 4: goal

A nivel grafo (nosotros):
* -2: parentId del nodo start
* -1: parentId del nodo goal  PROVISIONAL cuando aun no se ha resuelto


*****repasar lo del constructor y tal.
'''


#Initial values are hard coded (A nivel mapa): se les restan las paredes cuando se dan los puntos
MAP_PATH = "../../../../map1/map1.csv" #aqui habria que ir cambiando los mapas
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2


#Define node class (A nivel grafo/nodo)
'''
4 Parámetros de la clase Node:
Cada nodo puede contener un x e y con un identificador (unico, no hay dos nodos con el mismo id). 
Esos identificadores (myId) simplemente los haremos incrementales con un contador.
parentId: apunta al nodo del cual parte, el padre. 
'''
class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x 
        self.y = y
        self.myId = myId
        self.parentId = parentId
    def dump(self): # Dump es sacar por pantalla
        print("INFO: x = "+str(self.x)+\
                         " | y = "+str(self.y)+\
                         " | id = "+str(self.myId)+\
                         " | parentId = "+str(self.parentId) + "\n______________________________________________")


# Lista nodes: contiene los nodos del grafo
nodes = []


#Creamos el primer nodo, su parentId es -2 porque es el nodo inicio
init = Node(START_X, START_Y, 0, -2)

# init.dump() #para comprobar que el primer nodo está bien si queremos hacerlo


#Añadimos el primer nodo a nodos
nodes.append(init)


##Empezamos con mapa: creamos estructura de datos para mapa
charMap = [] #Lista de dos dimensiones de caracteres en python


# Esta funcion auxiliar vuelca el mapa por pantalla (estructura de datos). En un primer momento estará vacio.
## creamos función para volcar estructura de datos para mapa
def dumpMap():
    for line in charMap:
        print(line)




#Creamos mapa legible (to parse/parsing es decir, pasar de estructura de datos en un fichero a 
# una variable que podamos usar)
with open(MAP_PATH) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()



## Añadimos al mapa los puntos start (un 3) y end (un 4) en sus posiciones correspondientes.
charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

## Mostramos mapa con los puntos de start y goal colocados.
dumpMap()


############Empieza el algoritmo
done = False # clásica condición de parada del bucle `while`
goalParentId = -1 # -1: parentId del nodo goal PROVISIONAL cuando aun no se ha resuelto

###### Tambien se puede hacer en diagonal, seria un extra.
###### Se puede optimizar el codigo.


while not done:
    print("Number of nodes: "+str(len(nodes))) #mucha linea para identificar mejor el code
    for node in nodes:
        node.dump()
        
        # up
        '''Mirar hacia arriba en el mapa = x-1 porque definimos que x+ hacia abajo.'''
        tmpX = node.x - 1
        tmpY = node.y
        if( charMap[tmpX][tmpY] == '4' ): # 4 char para buscar la meta
            print("UP & GOAL!")
            goalParentId = node.myId #aqui sustituye por real
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("up:    mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # down
        tmpX = node.x + 1
        tmpY = node.y
        if( charMap[tmpX][tmpY] == '4' ):
            print("DOWN & GOAL!")
            goalParentId = node.myId#aqui sustituye por real
            done = True
            break #rompo el for si lo encuentro
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("down:  mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId) # tempX e Y son valores temporales con el incremento sumado
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # right
        tmpX = node.x
        tmpY = node.y + 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("RIGHT & GOAL!")
            goalParentId = node.myId #aqui sustituye por real
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("right: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # left
        tmpX = node.x
        tmpY = node.y - 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("LEFT & GOAL!")
            goalParentId = node.myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("left:  mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        dumpMap() #para ver como vamos en cada iteracion

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