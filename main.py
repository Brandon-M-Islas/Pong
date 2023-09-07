# Need this in order to hide pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import modules
import pygame
from pygame.locals          import *
from Objects import *
from mainMenu import mainMenu
from pauseMenu import pauseMenu
from gameplay import gameplay
from win32api import GetSystemMetrics

# Initializes the display that will hold everything
pygame.init()
flags   = pygame.SHOWN | pygame.RESIZABLE
screen  = pygame.display.set_mode((0.7*GetSystemMetrics(0), 0.7*GetSystemMetrics(1)), flags, display=0)

# Sets the clock that is used to limit the fps
clock   = pygame.time.Clock()

# Let's make a group to hold certain kinds of sprites
ALL        = pygame.sprite.Group()

# Let's make sprites (game objects)
BALL          = Ball(screen, [ALL])
LEFT_WALL     = Wall(screen, "LEFT", [ALL])
RIGHT_WALL    = Wall(screen, "RIGHT", [ALL])
TOP_WALL      = Wall(screen, "TOP", [ALL])
BOTTOM_WALL   = Wall(screen, "BOTTOM", [ALL])
PLAYER_ONE    = Player(screen, "ONE", [ALL])
PLAYER_TWO    = Player(screen, "TWO", [ALL])
SCOREBOARD    = Text(screen, "SCOREBOARD", "SCORE", [ALL])
TITLE         = Text(screen, "TITLE", "PONG", [ALL])
PAUSE         = Text(screen, "TITLE", "PAUSE", [ALL])
CONTINUE      = Text(screen, "OPTION", "CONTINUE", [ALL])
RETURN        = Text(screen, "OPTION", "RETURN TO MAIN MENU", [ALL])
SINGLE_PLAYER = Text(screen, "OPTION", "SINGLE PLAYER", [ALL])
TWO_PLAYER    = Text(screen, "OPTION", "TWO PLAYER", [ALL])
EXIT          = Text(screen, "OPTION", "EXIT", [ALL])
ARROW         = Arrow(screen, [ALL])

# Set the game to run
game_flag = "MAIN MENU"
paused = False
mode = None

CONTAINER = {"screen": screen,
              "clock": clock,
                "ALL": ALL,
               "flags": {"game_flag": game_flag,
                            "paused": paused,
                              "mode": mode}}

# This is the main gameplay loop
while CONTAINER["flags"]["game_flag"] != "EXIT":

    match CONTAINER["flags"]["game_flag"]:
        case "MAIN MENU":
            CONTAINER = mainMenu(CONTAINER)
        case "GAMEPLAY":
            CONTAINER = gameplay(CONTAINER)
        case "PAUSE MENU":
            CONTAINER = pauseMenu(CONTAINER)

quit()
