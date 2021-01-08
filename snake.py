import pygame
import random
import time
import math

green = (0, 192, 0)
red = (192, 0, 0)

def moveSnake(x, y):
    global running
    global snake
    global grid
    global appleX
    global appleY
    global apple
    global score
    global dead
    a = snake[0][0]
    b = snake[0][1]
    if a+x < 0 or a+x > 39 or b+y < 0 or b+y > 39 or grid[a+x][b+y] == 1:
        dead = True
        return

    if appleX == a+x and appleY == b+y:
        apple = False
        score += 1
        font = pygame.font.SysFont('text.ttf', 45)
        pygame.draw.rect(screen, (0,0,0), (0, 601, 600, 50))
        text = font.render(str(score), True, (255, 255, 255))
        screen.blit(text, (10, 610))
    else:
        temp = snake.pop()
        pygame.draw.rect(screen, (0,0,0), (temp[0]*15+2, temp[1]*15+2, 12, 12))
        grid[temp[0]][temp[1]] = 0
        
    snake.insert(0, [a + x, b + y]) 
    grid[a+x][b+y] = 1
    pygame.draw.rect(screen, green, ((a+x)*15+2, (b+y)*15+2, 12, 12))

def randomApple():
    global grid
    global appleX
    global appleY
    global apple
    apple = True
    found = False
    while not found:
        appleX = random.randint(0, 39)
        appleY = random.randint(0, 39)
        if grid[appleX][appleY] == 0:
            found = True
    pygame.draw.rect(screen, red, (appleX*15+2, appleY*15+2, 12, 12))
    
def main():
    global snake
    global grid
    global running
    global apple
    global score
    global dead
    dead = False
    score = 0
    apple = False
    x = 1
    y = 0
    snake = [[20, 20]]
    grid = [[0 for i in range(40)] for j in range(40)]
    grid[20][20] = 1

    clock = pygame.time.Clock()
    
    running = True
    while running:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not moved and not dead:
                if event.key == pygame.K_LEFT:
                    x = -1
                    y = 0
                    moved = True
                elif event.key == pygame.K_RIGHT:
                    x = 1
                    y = 0
                    moved = True
                elif event.key == pygame.K_UP:
                    x = 0
                    y = -1
                    moved = True
                elif event.key == pygame.K_DOWN:
                    x = 0
                    y = 1
                    moved = True
        if not apple:
            randomApple()        
        if not dead:
            moveSnake(x, y)
        pygame.display.update()
        clock.tick(13)
        moved = False
    pygame.quit()
    
def start():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((600, 650))
    pygame.display.set_caption("Snake")
    screen.fill((0, 0, 0))

    for i in range (1,40):
        pygame.draw.line(screen, (255,255,255), (15*i, 0), (15*i,600), 1)
        pygame.draw.line(screen, (255,255,255), (0, 15*i), (600,15*i), 1)
    pygame.draw.line(screen, (255,255,255), (0, 600), (600,600), 1)
    font = pygame.font.SysFont('text.ttf', 45)
    text = font.render('0', True, (255, 255, 255))
    screen.blit(text, (10, 610))
    pygame.display.update()
    main()

start()
