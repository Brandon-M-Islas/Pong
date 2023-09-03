# Import modules
from utilities.classes import *
from pygame.locals     import *
from math              import copysign, sin, cos, radians

# Holds the stuff to print the screen
def printScreen(OBJECTS: list[object], screen: pygame.surface.Surface):

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for object in OBJECTS:
        screen.fill(OBJECTS[object].color, OBJECTS[object].rect)

    # Flip() the display to put your work on screen
    pygame.display.flip()

# Moves the objects
def movement(OBJECTS: list[object], SCREEN: Screen, PLAYER_ONE_SCORE: int, PLAYER_TWO_SCORE: int):
    
    # Move all the objects
    for object in (OBJECTS["PLAYER_ONE"], OBJECTS["PLAYER_TWO"], OBJECTS["BALL"]):
            object.move()

    # Check if the players have met the upper or lower walls and stop them
    for player in (OBJECTS["PLAYER_ONE"], OBJECTS["PLAYER_TWO"]):
        collision = player.rect.collidelist([OBJECTS["TOP_WALL"], OBJECTS["BOTTOM_WALL"]])
        if collision == 0:
            player.rect.top    = OBJECTS["TOP_WALL"].rect.bottom
        if collision == 1:
            player.rect.bottom = OBJECTS["BOTTOM_WALL"].rect.top

    # Check if the ball has met any of the walls or players and change it's direction or assing points
    collidable = [OBJECTS["LEFT_WALL"], 
                  OBJECTS["RIGHT_WALL"], 
                  OBJECTS["TOP_WALL"], 
                  OBJECTS["BOTTOM_WALL"], 
                  OBJECTS["PLAYER_ONE"], 
                  OBJECTS["PLAYER_TWO"]]

    collision = OBJECTS["BALL"].rect.collidelist(collidable)
    
    # If ball hits the left wall
    if collision == 0:

        # Reset the ball and give player two a point
        OBJECTS["BALL"] = Object(SCREEN, POSITION = "BALL")
        PLAYER_TWO_SCORE += 1
        print(f"Player One: {PLAYER_ONE_SCORE}\nPlayer Two: {PLAYER_TWO_SCORE}\n")

    # If ball hits the right wall
    elif collision == 1:

        # Reset the ball and give player two a point
        OBJECTS["BALL"] = Object(SCREEN, POSITION = "BALL")
        PLAYER_ONE_SCORE += 1
        print(f"Player One: {PLAYER_ONE_SCORE}\nPlayer Two: {PLAYER_TWO_SCORE}\n")

    # If ball hits the top or bottom wall
    elif collision in (2, 3):

        # Change the vertical direction
        OBJECTS["BALL"].y_speed = -OBJECTS["BALL"].y_speed
        OBJECTS["BALL"].move()
    
    # If ball hits either player
    elif collision in (4, 5):

        # Determine angle
        if OBJECTS["BALL"].rect.center[1]   > collidable[collision].rect.bottom:
            BALL_CENTER = collidable[collision].rect.bottom
        elif OBJECTS["BALL"].rect.center[1] < collidable[collision].rect.top:
            BALL_CENTER = collidable[collision].rect.top
        else:
            BALL_CENTER = OBJECTS["BALL"].rect.center[1]

        PLAYER_DISTANCE   = collidable[collision].rect.height / 2
        RELATIVE_DISTANCE = (BALL_CENTER - collidable[collision].rect.center[1]) / PLAYER_DISTANCE
        ANGLE             = RELATIVE_DISTANCE * 45

        # Change the horizontal direction
        OBJECTS["BALL"].x_speed = -(copysign(1, OBJECTS["BALL"].x_speed))*OBJECTS["BALL"].speed*abs(cos(radians(ANGLE)))

        # Change the vertical direction
        OBJECTS["BALL"].y_speed = OBJECTS["BALL"].speed*sin(radians(ANGLE))

        # Move the ball
        OBJECTS["BALL"].move()


    return OBJECTS, PLAYER_ONE_SCORE, PLAYER_TWO_SCORE

