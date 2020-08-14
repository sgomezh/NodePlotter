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
evalMap["BeamSearch_CurrentEv"] = BeamSearch_CurrentEv
evalMap["BSearch2"] = BSearch2
evalMap["CurrentEv_NumSimulations"] = CurrentEv_NumSimulations
evalMap["mcts"] = mcts

def eval(self, heuristic):
    if self.V<=0.0:  #nodo sin hijos
        return -np.inf
    
    if len(self.ChildList) >= self.NumActions:  #No tiene más acciones
        return -np.inf 
    
    #Change by your prefered heuristic
    #return BeamSearch(self, 3)
    return evalMap[heuristic](self)

