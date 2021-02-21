import pygame
import os
from graphicModule import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze')


def setDirection(direction_pressed, direction):

    if direction_pressed == 1:
        direction[0] = 1
    elif direction_pressed == 2:
        direction[0] = 2
    elif direction_pressed == 3:
        direction[0] = 3
    elif direction_pressed == 4:
        direction[0] = 4
    elif direction_pressed == 0:
        pass


def movement(key_pressed, position):

    if key_pressed[pygame.K_RIGHT] and position.x + PERSON_WIDTH <= WIDTH - 5:
        position.x += VEL
        return 1
    
    elif key_pressed[pygame.K_LEFT] and position.x >= 5:
        position.x -= VEL
        return 2
    
    elif key_pressed[pygame.K_UP] and position.y >= 5:
        position.y -= VEL
        return 3
    
    elif key_pressed[pygame.K_DOWN] and position.y + PERSON_HEIGHT <= HEIGHT - 5:
        position.y += VEL
        return 4

    else:
        return 0
    

def draw(position, direction):
    
    WIN.fill(WHITE)

    if direction[0] == 1:
        WIN.blit(PERSON_RIGHT, (position.x, position.y))
    elif direction[0] == 2:
        WIN.blit(PERSON_LEFT, (position.x, position.y))
    elif direction[0] == 3:
        WIN.blit(PERSON_UP, (position.x, position.y))
    elif direction[0] == 4:
        WIN.blit(PERSON, (position.x, position.y))
    else:
        WIN.blit(PERSON, (position.x, position.y))

    pygame.draw.rect(WIN, BLACK, START_LINE)

    pygame.draw.rect(WIN, BLACK, RECT_1)
    pygame.draw.rect(WIN, BLACK, RECT_2)
    pygame.draw.rect(WIN, BLACK, RECT_3)
    pygame.draw.rect(WIN, BLACK, RECT_4)

    pygame.draw.rect(WIN, BLACK, END_LINE)

    pygame.display.update()

def main():
    
    clock = pygame.time.Clock()
    run = True
    position = pygame.Rect(PERSON_START_POSITION_X, PERSON_START_POSITION_Y, PERSON_WIDTH, PERSON_HEIGHT)
    direction = [0]

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()

        direction_pressed = movement(key_pressed, position)

        setDirection(direction_pressed, direction)
        draw(position, direction)

    pygame.quit()

main()