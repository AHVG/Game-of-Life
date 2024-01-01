import pygame 
import random

import constants

class App:

    def __init__(self) -> None:
        self.__running: bool = True
        self.__grid: list[list[bool]] = [[random.randint(0, 1) for _ in range(constants.NUMBER_OF_SQUARES)] for _ in range(constants.NUMBER_OF_SQUARES)]
        self.__surface = pygame.display.set_mode((600, 600)) 

    def is_running(self) -> bool:
        return self.__running

    def handle_render(self) -> None:
        
        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                pygame.draw.rect(self.__surface,
                                 constants.SQUARE_COLOR_ON_LIFE if self.__grid[line][column] else constants.SQUARE_COLOR_ON_DEATH, 
                                 pygame.Rect(column * constants.SQUARE_HEIGHT, 
                                             line * constants.SQUARE_WIDTH, 
                                             constants.SQUARE_WIDTH, 
                                             constants.SQUARE_HEIGHT)) 
        
        pygame.display.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

    def run(self) -> None:
        pygame.init()
        while self.is_running():
            self.handle_events()
            self.handle_render()