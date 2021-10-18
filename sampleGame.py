import pygame
import sys
import random
import math
from pygame import mouse
from pygame.locals import *

point = 0

class board:
    def __init__(self,row,col,posx,posy):
        self.row = row
        self.col = col
        self.isDraw = True
        self.posx = posx
        self.posy = posy

    def delete(self):
        self.isDraw = False

    def draw(self,screen):
        if(self.isDraw):
            pygame.draw.line(screen,(0,255,0),(self.posx,self.posy),(self.posx + 70,self.posy),10)

    def collision(self,x,y,velx,vely,count):
        global point
        if(not(self.isDraw)):
            return (velx, vely, count)
        if((x > self.posx) and (x < self.posx + 70) and (y > self.posy - 5) and (y < self.posy + 5)):
            self.delete()
            setPoint(100)
            return (velx, -vely, count - 1)
        return (velx, vely, count)
        
def setPoint(add):
    global point
    point = point + add

        

def main():
    global point
    #pygameを使用するための文(必須)
    pygame.init()
    #画面を作成
    screen = pygame.display.set_mode((500,400))
    #タイマーを作成、フレームレートの固定に使用
    ck = pygame.time.Clock()

    #マウスの位置変数
    mouseX = 40
    mouseY = 360

    #スピードアップカウント、これが一定以上の値になったら
    speedUpCount = 0
    #
    boardCount = 25

    #玉の位置変数
    pointX = random.randint(30,470)
    pointY = random.randint(80,200)
    #玉の速度の角度
    velAngle = random.randint(0,360)
    #玉の速度変数
    pointVelX = math.cos(math.radians(velAngle))
    pointVelY = math.sin(math.radians(velAngle))

    #テキスト描画用のフォント作成
    font = pygame.font.Font(None,32)
    font2 = pygame.font.Font(None,24)

    isFinish = False

    boards = []
    for i in range(0,5):
        for j in range(0,3):
            boards.append(board(i,j,60 + i * 80,100 + j * 40))

    while(1):
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

        if(isFinish):
            continue

        #フレームレートを30に固定
        ck.tick(30)
        #カウントを増加
        speedUpCount = speedUpCount + 1

        #カウントが120以上なら速度を1.2倍しカウントを0にする
        if(speedUpCount > 120):
            pointVelX = pointVelX * 1.2
            pointVelY = pointVelY * 1.2
            speedUpCount = 0

        #玉を移動させる
        pointX = pointX + pointVelX * 4.2
        pointY = pointY + pointVelY * 4.2

        #玉が左右の線についたら跳ね返す
        if((pointX < 25) or (pointX > 475)):
            pointVelX = -pointVelX
        #玉が上の線についたら跳ね返す
        if(pointY < 85):
            pointVelY = -pointVelY

        if(pointY > 355):
            if((pointX > mouseX - 20) and (pointX < mouseX + 20)):
                pointVelY = -pointVelY

        for b in boards:
            (pointVelX, pointVelY, boardCount) = b.collision(pointX, pointY, pointVelX, pointVelY, boardCount)

        #時間経過で得点を増やす
        setPoint(1)

        #画面を白で塗りつぶす
        screen.fill((255,255,255))

        #黒い枠を書く
        pygame.draw.rect(screen,(0,0,0),Rect(20,80,460,300))
        #↑は中も塗りつぶされるので白で中を塗りつぶして枠にする
        pygame.draw.rect(screen,(255,255,255),Rect(22,82,456,296))
        #自分の板を描画
        pygame.draw.line(screen,(255,0,0),(mouseX - 20,mouseY),(mouseX + 20,mouseY),3)
        #玉の描画
        pygame.draw.circle(screen,(0,0,255),(pointX,pointY),5)

        score = font.render("score:" + str(point),True,(0,0,0))
        screen.blit(score,[350,40])

        #板を表示する
        for b in boards:
            b.draw(screen)
        
        #玉が下にいったらFinishを表示させる
        if(pointY > 400):
            txt = font.render("Finish.",True,(0,0,0))
            result = font.render(str(point),True,(255,0,0))
            screen.blit(txt,[225,200])
            screen.blit(result,[225,250])
            isFinish = True
        

        #画面を更新、これがないと画面が変化しない
        pygame.display.update()
if(__name__ == "__main__"):
    main()