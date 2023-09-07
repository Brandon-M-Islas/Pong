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
def arrowLogic(ELEMENTS):

    # We reference these a bit so save them here explicitly
    ARROW = ELEMENTS["ARROW"]
    game_flag = ELEMENTS["game_flag"]

    # If the space button gets pressed
    if ELEMENTS["event"] == KEYDOWN and ELEMENTS["keysPressed"][K_SPACE]:

        # Check where the arrow is and set the flags accordingly
        match ARROW.option:
            case "CONTINUE":
                game_flag = "GAMEPLAY"
            case "RETURN":
                game_flag = "MAIN MENU"
                ELEMENTS["mode"] = None
            case "EXIT":
                game_flag = "EXIT"
                ELEMENTS["mode"] = None
    
    # If the down key or s key gets pressed
    elif ELEMENTS["event"] == KEYDOWN and (ELEMENTS["keysPressed"][K_DOWN] or ELEMENTS["keysPressed"][K_s]):

        # Check where the arrow is and move it accordingly
        match ARROW.option:
            case "CONTINUE":
                ARROW.option = "RETURN"
                ARROW.resize(ELEMENTS["screen"])
            case "RETURN":
                ARROW.option = "EXIT"
                ARROW.resize(ELEMENTS["screen"])

    # If the up key or the w key gets pressed
    if ELEMENTS["event"] == KEYDOWN and (ELEMENTS["keysPressed"][K_UP] or ELEMENTS["keysPressed"][K_w]):

        # Check where the arrow is ad move it accordingly
        match ARROW.option:
            case "RETURN":
                ARROW.option = "CONTINUE"
                ARROW.resize(ELEMENTS["screen"])
            case "EXIT":
                ARROW.option = "RETURN"
                ARROW.resize(ELEMENTS["screen"])

    return ARROW, game_flag, ELEMENTS["mode"]

# This is the logic that will run for the mainMenu screen
def pauseMenu(CONTAINER):

    # We single out the arrow and the game_flag because these will be referenced the most
    ARROW = CONTAINER["ALL"].sprites()[15]
    game_flag = CONTAINER["flags"]["game_flag"]
    mode = CONTAINER["flags"]["mode"]

    # We define which sprites are going to be on screen for this screen
    ON_SCREEN = pygame.sprite.Group()
    ON_SCREEN.add([CONTAINER["ALL"].sprites()[0],
                   CONTAINER["ALL"].sprites()[5],
                   CONTAINER["ALL"].sprites()[6],
                   CONTAINER["ALL"].sprites()[7],
                   CONTAINER["ALL"].sprites()[9],
                   CONTAINER["ALL"].sprites()[10],
                   CONTAINER["ALL"].sprites()[11],
                   CONTAINER["ALL"].sprites()[14],
                   ARROW])

    # We print the screen once at the start since it is a static screen
    ELEMENTS = {"screen": CONTAINER["screen"],
             "ON_SCREEN": ON_SCREEN,
                 "clock": CONTAINER["clock"]}
    printScreen(ELEMENTS)

    # Keep running this logic if the flag is main menu
    while game_flag == "PAUSE MENU":

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

                ELEMENTS = {"screen": CONTAINER["screen"],
                            "ON_SCREEN": ON_SCREEN,
                            "clock": CONTAINER["clock"]}
                
                printScreen(ELEMENTS)

            # If the user presses a key
            elif event.type == KEYDOWN:
                
                # Take note of which option the arrow is on before
                before = ARROW.option

                # Take that info and run the arrow logic
                ELEMENTS = {"event": event.type, 
                      "keysPressed": pygame.key.get_pressed(),
                        "game_flag": game_flag,
                           "screen": CONTAINER["screen"],
                             "mode": mode,
                            "ARROW": ARROW}
                ARROW, game_flag, mode  = arrowLogic(ELEMENTS)
                
                # If the arrow option changes
                if ARROW.option != before:

                    # reprint the screen
                    ELEMENTS = {"screen": CONTAINER["screen"],
                                "ON_SCREEN": ON_SCREEN,
                                "clock": CONTAINER["clock"]}
                    printScreen(ELEMENTS)

    if game_flag == "MAIN MENU":
        ARROW.option = "SINGLE PLAYER"
        CONTAINER["ALL"].sprites()[7].player_one_score = 0
        CONTAINER["ALL"].sprites()[7].player_two_score = 0
        for sprite in CONTAINER["ALL"].sprites():
            sprite.resize(CONTAINER["screen"])

    # Reassign the changed values of the arrow and flag to the container
    CONTAINER["flags"]["game_flag"] = game_flag
    CONTAINER["flags"]["mode"] = mode

    return CONTAINER