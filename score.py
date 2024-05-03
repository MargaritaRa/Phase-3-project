from setting import *
from os.path import join

class Score:
    def __init__(self):
        #placing the score surface ontop of the original surface
        # Game height and scoreboard need to have the same height, * the percentage we want it to take up, minus the padding
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        #rectangle that move things around
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface()

        #  font
        self.font = pygame.font.Font(join('.', 'graphics', 'Russo_One.ttf'),30)

        # increment
        self.increment_height = self.surface.get_height() /3

        # data
        self.score = 0
        self.level = 1
        self.lines = 0
    
    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white')
        text_rext = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rext)
    
    def run(self):
        #blit places one surface on top of another
        self.surface.fill(BACKGROUND)
        for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x,y), text)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, LINE_WHITE, self.rect, 2, 2)