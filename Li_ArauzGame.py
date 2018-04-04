####

#Hailey Li & Nina Arauz - Snake Game MyVersion 2018
#This game makes use to the PyGame package in Python and uses the Arrow keys to control the snake.
#This version of the snake game was modified from the tutorial posted by Syntec (on behalf of TheNewBoston.com)
#All modifications and changes we made are commented in-line below.

####

import pygame
import time
import random

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)


display_width = 800 #changed the window size
display_height  = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakes and Faces') #modified the caption

icon = pygame.image.load('snakehead2.png') #different apple (it is a face)
pygame.display.set_icon(icon)

img = pygame.image.load('snakehead.png') #different snake icon (snake head)
appleimg = pygame.image.load('snakehead2.png')

#fps
clock = pygame.time.Clock()

#face characteristics
AppleThickness = 40 #increased the size of the apple
block_size = 40
FPS = 13 #increased fps

direction = "right"

#font/text
smallfont = pygame.font.SysFont("monospace", 18) #changed the font style to monospace
medfont = pygame.font.SysFont("monospace", 30) #changed font size and style
largefont = pygame.font.SysFont("brush script", 70) #changed font style

#quitting the game
def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(red)
        message_to_screen("Holding", #changed from pause to holding
                          white,
                          -100,
                          size="medium")

        message_to_screen("Press C to continue or Q to quit.",
                          white,
                          25)
        pygame.display.update()
        clock.tick(3)
                    
#score keeper
def score(score):
    text = smallfont.render("How many 'meh' faces have you eaten?: "+str(score), True, black) #changed the words on the screen
    gameDisplay.blit(text, [0,0])

#apple location
def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY


#introduction of game
def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
   
        gameDisplay.fill(white)
        message_to_screen("Snakes and Faces",
                          red,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat the 'meh' faces.",
                          green,
                          -30)

        message_to_screen("The more faces you eat, the longer your arm gets",
                          green,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die!",
                          green,
                          50)

        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          180)
    
        pygame.display.update()
        clock.tick(15)
        
        

#snake movement
def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#movement of snake
def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

#boundaries of snake
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)

        
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

#snake variables
        snakeHead = []
        snakeHead.append(lead_x-75) #changed the center of the snake head
        snakeHead.append(lead_y-24)
        snakeList.append(snakeHead)


        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        score(snakeLength-1)

        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

        



        

        clock.tick(FPS)
        
    pygame.quit()
    quit()

game_intro()
gameLoop()
