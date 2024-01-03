import pygame
import random
import copy

import constants
import tile


class Grid:

    # TODO: fazer tamanho variavel do grid para o usuario escolher
    # TODO: trocar square por tile

    def __init__(self) -> None:
        self.__current_state: list[list[tile.Tile]] = [[tile.Tile(random.choices([False, True], [3, 1], k=1)[0],
                                                             pygame.Rect(column * constants.SQUARE_WIDTH + constants.MARGIN_BETWEEN_TILE + constants.MENU_SIZE[0], 
                                                             line * constants.SQUARE_HEIGHT + constants.MARGIN_BETWEEN_TILE, 
                                                             constants.SQUARE_WIDTH - 2 * constants.MARGIN_BETWEEN_TILE, 
                                                             constants.SQUARE_HEIGHT - 2 * constants.MARGIN_BETWEEN_TILE)) for column in range(constants.NUMBER_OF_SQUARES)] 
                                                  for line in range(constants.NUMBER_OF_SQUARES)]
        self.__next_state: list[list[tile.Tile]] = copy.deepcopy(self.__current_state)
        self.__frames_per_second: int = 20
        self.__frames: int = 0
        self.__paused: bool = False

        self.__helper_title_font = pygame.font.Font("./fonts/Minecraft.ttf", 50)
        self.__helper_font = pygame.font.Font("./fonts/Minecraft.ttf", 21)

        self.__speed_font = pygame.font.Font("./fonts/Minecraft.ttf", 25)

        self.__helper_title = self.__helper_title_font.render('Keys', False, (180, 180, 180))
        self.__arrow_up_text = self.__helper_font.render('Arrow UP - Increase simulation speed', False, (180, 180, 180))
        self.__arrow_down_text = self.__helper_font.render('Arrow DOWN - Decrease simulation speed', False, (180, 180, 180))
        self.__r_text = self.__helper_font.render('R - Reset the grid randomly', False, (180, 180, 180))
        self.__p_text = self.__helper_font.render('P - Pause the grid', False, (180, 180, 180))
        self.__click_text = self.__helper_font.render('Click - Switch tile state', False, (180, 180, 180))

        self.__speed_text = self.__speed_font.render(f"Speed: {self.__frames_per_second} frames per second", False, (180, 180, 180))


    def __reset(self):
        self.__current_state = [[tile.Tile(random.choices([False, True], [3, 1], k=1)[0],
                                                             pygame.Rect(column * constants.SQUARE_WIDTH + constants.MARGIN_BETWEEN_TILE + constants.MENU_SIZE[0], 
                                                             line * constants.SQUARE_HEIGHT + constants.MARGIN_BETWEEN_TILE, 
                                                             constants.SQUARE_WIDTH - 2 * constants.MARGIN_BETWEEN_TILE, 
                                                             constants.SQUARE_HEIGHT - 2 * constants.MARGIN_BETWEEN_TILE)) for column in range(constants.NUMBER_OF_SQUARES)] 
                                                  for line in range(constants.NUMBER_OF_SQUARES)]
        self.__next_state = copy.deepcopy(self.__current_state)


    def __get_neighbors_alive(self, line: int, column: int) -> int:
        alive = 0

        for d_line in range(-1, 2):
            for d_column in range(-1, 2):
                
                if (d_line == 0 and d_column == 0 or 
                    not (-1 < d_line + line < constants.NUMBER_OF_SQUARES and -1 < d_column + column < constants.NUMBER_OF_SQUARES)):
                    continue
                
                if self.__current_state[d_line + line][d_column + column].is_alive():
                    alive += 1

        return alive


    def handle_click(self) -> None:

        if pygame.mouse.get_pressed()[0]:
            for line in self.__current_state:
                for tile in line:
                    if tile.get_rect().collidepoint(pygame.mouse.get_pos()):
                        tile.switch_state()


    def handle_keydown(self, key: int) -> None:

        if key == pygame.K_DOWN:
            if self.__frames_per_second > constants.MIN_FRAMES:
                self.__frames_per_second -= constants.FRAME_STEP

        elif key == pygame.K_UP:
            if self.__frames_per_second < constants.MAX_FRAMES:
                self.__frames_per_second += constants.FRAME_STEP

        elif key == pygame.K_p:
            self.__paused = not self.__paused

        elif key == pygame.K_r:
            self.__reset()


    def update(self) -> None:

        if not self.__paused:
            self.__frames += 1

            if self.__frames >= 60.0 / self.__frames_per_second:
                self.__frames = 0

                for line in range(constants.NUMBER_OF_SQUARES):
                    for column in range(constants.NUMBER_OF_SQUARES):
                        neighbors = self.__get_neighbors_alive(line, column)

                        if self.__current_state[line][column] and neighbors < 2:
                            self.__next_state[line][column].kill()

                        elif self.__current_state[line][column] and neighbors > 3:
                            self.__next_state[line][column].kill()

                        elif neighbors == 3:
                            self.__next_state[line][column].revive()

                        elif neighbors == 2:
                            self.__next_state[line][column].keep_state()

                self.__current_state = copy.deepcopy(self.__next_state)

        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                self.__current_state[line][column].update()


    def draw_at(self, surface: pygame.Surface) -> None:

        surface.blit(self.__helper_title, (10, 30))
        surface.blit(self.__arrow_up_text, (10, 110))
        surface.blit(self.__arrow_down_text, (10, 150))
        surface.blit(self.__r_text, (10, 190))
        surface.blit(self.__p_text, (10, 230))
        surface.blit(self.__click_text, (10, 270))

        self.__speed_text = self.__speed_font.render(f"Speed: {self.__frames_per_second} frames per second", False, (180, 180, 180))
        surface.blit(self.__speed_text, (10, 390))

        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                self.__current_state[line][column].draw_at(surface)
