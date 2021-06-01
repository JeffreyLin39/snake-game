import random
import pygame

# Implementation of a linked list to represent snake
class Node:
        def __init__(self, next, coordinate):
                self.next = next
                self.coordinate = coordinate

class Snake:
        def __init__(self, head, tail, length):
                self.head = head
                self.tail = tail
                self.length = length
        def removeTail(self):
                self.tail = self.tail.next 
        def setHead(self, coordinate):
                temp = Node(None, coordinate)
                if self.length == 1:
                        self.tail.next = temp
                self.head.next = temp
                self.head = temp
# pygame stuff
def start():
        global screen
        global font
        pygame.init()
        screen = pygame.display.set_mode((600, 650))
        pygame.display.set_caption("Snake")
        pygame.draw.line(screen, (255,255,255), (0, 600), (600,600), 1)
        font = pygame.font.SysFont(None, 45)
        text = font.render('0', True, (255, 255, 255))
        screen.blit(text, (10, 610))
        pygame.display.update()
        main()

def main():
        global snake
        global grid
        global gameOver
        global apple
        gameOver = False
        running = True
        # create snake
        head = Node(None, [20, 20])
        tail = Node(head, [20, 20])
        snake = Snake(head, tail, 1)
        grid = [[0 for i in range(40)] for j in range(40)]
        grid[20][20] = 1
        x = 1
        y = 0
        generateApple()
        # main loop
        while running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
                        if event.type == pygame.KEYDOWN:
                                if gameOver:
                                    start() 
                                if event.key == pygame.K_LEFT:
                                        x = -1
                                        y = 0
                                elif event.key == pygame.K_RIGHT:
                                        x = 1
                                        y = 0
                                elif event.key == pygame.K_UP:
                                        x = 0
                                        y = -1
                                elif event.key == pygame.K_DOWN:
                                        x = 0
                                        y = 1
                    
                moveSnake(x, y)
                pygame.time.Clock().tick(20)
        pygame.quit()

def moveSnake(x, y):
        global gameOver
        global font
        global apple
        currX = snake.head.coordinate[0]
        currY = snake.head.coordinate[1]

        newX = currX + x
        newY = currY + y
        # Check if snake is dead
        if newX < 0 or newX > 39 or newY < 0 or newY > 39 or grid[newX][newY] == 1:
            gameOver = True
            return

        # uncomment for alternate game mode
        #if newX < 0:
        #        newX += 40
        #elif newX > 39:
        #        newX %= 40
        
        #if newY < 0:
        #        newY += 40
        #elif newY > 39:
        #        newY %= 40
        
        # Code to make the snake length longer
        if grid[newX][newY] == -1:
            snake.length += 1
            pygame.draw.rect(screen, (0,0,0), (0, 601, 600, 50))
            text = font.render(str(snake.length-1), True, (255, 255, 255))
            screen.blit(text, (10, 610))
            pygame.draw.rect(screen, (0,200,0), (newX*15+2, newY*15+2, 12, 12))
            grid[newX][newY] = 1
            snake.setHead([newX, newY])
            generateApple()
        # code to move the snake forward by 1
        else:
            pygame.draw.rect(screen, (0,200,0), (newX*15+2, newY*15+2, 12, 12))
            grid[newX][newY] = 1
            snake.setHead([newX, newY])
                        
            pygame.draw.rect(screen, (0,0,0), (snake.tail.coordinate[0]*15+2, snake.tail.coordinate[1]*15+2, 12, 12))
            grid[snake.tail.coordinate[0]][snake.tail.coordinate[1]] = 0
            snake.removeTail()


        pygame.display.update()

# Creates random apple             
def generateApple():
    global apple
    global grid
    found = False
    while not found:
        x = random.randint(0, 39)
        y = random.randint(0, 39)
        if grid[x][y] == 0:
            found = True
            apple = [x, y]
            grid[x][y] = -1
    pygame.draw.rect(screen, (200, 0, 0), (x * 15 + 2, y * 15 + 2, 12, 12))
    pygame.display.update()
start()
