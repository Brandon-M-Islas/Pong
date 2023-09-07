import pygame
from pygame.locals import *

# This is the logic that will run when we want to print the screen
def printScreen(ELEMENTS):

    # Fill the CONTAINER["screen"] with black to wipe away anything from last frame and draw everything on it
    ELEMENTS["screen"].fill("black")
    ELEMENTS["ON_SCREEN"].draw(ELEMENTS["screen"])

    # Show the changes on CONTAINER["screen"] and limit the fps to 60
    pygame.display.flip()
    ELEMENTS["clock"].tick(60)  

# This is the logic that will run when the arrow is being manipulated
def playerLogic(ELEMENTS):

    # We reference these a bit so save them here explicitly
    keysPressed = ELEMENTS["keysPressed"]
    PLAYER_ONE = ELEMENTS["PLAYER_ONE"]
    PLAYER_TWO = ELEMENTS["PLAYER_TWO"]
    BALL = ELEMENTS["BALL"]

    if (keysPressed[K_w] and keysPressed[K_s]) or (not keysPressed[K_w] and not keysPressed[K_s]):
        PLAYER_ONE.key = None
    elif keysPressed[K_w]:
        PLAYER_ONE.key = "UP"
    elif keysPressed[K_s]:
        PLAYER_ONE.key = "DOWN"

    if ELEMENTS["mode"] == "TWO PLAYER":
        if (keysPressed[K_UP] and keysPressed[K_DOWN]) or (not keysPressed[K_UP] and not keysPressed[K_DOWN]):
            PLAYER_TWO.key = None
        elif keysPressed[K_UP]:
            PLAYER_TWO.key = "UP"
        elif keysPressed[K_DOWN]:
            PLAYER_TWO.key = "DOWN"

    elif ELEMENTS["mode"] == "SINGLE PLAYER":
        if BALL.rect.center[1] < PLAYER_TWO.rect.center[1]:
            PLAYER_TWO.key = "UP"
        elif BALL.rect.center[1] > PLAYER_TWO.rect.center[1]:
            PLAYER_TWO.key = "DOWN"
        elif BALL.rect.center[1] == PLAYER_TWO.rect.center[1]:
            PLAYER_TWO.key = None
        

    return PLAYER_ONE, PLAYER_TWO

# This is the logic that will run for the mainMenu screen
def gameplay(CONTAINER):

    # We single out the arrow and the game_flag because these will be referenced the most
    game_flag = CONTAINER["flags"]["game_flag"]
    BALL = CONTAINER["ALL"].sprites()[0]
    PLAYER_ONE = CONTAINER["ALL"].sprites()[5]
    PLAYER_TWO = CONTAINER["ALL"].sprites()[6]
    SCOREBOARD = CONTAINER["ALL"].sprites()[7]

    # We define which sprites are going to be on screen for this screen
    ON_SCREEN = pygame.sprite.Group()
    ON_SCREEN.add([BALL,
                   PLAYER_ONE,
                   PLAYER_TWO,
                   SCOREBOARD])

    # We print the screen once at the start since it is a static screen
    ELEMENTS = {"screen": CONTAINER["screen"],
             "ON_SCREEN": ON_SCREEN,
                 "clock": CONTAINER["clock"]}
    printScreen(ELEMENTS)

    # Keep running this logic if the flag is gameplay
    while game_flag == "GAMEPLAY":

        # Poll for events
        for event in pygame.event.get():
            # If the user closes the window
            if event.type == QUIT:
                # Change the flag (for good practice)
                game_flag = "EXIT"
                # Exit the game
                quit()

            # If the user changes the size of the window
            elif event.type == VIDEORESIZE:
                # Resize (and reset) all the sprites
                for sprite in CONTAINER["ALL"].sprites():
                    sprite.resize(CONTAINER["screen"])

                # Reprint the screen
                ELEMENTS = {"screen": CONTAINER["screen"],
                            "ON_SCREEN": ON_SCREEN,
                            "clock": CONTAINER["clock"]}
                
                printScreen(ELEMENTS)

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_flag = "PAUSE MENU"

        # Determine how the player should move
        ELEMENTS = {"keysPressed": pygame.key.get_pressed(),
                           "mode": CONTAINER["flags"]["mode"],
                     "PLAYER_ONE": PLAYER_ONE,
                     "PLAYER_TWO": PLAYER_TWO, 
                           "BALL": BALL}   
        PLAYER_ONE, PLAYER_TWO = playerLogic(ELEMENTS)
            
        # Move everything
        ELEMENTS = {"screen": CONTAINER["screen"],
                    "ALL": CONTAINER["ALL"]}
        ON_SCREEN.update()
        for sprite in ON_SCREEN.sprites():
            sprite.collision(ELEMENTS)

        # reprint the screen
        ELEMENTS = {"screen": CONTAINER["screen"],
                    "ON_SCREEN": ON_SCREEN,
                    "clock": CONTAINER["clock"]}
        printScreen(ELEMENTS)

    # Reassign the changed values of the arrow and flag to the container
    CONTAINER["flags"]["game_flag"] = game_flag
    CONTAINER["ALL"].sprites()[0] = BALL
    CONTAINER["ALL"].sprites()[5] = PLAYER_ONE
    CONTAINER["ALL"].sprites()[6] = PLAYER_TWO
    CONTAINER["ALL"].sprites()[7] = SCOREBOARD

    return CONTAINER
    