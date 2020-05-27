
# ------------------------ LIBRERIAS -------------------------

import numpy as np
import graphics as gp
import sys
# ------------------------ LLAMADO DE FUNCIONES -------------------------

NOS = 2
file = None
if len(sys.argv)>1:
    # Esta variable almacena el numero de simulaciones que se haran por cada nodo
    NOS = int(sys.argv[1])
    if len(sys.argv)>2:
        file=sys.argv[2]

# Se llama a la funcion que dibuja el grafo
gp.main(NOS, file)
