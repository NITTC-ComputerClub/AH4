import pygame
import sys
import random
import math
from pygame import mouse
from pygame.locals import *

def main():
    #pygameを使用するための文(必須)
    pygame.init()
    #画面を作成
    screen = pygame.display.set_mode((500,400))

    #マウスの位置変数
    mouseX = 40
    mouseY = 360

    #玉の位置変数
    pointX = random.randint(30,470)
    pointY = random.randint(30,200)
    #玉の速度の角度
    velAngle = random.randint(0,360)

    while(1):
        #玉の速度変数
        pointVelX = math.cos(math.radians(velAngle))
        pointVelY = math.sin(math.radians(velAngle))

        #玉を移動させる
        pointX = pointX + pointVelX / 10
        pointY = pointY + pointVelY / 10

        #玉が左右の線についたら跳ね返す
        if((pointX < 20) or (pointX > 480)):
            velAngle = 360 - velAngle
        #玉が上の線についたら跳ね返す
        if(pointY < 20):
            velAngle = -velAngle - 180
            if(velAngle > 360):
                velAngle = velAngle - 360

        #画面を白で塗りつぶす
        screen.fill((255,255,255))

        #黒い枠を書く
        pygame.draw.rect(screen,(0,0,0),Rect(20,20,460,360))
        #↑は中も塗りつぶされるので白で中を塗りつぶして枠にする
        pygame.draw.rect(screen,(255,255,255),Rect(22,22,456,356))
        #自分の板を描画
        pygame.draw.line(screen,(255,0,0),(mouseX - 20,mouseY),(mouseX + 20,mouseY),3)
        #玉の描画
        pygame.draw.circle(screen,(0,0,255),(pointX,pointY),5)

        #イベント(マウスクリックやマウスを動かしたときの処理)
        for event in pygame.event.get():
            #終了(右上の×ボタン)を押したとき
            if(event.type == QUIT):
                #pygameの終了
                pygame.quit()
                #プログラムの終了
                sys.exit()
            #マウスを動かしたときの処理
            if(event.type == MOUSEMOTION):
                #マウスの位置を取得
                mouseX,mouseY = event.pos
                #マウスの位置が枠外なら戻す、y位置を固定
                if(mouseX > 460):
                    mouseX = 460
                elif(mouseX < 40):
                    mouseX = 40
                mouseY = 360
        

        #画面を更新、これがないと画面が変化しない
        pygame.display.update()
if(__name__ == "__main__"):
    main()