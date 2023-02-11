import pygame
import random
import time

# initializes the pygame library
pygame.init()

# 1. make a screen
screenWidth = 800
screenHeight = 600
gameScreen = pygame.display.set_mode((screenWidth,screenHeight))

# 2. give a screen a caption
pygame.display.set_caption('Snake Game')
pygame.display.update()

# displaying the score on the screen
font = pygame.font.SysFont(None,55)
def screenScore(text,color, x, y):
    screenText = font.render(text,True,color)
    gameScreen.blit(screenText,[x,y])

# making snake
def makeSnake(screen,color,sList,sizeOfSnake):
    for x,y in sList:
        pygame.draw.rect(screen, color, [x, y, sizeOfSnake,sizeOfSnake])

gameOver = False
# game loop
def play():
    exitGame = False
    global gameOver

    # 3. making the snake
    snakeX = 40
    snakeY = 40
    snakeSize = 10
    snakeLength = 1
    snakeList =[]

    # 6. making the food
    foodX = random.randint(10,screenWidth-10)
    foodY = random.randint(10,screenHeight-10)

    # about score
    score = 0

    # colors
    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)
    black = (0,0,0)

    # 4. moving the snake
    snakeVelocity = 5
    velocityX = 0
    velocityY = 0

    # 5. setting the time frame
    fps = 30
    clock = pygame.time.Clock()
    while not exitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True
                exit()
        
            # 4. moving the snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velocityY = velocityY - snakeVelocity
                    velocityX = 0
                    gameOver = False

                elif event.key == pygame.K_DOWN:
                    velocityY = velocityY + snakeVelocity
                    velocityX = 0
                    gameOver = False

                elif event.key == pygame.K_LEFT:
                    velocityX = velocityX - snakeVelocity
                    velocityY = 0
                    gameOver = False

                elif event.key == pygame.K_RIGHT:
                    velocityX = velocityX + snakeVelocity
                    velocityY = 0
                    gameOver = False

    
        # 4. moving the snake
        snakeX += velocityX
        snakeY += velocityY

        # 7. making the snake eat food
        if abs(snakeX - foodX) < 10 and abs(snakeY - foodY) < 10:
            # 8. printing the score on the screen
            score += 1

            # another food
            foodX = random.randint(10,screenWidth)
            foodY = random.randint(10,screenHeight)

            # 9. if snake eats food its length increases
            snakeLength += 5
        
        gameScreen.fill(white)

        # increasing the length of snake
        head = []
        head.append(snakeX)
        head.append(snakeY)
        snakeList.append(head)

        # preventing the snake to increase length infinitely
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # 11. if snake hits itself its dead
        for i in snakeList[1:]:
            if snakeList[0] == i:
                gameOver = True
                time.sleep(2)
                play()

        # 10. if snake hits the boundary its dead
        if snakeX == screenWidth or snakeX == 0 or snakeY == screenHeight or snakeY == 0:
            gameOver = True
            time.sleep(2)
            play()
            

        #displaying the score on the screen
        screenScore('Score is : '+ str(score),red,5,5)
        if gameOver == True:
            screenScore('Game Over',black,screenWidth/2,screenHeight/2)
            
        # 6. making the food
        pygame.draw.rect(gameScreen,blue,[foodX,foodY,snakeSize,snakeSize])

        # 3. making the snake
        makeSnake(gameScreen,red,snakeList,snakeSize)

        pygame.display.update()

        # 5. setting the time frame
        clock.tick(fps)

play()
# exits the screen
pygame.quit()
quit()