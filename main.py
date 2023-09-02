# Need this in order to hide pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import           pygame
from wall import Wall, Screen, Scale

def main():

    SCREEN = Screen()
    SCALE  = Scale()

    print(SCREEN.__dict__)
    
    LEFT_WALL   = Wall(SCREEN, SIDE =   "LEFT")
    RIGHT_WALL  = Wall(SCREEN, SIDE =  "RIGHT")
    TOP_WALL    = Wall(SCREEN, SIDE =    "TOP")
    BOTTOM_WALL = Wall(SCREEN, SIDE = "BOTTOM")

    print(LEFT_WALL.rect)

    # pygame setup
    pygame.init()

    flags  = pygame.SHOWN | pygame.RESIZABLE
    screen = pygame.display.set_mode((SCREEN.height, SCREEN.width), flags, display=0)

    clock   = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                SCALE.x, SCALE.y = [screen.get_width() / SCREEN.width, screen.get_height() / SCREEN.height]
                SCREEN.width, SCREEN.height = [screen.get_width(), screen.get_height()]

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    
    main()

    