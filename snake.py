import pygame
from pygame.locals import *
import random
pygame.init()


width=600
height=600

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")


#define game variable
cell_size= 10
direction=8#8 is up,2 is down, 6 is right,4 is left
update_snake=0
food=[0,0]
new_food=True
new_piece=[0,0]
score=0
game_over=False
clicked=False

#create snake
snake_pos=[[int(width/2),int(height/2)]]
snake_pos.append([int(width/2),int(height/2) + cell_size])
snake_pos.append([int(width/2),int(height/2)+cell_size *2])
snake_pos.append([int(width/2),int(height/2)+cell_size *3])

#define colors
bg=(0,0,0)
body_inner=(237,103,146)
body_outer=(97,221,237)
head=(180,180,180)
food_col=(248,251,50)
blue=(0,0,255)
red=(255,0,0)

#setup rect for 'play again'
again_rect=Rect(width//2-80,height//2,160,50)


#define font
font = pygame.font.SysFont(None,40)

def draw_screen():
    screen.fill(bg)

def draw_score():
    score_txt = "Score: " +str(score)
    score_img=font.render(score_txt,True,blue)
    screen.blit(score_img,(0,0))

def check_game_over(game_over):

    #first if snake has eaten itself
    head_count=0
    for seg in snake_pos:
        if snake_pos[0]==seg and head_count>0:
            game_over=True
        head_count+=1

    #check if snake gone out of screen
    if snake_pos[0][0]<0 or snake_pos[0][0] > width or snake_pos[0][1]<0 or snake_pos[0][1]>height:
        game_over=True
    return game_over

def draw_game_over():
    over_txt = "Game Over!"
    over_img = font.render (over_txt,True,blue)
    pygame.draw.rect(screen,red,(width//2-80,height //2 -60,160,50))
    screen.blit(over_img,(width//2-80,height//2 -50))

    again_text="Play Again"
    again_img= font .render(again_text,True,(89,80,70))
    pygame.draw.rect(screen,(255,200,150),again_rect)
    screen.blit(again_img,(width//2-80,height//2+10))




run=True
while run:

    draw_screen()
    draw_score()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!=2:
                direction=8
            if event.key == pygame.K_DOWN and direction!=8:
                direction=2
            if event.key == pygame.K_RIGHT and direction != 4:
                direction=6
            if event.key == pygame.K_LEFT and direction!=6:
                direction=4


    #create food
    if new_food==True:
        new_food=False
        food[0]=cell_size * random.randint(0,(int(width / cell_size))-1)#without int it doesnt work as in python 3 dividing two ints gives u a float
        food[1]=cell_size * random.randint(0,(int(height / cell_size))-1)

    #draw_food
    pygame.draw.rect(screen,food_col,(food[0],food[1],cell_size,cell_size))



    #check if food has been eaten
    if snake_pos[0]==food:
        new_food=True
        #create a new piece at the last pt of snke tail
        new_piece = list(snake_pos[-1])
        if direction==8:
            new_piece[1]+=cell_size
        if direction==2:
            new_piece[1]-=cell_size
        if direction==6:
            new_piece[0]-=cell_size
        if direction==4:
            new_piece[0]+=cell_size
        #attach new piece
        snake_pos.append(new_piece)

        #increase score
        score+=1

    if game_over ==False:
        if update_snake> 99:#this condition for the snake to appear not go in an infinite loop
            update_snake=0
            snake_pos=snake_pos[-1:]+snake_pos[:-1]
            #heading up
            if direction ==8:
                snake_pos[0][0]=snake_pos[1][0]
                snake_pos[0][1]=snake_pos[1][1]-cell_size
            if direction ==2:
                snake_pos[0][0]=snake_pos[1][0]
                snake_pos[0][1]=snake_pos[1][1]+cell_size
            if direction ==6:
                snake_pos[0][1]=snake_pos[1][1]
                snake_pos[0][0]=snake_pos[1][0]+cell_size
            if direction ==4:
                snake_pos[0][1]=snake_pos[1][1]
                snake_pos[0][0]=snake_pos[1][0]-cell_size

            game_over = check_game_over(game_over)


    if game_over==True:
        draw_game_over()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked== False:
            clicked=True
        if event.type == pygame.MOUSEBUTTONDOWN and clicked== True:
            clicked=False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset variables
                direction=8#8 is up,2 is down, 6 is right,4 is left
                update_snake=0
                food=[0,0]
                new_food=True
                new_piece=[0,0]
                score=0
                game_over=False
                

                #create snake
                snake_pos=[[int(width/2),int(height/2)]]
                snake_pos.append([int(width/2),int(height/2) + cell_size])
                snake_pos.append([int(width/2),int(height/2)+cell_size *2])
                snake_pos.append([int(width/2),int(height/2)+cell_size *3])
                



                
        #draw snake
    head = 1
    for x in snake_pos:
        if head==0:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,body_inner,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
        if head== 1:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,head,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
            head=0
            

            
    pygame.display.update()

    update_snake += 1

pygame.quit()


