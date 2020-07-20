
import subprocess

#se definen algunas variables antes de iterar
mode= "automatic_mode"
NOS= "2"
heuristic= "BFS"

#itera el comando dentro del for y cambia los parametros numericos

for i in range(1,10):
    seed = str(i*3)
    N = str(i*10)
    output = str(subprocess.check_output("python commands.py --heuristic " + heuristic + " --mode " + mode + " --seed " + seed + " --nos " + NOS + " --n " + N))
    print("el output es= " + output)

#limpiar putput
#sacar promedios por cada heuristica
#imprimir resultados
#proponer nuevas funciones