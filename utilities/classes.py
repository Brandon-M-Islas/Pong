# Import modules
import               pygame
from win32api import GetSystemMetrics
from random   import random

# Holds the dimensions of the current screen
class Screen:
    def __init__(self, width=0.7*GetSystemMetrics(0), height=0.7*GetSystemMetrics(1)):
        self.width  = width 
        self.height = height

# Main object to define all objects used in this project
class Object:

    # What happens when object is instantiated
    def __init__(self, SCREEN: Screen, POSITION: str):

        # Class Attributes
        self.color     = "white"
        self.side      = POSITION
        self.speed     = 0
        self.x_speed   = 0 
        self.y_speed   = 0
        self.moving    = False
        self.key       = None
        self.set(SCREEN)

    # What happens when print(Object())
    def __str__(self):
        return self.side

    # Setting the dimensions and position of the object
    def set(self, SCREEN: Screen):

        # Check what object is being set and then set the position and size (and speed for moving objects)
        match self.side:
            case       "LEFT":
                self.rect            = pygame.Rect(0, 0, 0.02*SCREEN.width,  SCREEN.height     )
                self.rect.topright   = (0, 0) 
            case      "RIGHT":
                self.rect            = pygame.Rect(0, 0, 0.03*SCREEN.width,  SCREEN.height     )
                self.rect.topleft    = (SCREEN.width, 0)
            case        "TOP":
                self.rect            = pygame.Rect(0, 0, SCREEN.width,       0.02*SCREEN.height)
                self.rect.bottomleft = (0, 0)
            case     "BOTTOM":
                self.rect            = pygame.Rect(0, 0, SCREEN.width,       0.03*SCREEN.height)
                self.rect.topleft    = (0, SCREEN.height)
            case    "DIVIDER":
                self.rect            = pygame.Rect(0, 0, 0.005*SCREEN.width, SCREEN.height     )
                self.rect.topleft    = (0.5*SCREEN.width - 0.5*self.rect.width, 0)
            case "PLAYER ONE":
                self.rect            = pygame.Rect(0, 0, 0.01*SCREEN.width,  0.2*SCREEN.height )
                self.rect.center     = (0.02*SCREEN.width, 0.5*SCREEN.height) 
                self.speed           = (SCREEN.height - self.rect.height) / 90
                self.y_speed         = (SCREEN.height - self.rect.height) / 90
            case "PLAYER TWO":
                self.rect            = pygame.Rect(0, 0, 0.01*SCREEN.width,  0.2*SCREEN.height )
                self.rect.center     = (0.98*SCREEN.width, 0.5*SCREEN.height) 
                self.speed           = (SCREEN.height - self.rect.height) / 90
                self.y_speed         = (SCREEN.height - self.rect.height) / 90
            case "BALL":
                self.rect            = pygame.Rect(0, 0, 0.01*SCREEN.width,  0.01*SCREEN.width )
                self.rect.center     = (0.5*SCREEN.width, 0.5*SCREEN.height)
                self.speed           = (SCREEN.width - self.rect.width) / 90
                self.x_speed         = (1 if random() < 0.5 else -1) * self.speed
                self.y_speed         = 0
                self.moving          = True

        # If the size gets too small it sets to 0, so just set it to 1 instead 
        if self.rect.width   == 0:
            self.rect.width  = 1
        if self.rect.height  == 0:
            self.rect.height = 1

    # Moving the object
    def move(self):

        # Check if this object is moving
        if self.moving:
            
            # Check what object is moving
            match self.side:

                # Check what key is being pressed and then move in that direction
                case "PLAYER ONE":        
                    match self.key:
                        case pygame.K_w:
                            self.rect = self.rect.move(0, -self.y_speed)
                        case pygame.K_s:
                            self.rect = self.rect.move(0,  self.y_speed)
                case "PLAYER TWO":
                    match self.key:
                        case pygame.K_UP:
                            self.rect = self.rect.move(0, -self.y_speed)
                        case pygame.K_DOWN:
                            self.rect = self.rect.move(0,  self.y_speed)
                case "BALL":
                    self.rect = self.rect.move(self.x_speed, self.y_speed)
