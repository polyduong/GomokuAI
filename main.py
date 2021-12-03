import pygame
import numpy as np
from Gomoku.constants import WIDTH, HEIGHT, SQUARE_SIZE, ROWS, COLS
from Gomoku.board import Board
import ctypes
import pygame_menu
import random

FPS = 60
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.display.set_mode((WIDTH, HEIGHT))
history = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gomoku Game')
global results
results = []

def get_pos_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def choose_option():
    global diff
    diff = 1
    def set_difficulty(value, difficulty):
        global diff
        diff = difficulty

    def play_game():
        global diff
        new_game(diff)

    def show_results():
        global results
        show(results)
        for item in results:
            print(item)
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Results ', show_results)
    menu.add.selector('Difficulty :', [('User1 Vs User2', 1), ('User1 Vs System', 2)], onchange=set_difficulty)
    menu.add.button('Play ', play_game)
    menu.add.button('Quit ', pygame_menu.events.EXIT)
    menu.mainloop(surface)

def show(results):
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE)
    idx = 1
    for item in results:
        menu.add.text_input('Game ' + str(idx) + ':', default=item)
        idx += 1

    def back():
        choose_option()
    menu.add.button('Back ', back)
    menu.mainloop(history)


def new_game(diff):
    run = True
    clock = pygame.time.Clock()
    board = Board()
    player = 1

    def get_random():
        while True:
            i = random.randint(0, ROWS)
            j = random.randint(0, COLS)
            if i < ROWS and j < COLS and board.available_square(i, j)\
                    and ((j - 1 >=0 and not board.available_square(i, j - 1))
                         or (j + 1 < COLS and not board.available_square(i, j + 1))
                         or (i - 1 >= 0 and not board.available_square(i - 1, j))
                         or (i + 1 < ROWS and not board.available_square(i + 1, j))):
                return i, j

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            global results

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                if board.available_square(row, col):
                    board.get_piece(row, col, player)
                    if board.check_win(row, col, player):
                        board.draw_piece(SCREEN)
                        pygame.display.update()
                        if player == 1:
                            mess = "User1 Thang!"
                        else:
                            mess = "User2 Thang!"
                        results.append(mess)
                        if ctypes.windll.user32.MessageBoxW(0, mess, "Greetings", 1):
                            board.set_empty()
                            choose_option()
                    player = player % 2 + 1
                    if player == 2 and diff == 2:
                        i, j = get_random()
                        board.get_piece(i, j, player)
                        if board.check_win(i, j, player):
                            board.draw_piece(SCREEN)
                            pygame.display.update()
                            if player == 1:
                                mess = "User1 Thang!"
                            else:
                                mess = "System Thang!"
                            results.append(mess)
                            if ctypes.windll.user32.MessageBoxW(0, mess, "Greetings", 1):
                                board.set_empty()
                                choose_option()
                        player = player % 2 + 1

        board.draw_piece(SCREEN)
        pygame.display.update()
    pygame.quit()

choose_option()
