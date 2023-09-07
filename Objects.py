import pygame
from pygame.locals import *
from random import random
from math import copysign, sin, cos, radians

class Ball(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, screen, groups):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, groups)

        self.descriptor = "BALL"
        self.resize(screen)

    def resize(self, screen):

        # Save the width and height for use
        screen_width  = screen.get_width()
        screen_height = screen.get_height()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([0.01*screen_width if 0.01*screen_width > 2 else 2 , 0.01*screen_width if 0.01*screen_width > 2 else 2])
        pygame.draw.circle(self.image, "white", self.image.get_rect().center, self.image.get_rect().width/2)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect        = self.image.get_rect()
        self.rect.center = (0.5*screen_width, 0.5*screen_height)

        # Add the speed
        self.speed       = (screen_width - self.rect.width) / 90
        self.x_speed     = (1 if random() < 0.5 else -1) * self.speed
        self.y_speed     = 0

    def update(self):
        self.rect = self.rect.move(self.x_speed, self.y_speed)

    def collision(self, ELEMENTS):
    
        LEFT_WALL   = ELEMENTS["ALL"].sprites()[1]
        RIGHT_WALL  = ELEMENTS["ALL"].sprites()[2]
        TOP_WALL    = ELEMENTS["ALL"].sprites()[3]
        BOTTOM_WALL = ELEMENTS["ALL"].sprites()[4]
        PLAYER_ONE  = ELEMENTS["ALL"].sprites()[5]
        PLAYER_TWO  = ELEMENTS["ALL"].sprites()[6]
        SCOREBOARD  = ELEMENTS["ALL"].sprites()[7]
        screen      = ELEMENTS["screen"]
        
        # Check if the ball has met any of the walls or players and change it's direction or assing points
        collidable = [LEFT_WALL, 
                    RIGHT_WALL, 
                    TOP_WALL, 
                    BOTTOM_WALL, 
                    PLAYER_ONE, 
                    PLAYER_TWO]

        collision = self.rect.collidelist(collidable)
        
        # If ball hits the left wall
        if collision == 0:

            # Reset the ball and give player two a point
            self.resize(screen)
            PLAYER_ONE.resize(screen)
            PLAYER_TWO.resize(screen)
            SCOREBOARD.player_two_score += 1
            SCOREBOARD.resize(screen)

        # If ball hits the right wall
        elif collision == 1:

            # Reset the ball and give player one a point
            self.resize(screen)
            PLAYER_ONE.resize(screen)
            PLAYER_TWO.resize(screen)
            SCOREBOARD.player_one_score += 1
            SCOREBOARD.resize(screen)

        # If ball hits the top or bottom wall
        elif collision in (2, 3):

            # Change the vertical direction
            self.y_speed = -self.y_speed
            self.update()

        # If ball hits either player
        elif collision in (4, 5):

            # Determine angle
            if self.rect.center[1]   > collidable[collision].rect.bottom:
                BALL_CENTER = collidable[collision].rect.bottom
            elif self.rect.center[1] < collidable[collision].rect.top:
                BALL_CENTER = collidable[collision].rect.top
            else:
                BALL_CENTER = self.rect.center[1]

            PLAYER_DISTANCE   = collidable[collision].rect.height / 2
            RELATIVE_DISTANCE = (BALL_CENTER - collidable[collision].rect.center[1]) / PLAYER_DISTANCE
            ANGLE             = RELATIVE_DISTANCE * 45

            # Change the horizontal direction
            self.x_speed = -(copysign(1, self.x_speed))*self.speed*abs(cos(radians(ANGLE)))

            # Change the vertical direction
            self.y_speed = self.speed*sin(radians(ANGLE))

            # Move the ball
            self.update()

class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, screen, port, groups):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, groups)

        self.descriptor = "PLAYER " + port
        self.key = None
        self.resize(screen)

    def resize(self, screen):

        screen_width  = screen.get_width()
        screen_height = screen.get_height()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([0.01*screen_width if 0.01*screen_width > 1 else 1, 0.2*screen_height if 0.2*screen_height > 1 else 1])
        self.image.fill("white")

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect  = self.image.get_rect()

        self.speed = (screen_height - self.rect.height) / 90

        match self.descriptor:
            case "PLAYER ONE":
                self.rect.center = (0.02*screen_width, 0.5*screen_height) 
            case "PLAYER TWO":
                self.rect.center = (0.98*screen_width, 0.5*screen_height) 

    def update(self):

        if self.key == "UP":
            self.rect = self.rect.move(0, -self.speed)
        elif self.key == "DOWN":
            self.rect = self.rect.move(0,  self.speed)


    def collision(self, ELEMENTS):

        CONTAINER = ELEMENTS["ALL"]

        collision = self.rect.collidelist([CONTAINER.sprites()[3], CONTAINER.sprites()[4]])

        if collision == 0:
            self.rect.top = CONTAINER.sprites()[3].rect.bottom
        if collision == 1:
            self.rect.bottom = CONTAINER.sprites()[4].rect.top

