import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    
    screen=pygame.display.set_mode((500,400))
    
    y=40
    x=210
    while(1):
        screen.fill((255,120,155))
        
        pygame.draw.rect(screen,(40,40,255),Rect(x,200,100,100))
        pygame.draw.rect(screen,(250,150,30),Rect(235,y,30,30))
        pygame.draw.rect(screen,(200,200,100),Rect(200,y,20,50))
        
        x=x+1
        
        if x>=380:
            x=10
        
        if y>=480:
            y=10
        
        y=y+1
        
        for event in pygame.event.get():
            if(event.type==QUIT):
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

if(__name__=='__main__'):
    main()