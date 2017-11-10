import pygame ,sys , time
from pygame.locals import *
#pygame start
pygame.init()

#window setup
WindowWidth = 400
WindowHeight = 400
WindowSurface = pygame.display.set_mode((WindowWidth,WindowHeight),0,32)

#setup Direction variable

DownLeft = 1
DownRight = 3
UpLeft = 7
UpRight = 9
MoveSpeed = 4

#set up the colors

Black = (0,0,0)
Red = (255,0,0)
Green = (0,225,0)
Blue = (0,0,225)

#set up block data structure

b1 = {'rect':pygame.Rect(300,80,50,100), 'color':Red, 'dir':UpRight}
b2 = {'rect':pygame.Rect(200,200,20,20), 'color':Green, 'dir':UpLeft}
b3 = {'rect':pygame.Rect(100,150,60,60), 'color':Blue, 'dir':DownLeft}
blocks = [b1 ,b2, b3]

#run the game loop
while True:
    #check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Draw the black background onto the surface
    WindowSurface.fill(Black)

    for b in blocks:
        #lets move the blocks
        if b['dir'] == DownLeft:
            b['rect'].left -= MoveSpeed
            b['rect'].top += MoveSpeed
        if b['dir'] == DownRight:
            b['rect'].left += MoveSpeed
            b['rect'].top += MoveSpeed
        if b['dir'] == UpLeft:
            b['rect'].left -= MoveSpeed
            b['rect'].top -= MoveSpeed
        if b['dir'] == UpRight:
            b['rect'].left += MoveSpeed
            b['rect'].top -= MoveSpeed
        #check if the blocks moved out of the window

        if b['rect'].top <0:
            #block has moved out of the top
            if b['dir'] == UpLeft:
                b['dir'] = DownLeft
            if b['dir'] == UpRight:
                b['dir'] = DownRight
            #block has moved out of the bottom
        if b['rect'].bottom > WindowHeight:
            if b['dir'] == DownLeft:
                b['dir'] = UpLeft
            if b['dir'] == DownRight:
                b['dir'] = UpRight
        if b['rect'].left <0:
            if b['dir'] == DownLeft:
                b['dir'] = DownRight
            if b['dir'] == UpLeft:
                b['dir'] = UpRight
        if b['rect'].right > WindowWidth:
            if b['dir'] == DownRight:
                b['dir'] = DownLeft
            if b['dir'] == UpRight:
                b['dir'] = UpLeft
        #draw the blocks
        pygame.draw.rect(WindowSurface,b['color'],b['rect'])
    pygame.display.update()
    time.sleep(0.02)









    pygame.display.update()
    time.sleep(0.02)
