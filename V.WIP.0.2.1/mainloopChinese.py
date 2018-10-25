import pygame
import sys

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("The Lost Memories")

icon = pygame.transform.scale(pygame.image.load('Game_spirite\\CG\\Loading.png'),(500,400))
icon.set_colorkey(icon.get_at((0,0)))

win.blit(icon,(0,50))

pygame.display.update()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

def dialog(string,color):
        font = pygame.font.Font('Game_Chinese_unicode_default\\NotoSansCJKtc-Medium.otf', 20)
        textsurface = font.render(string, False, color)
        text_canvas = pygame.transform.scale(pygame.image.load('Game_spirite\\Text_canvas\\Canvas1.jpg'),(500,100))
        text_canvas.set_colorkey(text_canvas.get_at((0,0)))
        win.blit(text_canvas,(0,400))
        win.blit(textsurface,(20,410))

def print_on_screen(string,color,delay_time=10):
        for i in range(len(string)):
                dialog(string[:(i+1)],color)
                pygame.display.update()
                pygame.time.delay(delay_time)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                                
                key = pygame.key.get_pressed()

                if key[pygame.K_SPACE]:
                        break

class block_object(object):
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def check(self,x,y):
                if self.x==x and self.y==y:
                        return True
                else:
                        return False
                
class game_obstacle(block_object):
        def __init__(self,touch,picture,x,y):
                super(game_obstacle,self).__init__(x,y)
                self.touch = touch
                self.picture = picture
        def check(self,x,y):
                touch = self.touch
                x1 = touch[0][0]
                y1 = touch[0][1]
                x2 = touch[1][0]
                y2 = touch[1][1]

                _check = []
                
                for i in range(x1,x2+10,10):
                        _check.append([i,y1])
                for i in range(y1+10,y2+10,10):
                        _check.append([x1,i])
                for i in range(y1+10,y2+10,10):
                        _check.append([x2,i])
                for i in range(x1+10,x2,10):
                        _check.append([i,y2])

                return [x,y] in _check
                        
        def winblit(self,x,y):
                win.blit(self.picture,(self.x-x,self.y-y,50,50))

bush_1_image = pygame.transform.scale(pygame.image.load('Game_spirite\\Object\\bush1.png').convert(),(100,100))
bush_1_image.set_colorkey(bush_1_image.get_at((0,0)))

shadow_picture = pygame.transform.scale(pygame.image.load('Game_spirite\\object\\shadow.png').convert(),(500,500))
shadow_picture.set_colorkey(shadow_picture.get_at((250,250)))

obstacle_full = []

obstacle = []

for i in range(200,1250,10):
        obstacle.append(block_object(i,150))
for i in range(160,1200,10):
        obstacle.append(block_object(200,i))
for i in range(160,1200,10):
        obstacle.append(block_object(1240,i))
for i in range(210,1240,10):
        if not(i==780 or i==790):
                obstacle.append(block_object(i,1190))
for i in range(1200,1290,10):
        obstacle.append(block_object(770,i))
        obstacle.append(block_object(800,i))
        
obstacle.append(block_object(780,1290))
obstacle.append(block_object(790,1290))
obstacle.append(game_obstacle([[670,720],[760,820]],bush_1_image,930,1000))
obstacle.append(game_obstacle([[370,520],[460,620]],bush_1_image,630,800))

obstacle_full.append(obstacle)

obstacle = []

for i in range(-10,260,10):
        obstacle.append(block_object(-250,i))
for i in range(-240,20,10):
        obstacle.append(block_object(i,250))
for i in range(-10,260,10):
        obstacle.append(block_object(20,i))

obstacle.append(block_object(-240,-20))
obstacle.append(block_object(-240,-30))
obstacle.append(block_object(-240,-40))
obstacle.append(block_object(-230,-50))
obstacle.append(block_object(-230,-60))
obstacle.append(block_object(-220,-70))
obstacle.append(block_object(-220,-80))
obstacle.append(block_object(-210,-90))
obstacle.append(block_object(-210,-100))
obstacle.append(block_object(-210,-110))
obstacle.append(block_object(-200,-120))
obstacle.append(block_object(-200,-130))
obstacle.append(block_object(-190,-140))
obstacle.append(block_object(-190,-150))
obstacle.append(block_object(-180,-160))
obstacle.append(block_object(-170,-170))
obstacle.append(block_object(-160,-180))
obstacle.append(block_object(-160,-190))
obstacle.append(block_object(-150,-200))
obstacle.append(block_object(-140,-210))
obstacle.append(block_object(-140,-200))
obstacle.append(block_object(-140,-190))
obstacle.append(block_object(-140,-180))
obstacle.append(block_object(-130,-170))
obstacle.append(block_object(-120,-170))
obstacle.append(block_object(-110,-170))
obstacle.append(block_object(-100,-170))
obstacle.append(block_object(-100,-180))
obstacle.append(block_object(-100,-190))
obstacle.append(block_object(-100,-200))
obstacle.append(block_object(-90,-210))
obstacle.append(block_object(-80,-200))
obstacle.append(block_object(-80,-190))
obstacle.append(block_object(-70,-180))
obstacle.append(block_object(-60,-170))
obstacle.append(block_object(-50,-160))
obstacle.append(block_object(-50,-150))
obstacle.append(block_object(-40,-140))
obstacle.append(block_object(-40,-130))
obstacle.append(block_object(-30,-120))
obstacle.append(block_object(-30,-110))
obstacle.append(block_object(-30,-100))
obstacle.append(block_object(-20,-90))
obstacle.append(block_object(-20,-80))
obstacle.append(block_object(-10,-70))
obstacle.append(block_object(-10,-60))
obstacle.append(block_object(0,-50))
obstacle.append(block_object(0,-40))
obstacle.append(block_object(0,-30))
obstacle.append(block_object(10,-20))

