
# ------------------------ LIBRERIAS -------------------------
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import math as mt
import numpy as np
import plotly.graph_objs as go
import networkx.drawing as nxdraw
import tkinter
import numpy as np
from matplotlib.widgets import Button
from networkx.drawing.nx_agraph import graphviz_layout
import subprocess
import graphics as gp
import properties as pr
import simulation as sm
import function1 as f1
import function2 as f2

#-------------------------------------------------------------------------------------------------------------------------------
def nodeEvluation(key):

    evaluation = sm.NodeMap[key].nodeEv
    return evauation
    
def updateNode(evOption_):


    # Se define el largo como el numero de nodos del grafo
    length = sm.G.number_of_nodes()
    # Se crea una lista para almacenar todos los nodos del grafo y posteriormente ordenarlos 
    nodeList= []
   
    for i in range(0, length): 
        nodeList[i] = sm.NodeMap[i]
        
    # Se ordena la lista de nodos segun su evaluacion (funcion)
    nodeList.sort(key = nodeEvaluation(, reverse = True)
    
    return nodeList   