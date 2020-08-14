

def writter(pos, heuristic, mode, seed, NOS, N, beststate):
    f = open ('results.txt','w')
    '''currentPos = pos
    f.seek(currentPos,2)

    #En caso de que sea el inicio del archivo (primera escritura)
    if i == 1:
        currentPos = 0
        f.write("------------------------------------------------------\n")
        f.write("Heuristic: " + heuristic + "\n")
        f.write("Mode: " + mode + "\n")
        f.write("Seed: " + seed + "\n")
        f.write("NOS: " + NOS + "\n")
        f.write("N: " + N + "\n")
        f.write("Result: " + str(beststate) + "\n")
        f.write("------------------------------------------------------\n")
        currentPos = f.tell()
    if i!= 1:
        f.seek(currentPos, 2)
        f.write("------------------------------------------------------\n")
        f.write("Heuristic: " + heuristic + "\n")
        f.write("Mode: " + mode + "\n")
        f.write("Seed: " + seed + "\n")
        f.write("NOS: " + NOS + "\n")
        f.write("N: " + N + "\n")
        f.write("Result: " + str(beststate) + "\n")
        f.write("------------------------------------------------------\n")
        currentPos = f.tell()
    print("currentPos= ", currentPos)

    f.write("------------------------------------------------------\n")
    f.write("Heuristic: " + heuristic + "\n")
    f.write("Mode: " + mode + "\n")
    f.write("Seed: " + seed + "\n")
    f.write("NOS: " + NOS + "\n")
    f.write("N: " + N + "\n")
    f.write("Result: " + str(beststate) + "\n")
    f.write("------------------------------------------------------\n")

    currentPos = f.tell()'''

    f.close()

    return currentPos

