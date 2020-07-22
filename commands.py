#----------------------------------LIBRERIAS-----------------------------------
import sys
import argparse
import main as m
#----------------------------------DEFINICION DE COMANDOS-----------------------------------
parser = argparse.ArgumentParser(description='comandos',)
parser.add_argument('--heuristic', action="store", dest="heuristic", type=str)
parser.add_argument('--mode', action="store", dest="mode", type=str)
parser.add_argument('--seed', action="store", dest="seed", type=int)
parser.add_argument('--nos', action="store", dest="nos", type=int)
parser.add_argument('--n', action="store", dest="n", type=int)
results = parser.parse_args()
'''print('mode     = {!r}'.format(results.mode))
print('seed     = {!r}'.format(results.seed))
print('nos     = {!r}'.format(results.nos))
print('n     = {!r}'.format(results.n))'''
#----------------------------------ASIGNACION DE VALORES-----------------------------------

heuristic = str(results.heuristic)
mode = str(results.mode)
seed = str(results.seed)
NOS = str(results.nos)
N = str(results.n)

'''if results.mode == None:
    mode = "interactive_mode"
else:
    mode = str(results.mode)

if results.seed == None:
    seed = 1
else:
    seed = int(results.seed)

if results.nos == None:
    NOS= 2
else:
    NOS = int(results.nos)

if results.n == None:
    N = 3
else:
    N = int(results.n)'''

print("heuristic= " + heuristic)
print("mode= " + mode)
print("seed= " + seed)
print("NOS= " + NOS)
print("N= " + N)

m.main(heuristic, mode, seed, N, NOS)






