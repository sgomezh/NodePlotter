
# ------------------------ LIBRERIAS -------------------------
import networkx as nx
import math as mt
import numpy as np
import plotly.graph_objs as go
import networkx.drawing as nxdraw
import numpy as np
import graphics as gp
import properties as pr
import simulation as sm

#-------------------------------------------------------------------------------------------------------------------------------

def function2(key):

    # Variable que almacena el resultado de la funcion
    result = 0
    
    # Se calcula el la division entre el numero total de acciones y las simulaciones realizadas, ya que la cantidad de accioens totales es constante y la cantidad de 
    # Simulaciones no, por lo que entre m�s simulaciones, menos prbabilidad de ser elegido como los mejores, ya que ha sido simulado muchas veces
    division = sm.NodeMap[key].NumActions / (sm.NodeMap[key].NumSimulations + 1)
    
    # Se calcula el promedio entre la mejor y peor evaluacion
    meanEv = (sm.NodeMap[key].BestEv + sm.NodeMap[key].WorstEv) / 2
    
    # Se calcula el resultado con la suma del promedio y la division
    result = (division + meanEv) / 100
    print ("result= ", result)
    
    return result