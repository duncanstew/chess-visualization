import pygame
import time
import random

'''
Program to make chess visualization of squares super easy
'''

pygame.init()
pygame.font.init()
WIDTH = 500
HEIGHT = 500

BLACK = (0,0,0)
WHITE = (232,235,239)
GREY = (119,136,153)

LETTERS = ['a','b','c','d','e','f','g','h']
NUMBERS = [1,2,3,4,5,6,7,8]
KEY = {'a': 1, 'b':2, 'c':3, 'd':4,'e':5,'f':6,'g':7,'h':8}
COORDINATES = {}
FONT = pygame.font.SysFont('Comic Sans MS', 50)

COUNT = 0

def makeCoordinates():
    temp = [ltr + str(num) for ltr in LETTERS for num in NUMBERS]
    for item in temp:
        COORDINATES[item] = ''

def convertCoordinates():
    for item in COORDINATES:
        rem = KEY[item[0]] + int(item[1])
        if rem % 2 == 0:
            COORDINATES[item] = 'black'
        else:
            COORDINATES[item] = 'white'

def drawRect(window, color):
    if color == 'black':
        color = BLACK
    else:
        color = WHITE

    pygame.draw.rect(window, color, (int(WIDTH/4), int(HEIGHT/4), int(WIDTH/2), int(HEIGHT/2)))

def drawText(window, coordinates):

    textSurface = FONT.render(coordinates, True, BLACK)
    h = int(HEIGHT/6) - textSurface.get_height()
    w = int(WIDTH/2) - textSurface.get_width()/2
    window.blit(textSurface,(w,h))








def main():
    global COUNT
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(GREY)
    makeCoordinates()
    convertCoordinates()

    run = True

    while run:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

            # Code that displays coordinate system on grid
            if events.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    coordinates = None
                    color = None
                    COUNT += 1
                    if COUNT % 2 == 1:
                        window.fill(GREY)
                        coordinates, color = random.choice(list(COORDINATES.items()))
                        drawText(window, coordinates)
                    else:
                        drawRect(window, color)



                elif pressed[pygame.K_q]:
                    pygame.quit()
                    run = False



        pygame.display.update()

    quit()
    pygame.quit()



if __name__ == "__main__":
    main()
