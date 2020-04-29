import pygame
from nodeProp import Node #tifa: importa la clase nodo
import node_manipulator
import simulation as sm
import properties as pr
from camera import Camera
import reader as rd

def click_node(NOS,id,n_manipulator):
    id_first_child = n_manipulator.generate_son(id)
    for i in range(1,NOS):
        n_manipulator.generate_son(id)
           
        #print("id_child= ", id_first_child)
        sm.Simulation(id, id_first_child, NOS)
        for node in n_manipulator.nodes:
            #node.update()
            newColor = pr.StateColor(node.id) # tifa: Funcion que asigna un color
            node.color_to(newColor)

def main(NOS):
    raiz = Node([27, 27], [200, 200, 200], 1, 0) #tifa: posicion y color definido (?)
    #print(raiz)
    n_manipulator = node_manipulator.NodeManipulator(raiz)   
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption("Node Plotter")
    done = False

           
    '''stateList = rd.reader()
    #lenght = len(stateList)
    #for i in range(lenght):

     #   dataList = stateList[i]

   #     childKey = int(dataList[0])
    #    parentKey = int(dataList[1])
     #   Evaluation = float(dataList[2])
     
      #  n_manipulator.generate_son(parentKey)
       # sm.CreateState(childKey, parentKey, 0, Evaluation)

        n_manipulator.update()

        screen.fill((33, 33, 33))
        n_manipulator.draw(screen)
        pygame.display.update()'''


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                id = n_manipulator.get_node_id(x,y)
                if id == -1: #ningun nodo seleccionado (seleccion automatica)
                    id = sm.BestState()
                    pos_x, pos_y = n_manipulator.nodes[id].pos
                    
                click_node(NOS,id,n_manipulator)
                #n_manipulator.nodes[id_child].color_to(pr.StateColor(id_child))

            '''else:
                print("apreto afuera") #tifa: aqui detecta si apreta afuera o no del nodo'''

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            n_manipulator.camera.drag(0, 9)
        if pressed[pygame.K_s]:
            n_manipulator.camera.drag(0, -9)
        if pressed[pygame.K_d]:
            n_manipulator.camera.drag(-9, 0)
        if pressed[pygame.K_a]:
            n_manipulator.camera.drag(9, 0)
        if pressed[pygame.K_z]:
            n_manipulator.camera.anchura -= 1
            n_manipulator.update_position()
        if pressed[pygame.K_x]:
            n_manipulator.camera.anchura += 1
            n_manipulator.update_position()
        if pressed[pygame.K_f]:
            n_manipulator.camera.altura -= 1
            n_manipulator.update_position()
        if pressed[pygame.K_r]:
            n_manipulator.camera.altura += 1
            n_manipulator.update_position()

        n_manipulator.update()

        screen.fill((33, 33, 33))
        n_manipulator.draw(screen)
        pygame.display.update()
        


'''if __name__ == '__main__':
    main(NOS)'''
