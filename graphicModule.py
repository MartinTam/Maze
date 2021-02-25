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


WALLS = [
    
    pygame.Rect(60, 50, 90, RECT_SIZE),     # Start the game
    pygame.Rect(860, 540, 90, RECT_SIZE),   # End the game

    pygame.Rect(50, 50, RECT_SIZE, 500),    # Left vertical border
    pygame.Rect(950, 50, RECT_SIZE, 500),   # Right vertical border
    pygame.Rect(150, 50, 800, RECT_SIZE),   # Up vertical border
    pygame.Rect(60, 540, 800, RECT_SIZE),   # Down vertical border

    pygame.Rect(60, 350, 100, RECT_SIZE),   # 1
    pygame.Rect(410, 440, RECT_SIZE, 100),  # 2
    pygame.Rect(770, 440, 180, RECT_SIZE),  # 3
    pygame.Rect(870, 250, 80, RECT_SIZE),   # 4
    pygame.Rect(870, 260, RECT_SIZE, 100),  # 5

    pygame.Rect(310, 60, RECT_SIZE, 190),   # 6
    pygame.Rect(150, 250, 270, RECT_SIZE),  # 7
    pygame.Rect(410, 260, RECT_SIZE, 100),  # 8
    pygame.Rect(230, 260, RECT_SIZE, 100),  # 9
    pygame.Rect(150, 160, RECT_SIZE, 90),   # 10
    pygame.Rect(150, 150, 90, RECT_SIZE),   # 11
    pygame.Rect(310, 350, 100, RECT_SIZE),  # 12
    pygame.Rect(310, 360, RECT_SIZE, 80),   # 13
    pygame.Rect(150, 440, 170, RECT_SIZE),  # 14

    pygame.Rect(600, 450, RECT_SIZE, 90),   # 15
    pygame.Rect(520, 440, 170, RECT_SIZE),  # 16
    pygame.Rect(520, 350, RECT_SIZE, 100),  # 17
    pygame.Rect(680, 360, RECT_SIZE, 90),   # 18
    pygame.Rect(600, 350, 180, RECT_SIZE),  # 19
    pygame.Rect(770, 160, RECT_SIZE, 200),  # 20
    pygame.Rect(680, 150, 200, RECT_SIZE),  # 21
    pygame.Rect(680, 160, RECT_SIZE, 100),  # 22
    pygame.Rect(600, 260, RECT_SIZE, 90),   # 23
    pygame.Rect(520, 250, 90, RECT_SIZE),   # 24
    pygame.Rect(520, 160, RECT_SIZE, 90),   # 25
    pygame.Rect(410, 150, 120, RECT_SIZE)   # 26
]