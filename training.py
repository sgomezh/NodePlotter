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

def candidateNodes():
    #Total de nodos de todo el arbol
    length = len(sm.StateMap)
    #Lista de nodos candidatos
    candidates = []
    
    for i in range(length):
        #Si el nodo no tiene hijos
        if sm.StateMap[i].NumChild == 0:
            #Se agrega a la lista de nodos candidatos
            candidates.append(sm.StateMap[i])
    #Se retorna la lista de nodos candidatos ordenados de mayor a menor (por su evaluacion)
    return sort(candidates) 

def training(random):

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

def ranking(selectecNode):
    candidates = candidateNodes()
    #Se busca la última posicion registrada del nodo seleccionado
    position= sm.StateMap[selectecNode.id].lastPosition
    #Largo de la lista de candidatos
    length = len(candidates)
    #Se calcula el ranking
    ranking = position / length
    return ranking




