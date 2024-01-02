import pygame

import constants


class Tile:

    def __init__(self, alive: bool = False, rect: pygame.Rect = None, selected: bool = False) -> None:
        self.__alive: bool = alive
        self.__selected = selected
        self.__rect = rect

    
    def is_alive(self) -> bool:
        return self.__alive
    

    def kill(self) -> None:
        self.__alive = False

    
    def revive(self) -> None:
        self.__alive = True


    def keep_state(self) -> None:
        pass

    
    def switch_state(self) -> None:
        self.__alive = not self.__alive


    def select(self) -> None:
        self.__selected = True

    
    def get_rect(self) -> pygame.Rect:
        return self.__rect

    
    def update(self) -> None:
        self.__selected = False

        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            self.__selected = True


    def draw_at(self, surface: pygame.Surface) -> None:
        color = constants.SQUARE_COLOR_WHEN_DEAD

        if self.__selected:
            color = constants.SQUARE_COLOR_WHEN_SELECTED
        
        elif self.__alive:
            color = constants.SQUARE_COLOR_WHEN_ALIVE

        
        pygame.draw.rect(surface, color, self.__rect)