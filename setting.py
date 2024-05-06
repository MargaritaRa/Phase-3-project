import pygame
from colour import Color


#Game size
COLUMNS = 10
ROWS = 20
# how large a cell is, how wide and tall
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

#window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

#game behavior
UPDATE_START_SPEED = 700
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET =  pygame.Vector2(COLUMNS // 2, -1)

#color
red = Color("#d11836")
colors = list(red.range_to(Color("#1fd118"),10))
BACKGROUND = '#4d4d4d'
LINE_WHITE = "#ffffff"
BLACK = "#000000"
PURPLE = '#8b43cc'
YELLOW = '#e8d915'
BLUE =  '#155be8'
ORANGE = '#e89915'
CYAN = '#43b4a4'
GREEN = '#1fd118'
RED = "#d11836"
PINK = "#f262f1"

#shapes
TETROMINOS = {
    "T" : { "shape": [(0,0), (-1,0), (1,0), (0,-1)], "color": PURPLE},
    "O" : { "shape": [(0,0), (0,-1), (1,0), (1,-1)], "color": YELLOW},
    "J" : { "shape": [(0,0), (0,-1), (0,1), (-1,1)], "color": BLUE},
    "L" : { "shape": [(0,0), (0,-1), (0,1), (1,1)], "color": ORANGE},
    "I" : { "shape": [(0,0), (0,-1), (0,-2), (0,1)], "color": CYAN},
    "S" : { "shape": [(0,0), (-1,0), (0,-1), (1,-1)], "color": GREEN},
    "Z" : { "shape": [(0,0), (1,0), (0, -1), (-1,-1)], "color": RED},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}