# Determines how the objects should move
def keyPresses(OBJECTS: list[object], keysPressed: pygame.key.ScancodeWrapper):

    # If they're pressing just w   
    if   keysPressed[K_w] and not keysPressed[K_s]:

        # Let the object know it's moving and which direction
        OBJECTS["PLAYER_ONE"].moving = True
        OBJECTS["PLAYER_ONE"].key    = K_w

    # If they're pressing just s
    elif not keysPressed[K_w] and keysPressed[K_s]:

        # Let the object know it's moving and which direction
        OBJECTS["PLAYER_ONE"].moving = True
        OBJECTS["PLAYER_ONE"].key    = K_s
    
    # If they're pressing both or neither
    else:

        # Let the object know it's not moving and set no direction
        OBJECTS["PLAYER_ONE"].moving = False
        OBJECTS["PLAYER_ONE"].key    = None

    # If they're pressing just the up key
    if   keysPressed[K_UP] and not keysPressed[K_DOWN]:

        # Let the object know it's moving and which direction
        OBJECTS["PLAYER_TWO"].moving = True
        OBJECTS["PLAYER_TWO"].key    = K_UP

    # If they're pressing just the down key
    elif not keysPressed[K_UP] and keysPressed[K_DOWN]:

        # Let the object know it's moving and which direction
        OBJECTS["PLAYER_TWO"].moving = True
        OBJECTS["PLAYER_TWO"].key    = K_DOWN

    # If they're pressing both or neither
    else:

        # Let the object know it's not moving and set no direction
        OBJECTS["PLAYER_TWO"].moving = False
        OBJECTS["PLAYER_TWO"].key    = None

    return OBJECTS

# Core gameplay loop
def core(screen: pygame.surface.Surface):

    # Pygame setup
    SCREEN  = Screen(screen.get_width(), screen.get_height())
    clock   = pygame.time.Clock()
    running = True

    # Creating variables
    LEFT_WALL        = Object(SCREEN, POSITION =    "LEFT")
    RIGHT_WALL       = Object(SCREEN, POSITION =   "RIGHT")
    TOP_WALL         = Object(SCREEN, POSITION =     "TOP")
    BOTTOM_WALL      = Object(SCREEN, POSITION =  "BOTTOM")
    # DIVIDER_WALL     = Object(SCREEN, POSITION = "DIVIDER")
    PLAYER_ONE       = Object(SCREEN, POSITION = "PLAYER ONE")
    PLAYER_TWO       = Object(SCREEN, POSITION = "PLAYER TWO")
    BALL             = Object(SCREEN, POSITION = "BALL")
    PLAYER_ONE_SCORE = 0
    PLAYER_TWO_SCORE = 0
    PAUSED           = True
    SPACE_HELD       = False
    
    # List holding all the objects that will be manipulated
    OBJECTS = {"LEFT_WALL":     LEFT_WALL,
               "RIGHT_WALL":    RIGHT_WALL,
               "TOP_WALL":      TOP_WALL,
               "BOTTOM_WALL":   BOTTOM_WALL,
            #    "DIVIDER_WALL": DIVIDER_WALL,
               "PLAYER_ONE":    PLAYER_ONE,
               "PLAYER_TWO":    PLAYER_TWO,
               "BALL":          BALL}
    
    printScreen(OBJECTS, screen)

    # Loop for the actual game
    while running:
        
        # Poll for events
        for event in pygame.event.get():

            # If the user closes the window
            if   event.type == QUIT:
                running = False

            # If the user changes the size of the window
            elif event.type == VIDEORESIZE:

                # Update the dimensions of the screen
                SCREEN.width, SCREEN.height = [screen.get_width(), screen.get_height()]

                # Update the position and size of the objects 
                for object in OBJECTS:
                    OBJECTS[object].set(SCREEN)

                printScreen(OBJECTS, screen)
                PAUSED = True

            # If the user presses or releases a key
            elif event.type == KEYDOWN or event.type == KEYUP:

                # If they press the space
                if event.type == KEYDOWN and pygame.key.get_pressed()[K_SPACE] and not SPACE_HELD:
                    PAUSED = not PAUSED
                    SPACE_HELD = True

                if event.type == KEYUP and not pygame.key.get_pressed()[K_SPACE]:
                    SPACE_HELD = False

                if PAUSED == False:

                    # Grab all the keys that are being pressed right now
                    keysPressed = pygame.key.get_pressed()

                    # Determine how to move the objects
                    OBJECTS = keyPresses(OBJECTS, keysPressed)


        # Check if the game is paused
        if PAUSED == False:

            # Move all the objects
            OBJECTS, PLAYER_ONE_SCORE, PLAYER_TWO_SCORE = movement(OBJECTS, SCREEN, PLAYER_ONE_SCORE, PLAYER_TWO_SCORE)

            printScreen(OBJECTS, screen)

            # Limits FPS to 60
            clock.tick(60)  

        # Exit on 5 points
        # if PLAYER_ONE_SCORE == 2 or PLAYER_TWO_SCORE == 2:
        #     running = False

    # Quit pygame
    # pygame.quit()
