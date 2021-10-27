import pygame
import random
import sys
from pygame.locals import *

def main():
    pygame.init()
    
    screen=pygame.display.set_mode((960,720))

    font = pygame.font.Font(None,40)
    
    ck = pygame.time.Clock()

    point = [250,300,100,50,-100,120,80,-300]
    sizes = [(100,100),(100,100),(100,60),(100,100),(40,100),(100,100),(100,100),(100,100)]
    speed = [1,1,2,2,3,2,3,4]

    bowl = pygame.image.load("bowl.png").convert_alpha()
    pics = [
        pygame.image.load("noodles.png").convert_alpha(),   #麺
        pygame.image.load("pork.png").convert_alpha(),      #チャーシュー
        pygame.image.load("menma.png").convert_alpha(),     #メンマ
        pygame.image.load("leek1.png").convert_alpha(),     #ネギ
        pygame.image.load("leek2.png").convert_alpha(),     #ネギ2
        pygame.image.load("egg.png").convert_alpha(),       #卵
        pygame.image.load("naruto.png").convert_alpha(),    #ナルト
        pygame.image.load("spider.png").convert_alpha(),    #虫
    ]

    y=40
    x=210

    pos = list([])
    count = 0
    score = 0
    
    cx = random.randint(100,300)
    cy = random.randint(0,100)

    flag = False

    dif = 100
    difcount = 0

    while(1):
        ck.tick(60)
        count = count + 1

        if(count >= dif):
            pos.append(( random.randint(180,460),random.randint(0,100),random.randint(0,7)))
            pos.append(( random.randint(500,780),random.randint(0,100),random.randint(0,7)))
            count = 0
            difcount += 1
            if(difcount == 10):
                dif -= 1
                difcount = 0
            
        
        screen.fill((255,255,255))
        
        screen.blit(bowl,Rect(x,520,100,100))
        #pygame.draw.rect(screen,(200,200,100),Rect(200,y,20,50))

        for i in range(0,len(pos)):
            j = len(pos) - i - 1
            num = pos[j][2]
            screen.blit(pics[num],Rect(pos[j][0],pos[j][1],sizes[num][0],sizes[num][1]))
            pos[j] = (pos[j][0],pos[j][1] + speed[num] ,pos[j][2])

            if((pos[j][1] > 540) and (x < pos[j][0] < (x + 200 - sizes[num][0]))):
                score += point[num]
                del pos[j]
        
        scoreTxt = font.render(str(score),True,(0,0,0))
        screen.blit(scoreTxt,[10,20])
        
        for event in pygame.event.get():
            if(event.type==QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == MOUSEMOTION):
                x,y = event.pos
                x = x - 100
            if(event.type == MOUSEBUTTONDOWN):
                flag = True
        
        pygame.display.update()

if(__name__=='__main__'):
    main()