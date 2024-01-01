import pygame 

import grid


class App:

    def __init__(self) -> None:
        self.__running: bool = True
        self.__grid: grid.Grid = grid.Grid()
        self.__surface: pygame.Surface = pygame.display.set_mode((600, 600)) 

    def is_running(self) -> bool:
        return self.__running

    def handle_events(self) -> None:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("TODO App::handle_events::MOUSEBUtTONDOWN")

    def handle_update(self) -> None:
        print("TODO App::handle_update")

    def handle_render(self) -> None:
        
        self.__grid.draw_at(self.__surface)
        
        pygame.display.flip()

    def run(self) -> None:
        pygame.init()

        while self.is_running():
            self.handle_events()
            self.handle_update()
            self.handle_render()