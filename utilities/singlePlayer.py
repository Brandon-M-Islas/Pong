import pygame
from pygame.locals import *
from keyPresses import keyPresses
from movement import movement

# This just needs to be the logic within the loop
def singlePlayer(OBJECTS: list):

    ON_SCREEN = {"LEFT_WALL":        OBJECTS["LEFT_WALL"],
                "RIGHT_WALL":       OBJECTS["RIGHT_WALL"],
                  "TOP_WALL":         OBJECTS["TOP_WALL"],
               "BOTTOM_WALL":      OBJECTS["BOTTOM_WALL"],
                "PLAYER_ONE":       OBJECTS["PLAYER_ONE"],
                "PLAYER_TWO":       OBJECTS["PLAYER_TWO"],
                      "BALL":             OBJECTS["BALL"],
          "PLAYER_ONE_SCORE": OBJECTS["PLAYER_ONE_SCORE"],
          "PLAYER_TWO_SCORE": OBJECTS["PLAYER_TWO_SCORE"],
                "SCOREBOARD":       OBJECTS["SCOREBOARD"]}

    # Poll for events
    for event in pygame.event.get():

        # If the user closes the window
        if   event.type == QUIT:
            OBJECTS["game_flag"] = "EXIT"

        # If the user changes the size of the window
        elif event.type == VIDEORESIZE:

            # Update the dimensions of the screen
            OBJECTS["SCREEN"].width, OBJECTS["SCREEN"].height = [OBJECTS["screen"].get_width(), OBJECTS["screen"].get_height()]

            # Update the position and size of the on screen objects 
            for object in ON_SCREEN:
                OBJECTS[object].set(OBJECTS["SCREEN"])

            # printScreen(OBJECTS, screen, GAME_FONT, PLAYER_ONE_SCORE, PLAYER_TWO_SCORE, PAUSED)
            OBJECTS["game_flag"] = "PAUSE MENU"

        # If the user presses or releases a key
        elif event.type == KEYDOWN or event.type == KEYUP:

            # If they press the space
            if event.type == KEYDOWN and pygame.key.get_pressed()[K_SPACE] and not OBJECTS["SPACE_HELD"]:
                OBJECTS["game_flag"]  = "PAUSE SCREEN"
                OBJECTS["SPACE_HELD"] = True

            if event.type == KEYUP and not pygame.key.get_pressed()[K_SPACE]:
                OBJECTS["SPACE_HELD"] = False

            if OBJECTS["game_flag"] != "PAUSE SCREEN":

                # Grab all the keys that are being pressed right now
                keysPressed = pygame.key.get_pressed()

                # Determine how to move the objects
                OBJECTS = keyPresses(OBJECTS, keysPressed)


    # Check if the game is paused
    if OBJECTS["game_flag"] != "PAUSE SCREEN":

        # Move all the objects
        OBJECTS = movement(OBJECTS)

        # printScreen(OBJECTS, screen, GAME_FONT, PLAYER_ONE_SCORE, PLAYER_TWO_SCORE, PAUSED)
        # SCOREBOARD = False

        # Limits FPS to 60
        # clock.tick(60)  

    # Exit on 5 points
    # if PLAYER_ONE_SCORE == 2 or PLAYER_TWO_SCORE == 2:
    #     running = False

# Quit pygame
# pygame.quit()
