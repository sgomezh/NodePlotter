import pygame
from nodeProp import Node 
import node_manipulator
import simulation as sm
import properties as pr
from camera import Camera
import reader as rd
import state as st
import sys
import heuristics as h
import training as t

def click_node(NOS,id,n_manipulator):
    #id_first_child = n_manipulator.generate_son(id)
    #for i in range(1,NOS):
        #n_manipulator.generate_son(id)
    
    for i in range(0,NOS):
        if i==0: id_first_child = n_manipulator.generate_son(id)
        else: n_manipulator.generate_son(id)
           
        #print("id_child= ", id_first_child)
        
    sm.Simulation(id, id_first_child, NOS)
        
    for node in n_manipulator.nodes:
        #node.update()
        newColor = pr.StateColor(node.id, len(n_manipulator.nodes)) 
        node.color_to(newColor)

def main(heuristic, NOS, mode, N, file):

    #se define la raiz y su color
    raiz = Node([27, 27], [200, 200, 200], 1, 0) 
    ranking = 1
    
    n_manipulator = node_manipulator.NodeManipulator(raiz)   

    if mode == "interactive_mode":
        pygame.init()
        screen = pygame.display.set_mode((900, 500), pygame.SRCALPHA, 32)
        pygame.display.set_caption("Node Plotter")
        done = False

        for i in range(N):
            #print("entro al for in range")
            id = sm.BestState(heuristic)
            if id == None: continue # do nothing
            #se imprime la info y se pasa el id del nodo seleccionado
            pos_x, pos_y = n_manipulator.nodes[id].pos

            #simulacion
            click_node(NOS,id,n_manipulator)
           

        print("bestEv: ", st.State.bestEv)   
        n_manipulator.update()

        screen.fill((33, 33, 33))
        n_manipulator.draw(screen)
        pygame.display.update()

    if mode == "read_file":
        stateList = rd.reader(file)
        lenght = len(stateList)
        for i in range(lenght):

            dataList = stateList[i]
            
            childKey = int(dataList[0])
            parentKey = int(dataList[1])
            Evaluation = float(dataList[2])
            Actions = int(dataList[3])
     
            n_manipulator.generate_son(parentKey)
            sm.CreateState(childKey, parentKey, Actions, Evaluation)

            for node in n_manipulator.nodes:
                #node.update()
                newColor = pr.StateColor(node.id, len(n_manipulator.nodes)) 
                node.color_to(newColor)
        print("bestEv", st.State.bestEv)          
        n_manipulator.update()

        screen.fill((33, 33, 33))
        n_manipulator.draw(screen)
        pygame.display.update()

    
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                return
                #done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                id = n_manipulator.get_node_id(x,y)
                #antes de simular, se guarda la información del nodo
                t.candidateNodes()
                #ningun nodo seleccionado (seleccion automatica)
                if id == -1 or len(sm.StateMap[id].ChildList) >= sm.StateMap[id].NumActions : 
                    id = sm.BestState(heuristic)
                    if id == None: continue # do nothing
                    pos_x, pos_y = n_manipulator.nodes[id].pos
                
                    
                click_node(NOS,id,n_manipulator)
                #n_manipulator.nodes[id_child].color_to(pr.StateColor(id_child))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    n_manipulator.camera.drag(0, 45)
                elif event.key == pygame.K_s:
                    n_manipulator.camera.drag(0, -45)
                elif event.key == pygame.K_d:
                    n_manipulator.camera.drag(-45, 0)
                elif event.key == pygame.K_a:
                    n_manipulator.camera.drag(45, 0)
                elif event.key == pygame.K_z:
                    n_manipulator.camera.anchura -= 1
                    n_manipulator.update_position()
                elif event.key == pygame.K_x:
                    n_manipulator.camera.anchura += 1
                    n_manipulator.update_position()
                elif event.key == pygame.K_r:
                    n_manipulator.camera.altura -= 1
                    n_manipulator.update_position()
                elif event.key == pygame.K_f:
                    n_manipulator.camera.altura += 1
                    n_manipulator.update_position()

        n_manipulator.update()

        screen.fill((33, 33, 33))
        n_manipulator.draw(screen)
        pygame.display.update()
        pygame.time.wait(10) #para no consumir tanto recurso
        

        
