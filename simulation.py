# ------------------------ LIBRERIAS -------------------------
import math as mt
import numpy as np
import tkinter
import numpy as np
import subprocess
import state
import properties as pr
import random
from scipy.stats import truncnorm
# ---------------------------------------------------- GENERADOR DE CLAVES ----------------------------------------------------------

    
#Parameters of the Fake Simulator
max_child = 100  # max number of children per node
mean_depth = 20 # profundidad media
init_sigma = 0.02 # std deviation of the children simulations
factor_sigma = 3 # init_sigma/factor_sigma is the std deviation of mu
init_mu = 0.9
init_V = 1.0

extrachild_penalty = 0.00 # penalización adicional por hijo extra

maxv = 2*(init_V/mean_depth)


# Se inicializa el mapa y se crea la primera casilla (nodo raiz)
StateMap = {}
StateMap[0] = state.State(None, 0)


# Archivo con árbol de verda
file1 = open('BR8-0.txt', 'r') 
count = 0

child_nodes={}
eval={}
max_eval=0.0
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 
    
    if(count>=20):
        # if line is empty 
        # end of file is reached 
        if not line: 
            break
        line= line.strip()
        elements = line.split(',')
        if int(elements[1]) not in child_nodes: child_nodes[int(elements[1])]=[]
        child_nodes[int(elements[1])].append(int(elements[0]))
        eval[int(elements[0])]= float(elements[2])
        if float(elements[2]) > max_eval: max_eval=float(elements[2])
      
print("max_eval=",max_eval)
    #if count == 24: break
file1.close() 
# ----------------------------------------

def BestState(heuristic):
    if len(StateMap)==1: return 0
    bestEval = -100000000
    bestState = None
    for (key,state) in StateMap.items():
        ev = state.eval(heuristic)
        if bestEval < ev:
            bestEval = ev
            bestState = key
    return bestState

# Con la misma clave utilizada para agregar un nodo al grafo, se agrega un elemento de la clase Nodo, de modo que se cree un diccionario de referencias entre el grafo y el mapa
def CreateState(key, parent, actions, eval):
    # La key que se ocupa para el grafo, es la misma que se ocupa para el mapa
    # Se hace una instancia de la clase Nodo (vacio)
    NewState = state.State(parent, key)
    
    # Se guarda el nodo inicializado en la misma posicion del grafo
    StateMap[key] = NewState

    # Como ya esta creado el nuevo nodo, se mete a la lista de "hijos visibles" del nodo
    (StateMap[parent].ChildList).append(key) 
    
    StateMap[parent].AddSimulation(eval, -1) 
    StateMap[parent].set_selected()
              
    # Se llama a simular el nodo para inicializarlo (Ver clase Nodo)
    StateMap[key].AddSimulation(eval, actions)
    if eval > state.State.bestEv:
        state.State.bestEv=eval
     

def truncate_normal(min,max,mu,sigma):
     if sigma==0:
        return mu
     else:
        return truncnorm.rvs((min - mu) / sigma, 
               (max - mu) / sigma, loc=mu, scale=sigma, size=1)[0]
    
def compute_parameters(parentEv, mu_parent, sigma_parent, V, id_child):
    v =  random.uniform (0.0,maxv)
    if v>V : v=V

    sigma_child = (V-v)*init_sigma
    if id_child==1:
        firstEv = parentEv
        mu_child = ((V-v)*mu_parent + v*firstEv)/V
    else:
        mu_child = truncate_normal(0,1,mu_parent - (id_child-1)*extrachild_penalty, sigma_child/factor_sigma)
            
        if sigma_child>0:
            firstEv = truncate_normal(0,1,mu_child,sigma_child)
        else:
            firstEv = mu_child
    return firstEv, mu_child, sigma_child, v

def Simulation(ParentKey, ChildKey, NOS):
    if ParentKey==0:
        bsg_id=0
    else: bsg_id = StateMap[ParentKey].bsg_id
    
    n_child = len(StateMap[ParentKey].ChildList)
    
    id_child = child_nodes[bsg_id][n_child]
    
    CreateState(ChildKey, ParentKey, 0, eval[id_child])
    
    StateMap[ParentKey].NumActions=len(child_nodes[bsg_id])
    if id_child in child_nodes: StateMap[ChildKey].NumActions = len(child_nodes[id_child])
    
    StateMap[ChildKey].bsg_id = id_child
    StateMap[ChildKey].V = 1.0
    

