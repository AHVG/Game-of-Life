

class App:

    def __init__(self) -> None:
        self.__running = True

    def is_running(self) -> bool:
        return self.__running

    def run(self) -> None:
        while self.is_running():
            print("TODO...")
