# ------------------------ LIBRERIAS -------------------------
import state
import simulation as sm
import numpy as np
import random
import math as mt



#-----------------------------FUNCION DE EVALUACION---------------------------------------


### Específicos para FakeEvaluation
# self.mu 
# self.sigma 
# self.V 
# self.fakeEv 

############# Heuristic Functions ###############

#Búsqueda en profundidad (nodo más profundo)
def DFS(self):
  
    return self.Level

#Búsqueda en achura (nodo menos profundo)
def BFS(self):

    return -self.Level

#Búsqueda en profundidad (informada)
def informed_DFS (self):

    return self.Level*100 + self.FirstEv

#Búsqueda en achura (informada)
def informed_BFS (self):

    return -self.Level*100 + self.FirstEv

def bestFirstEv(self):

    return self.FirstEv

def bestMeanEv(self):
    return self.MeanEv

def BeamSearch70 (self): 
    return BeamSearch_CurrentEv (self, 70)

def BeamSearch60 (self): 
    return BeamSearch_CurrentEv (self, 60)

def BeamSearch100 (self): 
    return BeamSearch_CurrentEv (self, 100)

def BeamSearch53 (self): 
    return BeamSearch_CurrentEv (self, 53)

def BeamSearch50 (self): 
    return BeamSearch_CurrentEv (self, 50)

def BeamSearch21 (self): 
    return BeamSearch_CurrentEv (self, 21)

def BeamSearch13 (self): 
    return BeamSearch_CurrentEv (self, 13)

def BeamSearch9 (self): 
    return BeamSearch_CurrentEv (self, 9)

def BeamSearch7 (self): 
    return BeamSearch_CurrentEv (self, 7)

def BeamSearch5 (self): 
    return BeamSearch_CurrentEv (self, 5)

def BeamSearch3 (self): 
    return BeamSearch_CurrentEv (self, 3)

def BeamSearch_CurrentEv (self, W): 

    SN=0
    if self.Level in state.State.level2selected:
        SN = state.State.level2selected[self.Level] 
        
    depth = self.Level
    b=10000; e=1
    children = len(self.ChildList)

    if self.id==0: #root node
        if children >= W*W: return -np.inf
        return -b*depth
    else:
        if children >= W: return (-b*depth + e*self.FirstEv) - (self.NumSimulations*b)


        if not self.Selected and SN>=W: return -np.inf
        return (-b*depth + e*self.FirstEv) 

#BeamSearch like evaluation
def BSearch2(self):
    
    if self.V==0.0:
        return -np.inf
    
    N1=0; SN=0; N=1
    if self.Level in state.State.level2nodes:
        N = state.State.level2nodes[self.Level] #nodos en nivel actual
    if self.Level+1 in state.State.level2nodes:
        N1 = state.State.level2nodes[self.Level+1] #nodos del siguiente nivel
    if self.Level in state.State.level2selected:
        SN = state.State.level2selected[self.Level]
        
    depth = self.Level
    children = len(self.ChildList)

    a=100000; b=10000; c=1000; d=100; e=1
    S=0
    if self.Selected: S=1
    if self.id==0: #root node
        return -a*N1/2 - b*depth
    else:
        return -a*N1 - b*depth -c*np.max(np.sqrt(N)-SN,0)*S - d*children + e*self.FirstEv


def CurrentEv_NumSimulations(self):
    return self.CurrentEv/self.NumSimulations

def mcts(self):
    
    if self.Parent != None:
        Ni = self.Parent.NumChild+2
    else:
        Ni = 2
    Np = self.NumChild+2
    UTC = self.MeanEv + random.randint(1,50) * mt.sqrt(mt.log(Np)/Ni)
    return UTC

