import pygame
import random
import math


pygame.init()
click ="right"
X=500 #500
Y=800  #800
#print("helo")

screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("Skier")
img= pygame.image.load("ski.png")
pygame.display.set_icon(img)


#---------------------player------------------->

playerimg=pygame.image.load("snowboard.png")
playerimgL=pygame.transform.flip(playerimg, True, False)
playerX=(X/2)-30 #220
playerY=(Y*2)/15  #100
change =0
def player(x):
    screen.blit(playerimg,(x,playerY))
def turn():
    screen.blit(playerimgL,(playerX,playerY)) 
    #pygame.display.update()


#----------------------Flags--------------------->

flagimg =pygame.image.load("flag.png")
flagX = random.randint(0,X-60) #0-440
flagY = Y      #random.randint(100,650)     800  200-850
changeflag =-0.7
dist=140 #distnace between flags
flag_state="makaynch"

def flags(x,y):
    global flag_state
    flag_state="kayn"
    screen.blit(pygame.transform.flip(flagimg, True, False),(x,y)) 
    screen.blit(flagimg,(x+dist,y))
    
#----------------------pinetree---------------->
pinetreeimg=[]
pinetreeX=[]
pinetreeY= []
changetree = []
pine_state =[]
num_trees=15



for i in range(num_trees):
    pinetreeimg.append(pygame.image.load("winter.png"))
    pinetreeX.append(random.randint(0,X-60)) #0-440
    pinetreeY.append(random.randint(Y,Y+450)) #800-1250
    changetree.append(-0.7)
    pine_state.append("makaynch")

def pine_generate(x,y,i):
    #global pine_state
    #pine_state[i] ="kayn"
    screen.blit(pinetreeimg[i],(x,y))

#--------- collision---------------->
def isCol2(playerX,playerY,flagX,flagY):
    distance =math.sqrt((math.pow(playerX-((flagX+70)),2))+(math.pow(playerY-flagY,2)))
    if distance < 50 :
     return True
    else: return False



def isCol(playerX,playerY,pinetreeX,pinetreeY):
    distance =math.sqrt((math.pow(playerX-pinetreeX,2))+(math.pow(playerY-pinetreeY,2)))
    if distance < 30: 
      return True
    else: return False
#--------------------Score----------------->
score_val=0
font=pygame.font.Font('freesansbold.ttf', 20)

textX=10
textY=10

def score(x,y):
    score=font.render("Score : "+str(int(score_val)), True, (200,60,40))
    screen.blit(score,(x,y))


#------------gameover----------->
over_font=pygame.font.Font('freesansbold.ttf', 60)
def game_over():
    gameover=over_font.render("Game Over", True, (250,0,0))
    rect=gameover.get_rect()
    rect.center=((X/2),(Y/2))
    screen.blit(gameover,rect)
def win():
    gameover=over_font.render("Win", True, (250,0,0))
    rect=gameover.get_rect()
    rect.center=((X/2),(Y/2))
    screen.blit(gameover,rect)

#------------------------------------------mainLoop--------------------------------->

test=True
while test:

    screen.fill((229,255,255))
    

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            test=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change = -0.6
                
                click="left"
            if event.key == pygame.K_RIGHT:
                change = 0.6
                click="right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change = 0
                click="front"
    

    #--------------------------player--------------->
    if playerX >= X-60:
        playerX = X-60
    if playerX <= 0:
        playerX = 0
    if click is "left":
        turn()    
    else:    
        player(playerX)
    playerX += change 

    #-----------------------flag----------->
    if flagX >= X-160:
        flagX = X-160
    if flagX <= 0:
        flagX = 0

    if flagY <= 0: 
      flag_state="makaynch" 
      flagY=Y 

    if flag_state is "makaynch":
        flagX= random.randint(0,640)
        flags(flagX,flagY)

    if flag_state is "kayn":
       flags(flagX,flagY)
       flagY += changeflag        

    col1 = isCol2(playerX, playerY, flagX, flagY)
    if col1:
        score_val += 0.01


    #-------------------------generate trees--------->
    for i in range(num_trees):
        pinetreeY[i] += changetree[i]
        if pinetreeX[i] >= X-60:
            pinetreeX[i] = X-60
        if pinetreeX[i] <= 0:
            pinetreeX[i] = 0    
    
        
        if pinetreeX[i] >= flagX-10 and pinetreeX[i] <= flagX+dist+46*2 :
            if  pinetreeY[i] >= flagY-30 and pinetreeY[i] <= flagY+40:
                pinetreeX[i]=random.randint(0,X-60)
                pinetreeY[i]=random.randint(Y,Y+450)



        if pinetreeY[i] <= -200: 
          pinetreeY[i]=random.randint(Y,Y+450)
          pinetreeX[i]=random.randint(0,X-60)
          pinetreeY[i] += changetree[i]

        pine_generate(pinetreeX[i],pinetreeY[i],i)   
               
        #--------------collison--------------->
        col= isCol(playerX,playerY,pinetreeX[i],pinetreeY[i])
        if col:
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        test=False
                        
                    game_over()

        if score_val>10.2:
            win()
            test=False   
            
            

        

        

    #score_val += 0.01
    score(textX,textY)

    pygame.display.update()