import pygame
from nodeProp import Node #tifa: importa la clase nodo
import node_manipulator
import simulation as sm
import properties as pr

def main(NOS):
    raiz = Node([27, 27], [200, 200, 200], 1, 0) #tifa: posicion y color definido (?)
    print(raiz)
    n_manipulator = node_manipulator.NodeManipulator(raiz)   
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption("PyGraphicGraf")
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                id = n_manipulator.get_node_id(x,y)
                print("id= ", id)
                id_child = n_manipulator.generate_son(x, y)
                print("id_child= ", id_child)
                sm.Simulation(id, id_child, NOS)
                child = n_manipulator.nodes[id_child]
                colorChild = pr.NodeColor(id_child)
                child.color_to(colorChild)
                child.size_to(id)

            '''else:
                print("apreto afuera") #tifa: aqui detecta si apreta afuera o no del nodo'''

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            n_manipulator.camera.drag(0,2)
        if pressed[pygame.K_s]:
            n_manipulator.camera.drag(0,-2)
        if pressed[pygame.K_d]:
            n_manipulator.camera.drag(-2,0)
        if pressed[pygame.K_a]:
            n_manipulator.camera.drag(2,0)

        n_manipulator.update()

        screen.fill((33, 33, 33))
        n_manipulator.draw(screen)
        pygame.display.update()


'''if __name__ == '__main__':
    main(NOS)'''
