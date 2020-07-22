
# ------------------------ LIBRERIAS -------------------------
import sys
import argparse
import random 
import numpy as np
import simulation as sm
import state as st
import heuristics as h
import graphics as gp
import node_manipulator as nd
import nodeProp as np
#------------------------ INSTRUCCION DESDE EL TERMINAL----------------

def non_interactive_expand(NOS,id):
        id_first_child = len(sm.StateMap)
        #print(id_first_child)
        for i in range(1,NOS):
            sm.Simulation(id, id_first_child, NOS)

def main(heuristic, mode, seed, N, NOS):

    #se castean algunas variables
    seed = int(seed)
    N = int(N)
    NOS = int(NOS)
    
    #se define la seed para los números random
    random.seed(seed)
    np.random.seed(seed)

    file = None

    '''if len(sys.argv)>1:
        # Esta variable almacena el numero de simulaciones que se haran por cada nodo
        NOS = int(sys.argv[1])
        if len(sys.argv)>2: 
            file=sys.argv[2]'''
                

    if mode == "automatic_mode":
        for i in range(N):
            id = sm.BestState(heuristic)
            if id == None: continue # do nothing
            non_interactive_expand(NOS,id)
            
        print("bestEv", st.State.bestEv)     
        sys.exit(0)

    # Se llama a la funcion que dibuja el grafo
    gp.main(heuristic, NOS, mode, N, file)

    #Se escribe el resultado en el archivo
    #writter(heuristic, mode, seed, NOS, N, beststate)
        
    