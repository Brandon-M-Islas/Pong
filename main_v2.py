# Need this in order to hide pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import modules
import pygame
from   utilities.classes      import *
from   utilities.functions    import *
from   utilities.singlePlayer import singlePlayer

# Overarching Game Loop
def game():

    # Initializing the pygame stuff forever
    pygame.init()
    flags   = pygame.SHOWN | pygame.RESIZABLE
    screen  = pygame.display.set_mode((SCREEN.width, SCREEN.height), flags, display=0)

    # Creating variables
    SCREEN           = Screen()
    LEFT_WALL        = Object(SCREEN, POSITION =    "LEFT")
    RIGHT_WALL       = Object(SCREEN, POSITION =   "RIGHT")
    TOP_WALL         = Object(SCREEN, POSITION =     "TOP")
    BOTTOM_WALL      = Object(SCREEN, POSITION =  "BOTTOM")
    # DIVIDER_WALL     = Object(SCREEN, POSITION = "DIVIDER")
    PLAYER_ONE       = Object(SCREEN, POSITION = "PLAYER ONE")
    PLAYER_TWO       = Object(SCREEN, POSITION = "PLAYER TWO")
    BALL             = Object(SCREEN, POSITION = "BALL")
    SCOREBOARD       = Object(SCREEN, POSITION = "SCOREBOARD")
    SPACE_HELD       = False
    game_flag        = "MAIN MENU"

    # List holding all the objects that will be manipulated
    ONE_PLAYER_OBJECTS = {"LEFT_WALL":        LEFT_WALL,
                         "RIGHT_WALL":       RIGHT_WALL,
                           "TOP_WALL":         TOP_WALL,
                        "BOTTOM_WALL":      BOTTOM_WALL,
                         "PLAYER_ONE":       PLAYER_ONE,
                         "PLAYER_TWO":       PLAYER_TWO,
                               "BALL":             BALL,
                   "PLAYER_ONE_SCORE": PLAYER_ONE_SCORE,
                   "PLAYER_TWO_SCORE": PLAYER_TWO_SCORE,
                         "SPACE_HELD":       SPACE_HELD,
                         "SCOREBOARD":       SCOREBOARD,
                          "GAME_FONT":        GAME_FONT,
                             "SCREEN":           SCREEN,
                             "screen":           screen,
                          "game_flag":        game_flag}
    
    TWO_PLAYER_OBJECTS = {"LEFT_WALL":        LEFT_WALL,
                         "RIGHT_WALL":       RIGHT_WALL,
                           "TOP_WALL":         TOP_WALL,
                        "BOTTOM_WALL":      BOTTOM_WALL,
                         "PLAYER_ONE":       PLAYER_ONE,
                         "PLAYER_TWO":       PLAYER_TWO,
                               "BALL":             BALL,
                   "PLAYER_ONE_SCORE": PLAYER_ONE_SCORE,
                   "PLAYER_TWO_SCORE": PLAYER_TWO_SCORE,
                         "SPACE_HELD":       SPACE_HELD,
                         "SCOREBOARD":       SCOREBOARD,
                          "GAME_FONT":        GAME_FONT,
                             "SCREEN":           SCREEN,
                             "screen":           screen,
                          "game_flag":        game_flag}

    # Check the game flag and run the appropriate logic for that loop
    while game_flag != "EXIT":
        match game_flag:
            case "MAIN MENU":
                pass # main menu screen
            case "SINGLE PLAYER":
                pass # single player logic
            case "TWO PLAYER":
                TWO_PLAYER_OBJECTS = singlePlayer(TWO_PLAYER_OBJECTS) # second player logic
                if game_flag != "TWO PLAYER":
                    pass ## SOMETHING HERE TO PASS THE SCREENS ONTO ANOTHER LIST
            case "PAUSE MENU":
                pass # new screen for pause

    pygame.quit()
    
if __name__ == "__main__":

    game()