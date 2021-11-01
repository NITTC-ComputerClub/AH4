from math import e
from os import times
import pygame
import random
import sys
from pygame.locals import *

name_list = list()
score_list = list()
data_list = list()

def main():
    global name_list,score_list,data_list
    pygame.init()
    pygame.mixer.init()
    
    screen=pygame.display.set_mode((960,720))
    pygame.display.set_caption("ラーメン作るのあきラーメン")

    font = pygame.font.Font(None,40)
    
    ck = pygame.time.Clock()

    point = [250,300,100,50,-100,120,80,-300]
    sizes = [(100,100),(100,100),(100,60),(100,100),(40,100),(100,100),(100,100),(100,100)]
    speed = [1,1,2,2,3,2,3,4]

    sound1 = pygame.mixer.Sound("music/itadaki.wav")
    
    bowl = pygame.image.load("image/bowl.png").convert_alpha()
    pics = [
        pygame.image.load("image/noodles.png").convert_alpha(),   #麺
        pygame.image.load("image/pork.png").convert_alpha(),      #チャーシュー
        pygame.image.load("image/menma.png").convert_alpha(),     #メンマ
        pygame.image.load("image/leek1.png").convert_alpha(),     #ネギ
        pygame.image.load("image/leek2.png").convert_alpha(),     #ネギ2
        pygame.image.load("image/egg.png").convert_alpha(),       #卵
        pygame.image.load("image/naruto.png").convert_alpha(),    #ナルト
        pygame.image.load("image/spider.png").convert_alpha(),    #虫
    ]
    readRankingFile()

    y=40
    x=210

    pos = list([])
    count = 0
    score = 0
    
    cx = random.randint(100,300)
    cy = random.randint(0,100)

    isMenu = True
    isRanking = False

    dif = 100
    difcount = 0

    fps = 60
    fpscount = 0

    times = 30

    while(1):
        ck.tick(fps)
        fpscount += 1
        count += 1
        
        for event in pygame.event.get():
            if(event.type==QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == MOUSEMOTION):
                x,y = event.pos
                x = x - 100
            if(event.type == MOUSEBUTTONDOWN):
                flag = True
            if(event.type == KEYDOWN):
                if(event.key == K_SPACE):
                    if(isMenu):
                        isMenu = False
                        isRanking = False
                    elif(isRanking):
                        times = 30
                        isMenu = True
                        isRanking = False
                elif(event.key == K_r and isMenu):
                    isRanking = True
                    isMenu = False
        screen.fill((255,255,255))

        if(isRanking):
            showRanking(screen)
            pygame.display.update()
            continue

        if(isMenu):
            Menu(screen)
            pygame.display.update()
            continue
        
        if(times <= 0):
            writeRainking("",score)
            sound1.play()
            readRankingFile()
            isMenu = False
            isRanking = True
            score = 0
            time = 30
            dif = 100
            difcount = 0
            fpscount = 0
            pos = list()
        

        if(count >= dif):
            pos.append(( random.randint(180,460),random.randint(0,100),random.randint(0,7)))
            pos.append(( random.randint(500,780),random.randint(0,100),random.randint(0,7)))
            count = 0
            difcount += 1
            if(difcount == 10):
                dif -= 1
                difcount = 0
        
        if(fpscount >= fps):
            times -= 1
            fpscount = 0
        
        plus = ":"
        if(times % 60 < 10):
            plus = ":0"
        t = str(times // 60) + plus + str(times % 60)
        time = font.render(t,True,(0,0,0) )
        screen.blit(time,[20,80])

        screen.blit(bowl,Rect(x,520,100,100))
        #pygame.draw.rect(screen,(200,200,100),Rect(200,y,20,50))

        for i in range(0,len(pos)):
            j = len(pos) - i - 1
            num = pos[j][2]
            screen.blit(pics[num],Rect(pos[j][0],pos[j][1],sizes[num][0],sizes[num][1]))
            pos[j] = (pos[j][0],pos[j][1] + speed[num] ,pos[j][2])

            if((640 > pos[j][1] > 540) and (x < pos[j][0] < (x + 200 - sizes[num][0]))):
                score += point[num]
                del pos[j]
        
        scoreTxt = font.render(str(score),True,(0,0,0))
        screen.blit(scoreTxt,[20,30])
        
        pygame.display.update()

def showRanking(screen):
    global name_list,score_list,data_list

    font = pygame.font.Font("font/sjis_sp_setofont.ttf",40)
    font2 = pygame.font.Font("font/sjis_sp_setofont.ttf",64)
    font3 = pygame.font.Font("font/sjis_sp_setofont.ttf",30)
    rank = font2.render("ランキング",True,(0,0,0))
    screen.blit(rank,[360,60])
    
    for i in range(3):
        num = score_list[i][1]
        text = name_list[num] + "           " + str(score_list[i][0])
        txt = font.render(text,True,(0,0,0))
        screen.blit(txt,[280,140 + 50 * i])

    #result = pygame.image.load("").convert_alpha()

    space = font3.render("Spaceキーを押してメニューに戻る",True,(0,0,0))
    screen.blit(space,[480,600])

def readRankingFile():
    global name_list,score_list,data_list
    file = open("data/Ranking.csv",mode="r")

    lines = file.read()
    count = 0
    for line in lines.split("\n"):
        data = line.split(',')
        if(count == 0):
            count += 1
            continue

        name_list.append(data[0])
        score_list.append([int(data[1]),count - 1])
        data_list.append(data[2])
        count += 1
    
    score_list.sort(reverse=True)

def writeRainking(name, score):
    file = open("data/Ranking.csv",mode="a")

    csv = "\nguests" + "," + str(score) + ",0"

    file.write(csv)


def Menu(screen):
    screen.fill((255,255,255))

    font1 = pygame.font.Font("font/sjis_sp_setofont.ttf",64)
    font2 = pygame.font.Font("font/sjis_sp_setofont.ttf",40)
    
    title = font1.render("ラーメン作るのあきラーメン",True,(0,0,0))
    screen.blit(title,[150,250])

    space = font2.render("SPACEキーを押してゲームをスタート",True,(0,0,0))
    screen.blit(space,[200,450])

    rank = font2.render("Rキーでランキング",True,(0,0,0))
    screen.blit(rank,[280,550])

if(__name__=='__main__'):
    main()