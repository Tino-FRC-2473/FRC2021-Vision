DISTANCE_THRESHOLD = 10  # units in feet, smallest distance of red ball as marker with wiggle room
FRAME_WIDTH = 1920
FRAME_HEIGHT = 1080
LEFT_BOUND = 860  # 960 (center) - 100 px
RIGHT_BOUND = 1060  # 960 (center) + 100 px

def determinePattern(dist, x1, x2, x3):
    center_ball_x = x1
    if (x2 < RIGHT_BOUND and x2 > LEFT_BOUND):
        center_ball_x = x2
    elif (x3 is not None and x3 < RIGHT_BOUND and x3 > LEFT_BOUND):
        center_ball_x = x3

    left_zone_ball = False
    right_zone_ball = False

    if (x1 != center_ball_x and x1 < LEFT_BOUND):
        left_zone_ball = True
    elif (x1 != center_ball_x and x1 > RIGHT_BOUND):
        right_zone_ball = True

    if (x2 != center_ball_x and x2 < LEFT_BOUND):
        left_zone_ball = True
    elif (x2 != center_ball_x and x2 > RIGHT_BOUND):
        right_zone_ball = True

    if (x3 is not None and x3 != center_ball_x and x3 < LEFT_BOUND):
        left_zone_ball = True
    elif (x3 is not None and x3 != center_ball_x and x3 > RIGHT_BOUND):
        right_zone_ball = True

    print("left zone: ", left_zone_ball)
    print("right zone: ", right_zone_ball)

    pattern = patternGenerator(dist, left_zone_ball, right_zone_ball)
    return pattern

# Path A red: 1
# Path A blue: 2
# Path B red: 3
# Path B blue: 4

def patternGenerator(distance, left, right):
    if(distance < DISTANCE_THRESHOLD):
        if(left):
            return 1
        else:
            return 3
    else:
        if(not right):
            return 2
        else:
            return 4
