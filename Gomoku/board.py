import pygame
import numpy as np
from .piece import Piece
from .constants import ROWS, BG_COLOR, LINE_COLOR, LINE_WIDTH, SQUARE_SIZE, WIDTH, HEIGHT, COLS, P1, P2, CIRCLE_COLOR, CROSS_COLOR

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.create_board()

    def draw_line(self, screen):
        screen.fill(BG_COLOR)
        line = 1

        for row in range(ROWS - 1):
            pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * line), (WIDTH, SQUARE_SIZE * line), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * line, 0), (SQUARE_SIZE * line, HEIGHT), LINE_WIDTH)
            line += 1

    # def draw_piece(self, screen):
    #     self.draw_line(screen)
    #     for row in range(ROWS):
    #         for col in range(COLS):
    #             piece = self.board[row][col]
    #             if piece != 0:
    #                 piece.draw(screen)
                # if self.board[row][col] == P1:
                #     Piece.draw(screen)
                # elif self.board[row][col] == P2:
                #     Piece.draw(screen)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col] = self.board[row][col]
        piece.move(row, col)

    def get_piece(self, row, col, player):
        self.board[row][col] = Piece(row, col, player)

    def set_empty(self):
        for i in range(ROWS):
            for j in range(COLS):
                self.board[i][j] = 0

    def check_win(self, x, y, player):
        count = 0
        i, j = x, y
        while (j < COLS and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            j += 1
        j = y
        while (j >= 0 and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            j -= 1
        if count >= 6:
            return True
        # check cột
        count = 0
        i, j = x, y
        while (i < ROWS and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            i += 1
        i = x
        while (i >= 0 and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            i -= 1
        if count >= 6:
            return True
        # check cheo phai
        count = 0
        i, j = x, y
        while (i >= 0 and j < COLS and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            i -= 1
            j += 1
        i, j = x, y
        while (i <= ROWS and j >= 0 and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            i += 1
            j -= 1
        if count >= 6:
            return True
        # check cheo trai
        count = 0
        i, j = x, y
        while (i < COLS and j < ROWS and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            i += 1
            j += 1
        i, j = x, y
        while (i >= 0 and j >= 0 and type(self.board[i][j]) == type(Piece(0, 0, 0)) and self.board[i][j].player == player):
            count += 1
            i -= 1
            j -= 1
        if count >= 6:
            return True
        return False

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    def draw_piece(self, screen):
        self.draw_line(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    return False
        return True
