# ------------------------ LIBRERIAS -------------------------
import state
import simulation as sm
import numpy as np
import random
import math as mt

def define_seed(seed):
    random.seed(seed)

def eval(self):
    if self.V<=0.0:  #nodo sin hijos
        return -np.inf
    
    if len(self.ChildList) >= self.NumActions:  #No tiene más acciones
        return -np.inf 
    
    #Change by your prefered heuristic
    return BeamSearch_CurrentEv(self, 3)
    #return BFS(self)


############# Heuristic Functions ###############

## Components of the state (self)
# bestEv 
# worstEv 
# level2selected = {} #Number of nodes selected by level of the tree
# level2nodes = {} #Number of nodes by lebel

# self.id # Clave o identificador del nodo. Esta es la que se asocia con StateMap
# self.FirstEv # Primera evaluacion del nodo, una vez asignada no se puede cambiar
# self.CurrentEv  # Almacena la evaluacion actual, cambia cada vez que se simula el nodo
# self.MeanEv # Promedio de todas las evaluaciones obtenidas
# self.StdDev  # Desviacion estandar de todas las evaluaciones obtenidas
# self.BestEv  # La mayor evaluacion obtenida
# self.WorstEv  #Peor evaluacion del nodo
# self.NumActions  # Numero total de casos posibles producidos por el simulador
# self.ChildList []  # Esto representa una  lista dinamica, para apregar datos se utiliza el metodo append()
# self.NumSimulations # Numero de veces que el nodo ha sido simulado
# self.Selected # Mark if the node has been selected
# self.Parent
# self.Level  # nivel del nodo

### Específicos para FakeEvaluation
# self.mu 
# self.sigma 
# self.V 
# self.fakeEv 

#Búsqueda en profundidad (nodo más profundo)
def DFS (self):
    return self.Level

#Búsqueda en achura (nodo menos profundo)
def BFS (self):
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

def BeamSearch (self, W):  
    SN=0;
    if self.Level in state.State.level2selected:
        SN = state.State.level2selected[self.Level]
        
    depth = self.Level
    b=10000; e=1
    children = len(self.ChildList)

    if self.id==0: #root node
        if children >= W*W: return -np.inf
        return -b*depth
    else:
        if children >= W: return -np.inf# se descarta
        if not self.Selected and SN>=W: return -np.inf
        return -b*depth + e*self.FirstEv  

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
def eval6(self):
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


def eval2(self):
    return self.CurrentEv/self.NumSimulations

def mcts(self):
    if self.Parent != None:
        Ni = self.Parent.NumChild+2
    else:
        Ni = 2
    Np = self.NumChild+2
    UTC = self.MeanEv + random.randint(1,50) * mt.sqrt(mt.log(Np)/Ni)
    return UTC

def eval4(self):
    return mt.log((self.BestEv - self.WorstEv) / (self.StdDev+1))
   
def eval10(self):
    if self.V==0.0:
        return -np.inf
    return (len(sm.StateMap) - self.NumSimulations) * self.MeanEv