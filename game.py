import pygame
import random
import sys
from pygame.locals import *

def main():
    pygame.init()
    
    screen=pygame.display.set_mode((500,400))

    font = pygame.font.Font(None,40)
    
    ck = pygame.time.Clock()

    point = [100,200,400]
    color = [(255,150,30),(0,255,0),(0,0,255)]
    sizes = [(30,30),(30,60),(60,30)]

    y=40
    x=210

    pos = list([])
    count = 0
    score = 0
    
    cx = random.randint(100,300)
    cy = random.randint(0,100)

    flag = False

    while(1):
        ck.tick(60)
        count = count + 1

        if(count == 90):
            pos.append(( random.randint(100,300),random.randint(0,100),random.randint(0,2)))
            count = 0
        
        screen.fill((255,255,255))
        
        pygame.draw.rect(screen,(40,40,255),Rect(x,300,100,100))
        #pygame.draw.rect(screen,(200,200,100),Rect(200,y,20,50))

        for i in range(0,len(pos)):
            j = len(pos) - i - 1
            num = pos[j][2]
            pygame.draw.rect(screen,color[num],Rect(pos[j][0],pos[j][1],sizes[num][0],sizes[num][1]))
            pos[j] = (pos[j][0],pos[j][1] + 1,pos[j][2])

            if((pos[j][1] > 300) and (x < pos[j][0] < (x + 100 - sizes[num][0]))):
                score += point[num]
                del pos[j]
        
        scoreTxt = font.render(str(score),True,(0,0,0))
        screen.blit(scoreTxt,[10,20])
        
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