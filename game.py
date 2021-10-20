import pygame
import random
import sys
from pygame.locals import *

def main():
    pygame.init()
    
    screen=pygame.display.set_mode((500,400))
    
    ck = pygame.time.Clock()


    y=40
    x=210

    pos = [(20, 400), (100, 150), (40, 200), (0, 10)]
    
    cx = random.randint(100,300)
    cy = random.randint(0,100)

    flag = False

    while(1):
        ck.tick(60)
        
        if(flag):
            cx = random.randint(100,300)
            cy = random.randint(0,100)
            flag = False

        screen.fill((255,255,255))
        
        pygame.draw.rect(screen,(40,40,255),Rect(x,200,100,100))
        pygame.draw.rect(screen,(250,150,30),Rect(cx,cy,30,30))
        #pygame.draw.rect(screen,(200,200,100),Rect(200,y,20,50))

        for p in pos:
            pygame.draw.rect(screen,(250,150,30),Rect(p[0],p[1],30,30))
        
        for i in range(0,len(pos)):
            pos[i] = (pos[i][0],pos[i][1] + 1)
        
        
        if x>=380:
            x=10
        
        if y>=480:
            y=10
        
        y=y+1
        
        for event in pygame.event.get():
            if(event.type==QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == MOUSEMOTION):
                x,y = event.pos
                x = x - 50
            if(event.type == MOUSEBUTTONDOWN):
                flag = True

        
        pygame.display.update()

if(__name__=='__main__'):
    main()