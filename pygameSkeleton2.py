import pygame
import sys

#function for rescaling - crop surface of goalLeft
def cropSurface(newWidth,newHeight,cropWidth,cropHeight,image):
    newSurf = pygame.Surface((newWidth,newHeight),
    pygame.SRCALPHA,32)

    newSurf.blit(image,(0,0),(cropWidth,cropHeight,newWidth,newHeight))
    return newSurf



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



foot = pygame.image.load("characterFoot.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot,(footWidth*rescaleFactor,footHeight*rescaleFactor))
foot = pygame.transform.rotate(foot,90)



rescaleBall = 2
ball = pygame.image.load("ball.png").convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(ball,(ballWidth*rescaleBall,ballHeight*rescaleBall))



goalLeft = pygame.image.load("goalLeft.png").convert_alpha()
goalLeft = pygame.transform.scale(goalLeft,(250,270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
adjust = 12
goalLeft = cropSurface(goalLeftWidth/2+adjust,goalLeftHeight/2+adjust,goalLeftWidth/2-adjust,goalLeftHeight/2-adjust,goalLeft)



goalMiddle = pygame.image.load("goalMiddle.png").convert_alpha() #convert.alpha takes care of extra image you dont want
goalMiddle = pygame.transform.scale(goalMiddle,(250,270)) #size of goal
goalMiddleHeight = goalMiddle.get_rect().height
goalMiddleWidth = goalMiddle.get_rect().width
goalMiddle = cropSurface(goalMiddleWidth,goalMiddleHeight/2+adjust,0,goalMiddleHeight/2-adjust,goalMiddle)




goalRight = pygame.image.load("goalRight.png").convert_alpha()
goalRight = pygame.transform.scale(goalRight,(250,270))
goalRightWidth = goalRight.get_rect().width
goalRightHeight = goalRight.get_rect().height

goalRight = cropSurface(goalRightWidth/2+adjust,goalRightHeight/2+adjust,0,goalRightHeight/2-adjust,goalRight)

goalStart = (width-goalLeft.get_rect().width-goalMiddle.get_rect().width-goalRight.get_rect().width)/2

screen.blit(goalLeft,(goalStart,0))
screen.blit(goalMiddle,(goalStart+goalLeft.get_rect().width,0))
screen.blit(goalRight,(goalStart+goalLeft.get_rect().width+goalMiddle.get_rect().width,0))

playerX = width/2
playerY = 530

screen.blit(player,(playerX-player.get_rect().width/2,playerY-player.get_rect().height/2))

ballX = width/2
bally = 450

#the foot will only show when the action of kicking is activated.
screen.blit(foot,(0,0))
screen.blit(ball,(ballX-ball.get_rect().width/2,bally-ball.get_rect().width/2))



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