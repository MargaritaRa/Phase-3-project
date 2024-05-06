from setting import *
from pygame.image import load
from os import path
import matplotlib.pyplot as plt
import numpy as np

class Preview:
    def __init__(self):

        #general
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING, PADDING))

        # shapes
        self.shape_surfaces = {shape: load(path.join('.','graphics',f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}
        
        #  image poisition data
        self.increment_height = self.surface.get_height() / 3

    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center = (x, y))
            self.surface.blit(shape_surface,rect)

    def run(self, next_shapes):
        self.surface.fill(BACKGROUND)
        # gradient_colors = [(255, 255, 255), (242, 98, 241)] 
        # num_gradient_steps = WINDOW_HEIGHT  # Number of steps in the gradient
        # gradient_step = 1 / num_gradient_steps
            
        # for i in range(num_gradient_steps):
        #     color = tuple(int(gradient_colors[0][c] * (1 - gradient_step * i) + gradient_colors[1][c] * gradient_step * i) for c in range(3))
        #     pygame.draw.rect(self.display_surface, color, (0, i, WINDOW_WIDTH, 1))

        self.display_pieces(next_shapes)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, LINE_WHITE, self.rect, 2, 2)