
# ------------------------ LIBRERIAS -------------------------
import math as mt
import numpy as np
import tkinter
import numpy as np
import subprocess
import node as nd
import properties as pr
import function1 as f1
import function2 as f2
import paramiko
# ---------------------------------------------------- GENERADOR DE CLAVES ----------------------------------------------------------
# Se inicializa el mapa y se crea la primera casilla (nodo raiz)
NodeMap = {}
NodeMap[0] = nd.Nodo(None, 0)


# Con la misma clave utilizada para agregar un nodo al grafo, se agrega un elemento de la clase Nodo, de modo que se cree un diccionario de referencias entre el grafo y el mapa
def CreateNode(ChildKey, ParentKey):

    # La key que se ocupa para el grafo, es la misma que se ocupa para el mapa
    # Se hace una instancia de la clase Nodo (vacio)
    NewNode = nd.Nodo(ParentKey, ChildKey)
    
    # Se guarda el nodo inicializado en la misma posicion del grafo
    NodeMap[ChildKey] = NewNode
    
    return NewNode

# --------------------------------------------------------- SIMULACION DE UN NODO ----------------------------------------------------
NodeSimulations = 0
# Se recibe una evaluacion y un numero de acciones a partir del simulador. A partir de ello, se rellena el nodo del mapa y se agregan hijos a un nodo del grafo
def Simulation(ParentKey, ChildKey, NOS):

    global NodeSimulations
    
    if NodeSimulations == 0:
        # NodeSimulations almacena una cantidad inicial minima de simulaciones que deben aparecer al apretar un nodo
        NodeSimulations = NOS #NOS = number of simulations   
    
    # Se crea un arreglo que guardara el camino desde la raiz al nodo actual
    pathStack = [] 
    
    # Se crea una copia auxiliar que guarde la  informacion del nodo actual
    AuxNode = NodeMap[ParentKey] 
    pathStack.insert(0,len(NodeMap[ParentKey].ChildList)+1)
    
    while AuxNode.IdLastChild != None: 
    
        # Se mete a la pila el nuevo hijo
        pathStack.insert(0,AuxNode.IdLastChild) 
        
        # Se obtiene el padre de nodo (con toda su informacion para crear el camino hacia arriba) 
        AuxNode = AuxNode.Parent 
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
    
    for i in range(NodeSimulations-1):
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
    #command = "ssh tifa@158.251.88.197 ./BSG_SIMULATOR BR/BR10.txt -i 1 --min_fr=0.98 -t 10 -f BR --actions=" + simulations
    #pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #while True:
    #    line = pipe.stdout.readline()
    #    if line:
    #        print("line = " + line)
    #    if not line:
    #        break
    #return 
    # Se separa el output por salto de linea 
    output = output.split('\\n')
    
    # Recorre toda la cadena del output para poder encontrar el inicio de la simulacion
    for i in range(len(output)): 
          
          
          # La variable position almacena la posicion del inicio de esta cadena, en caso de que no se encuentre, devuelve -1
          position = output[i].find("##start simulation") 
          
          if position != -1: 
              
              # Crea un nodo para luego insertarlo en el mapa y el grafo
              NewNode = CreateNode(ChildKey, ParentKey) 
              
              # Como ya esta creado el nuevo nodo, se mete a la lista de "hijos visibles" del nodo
              (NodeMap[ParentKey].ChildList).append(ChildKey) 
     
              # Se avanza un espacio para guardar las acciones
              path = output[i+1] 
              
              # Se separa el numero de simulaciones del nodo
              path = path.split(';')
              
              # Se separa el numero de acciones del nodo
              Actions = int(path[depth-1].split('/')[1])
              
              # Se obtiene la evaluacion a traves del simulador
              # Luego se avanza dos espacios para guardar la evaluacion del nodo 
              Evaluation = float(output[i+2])
              
              # Llama al metodo que inicializa el nodo 
              NodeMap[ParentKey].AddSimulation(Evaluation, Actions) 
              
              # Se llama a simular el nodo para inicializarlo (Ver clase Nodo)
              NodeMap[ChildKey].AddSimulation(Evaluation, 0)
                            
    print("La evaluacion del nodo ", ParentKey, "es ", Evaluation)
          
    return ParentKey, NodeSimulations