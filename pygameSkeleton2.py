import pygame
import sys

#can also do import pygame, sys
pygame.init()

width = 900
height = 700
screenDim = (width,height)

screen = pygame.display.set_mode(screenDim) #set_mode requires a tuple as input
pygame.display.set_caption("My First Game")

grassImage = pygame.image.load("grass.png").convert() #loading an image loads an image and sticks it onto a python object called a surface.
#convert makes the pixel values of the surface and the image the same.
#convert_alpha takes care of transparency around the image so you see the object on the screen image but not the rest of the image rectangle.
grassImage = pygame.transform.scale(grassImage,(width,height)) #this will transform the image to the size of our window

#to get it onto the screen
screen.blit(grassImage,(0,0)) #blit takes input of surface and coordinates.
#image is still not sclaed to size of window so we need to scale it.


rescaleFactor = 3
#to load the player
player = pygame.image.load("characterBody.png").convert_alpha()
playerWidth = player.get_rect().width #go into surface, get recatngle surface, and look at width
playerHeight = player.get_rect().height #no parentheses for width and height as they are variables not functions
player = pygame.transform.scale(player,(playerWidth*rescaleFactor,playerHeight*rescaleFactor))
player = pygame.transform.rotate(player,90)
screen.blit(player,(0,0))
foot = pygame.image.load("characterFoot.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot,(footWidth*rescaleFactor,footHeight*rescaleFactor))

foot = pygame.transform.rotate(foot,90)
screen.blit(foot,(0,0))

rescaleBall = 2
ball = pygame.image.load("ball.png").convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(ball,(ballWidth*rescaleBall,ballHeight*rescaleBall))

screen.blit(ball,(0,0))

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