obstacle_full.append(obstacle)

obstacle = []

def find_obstacle(x,y,plot):
        global obstacle_full

        if plot==2:
                obstacle = obstacle_full[0]
        elif plot==5 or plot==8:
                obstacle = obstacle_full[1]
        else:
                raise Exception("Except plot status:"+str(plot))
                
        re = False

        for i in obstacle:
                re = re or i.check(x,y)
        return not re

class game_map(object):
        def __init__(self,scroll_x,scroll_y,picture):
                self.scroll_x = scroll_x
                self.scroll_y = scroll_y
                self.picture = picture
        def winblit(self,x,y):
                win.blit(self.picture,(self.scroll_x-x,self.scroll_y-y,50,50))

class game_player(object):
        def __init__(self,path,x,y,speed):
                self.x = x
                self.y = y
                self.speed = speed
                self.picture = []
                for i in range(4):
                        toAppend = []
                        for j in range(3):
                                if i==0:
                                        toAppend.append(pygame.transform.scale(pygame.image.load('Game_spirite\\Spirite\\up '+str(j+1)+'.png').convert(),(30,50)))
                                elif i==1:
                                        toAppend.append(pygame.transform.scale(pygame.image.load('Game_spirite\\Spirite\\down '+str(j+1)+'.png').convert(),(30,50)))
                                elif i==2:
                                        toAppend.append(pygame.transform.scale(pygame.image.load('Game_spirite\\Spirite\\left '+str(j+1)+'.png').convert(),(30,50)))
                                elif i==3:
                                        toAppend.append(pygame.transform.scale(pygame.image.load('Game_spirite\\Spirite\\right '+str(j+1)+'.png').convert(),(30,50)))
                        self.picture.append(toAppend)
                for i in range(4):
                        for j in range(3):
                                self.picture[i][j].set_colorkey(self.picture[i][j].get_at((0,0)))
                self.step_costume = [1,0]
        def check_key_pressed(self,key,plot):
                global step
                
                try:
                        step += 1
                except NameError:
                        step = 0
                
                if key[pygame.K_LEFT]:
                        if find_obstacle(self.x-self.speed,self.y,plot) :
                                self.x -= self.speed
                                if self.step_costume[0]==2:
                                        if self.step_costume[1]<=1:
                                                self.step_costume[1]+=1
                                        else:
                                                self.step_costume[1]=0
                                else:
                                        self.step_costume = [2,0]
                        else:
                                self.step_costume = [2,0]
                elif key[pygame.K_RIGHT]:
                        if find_obstacle(self.x+self.speed,self.y,plot) :
                                self.x += self.speed
                                if self.step_costume[0]==3:
                                        if self.step_costume[1]<=1:
                                                self.step_costume[1]+=1
                                        else:
                                                self.step_costume[1]=0
                                else:
                                        self.step_costume = [3,0]
                        else:
                                self.step_costume = [3,0]
                elif key[pygame.K_DOWN] :
                        if find_obstacle(self.x,self.y+self.speed,plot) :
                                self.y += self.speed
                                if self.step_costume[0]==1:
                                        if self.step_costume[1]<=1:
                                                self.step_costume[1]+=1
                                        else:
                                                self.step_costume[1]=0
                                else:
                                        self.step_costume = [1,0]
                        else:
                                self.step_costume = [1,0]
                elif key[pygame.K_UP] :
                        if find_obstacle(self.x,self.y-self.speed,plot) :
                                self.y -= self.speed
                                if self.step_costume[0]==0:
                                        if self.step_costume[1]<=1:
                                                self.step_costume[1]+=1
                                        else:
                                                self.step_costume[1]=0
                                else:
                                        self.step_costume = [0,0]
                        else:
                                self.step_costume = [0,0]
                else:
                        step -= 1
        def winblit(self):
                win.blit(self.picture[self.step_costume[0]][self.step_costume[1]],(250,250,50,50))

