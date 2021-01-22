import pygame
pygame.init()


width = 900
height = 700
screenDimension = (width,height)

screen = pygame.display.set_mode(screenDimension)
pygame.display.set_caption("Exercise One")




finished = False
while finished != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit()
    pygame.display.flip()