# --- Fake simulations ------- #
def FakeSimulation(ParentKey, ChildKey, NOS):

    id_child = len(StateMap[ParentKey].ChildList)+1
    parentEv = StateMap[ParentKey].fakeEv
    V = StateMap[ParentKey].V
    sigma = StateMap[ParentKey].sigma
    mu = StateMap[ParentKey].mu
    
    for i in range(0,NOS):
        #fake eval
        firstEv, mu_child, sigma_child, v = compute_parameters(parentEv, mu, sigma, V, id_child)  
        
        CreateState(ChildKey, ParentKey, max_child, firstEv)
        
        StateMap[ChildKey].mu = mu_child
        StateMap[ChildKey].sigma = sigma_child
        StateMap[ChildKey].V = V-v
        StateMap[ChildKey].fakeEv = firstEv
        
        V2 = StateMap[ChildKey].V
        if V2 > 0:
            StateMap[ChildKey].NumActions = int(V2*max_child)
        else:
            StateMap[ChildKey].NumActions = 0
        #int(random.uniform(StateMap[ChildKey].V,1)*max_child)
        id_child = id_child+1

        ChildKey=ChildKey+1

# --------------------------------------------------------- SIMULACION DE UN NODO ----------------------------------------------------
StateSimulations = 0
# Se recibe una evaluacion y un numero de acciones a partir del simulador. A partir de ello, se rellena el nodo del mapa y se agregan hijos a un nodo del grafo
def RealSimulation(ParentKey, ChildKey, NOS):

    global StateSimulations
    
    if StateSimulations == 0:
        # StateSimulations almacena una cantidad inicial minima de simulaciones que deben aparecer al apretar un nodo
        StateSimulations = NOS #NOS = number of simulations   
    
    # Se crea un arreglo que guardara el camino desde la raiz al nodo actual
    pathStack = [] 
    
    # Se crea una copia auxiliar que guarde la  informacion del nodo actual
    AuxState = StateMap[ParentKey] 
    pathStack.insert(0,len(StateMap[ParentKey].ChildList)+1)
    
    while AuxState.IdLastChild != None: 
    
        # Se mete a la pila el nuevo hijo
        pathStack.insert(0,AuxState.IdLastChild) 
        
        # Se obtiene el padre de nodo (con toda su informacion para crear el camino hacia arriba) 
        AuxState = AuxState.Parent 
        # Se vuelve a iterar siempre y cuando su IdChild no None, que es el caso del nodo raiz
   
    
    # El lector lee la cantidad de simulaciones por cada nodo y las ordena separadas por comas
    reader="" 
    
    # Se inicializa la variable   que recibira el numero que se esta leyendo de la cadena. Representa la cantidad de simulaciones que se hicieron para llegar     al nodo actual
    number=0
    
    # Se recorre pathStack para dejarlo en formato "simulaciones1, simulaciones2, ... , simulaciones3"
    for e in range(len(pathStack)):
    
        number = str(pathStack[e])
        reader+= number
        reader += ','   
   
   # Se inicializa la profundidad del nodo actual
    depth = 0 
    
    # Se calcula la profundidad del grafo segun la cantidad de simulaciones por nodos registradas en el lector anterior
    for f in range(len(reader)):
    
      # Se lee el reader, si es un numero, entonces aumenta la profundidad (entre largo el reader, m�s grande la profundidad)
        if reader[f].isnumeric():
            depth = depth+1  
     
    # Se hace una copia del lector para
    simulations = reader
      
    for i in range(StateSimulations-1):
       simulations = simulations + "\;" + reader.replace(reader[len(reader)-2], str(int(number)+i+1))
       
    print("Simulations=", simulations)
    
    # Se llama al simulador para obtener la evaluacion y numero de acciones de un caso
    #ssh = paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    #ssh.connect("158.251.88.197", username = "tifa", password = "ScHrOdL223")
    #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("./BSG_SIMULATOR BR/BR10.txt -i 1 --min_fr=0.98 -t 10 -f BR --actions="+simulations)
    output = str(subprocess.check_output("ssh tifa@158.251.88.197 ./BSG_SIMULATOR BR/BR10.txt -i 1 --min_fr=0.98 -t 10 -f BR --actions="+simulations, shell=True))
    #output = str(subprocess.check_output("echo %PATH%" , shell=True))
    print(output)

    # Se separa el output por salto de linea 
    output = output.split('\\n')
    
    # Recorre toda la cadena del output para poder encontrar el inicio de la simulacion
    for i in range(len(output)): 
             
          # La variable position almacena la posicion del inicio de esta cadena, en caso de que no se encuentre, devuelve -1
          position = output[i].find("##start simulation") 
          
          if position != -1: 

              # Se avanza un espacio para guardar las acciones
              path = output[i+1] 
              
              # Se separa el numero de simulaciones del nodo
              path = path.split(';')
            
              # Se separa el numero de acciones del nodo
              Actions = int(path[depth-1].split('/')[1])
              
              # Se obtiene la evaluacion a traves del simulador
              # Luego se avanza dos espacios para guardar la evaluacion del nodo 
              Evaluation = float(output[i+2])
                
              # Crea un nodo para luego insertarlo en el mapa y el grafo
              NewState = CreateState(ChildKey, ParentKey, Actions, Evaluation) 
                        
              ChildKey=ChildKey+1
                            
    print("La evaluacion del nodo ", ParentKey, "es ", Evaluation)
          
    return ParentKey, StateSimulations