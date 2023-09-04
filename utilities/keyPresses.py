import pygame
from pygame.locals import *

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