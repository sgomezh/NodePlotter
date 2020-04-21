

# ------------------------ LIBRERÍAS -------------------------

import math as mt
import numpy as np
import simulation as sm
import node as nd

#---------------------------------MEJOR EVALUACION DEL GRAFO---------------------------------------
    
def BestMapEv():

    #length = sm.G.number_of_nodes()
    bestEv = 0
    length = len(sm.NodeMap)
    # Recorre todos los nodos que existen, los busca en el mapa para obtener la informacion y luego obtiene la mejor evaluacion de todo los nodos del grafo
    if length == 1:
        bestEv = sm.NodeMap[0].CurrentEv
    else:
        for i in range(1, length): 
        
            if bestEv < sm.NodeMap[i].BestEv:
                bestEv = sm.NodeMap[i].BestEv
                
    return bestEv
    
#----------------------------------MEJOR EVALUACION DEL GRAFO---------------------------------------
    
def WorstMapEv():
    
    length = len(sm.NodeMap)
    worstEv = mt.inf
    
    # Recorre todos los nodos que existen, los busca en el mapa para obtener la informacion y luego obtiene la peor evaluacion de todo los nodos del grafo
    for i in range(0, length): 
    
         if worstEv > sm.NodeMap[i].WorstEv:
             worstEv = sm.NodeMap[i].WorstEv
             
    return worstEv
#-----------------------------------TAMAÑO DEL NODO----------------------------------------

def NodeSize(key):
    
    # Se crea la lista que almacenar� todos los respectivos tama�os
    node_size = 10

    if key in sm.NodeMap:
        # Se define el tama�o segun su simulacion
        node_size = int(mt.log(sm.NodeMap[key].NumSimulations + 1))+10  

    keyStr = str(key)
    nodeSizeStr = str(node_size)
    print("El tamaño del nodo "+ keyStr + "es: " + nodeSizeStr)

    return  node_size 
 
 
#----------------------------------COLOR DEL NODO-----------------------------------------
    
def NodeColor(key):

    # Se crea la lista que almacera todos los colores que deban tomar los nodos
    color_array = []

    # Se definen los colores mazimos y minimos para que esten dentro de un rango
    ColorMin = 155
    ColorMax = 255
    R = 0
    G = 0
    B = 0
    
    #Se recibe la mejor evaluacion de todo el grafo para poder comparar con la del nodo actual
    bestMapEv = BestMapEv()
    worstMapEv = WorstMapEv()
    print( "best map ev= ", bestMapEv)
    print("worst map ev= ", worstMapEv)
    print("Current= ", sm.NodeMap[key].CurrentEv)


    # En caso de que sea la mejor evaluacion, se le asigna el color amarillo 
    if sm.NodeMap[key].BestEv == bestMapEv:
        color_array = [255,255,0]
            
    # Sino, se calcula el color de forma gradual segun su porcentaje en funcion de su mejor y peor evaluacion    
    else:
        Percentage = ((sm.NodeMap[key].CurrentEv - worstMapEv) / (bestMapEv - worstMapEv))
        print("percentage= ", Percentage)
        R = int(ColorMin + Percentage*(ColorMax - ColorMin ))
        G = int(ColorMin + Percentage*(ColorMax - ColorMin ))
        B = int(ColorMin + Percentage*(ColorMax - ColorMin ))
        
        print("R= ", R)
        print("G= ", G)
        print("B= ", B)
        
        color_array = [R,G,B]
     
    # Se retorna un arreglo que contiene todos los colores de los nodos      
    return color_array
    

    
#-------------------------INFORMACION GENERAL DEL GRAFO Y EL NODO----------------------------------
     
def PrintInformation(ParentKey):

    # Se imprime informacion general de todo el grafo y del nodo actual (el que se esta clickeando)

    MeanEv = str(round(sm.NodeMap[ParentKey].MeanEv,4))
    numSimulations = str(round(sm.NodeMap[ParentKey].NumSimulations, 4))
    numActions = str(round(sm.NodeMap[ParentKey].NumActions, 4))
    firstEv = str(round(sm.NodeMap[ParentKey].FirstEv, 4))
    bestEvGraf = str(round(BestEv(), 4))
    nodeNumber = str(ParentKey)
    
    information = str("INFORMACION\n"+ 
    "Mejor evaluacion del grafo: "+
    bestEvGraf+ "\n"+
    "Primera evaluacion del nodo "+ nodeNumber+ ":"+
    firstEv+ "\n"+
    "Evaluacion promedio del nodo "+ nodeNumber+ ":"+ 
    MeanEv+  "\n"+
    "Numero de simulaciones: "+
    numSimulations+  "\n"+
    "Numero de acciones: "+
    numActions)
    
    return information
    

    
    

                