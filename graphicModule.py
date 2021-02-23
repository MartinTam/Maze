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
GREY = (128, 128, 128)

PERSON_START_POSITION_X = 80
PERSON_START_POSITION_Y = 60

PERSON_DOWN = pygame.transform.scale( pygame.image.load(os.path.join('images', 'person.png')), (50,50) )
PERSON_RIGHT = pygame.transform.rotate( PERSON_DOWN, 90 )
PERSON_LEFT = pygame.transform.rotate( PERSON_DOWN, -90 )
PERSON_UP = pygame.transform.rotate( PERSON_DOWN, 180 )
PERSON = PERSON_DOWN
VEL = 5

START_LINE = pygame.Rect(60, 50, 90, RECT_SIZE) # Start the game

RECT_1 = pygame.Rect(50, 50, RECT_SIZE, 500)    # Left vertical border
RECT_2 = pygame.Rect(950, 50, RECT_SIZE, 500)   # Right vertical border
RECT_3 = pygame.Rect(150, 50, 800, RECT_SIZE)   # Up vertical border
RECT_4 = pygame.Rect(60, 540, 800, RECT_SIZE)   # Down vertical border

END_LINE = pygame.Rect(860, 540, 90, RECT_SIZE) # End the game

# Walls of the maze:

WALLS = [
    pygame.Rect(60, 350, 120, RECT_SIZE),   # 1
    pygame.Rect(400, 440, RECT_SIZE, 100),  # 2
    pygame.Rect(750, 440, 200, RECT_SIZE),  # 3
    pygame.Rect(850, 250, 100, RECT_SIZE),  # 4
    pygame.Rect(850, 260, RECT_SIZE, 100)   # 5
]