import pygame
import random
import copy

import constants


class Grid:

    def __init__(self) -> None:
        self.__current_state: list[list[bool]] = [[random.choice([0, 0, 0, 1]) for _ in range(constants.NUMBER_OF_SQUARES)] for _ in range(constants.NUMBER_OF_SQUARES)]
        self.__next_state: list[list[bool]] = copy.deepcopy(self.__current_state)

    def __get_neighbors_alive(self, line: int, column: int) -> int:
        alive = 0

        for d_line in range(-1, 2):
            for d_column in range(-1, 2):
                
                if (d_line == 0 and d_column == 0 or 
                    not (-1 < d_line + line < constants.NUMBER_OF_SQUARES and -1 < d_column + column < constants.NUMBER_OF_SQUARES)):
                    continue
                
                if self.__current_state[d_line + line][d_column + column]:
                    alive += 1

        return alive

    def handle_click(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x, mouse_y = int(mouse_x // constants.SQUARE_WIDTH), int(mouse_y // constants.SQUARE_HEIGHT)

            if (0 < mouse_x < constants.NUMBER_OF_SQUARES and
                0 < mouse_y < constants.NUMBER_OF_SQUARES):
                self.__current_state[mouse_y][mouse_x] = not self.__current_state[mouse_y][mouse_x]

    def update(self): 

        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                neighbors = self.__get_neighbors_alive(line, column)

                if self.__current_state[line][column] and neighbors < 2:
                    self.__next_state[line][column] = False
                elif self.__current_state[line][column] and neighbors > 3:
                    self.__next_state[line][column] = False
                elif neighbors == 3:
                    self.__next_state[line][column] = True
                elif neighbors == 2:
                    self.__next_state[line][column] = self.__current_state[line][column]
                    pass

        self.__current_state: list[list[bool]] = copy.deepcopy(self.__next_state)
    
    def draw_at(self, surface: pygame.Surface) -> None:
        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                pygame.draw.rect(surface,
                                 constants.SQUARE_COLOR_WHEN_ALIVE if self.__current_state[line][column] else constants.SQUARE_COLOR_WHEN_DEAD, 
                                 pygame.Rect(column * constants.SQUARE_HEIGHT + 1, 
                                             line * constants.SQUARE_WIDTH + 1, 
                                             constants.SQUARE_WIDTH - 2, 
                                             constants.SQUARE_HEIGHT - 2))