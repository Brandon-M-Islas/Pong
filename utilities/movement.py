from classes_v2 import *
from math import copysign, sin, cos, radians

# Moves the objects
def movement(OBJECTS: list[object]):
    
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
        OBJECTS["BALL"]                         = Object(OBJECTS["SCREEN"], POSITION = "BALL")
        OBJECTS["PLAYER_ONE"]                   = Object(OBJECTS["SCREEN"], POSITION = "PLAYER ONE")
        OBJECTS["PLAYER_TWO"]                   = Object(OBJECTS["SCREEN"], POSITION = "PLAYER TWO")
        OBJECTS["SCOREBOARD"].player_two_score += 1

    # If ball hits the right wall
    elif collision == 1:

        # Reset the ball and give player one a point
        OBJECTS["BALL"]                         = Object(OBJECTS["SCREEN"], POSITION = "BALL")
        OBJECTS["PLAYER_ONE"]                   = Object(OBJECTS["SCREEN"], POSITION = "PLAYER ONE")
        OBJECTS["PLAYER_TWO"]                   = Object(OBJECTS["SCREEN"], POSITION = "PLAYER TWO")
        OBJECTS["SCOREBOARD"].player_one_score += 1

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

    return OBJECTS