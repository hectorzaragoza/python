import pygame
import sys

#can also do import pygame, sys
pygame.init()

width = 900
height = 700
screenDim = (width,height)

screen = pygame.display.set_mode(screenDim) #set_mode requires a tuple as input
pygame.display.set_caption("Prince of Persia")

finished = False
while finished != True: #while the game is not finished = False, continue into the for loops
    #processing all the events
    for event in pygame.event.get(): #This will process the series of event1, event2,...
    #do appropriate things the events
        if event.type == pygame.QUIT: #you can find what things are inside libraries by looking into documentation and what you can do with them.
            finished = True
        #in this case, event has a property called type
            pygame.quit()
            sys.exit() #this ends python at this line.

    pygame.display.flip() #update method/load next frame

#pygame.quit()