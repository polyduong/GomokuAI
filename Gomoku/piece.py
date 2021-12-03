import pygame

from .constants import SQUARE_SIZE, CIRCLE_COLOR, CROSS_COLOR, CIRCLE_WIDTH, CIRCLE_RADIUS, SPACE, CROSS_WIDTH , P1, P2


class Piece:
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        # self.color = color
        self.player = player
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, screen):
        if self.player == P1:
            pygame.draw.circle(screen, CIRCLE_COLOR, (self.x, self.y), CIRCLE_RADIUS, CIRCLE_WIDTH)
        elif self.player == P2:
            pygame.draw.line(screen, CROSS_COLOR, (self.x + SPACE, self.y - SPACE), (self.x - SPACE, self.y + SPACE),
                             CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOR, (self.x + SPACE, self.y + SPACE), (self.x - SPACE, self.y - SPACE),
                             CROSS_WIDTH)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # def __repr__(self):
    #     return str(self.color)