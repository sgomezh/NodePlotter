
# ------------------------ LIBRERIAS -------------------------
import networkx as nx
import math as mt
import numpy as np
import plotly.graph_objs as go
import networkx.drawing as nxdraw
import simulation as sm
import properties as pr
import function1 as f1
import function2 as f2
# ------------------------ DEFINICION DE CLASE NODO Y SUS METODOS -------------------------
# Esta clase define la informacion que se guarda en el nodo (cada nodo se guarda en el mapa NodeMap)


class Nodo:
    hashkey_ = 0
    def __init__(self, Parent, hashKey):  # Constructor del nodo
        
        self.hashKey = hashKey # Clave o identificador del nodo. Esta es la que se asocia con NodeMap
        
        # Se declara la variable hashkey global para poder usarla en otros metodos
        
        global hashkey_
        hashkey_ = hashKey
        
        self.FirstEv = 0 #Primera evaluacion del nodo, una vez asignada no se puede cambiar
        self.CurrentEv = 0 # Almacena la evaluacion actual, cambia cada vez que se simula el nodo
        self.MeanEv = 0  # Promedio de todas las evaluaciones obtenidas
        self.SquareMeanEv = 0
        self.StdDev  = 0  # Desviacion estandar de todas las evaluaciones obtenidas
        self.BestEv = 0  # La mayor evaluacion obtenida
        self.WorstEv = 0 # mt.inf #Pero evaluacion del nodo
        self.NumActions = 0  # Numero total de casos posibles producidos por el simulador
        self.ChildList = []  # Esto representa una  lista dinamica, para apregar datos se utiliza el metodo append()
        self.Path = [] #Pila de nodos (desde la raiz) para llegar al nodo actual. Utiliza el metodo extend()
        self.NumSimulations = 0 # Numero de veces que el nodo ha sido simulado
        self.IdLastChild = None
        self.Parent = None
        self.NodeEv = 0
        if Parent != None:
            self.Parent = sm.NodeMap[Parent]
            self.IdLastChild = len(self.Parent.ChildList)+1

# ------------------------ PROMEDIO DE LAS EVALUACIONES -------------------------

    # Calcula el promedio cada vez que se hace una simulacion con el nuevo dato (nueva evaluacion)
    def Mean(self, Evaluation):
    
        Data = self.MeanEv * (self.NumSimulations-1)
        Sum = Data + Evaluation
        NewMean= Sum / (self.NumSimulations)
        return NewMean

# ------------------------ PROMEDIO DE LAS EVALUACIONES AL CUADRADO-------------------------

    # Calcula el promedio de los cuadrados cada vez que se hace una simulacion con el nuevo dato (nueva evaluacion)
    def SquareMean(self, Evaluation):
    
        Data = self.SquareMeanEv * (self.NumSimulations-1)
        Sum = Data + (Evaluation**2)
        NewSquareMean = Sum / (self.NumSimulations)
        return NewSquareMean

# ------------------------ DESVIACION ESTANDAR DE LAS EVALUACIONES -------------------------

    # Se calcula la desviacion estandar en funcion del promedio 
    def StandardDev(self, Evaluation):
    
        SquareMean = self.SquareMeanEv
        Mean = self.MeanEv
        Diff = np.max(SquareMean - (Mean**2),0)
        StdDev = mt.sqrt(Diff)
        return StdDev

# ------------------------  DE LAS EVALUACIONES -------------------------

    # Cuando se apreta un nodo para que despliegue un hijo, se llama al simulador pata guardar las informacion que retorna en los atributos de la clase
    def AddSimulation(self, Evaluation, Actions):
    
        # Cuando se apreta un nodo para que despliegue un hijo, se llama al simulador pata guardar las informacion que retorna en los atributos de la clase
        # Cada vez que se llama este metodo se agrega una simulacion
        self.NumSimulations = self.NumSimulations + 1
        
        #Solo si no hay una primera evaluacion se asigna, sino no
        if self.FirstEv == 0: 
            self.FirstEv = Evaluation
            
        # Se calcula la peor o mejor evaluacion 
        if Evaluation > self.BestEv:
            self.BestEv = Evaluation
            
        if Evaluation < self.WorstEv:
            self.WorstEv = Evaluation
            
        # Se asigna el numero de acciones y segun la evaluacion se calcula el promedio y la desviacion estandar
        self.NumActions = Actions
        self.MeanEv = self.Mean(Evaluation)
        self.SquareMeanEv = self.SquareMean(Evaluation)
        self.StdDev = self.StandardDev(Evaluation)
        self.CurrentEv = Evaluation
        
