
# ------------------------ LIBRERIAS -------------------------
import networkx as nx
import math as mt
import numpy as np
import plotly.graph_objs as go
import networkx.drawing as nxdraw
import tkinter
import numpy as np
import graphics as gp
import properties as pr
import simulation as sm

#-----------------------------ALGO SIMILAR A UCB---------------------------------

def function1(key):

    # Variable que almacena el resultado de la funcion
    result = 0 
    meanSimulations = 0
    squareRoot = 0
    
    # Se calcula el promedio entre las simulaciones hechas y todas las simulaciones posibles (o numero de acciones)
    meanSimulations = (sm.NodeMap[key].BestEv + sm.NodeMap[key].WorstEv)/2
    
    # Se crea una copia del padre paraacceder a sus datos
    Parent = sm.NodeMap[key].Parent
    print("Parent: ", Parent)
    
    # Se verifica que exista el padre (en caso de que sea el primer nodo) y se calcula el la raiz de la division entre el logaritmo de las simulaciones del padre del nodo actual y las simulaciones del nodo actual
    if Parent != None:
        squareRoot = mt.sqrt((mt.log(Parent.CurrentEv)) / (sm.NodeMap[key].CurrentEv)+0.01)
    else:
        squareRoot = 1
    
    # Se calcula el resultado con la suma del promedio y l raiz
    result = meanSimulations + squareRoot
    
    return result


    
    
        
