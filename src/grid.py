import pygame
import random
import copy

import constants


class Grid:

    # TODO: Fazer uma classe para tile?

    def __init__(self) -> None:
        self.__current_state: list[list[bool]] = [[random.choice([0, 0, 0, 1]) for _ in range(constants.NUMBER_OF_SQUARES)] for _ in range(constants.NUMBER_OF_SQUARES)]
        self.__next_state: list[list[bool]] = copy.deepcopy(self.__current_state)
        self.__number_of_frames_until_updated: int = 20
        self.__frames: int = 0
        self.__paused: bool = False


    def __reset(self):
        self.__current_state = [[random.choice([0, 0, 0, 1]) for _ in range(constants.NUMBER_OF_SQUARES)] for _ in range(constants.NUMBER_OF_SQUARES)]
        self.__next_state = copy.deepcopy(self.__current_state)


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


    def handle_click(self) -> None:

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if mouse_x < constants.MENU_SIZE[0]:
                return
            
            mouse_x -= constants.MENU_SIZE[0]
            
            mouse_x, mouse_y = int(mouse_x// constants.SQUARE_WIDTH), int(mouse_y // constants.SQUARE_HEIGHT)

            if (0 < mouse_x < constants.NUMBER_OF_SQUARES and
                0 < mouse_y < constants.NUMBER_OF_SQUARES):
                self.__current_state[mouse_y][mouse_x] = not self.__current_state[mouse_y][mouse_x]


    def handle_keydown(self, key: int) -> None:

        if key == pygame.K_UP:
            self.__number_of_frames_until_updated -= 5

            if self.__number_of_frames_until_updated < constants.MIN_FRAMES:
                self.__number_of_frames_until_updated += 5

        elif key == pygame.K_DOWN:
            self.__number_of_frames_until_updated += 5

            if self.__number_of_frames_until_updated > constants.MAX_FRAMES:
                self.__number_of_frames_until_updated -= 5

        elif key == pygame.K_p:
            self.__paused = not self.__paused

        elif key == pygame.K_r:
            self.__reset()


    def update(self) -> None:

        if self.__paused:
            return

        self.__frames += 1

        if self.__frames < self.__number_of_frames_until_updated:
            return

        self.__frames = 0

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

        self.__current_state: list[list[bool]] = copy.deepcopy(self.__next_state)


    def draw_at(self, surface: pygame.Surface) -> None:

        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                pygame.draw.rect(surface,
                                 constants.SQUARE_COLOR_WHEN_ALIVE if self.__current_state[line][column] else constants.SQUARE_COLOR_WHEN_DEAD, 
                                 pygame.Rect(column * constants.SQUARE_WIDTH + 1 + constants.MENU_SIZE[0], 
                                             line * constants.SQUARE_HEIGHT + 1, 
                                             constants.SQUARE_WIDTH - 2, 
                                             constants.SQUARE_HEIGHT - 2))