shadow = game_map(0,0,shadow_picture)

maps_full = []

maps = []

for i in range(0,4):
        toAppend = []
        for j in range(0,4):
                toAppend.append(game_map(j*500,i*500,pygame.transform.scale(pygame.image.load('Game_spirite\\Map\\slice_'+str(i)+'_'+str(j)+'.png').convert(),(500,500))))
        maps.append(toAppend)

maps_full.append(maps)

maps = pygame.transform.scale(pygame.image.load('Game_spirite\\Map\\boat_bg.png').convert(),(300,750))
maps.set_colorkey(maps.get_at((0,0)))
maps = game_map(0,0,maps)

maps_full.append(maps)

spirite = game_player('Game_spirite\\Spirite\\',500,600,10)

pygame.mixer.music.load('Game_music\\BGM1.mid')
pygame.mixer.music.play(-1)

plot = 1

delay_time = 100

obstacle = obstacle_full[0]

maps = maps_full[0]

while True :
        if plot==1:
                talk =["第零章：所有事情的開頭",
                        "!!!",
                        "糟糕 ! 超過三點了 ! 我應該在碼頭的!"
                        "快 ! 沒時間了 !"]

                for i in range(len(talk)):
                        pygame.time.delay(delay_time)

                        win.fill((0,0,0))

                        for j in range(0,4):
                                for k in range(0,4):
                                        maps[j][k].winblit(spirite.x,spirite.y)

                        for j in obstacle:
                                if type(j) is game_obstacle:
                                        j.winblit(spirite.x,spirite.y)

                        spirite.winblit()

                        if i==0:
                                print_on_screen(talk[i],RED)
                        else:
                                print_on_screen(talk[i],BLACK)

                        pygame.display.update()

                plot=2
                
        elif plot==2:
                pygame.time.delay(delay_time)
                
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                                
                key = pygame.key.get_pressed()

                win.fill((0,0,0)) # fill background black color

                for i in range(0,4):
                        for j in range(0,4):
                                maps[i][j].winblit(spirite.x,spirite.y) # fill map

                for i in obstacle:
                        if type(i) is game_obstacle:
                              i.winblit(spirite.x,spirite.y)

                spirite.check_key_pressed(key,plot)
                
                spirite.winblit() # fill spirite

                pygame.display.update()

                if (spirite.y in [1280,1270,1260]) and (spirite.x in [790]) and key[pygame.K_SPACE]:
                        plot = 3
                        
        elif plot==3:
                talk = [['Carlos? Are you here?',WHITE,50],
                        ['?? Carlos?',WHITE,50],
                        ['The boat is very dark...',WHITE,50],
                        ['Where is the light switch?',WHITE,50]]

                talk = [['卡倫? 人呢...?',WHITE,50],
                        ['?? 你在嗎?',WHITE,50],
                        ['船好暗啊...',WHITE,50],
                        ['燈的開關呢?',WHITE,50]]
                
                for i in range(len(talk)):
                        win.fill((0,0,0))
                        print_on_screen(talk[i][0],talk[i][1],talk[i][2])
                        pygame.display.update()
                        
                plot = 4
                
        elif plot==4:
                spirite.x = -240
                spirite.y = 240

                spirite.step_costume = [0,0]

                maps = maps_full[1]
                
                win.fill((0,0,0))

                maps.winblit(spirite.x,spirite.y)

                spirite.winblit()

                shadow.winblit(0,0)

                pygame.display.update()

                pygame.time.delay(delay_time*5)

                win.fill((0,0,0))

                maps.winblit(spirite.x,spirite.y)

                spirite.winblit()

                shadow.winblit(0,0)

                print_on_screen("卡倫呢?",WHITE,50)

                pygame.display.update()
                
                plot = 5
                
        elif plot==5:
                pygame.time.delay(delay_time)

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                key = pygame.key.get_pressed()

                win.fill((0,0,0))

                maps.winblit(spirite.x,spirite.y)

                spirite.check_key_pressed(key,plot)

                spirite.winblit()

                shadow.winblit(0,0)

                pygame.display.update()
                
                if [spirite.x,spirite.y] in [[-130,-160],[-120,-160],[-110,-160],[-100,-160]] and key[pygame.K_SPACE]:
                        plot = 6

        elif plot==6:
                win.fill((0,0,0))
                pygame.display.update()
                talk = [['我轉動著方向盤，但沒事發生',GREEN,50],
                        ['彷彿時間暫停一般，船裡的寂靜令人覺得毛骨悚然',GREEN,50],
                        ['............',WHITE,100],
                        ['當我在想著個像是方向盤的物體究竟是不是方向盤時',GREEN,50],
                        ['燈，被打開了',GREEN,50]]
                
                for i in range(len(talk)):
                        win.fill((0,0,0))
                        maps.winblit(spirite.x,spirite.y)
                        spirite.winblit()
                        shadow.winblit(0,0)
                        print_on_screen(talk[i][0],talk[i][1],talk[i][2])
                        pygame.display.update()

                plot = 7

        elif plot==7:
                win.fill((0,0,0))
                maps.winblit(spirite.x,spirite.y)
                spirite.winblit()
                pygame.time.delay(delay_time*2)
                pygame.display.update()
                win.fill((0,0,0))
                maps.winblit(spirite.x,spirite.y)
                spirite.winblit()
                shadow.winblit(0,0)
                pygame.time.delay(delay_time)
                pygame.display.update()
                win.fill((0,0,0))
                maps.winblit(spirite.x,spirite.y)
                spirite.winblit()
                pygame.time.delay(int(delay_time/2))
                pygame.display.update()

                win.fill((0,0,0))
                maps.winblit(spirite.x,spirite.y)
                spirite.winblit()
                pygame.time.delay(delay_time)
                pygame.display.update()

                step = 0

                plot = 8

        elif plot==8:
                pygame.time.delay(delay_time)

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                key = pygame.key.get_pressed()

                win.fill((0,0,0))

                maps.winblit(spirite.x,spirite.y)

                spirite.check_key_pressed(key,plot)

                spirite.winblit()
                
                if [spirite.x,spirite.y] in [[-130,-160],[-120,-160],[-110,-160],[-100,-160]] and key[pygame.K_SPACE]:
                        print_on_screen('A strange wheel.',WHITE,50)

                        while pygame.key.get_pressed()[pygame.K_SPACE]:
                                for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                pygame.display.update()

                if step >= 30:
                        talk = [['砰!!!',RED,1],
                                ['!?',WHITE,30],
                                ['甚麼聲音??',WHITE,50]]
                        for i in range(len(talk)):
                                win.fill((0,0,0))
                                maps.winblit(spirite.x,spirite.y)
                                spirite.winblit()
                                if i==0:
                                        pygame.mixer.music.load('Game_music\\broke_glass.mp3')
                                        pygame.mixer.music.play(0)
                                print_on_screen(talk[i][0],talk[i][1],talk[i][2])
                                pygame.display.update()

                        step = 0

                        plot = 9

        elif plot==9:
                pygame.mixer.music.load('Game_music\\BGM1.mid')
                pygame.mixer.music.play(-1)
                win.fill((0,0,0))
                pygame.display.update()
                pygame.time.delay(delay_time*30)
                talk = [['當你問起我究竟誰是卡倫時，',WHITE,30],
                        ['或如果你問我，我又是誰?',WHITE,30],
                        ['我現在就可以告訴你。',WHITE,30],
                        ['卡倫，是我哥哥',WHITE,30],
                        ['是個十五歲的青少年',WHITE,30],
                        ['我名叫溪昵，名字有點饒舌',WHITE,30],
                        ['有天當我再找哥哥到底去哪裡時，',WHITE,30],
                        ['我誤觸到發動的機關',WHITE,30],
                        ['過了不久便撞到了東西，船沉了，',WHITE,30],
                        ['我連反應的時間都來不及，更別說逃跑了',WHITE,30],
                        ['所以，故事就這樣開始了',WHITE,30]]
                
                for i in range(len(talk)):
                        win.fill((0,0,0))
                        print_on_screen(talk[i][0],talk[i][1],talk[i][2])
                        pygame.display.update()

                plot = 10

        elif plot==10:
                win.fill((0,0,0))
                font = pygame.font.Font('Game_Chinese_unicode_default\\NotoSansCJKtc-Medium.otf', 75)
                font_2 = pygame.font.Font('Game_Chinese_unicode_default\\NotoSansCJKtc-Medium.otf',10)
                textsurface_up = font.render('未        完', False, RED)
                textsurface_down = font.render('待續',False,RED)
                textsurface_version = font_2.render('V.WIP.0.2.1',False,GREEN)
                win.blit(textsurface_up,(65,100))
                win.blit(textsurface_down,(100,200))
                win.blit(textsurface_version,(440,480))
                pygame.display.update()

                while True:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                        
                        key = pygame.key.get_pressed()

                        if not(key[pygame.K_SPACE]):
                                break
                
                while True:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                        
                        key = pygame.key.get_pressed()

                        if key[pygame.K_SPACE]:
                                break
                plot = 11
        elif plot==11:
                break
                
pygame.quit()