def tifa(self):

    SN=0 #numero de nodos seleccionados en el nivel actual
    SN2 = 0 #numero de nodos seleccionados en el nivel siguiente
    TSN = 0 #numero de nodos totales en el nivel actual

    #se verifica que el nivel seleccionado esté en el mapa
    if self.Level in state.State.level2selected: 
        SN = state.State.level2selected[self.Level] 
    
    #se define el siguiente nivel
    nextLevel = int(self.Level) + 1 
    
    #se verifica que el nivel seleccionado esté en el mapa
    if nextLevel in state.State.level2selected: 
        SN2 = state.State.level2selected[nextLevel] 

    #se verifica que el nivel 
    if self.Level in state.State.level2nodes:
        TSN = state.State.level2nodes[self.Level]

    #la profundidad del nodo es el nivel en el que se encuentra
    depth = self.Level 

    #se definen las constantes
    a=1000000
    b=10000
    c=1000
    d=100
    e=10 

    #se obtiene la cantidad de hijos del nodo
    children = len(self.ChildList)

    #se obtienen la cantidad de nodo/estados en todos los niveles
    totalNodes = len(sm.StateMap)
   
    #W varía segun la cantidad de nodos totales y nodos seleccionados 
    W = totalNodes - SN

    #si es el nodo raiz
    if self.id==0: 

        #si la cantidad de hijos es mayor a W^2 (es decir, la cantidad de hijos es W veces mas grande que W)
        if children > W*W: 
            #se castiga la evaluacion del nodo pero no se descarta 
            return (-a*children)-(b*SN2)-(c*max(mt.sqrt(totalNodes-TSN), 0))-d*depth

        return -(b*SN2)-(c*max(mt.sqrt(totalNodes-TSN), 0))-d*depth

    else:
        if children >= W: 
            return -(b*SN2)-(c*max(mt.sqrt(totalNodes-TSN), 0))-d*depth+e*self.MeanEv

        if not self.Selected and SN>=W: 
            return (-a*children)-(b*SN2)-(c*max(1/(mt.log(totalNodes-TSN +0.0001)), 0))
        
        return (-b*depth + e*self.MeanEv) 

'''def eval4(self):
   
    return mt.log((self.BestEv - self.WorstEv) / (self.StdDev+1))
   
def eval10(self):

    if self.V==0.0:
        return -np.inf
    return (len(sm.StateMap) - self.NumSimulations) * self.MeanEv'''
#---------------------------DEFINICION DEL MAPA DE HEURISTICAS--------------------------------

evalMap={}
evalMap["BFS"] = BFS
evalMap["DFS"] = DFS
evalMap["informed_DFS"] = informed_DFS 
evalMap["informed_BFS"] = informed_BFS
evalMap["bestFirstEv"] = bestFirstEv
evalMap["bestMeanEv"] = bestMeanEv
evalMap["BeamSearch3"] = BeamSearch3
evalMap["BeamSearch5"] = BeamSearch5
evalMap["BeamSearch7"] = BeamSearch7
evalMap["BeamSearch9"] = BeamSearch9
evalMap["BeamSearch13"] = BeamSearch13
evalMap["BeamSearch21"] = BeamSearch21
evalMap["BeamSearch50"] = BeamSearch50
evalMap["BeamSearch53"] = BeamSearch53
evalMap["BeamSearch100"] = BeamSearch100
evalMap["BeamSearch60"] = BeamSearch60
evalMap["BeamSearch70"] = BeamSearch70
evalMap["BeamSearch_CurrentEv"] = BeamSearch_CurrentEv
evalMap["BSearch2"] = BSearch2
evalMap["CurrentEv_NumSimulations"] = CurrentEv_NumSimulations
evalMap["mcts"] = mcts
evalMap["tifa"] = tifa

def eval(self, heuristic):
    if self.V<=0.0:  #nodo sin hijos
        return -np.inf
    
    if len(self.ChildList) >= self.NumActions:  #No tiene más acciones
        return -np.inf 
    
    #Change by your prefered heuristic
    #return BeamSearch(self, 3)
    return evalMap[heuristic](self)

