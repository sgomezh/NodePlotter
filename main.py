
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

def non_interactive_expand(id):
        id_first_child = len(sm.StateMap)
        #print(id_first_child)
        #for i in range(1,NOS):
        sm.Simulation(id, id_first_child, 1)

def main(heuristic, mode, N, NOS):

    #se castean algunas variables
    N = int(N)
    NOS = int(NOS)
    
    #se define la seed para los números random

    file = None             

    if mode == "automatic_mode":
        for i in range(N):
            id = sm.BestState(heuristic)
            if id == None: print (i); break; #continue # do nothing
                
            if len(sm.StateMap[id].ChildList) == 0: i -=1 #el primer hijo no cuenta
            
            non_interactive_expand(id)
            
        print("bestEv", st.State.bestEv)     
        sys.exit(0)
    

    # Se llama a la funcion que dibuja el grafo
    gp.main(heuristic, NOS, mode, N, file)

        
    