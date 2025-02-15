import pygame
import random
import sys

pygame.init()

SW, SH = 800, 800
BLOCK_SIZE = 50

screen = pygame.display.set_mode((800,800))


pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("img\icon.png"))
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x,self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x,y, BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen,"green",rect,1)

screen.fill((46, 66, 41))

drawGrid()

snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    snake.update()

    screen.fill((46, 66, 41))
    drawGrid()

    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    pygame.display.update()
    clock.tick(10)    
