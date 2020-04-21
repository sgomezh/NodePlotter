

# ------------------------ LIBRERÍAS -------------------------

import math as mt
import numpy as np
import simulation as sm
import state

#---------------------------------MEJOR EVALUACION DEL GRAFO---------------------------------------
    
def BestMapEv():

    bestEv = 0
    length = len(sm.StateMap)
    # Recorre todos los nodos que existen, los busca en el mapa para obtener la informacion y luego obtiene la mejor evaluacion de todo los nodos del grafo
    if length == 1:
        bestEv = sm.StateMap[0].CurrentEv
    else:
        for i in range(1, length): 
        
            if bestEv < sm.StateMap[i].BestEv:
                bestEv = sm.StateMap[i].BestEv
                
    return bestEv
    
#----------------------------------MEJOR EVALUACION DEL GRAFO---------------------------------------
    
def WorstMapEv():
    
    length = len(sm.StateMap)
    worstEv = mt.inf
    
    # Recorre todos los nodos que existen, los busca en el mapa para obtener la informacion y luego obtiene la peor evaluacion de todo los nodos del grafo
    for i in range(0, length): 
    
         if worstEv > sm.StateMap[i].WorstEv:
             worstEv = sm.StateMap[i].WorstEv
             
    return worstEv

 
#----------------------------------COLOR DEL NODO-----------------------------------------
    
def StateColor(key):

    # Se crea la lista que almacera todos los colores que deban tomar los nodos
    color_array = []

    # Se definen los colores mazimos y minimos para que esten dentro de un rango
    ColorMin = [255,0,0]
    ColorMed = [255,255,0]
    ColorMax = [0,255,0]
    R = 0
    G = 0
    B = 0
    
    #Se recibe la mejor evaluacion de todo el grafo para poder comparar con la del nodo actual

    #print( "best map ev= ", bestMapEv)
    #print("worst map ev= ", worstMapEv)
    #print("Current= ", sm.StateMap[key].CurrentEv)

    #state.State.worstEv= 0.90
    # En caso de que sea la mejor evaluacion, se le asigna el color amarillo 
    if state.State.bestEv == sm.StateMap[key].FirstEv:
        color_array = [0,200,0]
    
   
    # Sino, se calcula el color de forma gradual segun su porcentaje en funcion de su mejor y peor evaluacion    
    else:
        Percentage = ((sm.StateMap[key].FirstEv - state.State.worstEv) / (state.State.bestEv - state.State.worstEv))
        #print("percentage= ", Percentage)
        if Percentage < 0.5:
            R= 255; G=int((2*Percentage)*255)
        else:
            R = 255-int((2*(Percentage-0.5))*255) ; G=255
        
        #R = int(ColorMin[0] + Percentage*(ColorMax[0] - ColorMin[0] ))
        #G = int(ColorMin + Percentage*(ColorMax - ColorMin ))
        #B = int(ColorMin[2] + Percentage*(ColorMax[2] - ColorMin[2] ))
        
        #print("R= ", R)
        #print("G= ", G)
        #print("B= ", B)
        
        color_array = [R,G,B]
     
    # Se retorna un arreglo que contiene todos los colores de los nodos      
    return color_array
    

    
#-------------------------INFORMACION GENERAL DEL GRAFO Y EL NODO----------------------------------
     
def PrintInformation(ParentKey):

    # Se imprime informacion general de todo el grafo y del nodo actual (el que se esta clickeando)

    MeanEv = str(round(sm.StateMap[ParentKey].MeanEv,4))
    numSimulations = str(round(sm.StateMap[ParentKey].NumSimulations, 4))
    numActions = str(round(sm.StateMap[ParentKey].NumActions, 4))
    firstEv = str(round(sm.StateMap[ParentKey].FirstEv, 4))
    bestEvGraf = str(round(BestEv(), 4))
    stateNumber = str(ParentKey)
    
    information = str("INFORMACION\n"+ 
    "Mejor evaluacion del grafo: "+
    bestEvGraf+ "\n"+
    "Primera evaluacion del nodo "+ stateNumber+ ":"+
    firstEv+ "\n"+
    "Evaluacion promedio del nodo "+ stateNumber+ ":"+ 
    MeanEv+  "\n"+
    "Numero de simulaciones: "+
    numSimulations+  "\n"+
    "Numero de acciones: "+
    numActions)
    
    return information
    

    
    

                