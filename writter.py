

def writter(heuristic, mode, seed, NOS, N, beststate):
    f = open ('results.txt','w')

    f.write("------------------------------------------------------\n")
    f.write("Heuristic: " + heuristic + "\n")
    f.write("Mode: " + mode + "\n")
    f.write("Seed: " + seed + "\n")
    f.write("NOS: " + NOS + "\n")
    f.write("N: " + N + "\n")
    f.write("Result: " + beststate + "\n")
    f.write("------------------------------------------------------\n")

    f.close()