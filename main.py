# Need this in order to hide pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import modules
import                          pygame
from utilities.classes   import *
from utilities.functions import *
from pygame.locals       import *

# Where the game actually runs
def game():

    pygame.init()
    SCREEN  = Screen()
    flags   = pygame.SHOWN | pygame.RESIZABLE
    screen  = pygame.display.set_mode((SCREEN.width, SCREEN.height), flags, display=0)
    
    # main()
    core(screen)

    pygame.quit()
    
if __name__ == "__main__":

    game()