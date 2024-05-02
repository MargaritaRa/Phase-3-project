from setting import *
from random import choice
from timer import Timer

class Game:
    def __init__(self):
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        #lines
        #let's make a copy of the surface that works on it's own
        self.line_surface = self.surface.copy()
        self.line_surface.fill ((0,255,0))
        #tells hide this color and never show again
        self.line_surface.set_colorkey((0,255,0))
        #line transparancy 
        self.line_surface.set_alpha(120)

        #tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

        #  timer
        self.timers = {
            'vertical move': Timer(UPDATE_START_SPEED, True, self.move_down),
            'horizontal move': Timer(MOVE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()
        
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

    def draw_grid(self):

        # don't want to start at zero, want to start at 1
        for col in range(1,COLUMNS):
            x = col * CELL_SIZE
            # this takes in 4 position for the draw.line(surface, color, start_position, end_position, width)
            pygame.draw.line(self.line_surface, LINE_WHITE , (x,0 ), (x, self.surface.get_height()), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_WHITE , (0,y), (self.surface.get_width(),y))
        
        self.surface.blit(self.line_surface, (0,0))

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()

    def run(self):
        # update
        self.input()
        self.timer_update()
        self.sprites.update()


        #drawing
        self.surface.fill(BACKGROUND)
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        # pygame.draw.rect(surface, color, rect, width, corner radius)
        pygame.draw.rect(self.display_surface, LINE_WHITE, self.rect, 2, 2)

class Tetromino:
    #  takes blocks and place them in a specifi shape
    def __init__(self, shape, group):

        #setup
        self.block_positions = TETROMINOS[shape]["shape"]
        self.color = TETROMINOS[shape]["color"]

        #create blocks
        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]
    
    # collisions
    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount)) for block in self.blocks]
        return True if any(collision_list) else False
    
    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y + amount)) for block in self.blocks]
        return True if any(collision_list) else False
    
    # movement
    def move_horizontal(self, amount):
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount

    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1

class Block(pygame.sprite.Sprite):
    # Sprite a class bulit in that makes it easy to build a surface with a rectangle
    def __init__(self, group, pos, color):

        #general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE,CELL_SIZE))
        self.image.fill(color)

        #position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

    def horizontal_collide(self, x):
        if not 0 <= x < COLUMNS:
            return True
    
    def vertical_collide(self, y):
        if y >= ROWS:
            return True
        
    def update(self):
        # self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)
        self.rect.topleft = self.pos * CELL_SIZE

