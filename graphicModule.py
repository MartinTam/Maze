import pygame
import os

FPS = 60

WIDTH = 1000
HEIGHT = 600
PERSON_WIDTH = 50
PERSON_HEIGHT = 50
RECT_SIZE = 10

WHITE = (255, 255, 255)
BLACK = (0,0,0)

PERSON_START_POSITION_X = 80
PERSON_START_POSITION_Y = 40

PERSON = pygame.transform.scale( pygame.image.load(os.path.join('images', 'person.png')), (50,50) )
PERSON_RIGHT = pygame.transform.rotate( PERSON, 90 )
PERSON_LEFT = pygame.transform.rotate( PERSON, -90 )
PERSON_UP = pygame.transform.rotate( PERSON, 180 )
VEL = 5

START_LINE = pygame.Rect(60, 30, 90, RECT_SIZE)

RECT_1 = pygame.Rect(50, 50, RECT_SIZE, 500)
RECT_2 = pygame.Rect(950, 50, RECT_SIZE, 500)
RECT_3 = pygame.Rect(150, 50, 800, RECT_SIZE)
RECT_4 = pygame.Rect(60, 540, 800, RECT_SIZE)

END_LINE = pygame.Rect(860, 570, 90, RECT_SIZE)