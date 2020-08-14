import subprocess
import writter as w

#se definen algunas variables antes de iterar
mode= "automatic_mode"
NOS= "2"
heuristic= "BFS"
iterations = 10
evaluationSum = 0
pos = 0

#itera el comando dentro del for y cambia los parametros numericos

for i in range(1,iterations+1):


    seed = str(i*3)
    N = str(i*10)

    output = str(subprocess.check_output("python commands.py --heuristic " + heuristic + " --mode " + mode + " --seed " + seed + " --nos " + NOS + " --n " + N))

    startLoc = output.find("bestEv") + 7
    endLoc = len(output)-5

    evaluation = float(output[startLoc:endLoc])

    evaluationSum = evaluationSum + evaluation

    print("Evaluation: ", evaluation)

    #Se escribe el resultado en el archivo
    #pos = w.writter(pos, heuristic, mode, seed, NOS, N, evaluation)

meanEvaluation = evaluationSum / iterations

print("Mean evaluation: ", meanEvaluation)
print("Heuristic: ", heuristic)

#proponer nuevas funciones