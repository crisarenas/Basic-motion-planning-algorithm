#! /usr/bin/env python
'''
A nivel del mapa original:
* 0:libre
* 1: ocupado muro u obstaculo

A mayores:
- 2: visitados
- 3: start
- 4: goal

A nivel grafo (nosotros):
- -2: parentId del nodo origen
* -1: parentId del nodo goal



Initial values are hard coded (A nivel mapa)

*****repasar lo del constructor y tal.
'''

#initial values are hard-coded/usr/local/s
FILE_NAME = "../../../../map1/map1.csv" #aqui habria que ir cambiando los mapas
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2


#Define node class
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
    def dump(self): # Dump es forzar por pantalla
        print("---------- x "+str(self.x)+\
                         " | y "+str(self.y)+\
                         " | id "+str(self.myId)+\
                         " | parentId "+str(self.parentId))


# nodes contendrá los nodos del grafo
nodes = []


#Creamos el primer nodo
init = Node(START_X, START_Y, 0, -2)

# init.dump() #para comprobar que el primer nodo está bien si queremos


#Añadimos el primer nodo a nodos
nodes.append(init)


##Empezamos con mapa
charMap = [] #la forma mas sencilla de cargar el fichero es una lista de dos dimensiones de caracteres en python


# Esta funcion auxiliar vuelca el mapa por pantalla (estructura de datos). En un primer momento estará vacio.
def dumpMap():
    for line in charMap:
        print(line)


#para llenar la estructura de datos del mapa
#Llenamos estructuras de datos para mapa (to parse/parsing es decir, pasar de estructura de datos en un fichero a 
# una variable que podamos usar)
with open(FILE_NAME) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()



#a nivel mapa, le añadimos al mapa la info de origen y destino
charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

dumpMap()


############Empieza el algoritmo
done = False
goalParentId = -1 #-1: parentId del nodo goal

while not done:
    print("--------------------- number of nodes: "+str(len(nodes))) #mucha linea para identificar mejor el code
    for node in nodes:
        node.dump()
###### Tambien se puede hacer en diagonal, seria un extra.
###### Se puede optimizar el codigo.


        # up
        '''Para mirar hacia arriba en el mapa es hacia arriba un paso en x porque definimos que x es 
        positiva hacia abajo.'''
        tmpX = node.x - 1
        tmpY = node.y
        if( charMap[tmpX][tmpY] == '4' ): # 4 char para buscar la meta
            print("up: GOALLLL!!!")
            goalParentId = node.myId #aqui sustituye por real
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("up: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # down
        tmpX = node.x + 1
        tmpY = node.y
        if( charMap[tmpX][tmpY] == '4' ):
            print("down: GOALLLL!!!")
            goalParentId = node.myId#aqui sustituye por real
            done = True
            break #rompo el for si lo encuentro
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("down: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId) # tempX e Y son valores temporales con el incremento sumado
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # right
        tmpX = node.x
        tmpY = node.y + 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("right: GOALLLL!!!")
            goalParentId = node.myId #aqui sustituye por real
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("right    : mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # left
        tmpX = node.x
        tmpY = node.y - 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("left: GOALLLL!!!")
            goalParentId = node.myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("left: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        dumpMap() #para ver como vamos en cada iteracion

print("%%%%%%%%%%%%%%%%%%%")
ok = False
while not ok:
    for node in nodes:
        if( node.myId == goalParentId ):
            node.dump()
            goalParentId = node.parentId
            if( goalParentId == -2):
                print("%%%%%%%%%%%%%%%%%2")
                ok = True
