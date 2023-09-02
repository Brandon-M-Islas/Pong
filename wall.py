import               pygame
from win32api import GetSystemMetrics

class Screen:
    height = 0.5 * GetSystemMetrics(0) 
    width  = 0.5 * GetSystemMetrics(1)

class Scale:
    y = 1
    x = 1

class Wall:

    def __init__(self, SCREEN: Screen, SIDE: str):
        print(SCREEN.__dict__)
        match SIDE:
            case "LEFT":
                self.rect = pygame.rect(0, 0, 0.2*SCREEN.width, SCREEN.height)
            case "RIGHT":
                self.rect = pygame.rect(0.8*SCREEN.width, 0, 0.2*SCREEN.width, SCREEN.height)
            case "TOP":
                self.rect = pygame.rect(0, 0, SCREEN.width, 0.2*SCREEN.height)
            case "BOTTOM":
                self.rect = pygame.rect(0, 0.8*SCREEN.height, SCREEN.width, 0.2*SCREEN.height)
        

    def __str__(self):
        return f"wall"

    def myfunc(self):
        pass