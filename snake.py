import pygame
import random

pygame.init()
clock = pygame.time.Clock()

gridNumber = 20

gridSize = [gridNumber, gridNumber]

WIDTH = 30
HEIGHT = 30
MARGIN = 3

GAME_WIDTH = (gridNumber * WIDTH) + ((gridNumber+1) * MARGIN)
GAME_HEIGHT = (gridNumber * HEIGHT) + ((gridNumber+1) * MARGIN)
FPS = 15

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)



#----------Creating Grids----------------
grid = []
for row in range(gridNumber):
    grid.append([])
    for column in range(gridNumber):
        grid[row].append(0)



window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))

startPos = [9,9]
xMotion = 0
yMotion = 0


snakeList = []
snakeLength = 1


rndX = random.randint(0,gridNumber-1)
rndY = random.randint(0,gridNumber-1)
applePos = [rndX, rndY]




gameStart = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if yMotion != 0 or gameStart == 0:
                    gameStart = 1
                    xMotion = -1
                    yMotion = 0
            elif event.key == pygame.K_RIGHT:
                if yMotion != 0 or gameStart == 0:
                    gameStart = 1
                    xMotion = 1
                    yMotion = 0
            elif event.key == pygame.K_UP:
                if xMotion != 0 or gameStart == 0:
                    gameStart = 1
                    xMotion = 0
                    yMotion = -1
            elif event.key == pygame.K_DOWN:
                if xMotion != 0 or gameStart == 0:
                    gameStart = 1
                    xMotion = 0
                    yMotion = 1


    window.fill(black)


    startPos[0] += xMotion
    startPos[1] += yMotion

    # -----------Border Check------------------
    if startPos[0] > gridSize[0] - 1:
        startPos[0] = 0
    elif startPos[0] < 0:
        startPos[0] = gridSize[0]
    elif startPos[1] > gridSize[1] - 1:
        startPos[1] = 0
    elif startPos[1] < 0:
        startPos[1] = gridSize[1]



    #-----------Drawing Grids------------------
    for row in range(gridNumber):
        for column in range(gridNumber):
            color = white
            pygame.draw.rect(window, color, ((MARGIN+WIDTH)*column + MARGIN, (MARGIN + HEIGHT)*row + MARGIN, WIDTH, HEIGHT))



    #-------------Drawing Snake-----------
    snakeHead = []
    snakeHead.append(startPos[0])
    snakeHead.append(startPos[1])
    snakeList.append(snakeHead)

    if len(snakeList) > snakeLength:
        snakeList.pop(0)

    #-----------Game Over------------

    for eachSegment in snakeList[:-1]:
        if eachSegment == snakeHead:
            snakeList = []
            snakeLength = 1
            startPos = [9, 9]
            rndX = random.randint(0, gridNumber - 1)
            rndY = random.randint(0, gridNumber - 1)
            applePos = [rndX, rndY]


    for i in snakeList:
        pygame.draw.rect(window, red, ((MARGIN + WIDTH) * i[0] + MARGIN, (MARGIN + HEIGHT) * i[1] + MARGIN, WIDTH, HEIGHT))

    #--------------Drawing Apple---------------
    pygame.draw.rect(window, blue, ((MARGIN + WIDTH) * rndX + MARGIN, (MARGIN + HEIGHT) * rndY + MARGIN, WIDTH, HEIGHT))




    #----------Eat Apple----------------------
    if startPos == applePos:
        snakeLength += 1
        pygame.draw.rect(window, white, ((MARGIN + WIDTH) * rndX + MARGIN, (MARGIN + HEIGHT) * rndY + MARGIN, WIDTH, HEIGHT))#deletes apple
        rndX = random.randint(0, gridNumber-1)
        rndY = random.randint(0, gridNumber-1)
        rndApple = [rndX, rndY]
        while (rndApple in snakeList):
            rndX = random.randint(0, gridNumber - 1)
            rndY = random.randint(0, gridNumber - 1)
            rndApple = [rndX, rndY]
        applePos = rndApple
        pygame.draw.rect(window, blue, ((MARGIN + WIDTH) * rndX + MARGIN, (MARGIN + HEIGHT) * rndY + MARGIN, WIDTH, HEIGHT))#draws apple


    pygame.display.update()
    clock.tick(FPS)



pygame.quit()