class Text(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, screen, level, text, groups):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, groups)

        self.level = level
        self.text = text
        self.descriptor = self.level + ": " + self.text
        if self.descriptor == "SCOREBOARD: SCORE":
            self.player_one_score = 0
            self.player_two_score = 0
        self.resize(screen)

    def resize(self, screen):

        screen_width  = screen.get_width()
        screen_height = screen.get_height()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        pygame.freetype.init()

        match self.level:
            case "TITLE":
                self.font = pygame.freetype.SysFont("Ariel", screen_width*0.1)
                self.image, self.rect = self.font.render(self.text, (255, 255, 255))
                self.rect.topleft = ((screen.get_width()-self.rect.width)/2, 0.1*screen.get_height())
            case "OPTION":
                self.font = pygame.freetype.SysFont("Ariel", screen_width*0.05)
                self.image, self.rect = self.font.render(self.text, (255, 255, 255))
                match self.text:
                    case "SINGLE PLAYER" | "CONTINUE":
                        self.rect.topleft = ((screen.get_width()-self.rect.width)/2, 0.5*screen.get_height())
                    case "TWO PLAYER" | "RETURN TO MAIN MENU":
                        self.rect.topleft = ((screen.get_width()-self.rect.width)/2, 0.6*screen.get_height())
                    case "EXIT":
                        self.rect.topleft = ((screen.get_width()-self.rect.width)/2, 0.7*screen.get_height())
            case "SCOREBOARD":
                self.font = pygame.freetype.SysFont("Ariel", screen_width*0.02)
                self.image, self.rect = self.font.render(f"{self.player_one_score}    {self.text}    {self.player_two_score}", (255, 255, 255))
                self.rect.topleft = ((screen.get_width()-self.rect.width)/2, 0.01*screen.get_height())

    def update(self):
        pass

    def collision(self, ALL):
        pass

class Wall(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, screen, side, groups):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, groups)

        self.descriptor = side + " WALL"
        self.resize(screen)

    def resize(self, screen):

        screen_width  = screen.get_width()
        screen_height = screen.get_height()

        match self.descriptor:
            case       "LEFT WALL":
                self.rect            = pygame.Rect(0, 0, 0.02*screen_width if 0.02*screen_width > 1 else 1, screen_height)
                self.rect.topright   = (0, 0) 
            case      "RIGHT WALL":
                self.rect            = pygame.Rect(0, 0, 0.03*screen_width if 0.03*screen_width > 1 else 1, screen_height)
                self.rect.topleft    = (screen_width, 0)
            case        "TOP WALL":
                self.rect            = pygame.Rect(0, 0, screen_width, 0.02*screen_height if 0.02*screen_height > 1 else 1)
                self.rect.bottomleft = (0, 0)
            case     "BOTTOM WALL":
                self.rect            = pygame.Rect(0, 0, screen_width, 0.03*screen_height if 0.03*screen_height > 1 else 1)
                self.rect.topleft    = (0, screen_height)

    def collision(self):
        pass

class Arrow(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, screen, groups):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, groups)

        self.descriptor = "ARROW"
        self.option = "SINGLE PLAYER"
        self.resize(screen)

    def resize(self, screen):

        screen_width  = screen.get_width()
        screen_height = screen.get_height()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        pygame.freetype.init()
        font = pygame.freetype.SysFont("Ariel", screen_width*0.05)
        text_image, text_rect = font.render("SINGLE PLAYER", (255, 255, 255))

        arrow = pygame.Surface([100, 100])
        arrow.fill("black")

        pygame.draw.polygon(arrow, "white", ((0, 0), (0, 100), (100, 50)))
        self.image = pygame.transform.scale(arrow, (text_rect.height, text_rect.height))
        self.rect  = self.image.get_rect()

        match self.option:
            case "SINGLE PLAYER" | "CONTINUE":
                self.rect.center = (screen_width*0.15, screen_height*0.5 + text_rect.height*0.5)
            case "TWO PLAYER" | "RETURN":
                self.rect.center = (screen_width*0.15, screen_height*0.6 + text_rect.height*0.5)
            case "EXIT":
                self.rect.center = (screen_width*0.15, screen_height*0.7 + text_rect.height*0.5)

    def update(self, keysPressed):
        pass
