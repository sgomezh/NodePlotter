
# ------------------------ LIBRERIAS -------------------------

import random 
import numpy as np
import graphics as gp
import sys
import argparse
import simulation as sm
import heuristics as h
import node_manipulator as nd
import nodeProp as np
import state as st

#------------------------ INSTRUCCION DESDE EL TERMINAL----------------

parser = argparse.ArgumentParser(
    description='comandos',
)
parser.add_argument('--mode', action="store", dest="mode", type=int)
parser.add_argument('--seed', action="store", dest="seed", type=int)
parser.add_argument('--nos', action="store", dest="nos", type=int)
parser.add_argument('--n', action="store", dest="n", type=int)

results = parser.parse_args()
'''print('mode     = {!r}'.format(results.mode))
print('seed     = {!r}'.format(results.seed))
print('nos     = {!r}'.format(results.nos))
print('n     = {!r}'.format(results.n))'''

if results.mode == None:
    mode = 0
else:
    mode = int(results.mode)

if results.seed == None:
    seed = 1
else:
    seed = int(results.seed)

if results.nos == None:
    nos = 2
else:
    nos = int(results.nos)

if results.n == None:
    n = 3
else:
    n = int(results.n)

# ------------------------ LLAMADO DE FUNCIONES -------------------------

# option = 0 (modo manual) option = 1 (se ejecuta automaticamente mostrando el grafico) option = 2 (se ejecuta automaticamente sin mostrar el grafico)
option = mode

# NOS = cantidad de nodos creados por cada simulacion (hay problemas con NOS=1)
NOS = nos

# n = cantidad de vces que se ejecuta la heuristica
N = n

# seed para cada random de cada archivo que usa random
np.random.seed(seed)
sm.define_seed(seed)
h.define_seed(seed)
nd.define_seed(seed)
np.define_seed(seed)
st.define_seed(seed)


print ("mode: " + str(option) + " seed: "+ str(seed) + " NOS: " + str(NOS) + " N: " + str(N))
file = None
'''if len(sys.argv)>1:
    # Esta variable almacena el numero de simulaciones que se haran por cada nodo
    NOS = int(sys.argv[1])
    if len(sys.argv)>2: 
        file=sys.argv[2]'''

# Se llama a la funcion que dibuja el grafo
gp.main(NOS, option, N, file)
