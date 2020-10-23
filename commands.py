#-------------------------------------LIBRERIAS-------------------------------------
import sys
import argparse
import numpy as np
import random 
#----------------------------------DEFINICION DE COMANDOS-----------------------------------
parser = argparse.ArgumentParser(description='comandos',)
parser.add_argument('--heuristic', action="store", dest="heuristic", type=str)
parser.add_argument('--mode', action="store", dest="mode", type=str)
parser.add_argument('--seed', action="store", dest="seed", type=int)
parser.add_argument('--nos', action="store", dest="nos", type=int)
parser.add_argument('--n', action="store", dest="n", type=int)
results = parser.parse_args()
#----------------------------------ASIGNACION DE VALORES-----------------------------------

heuristic = str(results.heuristic)
mode = str(results.mode)
seed = int(results.seed)
NOS = str(results.nos)
N = str(results.n)

#Esto debe ser llamado antes de cualquier libreria interna
random.seed(seed)
np.random.seed(seed)

#----------------------------------OUTPUT----------------------------------
print("heuristic= " + heuristic)
print("mode= " + mode)
print("seed= " + str(seed))
print("NOS= " + NOS)
print("N= " + N)
#----------------------------------LLAMADA AL MAIN-----------------------------------
import main as m
m.main(heuristic, mode, N, NOS)






