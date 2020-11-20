import random as r
import heuristics as h
import simulation as sm

def sort(candidates):
    #Largo de la lista de candidatos
    n = len(candidates) 
    #Ordenamiento descendiente de la lista (por su evaluacion)
    for i in range(n,0,-1):  
        for j in range(n, n - i,-1):  
            if (candidates[j].CurrentEv < candidates[j - 1].CurrentEv):  
                candidates[j], candidates[j-1] = candidates[j-1], candidates[j] 
    position(candidates)
    return candidates

def writeFile(selectedNode):
    #Total de nodos de todo el arbol
    length = len(sm.StateMap)
    '''#-----------ANTIGUA SELECCION DE NODOS CANDIDATOS (NODOS HOJA)----------
    for i in range(length):
        #Si el nodo no tiene hijos
        if sm.StateMap[i].NumChild == 0:
            #Se agrega a la lista de nodos candidatos
            candidates.append(sm.StateMap[i])
    #Se retorna la lista de nodos candidatos ordenados de mayor a menor (por su evaluacion)
    return sort(candidates) '''
    #----------------NUEVA SELECCIÓN DE NODOS CANDIDATOS------
    id = str(selectedNode)
    archivo = open('data.txt','w')
    archivo.write("ID nodo seleccionado: ")
    archivo.write(id)
    archivo.write('\n')
    #se escribe en un archivo sus atributos más importantes
    archivo.write("ID nodo actual")
    archivo.write('\t')
    archivo.write("evaluacion promedio")
    archivo.write('\t')
    archivo.write("Desviacion estandar")
    archivo.write('\t')
    archivo.write("Primera evaluacion")
    archivo.write('\t')
    archivo.write("Evauacion actual")
    archivo.write('\t')
    archivo.write("Mejor evaluacion")
    archivo.write('\t')
    archivo.write("Numero de hijos")
    archivo.write('\n')
    for i in range (0,length):
        #se recorren todos los nodos 
        currentNode = sm.StateMap[i]
        archivo.write(str(currentNode.id))
        archivo.write('\t')
        archivo.write(str(currentNode.MeanEv))
        archivo.write('\t')
        archivo.write(str(currentNode.StdDev))
        archivo.write('\t')
        archivo.write(str(currentNode.FirstEv))
        archivo.write('\t')
        archivo.write(str(currentNode.CurrentEv))
        archivo.write('\t')
        archivo.write(str(currentNode.BestEv))
        archivo.write('\t')
        archivo.write(str(currentNode.NumChild))
        archivo.write('\n')
        archivo.write('------------------------------------------------- \n')
        #agregar cantidad total de nodos
    archivo.close()

def getCandidateNodes():
    #esta funcion retorna los nodos ordenados por la evaluacion de la heuristica
    #Total de nodos de todo el arbol
    length = len(sm.StateMap)
    #Lista de nodos candidatos
    candidates = []
    '''#-----------ANTIGUA SELECCION DE NODOS CANDIDATOS (NODOS HOJA)----------
    for i in range(length):
        #Si el nodo no tiene hijos
        if sm.StateMap[i].NumChild == 0:
            #Se agrega a la lista de nodos candidatos
            candidates.append(sm.StateMap[i])
    #Se retorna la lista de nodos candidatos ordenados de mayor a menor (por su evaluacion)
    return sort(candidates) '''
    #----------------NUEVA SELECCIÓN DE NODOS CANDIDATOS------
    for i in range (0,length):
        #se recorren todos los nodos y se agregan a la lista de candidatos
        candidates.append(sm.StateMap[i])
    return sort(candidates) 


def values(random):

    if random :

        #Un número random entre 1 y 2 define que variable se va a modificar. (El rango puede ampliarse si hay mas variables)
        variable = r.randint(1,2)
        #Constante que limita el rango en el que varian los valores (se puede cambiar)
        C = 100 
        value= r.randint(C - 0.1*C, C + 0.1*C)
        return variable, value
    else:
        value= r.randint(C - 0.1*C, C + 0.1*C)
        variable = 0
        return variable, value

def position(candidates):
    #Largo de la lista de candidatos
    length = len(candidates)
    
    for i in range(length):
        #Se recorre la lista para asignar la ultima posición registrada del nodo en los nodos candidatos
        sm.StateMap[candidates[i].id].lastPosition = i

def ranking(selectedNode):
    #esta funcion determina la calidad de la heuristica
    candidates = getCandidateNodes()
    #Se busca la última posicion registrada del nodo seleccionado
    position= sm.StateMap[selectedNode.id].lastPosition
    #Largo de la lista de candidatos
    length = len(candidates)
    #Se calcula el ranking
    ranking = position / length
    return ranking




