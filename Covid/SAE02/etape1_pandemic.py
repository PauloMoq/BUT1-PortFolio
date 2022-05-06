# Usefull to delete useless messages
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import random
import constants
import engine
import time



def draw(scene, font, persons):
    '''
        Draws a population of persons on the scene
    '''
    # Background
    scene.fill(constants.BACKGROUND_COLOR)
    # Drawing all the people
    for p in persons:
        # one disk per person
        pygame.draw.circle(scene, constants.PALETTE[p[2]], ((int)(p[0]), (int)(p[1])), constants.PERSON_RADIUS)
        # if the person is infected, we draw their infectionTTL
        if p[2] == constants.INFECTED:
            ttlText = font.render(str(p[3]), True, (255, 255, 255), constants.PALETTE[p[2]])
            ttlRect = ttlText.get_rect()
            ttlRect.center = ((int)(p[0]), (int)(p[1]))
            scene.blit(ttlText, ttlRect)



def display_final_state(persons):
    '''
    Displays various statistics about the simulation
    '''
    healthy=0
    infected=0
    immune=0

    for p in persons:
        if(p[2] == constants.HEALTHY):
            healthy+=1
        if(p[2]== constants.INFECTED):
            infected+=1
        if(p[2]==constants.IMMUNE):
            immune+=1
    
    
    print("A la fin de la simulation, pour une population de", constants.POPULATION_SIZE,"personnes, il y a :")
    print("-",healthy, "personnes en bonne santé, soit",healthy*100/constants.POPULATION_SIZE,"%")
    print("-",infected, "personnes infectées, soit",infected*100/constants.POPULATION_SIZE,"%")
    print("-",immune, "personnes guéries, soit",immune*100/constants.POPULATION_SIZE,"%")
            

            
if __name__ == '__main__':
    # Program initialization
    random.seed(constants.SEED)
    persons = engine.createPopulation()
    endSimulation = False
    frameNumber = 0
    startTime = time.time()
    
    # pygame initialization
    pygame.init()
    pygame.display.set_caption('Covid Simulator')
    clock = pygame.time.Clock()
    scene = pygame.display.set_mode((constants.SCENE_WIDTH, constants.SCENE_HEIGHT))
    font = pygame.font.Font(None, 14)

        

    # main loop
    while not endSimulation:
                     
        for j in range (0, len(persons)):
            # update of the person : direction and health state
            engine.update(persons[j])
            
            # find collisions between persons
            colls = engine.computeCollisions(persons,j)

            # contaminated persons infect healthy persons
            engine.processCollisions(persons, colls)

            # display update
            deltaTime = clock.tick()
            pygame.display.update()
        frameNumber += 1
            # time.sleep(0.2)
        # draw scene
        draw(scene,font,persons)

                

        # end if there isn't infected person
        endSimulation = engine.endSimulation(persons)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endSimulation = True
        

    endTime = time.time()
    # print average FPS
    print("FPS moyen durant la simulation :", frameNumber / (endTime - startTime))
    print()

    # print statistics about persons
    display_final_state(persons)
    
    pygame.quit()
