import pygame
import random
import os
import sys

pygame.init()

# image
BLACKSPACE = pygame.image.load(os.path.join('download.jpeg'))

# defining variables
WINDOW = (800, 800)
# pyWIDTH, HEIGHT = 800, 800
# colorz
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
DARKGREEN = (1, 50, 32)
LIGHTGREEN = (144, 238, 144)
# velocity
CITY = 5
# FPS
FPS = 60  # Increased FPS to make it smoother
x = 400
y = 400
xchange = 0
ychange = 0
WIN = pygame.display.set_mode((800, 800))
width = 20
score = 0


score_font = pygame.font.SysFont("impact", 35)
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    WIN.blit(value, [0, 0])
 
def our_snake(snakeblock, snakeBody):
    for i in snakeBody:
        pygame.draw.rect(WIN, DARKGREEN, [i[0], i[1], snakeblock, snakeblock])

# setting the caption
pygame.display.set_caption('SNAKE')
foodx = round(random.randrange(0,800 - width)/20)*20 
foody = round(random.randrange(0,800 - width)/20)*20
over = False
snakelength = 1
def collisionDetect():
    global x, y, foody, foodx, score, snakelength
    if x == foodx and y == foody:
            foodx = round(random.randrange(0, 800 - width) / 20) * 20
            foody = round(random.randrange(0, 800 - width) / 20) * 20
            x = round(x/20)*20
            y = round(y/20)*20
            snakelength += 1
            print(snakelength)

def main():
    global x, y, xchange, ychange, width, height, foodx, foody, score, snakelength
    snakeBody = []
    loop = False
    over = False
    snakelength = 1
    clock = pygame.time.Clock()
    if over == True: 
            WIN.fill(RED)
            pygame.display.update()
            
    while not over :
        
        collisionDetect()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x> 0:
                    xchange = -width
                    ychange = 0
                elif event.key == pygame.K_RIGHT and x <800 - width:
                    xchange = width
                    ychange = 0
                elif event.key == pygame.K_UP and y> 0:
                    ychange = -width
                    xchange = 0
                elif event.key == pygame.K_DOWN and y < 800 -width:
                    ychange = width
                    xchange = 0
        if round(x / width) * width >= 800 - width or round(x / width) * width < 0 or round(y / width) * width >= 800 - width or round(y / width) * width < 0:
                over = True
                


                
        
        
        
        x += xchange
        y += ychange

        WIN.fill(BLACK)
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snakeBody.append(snake_Head)
        if len(snakeBody) > snakelength:
            del snakeBody[0]
 
        for i in snakeBody[:-1]:
            if i == snake_Head:
                over = True
 
        our_snake(width, snakeBody)
        # draw the rectangle at (x, y) with the specified width and height
        Your_score(snakelength -1)
        SNAKE = pygame.draw.rect(WIN, LIGHTGREEN, [x, y, width, width]) 
        food = pygame.draw.rect(WIN, RED, [foodx, foody, width, width])

        pygame.display.update()
        clock.tick(10)

#python3 snakegame.py
if __name__ == '__main__':
    main()


