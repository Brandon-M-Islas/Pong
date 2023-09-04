import pygame
# Holds the stuff to print the screen
def printScreen(OBJECTS: list[object]):

    # Fill the screen with a color to wipe away anything from last frame
    OBJECTS["screen"].fill("black")

    # RENDER YOUR GAME HERE
    for object in OBJECTS:
        OBJECTS["screen"].fill(OBJECTS[object].color, OBJECTS[object].rect)

    # Print the score onto the screen
    OBJECTS["screen"].blit(OBJECTS["SCOREBOARD"].surface, ((OBJECTS["screen"].get_width()-OBJECTS["SCOREBOARD"].rect.width)/2, 0.01*OBJECTS["screen"].get_height()))

    pygame.display.flip()