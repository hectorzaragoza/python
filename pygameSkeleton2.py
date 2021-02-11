import pygame
import sys
import math

#Creating a Game Class
class Game:
    def __init__(self,screen,screenDimensions):
        self.fps = 30
        self.screenDimensions = screenDimensions
        self.frame = pygame.time.Clock()
        self.screen = screen

    def updateFrame(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

class Background(Game): #loading background images and setting them up.
    def __init__(self,screen,screenDimensions):
        Game.__init__(self,screen,screenDimensions)
        self.goalLeft = None #None is a value of none...
        self.goalMiddle = None
        self.goalRight = None
        self.adjust = 12
        self.grassImage = None

    def loadGrass(self,name):
        self.grassImage = pygame.image.load(name).convert()
        self.grassImage = pygame.transform.scale(self.grassImage,self.screenDimensions)

    def cropSurface(self,newWidth,newHeight,cropWidth,cropHeight,image):
        newSurf = pygame.Surface((newWidth,newHeight),
        pygame.SRCALPHA,32)
        newSurf.blit(image,(0,0),(cropWidth,cropHeight,newWidth,newHeight))
        return newSurf

    def loadGoalLeft(self,name):
        self.goalLeft = pygame.image.load(name).convert_alpha()
        self.goalLeft = pygame.transform.scale(goalLeft,(250,270))
        goalLeftWidth = self.goalLeft.get_rect().width
        goalLeftHeight = self.goalLeft.get_rect().height
        self.goalLeft = cropSurface(goalLeftWidth/2+self.adjust,goalLeftHeight/2+self.adjust,goalLeftWidth/2-self.adjust,goalLeftHeight/2-self.adjust,self.goalLeft)

    def loadGoalMiddle(self,name):
        self.goalMiddle = pygame.image.load(name).convert_alpha() #convert.alpha takes care of extra image you dont want
        self.goalMiddle = pygame.transform.scale(self.goalMiddle,(250,270)) #size of goal
        goalMiddleHeight = self.goalMiddle.get_rect().height
        goalMiddleWidth = self.goalMiddle.get_rect().width
        self.goalMiddle = cropSurface(goalMiddleWidth,goalMiddleHeight/2+self.adjust,0,goalMiddleHeight/2-self.adjust,self.goalMiddle)

    def loadGoalRight(self,name):
        self.goalRight = pygame.image.load(name).convert_alpha()
        self.goalRight = pygame.transform.scale(self.goalRight,(250,270))
        goalRightWidth = self.goalRight.get_rect().width
        goalRightHeight = self.goalRight.get_rect().height
        self.goalRight = cropSurface(goalRightWidth/2+self.adjust,goalRightHeight/2+self.adjust,0,goalRightHeight/2-self.adjust,self.goalRight)

    def setStart(self):
        self.goalStart = (self.screenDimensions[0]-self.goalLeft.get_rect().width-self.goalMiddle.get_rect().width-self.goalRight.get_rect().width)/2

    def blitBackground(self):
        self.screen.blit(self.goalLeft,(self.goalStart,0))
        self.screen.blit(self.goalMiddle,(self.goalStart+goalLeft.get_rect().width,0))
        self.screen.blit(self.goalRight,(self.goalStart+self.goalLeft.get_rect().width+self.goalMiddle.get_rect().width,0))

class Ball(Game):
    def __init__(self,screen,screenDimensions):
        Game.__init__(self,screen,screenDimensions)
        self.ballX = self.screenDimensions[0]/2
        self.bally = 450
        self.ball = None

    def loadBall(self,name,rescaleBall):
        self.ball = pygame.image.load(name).convert_alpha()
        ballWidth = self.ball.get_rect().width
        ballHeight = self.ball.get_rect().height
        self.ball = pygame.transform.scale(self.ball,(ballWidth*rescaleBall,ballHeight*rescaleBall))

    def blitBall(self):
        self.screen.blit(self.ball,(self.ballX-self.ball.get_rect().width/2,self.bally-self.ball.get_rect().height/2))

    def setKickDirection(self,playerX,playerY):
        xMove = (playerX-self.ballX)/10
        yMove = (playerY-self.bally)/10
        normMove = 1/math.sqrt(xMove**2+yMove**2)
        self.ballXDirection = xMove*normMove
        self.ballYDirection = yMove*normMove
    
    def kickBall(self):
        self.ballX -= speed*self.ballXDirection
        self.bally -= speed*self.ballYDirection

class Player(Game):
    def __init__(self,screen,screenDimensions):
        Game.__init__(self,screen,screenDimensions)
        self.player = None
        self.playerStart = self.player
        self.foot = None
        self.footStart = self.foot
        self.playerX = self.screenDimensions[0]/2
        self.playerY = 530
        self.playerXOriginal = self.playerX
        self.playerYOriginal = self.playerY
        self.footX = None
        self.footY = None
        self.currentRotation = 0
        self.radius = 80
        self.deltaTheta = int(90/(self.radius/5))

    def loadPlayer(self,name,rescale):
        self.player = pygame.image.load(name).convert_alpha()
        playerWidth = self.player.get_rect().width
        playerHeight = self.player.get_rect().height
        self.player = pygame.transform.scale(self.player,
                                        (playerWidth*rescale,
                                         playerHeight*rescale))
        self.player = pygame.transform.rotate(self.player,90)
        self.playerStart = self.player

    def loadFoot(self,name,rescale):
        self.foot = pygame.image.load(name).convert_alpha()
        footWidth = self.foot.get_rect().width
        footHeight = self.foot.get_rect().height
        self.foot = pygame.transform.scale(self.foot,
                                      (footWidth*rescale,
                                       footHeight*rescale))
        self.foot = pygame.transform.rotate(self.foot,90)
        self.footStart = self.foot

    def rotatePlayer(self,angle):
        self.player = pygame.transform.rotate(self.playerStart,angle)

    def rotateFoot(self,angle):
        self.foot = pygame.transform.rotate(self.footStart,angle)

    def movePlayer(self,direction):
        if direction == "Left":
            self.deltaTheta *= -1 #deltaTheta * -1

        finalRot = (self.currentRotation+self.deltaTheta)*math.pi/180
        
        Hypotenuse = (self.radius*math.sin(finalRot)/
                      (math.sin((math.pi-finalRot)/2)))

        changeX = Hypotenuse*math.cos(math.pi/2-(math.pi-finalRot)/2)
        changeY = Hypotenuse*math.sin(math.pi/2-(math.pi-finalRot)/2)


        self.currentRotation = self.currentRotation + self.deltaTheta
        self.player = pygame.transform.rotate(self.playerStart,self.currentRotation)
        self.playerX = self.playerXOriginal + changeX
        self.playerY = self.playerYOriginal - changeY
        
        if direction == "Left":#revert
            self.deltaTheta *= -1 
               
    def blitPlayer(self):
        self.screen.blit(self.player,(self.playerX-self.player.get_rect().width/2,
                    self.playerY-self.player.get_rect().height/2))
        
    def blitFoot(self):
        self.screen.blit(self.foot,(self.footX - self.foot.get_rect().width/2,
                          self.footY - self.foot.get_rect().height/2))

    def playerShoot(self,ballX,ballY):
        xMove = (self.playerX-ballX)/10
        yMove = (self.playerY-ballY)/10
        self.playerX -= xMove
        self.playerY -= yMove

    def positionFoot(self,ballX,ballY):
        xMove = (self.playerX-ballX)/10
        yMove = (self.playerY-ballY)/10
        normMove = 1/math.sqrt(xMove**2+yMove**2)
        distanceToShoulder = 20
        shoulderAngle = self.currentRotation*math.pi/180

        self.footX = (self.playerX +
                 distanceToShoulder*math.cos(shoulderAngle)-
                 20*xMove*normMove)
        self.footY = (self.playerY -
                 distanceToShoulder*math.sin(shoulderAngle)-
                 20*yMove*normMove)
        self.foot = pygame.transform.rotate(self.footStart,self.currentRotation)

#function for rescaling - crop surface of goalLeft
def cropSurface(newWidth,newHeight,cropWidth,cropHeight,image):
    newSurf = pygame.Surface((newWidth,newHeight),
    pygame.SRCALPHA,32)

    newSurf.blit(image,(0,0),(cropWidth,cropHeight,newWidth,newHeight))
    return newSurf

def movePlayer(direction,radius,absRot): #absRot is current position
    yChange = 5
    deltaTheta = int(90/(radius/yChange)) #angle stepsize
    if direction == "Left":
        deltaTheta *= -1 #this is deltaTheta = deltaTheta * -1
    
    finalRot = (absRot+deltaTheta)*math.pi/180

    Hypotenuse = (radius*math.sin(finalRot)/(math.sin((math.pi-finalRot)/2)))

    newX = Hypotenuse*math.cos(math.pi/2-(math.pi-finalRot)/2)
    newY = Hypotenuse*math.sin(math.pi/2-(math.pi-finalRot)/2)

    return newX, newY, absRot + deltaTheta


def UpdateFrameImages(showFoot = False): #creeating this function to refresh frame images more easily by calling funciton instead of entire code
    global screen, grassImage,goalLeft,goalMiddle,goalRight,ball,player
    global goalStart,ballX,bally,playerX,playerY
    screen.blit(grassImage,(0,0))
    screen.blit(goalLeft,(goalStart,0))
    screen.blit(goalMiddle,(goalStart+goalLeft.get_rect().width,0))
    screen.blit(goalRight,(goalStart+goalLeft.get_rect().width+goalMiddle.get_rect().width,0))
    if showFoot:
        global foot, footX, footY
        screen.blit(foot,(footX-foot.get_rect().width/2,footY-foot.get_rect().width/2))
    screen.blit(ball,(ballX-ball.get_rect().width/2,bally-ball.get_rect().width/2))
    screen.blit(player,(playerX-player.get_rect().width/2,playerY-player.get_rect().height/2))

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
playerStart = player #THis is going to be our default reference for the player.

currentRotation = 0



foot = pygame.image.load("characterFoot.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot,(footWidth*rescaleFactor,footHeight*rescaleFactor))
foot = pygame.transform.rotate(foot,90)
footStart = foot


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


goalHeight = goalLeft.get_rect().height

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

playerXOriginal=playerX
playerYOriginal=playerY
screen.blit(player,(playerX-player.get_rect().width/2,playerY-player.get_rect().height/2))

ballX = width/2
bally = 450

radius = playerY - bally #radius between ball and player
#the foot will only show when the action of kicking is activated.
screen.blit(foot,(0,0))
screen.blit(ball,(ballX-ball.get_rect().width/2,bally-ball.get_rect().width/2))




#defining frame rate
frame = pygame.time.Clock()

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
#Processing Actions of Pressing Keys and Pass Statemnet
#What do we want the images to do when we interact with keyboard
#So, we need to process the keyboard keys
    pressedKeys = pygame.key.get_pressed()
    #pressedKeys = [False, False, False,...,True,False,...] This is going through the values of all the keys
    print(pygame.K_LEFT, pressedKeys[pygame.K_LEFT],pressedKeys[pygame.K_RIGHT],pressedKeys[pygame.K_SPACE])
    if pressedKeys[pygame.K_LEFT] == 1:
        if currentRotation > -90:
            changeX, changeY, currentRotation = movePlayer("Left",radius,currentRotation)
            player = pygame.transform.rotate(playerStart,currentRotation)
            playerX = playerXOriginal + changeX
            playerY = playerYOriginal - changeY
        #== 1 is true so Left key has been pressed
        #pass #this pass statement lets us move beyond this code, so it does nothing. But, pass statement lets you build code structure but you are not necessarily finishing it all
    elif pressedKeys[pygame.K_RIGHT] == 1:
        if currentRotation < 90:
            changeX, changeY, currentRotation = movePlayer("Right",radius,currentRotation)
            player = pygame.transform.rotate(playerStart,currentRotation)
            playerX = playerXOriginal + changeX
            playerY = playerYOriginal - changeY
        #move player right
        #pass
    elif pressedKeys[pygame.K_SPACE] == 1:
        xMove = (playerX-ballX)/10
        yMove = (playerY-bally)/10
        normMove = 1/math.sqrt(xMove**2+yMove**2)
        distanceToShoulder = 20
        shoulderAngle = currentRotation*math.pi/180
        for i in range(3):
            playerX -= xMove
            playerY -= yMove
            UpdateFrameImages()
            pygame.display.flip()
            frame.tick(30)
        footX = (playerX + distanceToShoulder*math.cos(shoulderAngle)-20*xMove*normMove)
        footY = (playerY - distanceToShoulder*math.sin(shoulderAngle)-20*yMove*normMove)
        foot = pygame.transform.rotate(footStart, currentRotation)
        UpdateFrameImages(True)
        pygame.display.flip()
        
        #xmove and ymove that define the x and y positions as we move towards the ball and updating position
        
        ballXDirection = xMove*normMove
        ballYDirection = yMove*normMove

        speed = 10

        while bally >= goalHeight:
            ballX -= speed*ballXDirection
            bally -= speed*ballYDirection
            UpdateFrameImages()
            pygame.display.flip()
            frame.tick(30)
        #frame.tick(1) this pause here would apply only to SPace pressing
    #the following line will refresh the player image given keyboard movement functions.
    UpdateFrameImages()

    pygame.display.flip() #update method/load next frame
    frame.tick(30) #Desired FPS, if we put 30, we will never go above 30 FPS

#pygame.quit()