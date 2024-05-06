# from setting, import everything
from setting import *
from sys import exit
import matplotlib.pyplot as plt
import numpy as np

#components
from game import Game
from score import Score
from preview import Preview

from random import choice

class Main:

    def __init__(self):
        # general
        pygame.init()
        #display layout
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        # shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
       

        # components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level
        
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            #Background fill color
            # self.display_surface.fill((0, 0, 0))
            gradient_colors = [(255, 255, 255), (242, 98, 241)] 
            num_gradient_steps = WINDOW_HEIGHT  # Number of steps in the gradient
            gradient_step = 1 / num_gradient_steps
            
            for i in range(num_gradient_steps):
                color = tuple(int(gradient_colors[0][c] * (1 - gradient_step * i) + gradient_colors[1][c] * gradient_step * i) for c in range(3))
                pygame.draw.rect(self.display_surface, color, (0, i, WINDOW_WIDTH, 1))

            #Run the game.py settings
            self.game.run() 
            self.score.run()
            self.preview.run(self.next_shapes)

            pygame.display.update()
            self.clock.tick()

# to make sure we only run our setting and not anything else
if __name__ == '__main__':
    main = Main()
    main.run()