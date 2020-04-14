
# ------------------------ LIBRERIAS -------------------------

import numpy as np
import graphics as gp
# ------------------------ LLAMADO DE FUNCIONES -------------------------

# Esta variable almacena el numero de simulaciones que se haran por cada nodo
NOS = 1

# Se pregunta por la cantidad de nodos simulados a la vez, independientemente si es manual o automatico
#NOS = int(input("Introduzca la cantidad de simulaciones por nodo: "))

# Se llama a la funcion que dibuja el grafo
#gp.DrawGRaph(fig, NOS, evOption, simOption, iterator) 
gp.main(NOS)
