DISTANCE_THRESHOLD = 14  # units in feet, smallest distance of red ball as marker with wiggle room
PATHS = ['A RED', 'A BLUE', 'B RED', 'B BLUE']


# dist is distance to closest ball, x_coords is array of the center coords of all balls detected
def determinePattern(dist, x_coords):
    path = getPath(dist)  # determine the path color

    if len(x_coords) == 3:
        x1 = x_coords[0]  # closest ball
        x2 = x_coords[1]  # 2nd closest ball
        x3 = x_coords[2]  # 3rd closest ball

    if path:  # compare the red paths
        if abs(x3-x1) > 180:  # horizontal distance buffer calculated from path a red (in px)
            path = PATHS[0]  # path a red
        else:
            path = PATHS[2]  # path b red

    else:  # compare the blue paths
        if abs(x2-x1) > 450:  # subject to change, horizontal distance buffer (in px)
           path = PATHS[1]  # path a blue
        else:
           path = PATHS[3]  # path b blue

    return path


def getPath(distance):
    return distance < DISTANCE_THRESHOLD  # true -> red, false -> blue



# OLD STRATEGY

# FRAME_WIDTH = 1920
# FRAME_HEIGHT = 1080
# LEFT_BOUND = 860  # 960 (center) - 100 px
# RIGHT_BOUND = 1060  # 960 (center) + 100 px

#  if x2 < RIGHT_BOUND and x2 > LEFT_BOUND:
#             center_ball_x = x2
#         elif x3 is not None and x3 < RIGHT_BOUND and x3 > LEFT_BOUND:
#             center_ball_x = x3
#
#         left_zone_ball = False
#         right_zone_ball = False
#
#         if x1 != center_ball_x and x1 < LEFT_BOUND:
#             left_zone_ball = True
#         elif x1 != center_ball_x and x1 > RIGHT_BOUND:
#             right_zone_ball = True
#
#         if x2 != center_ball_x and x2 < LEFT_BOUND:
#             left_zone_ball = True
#         elif x2 != center_ball_x and x2 > RIGHT_BOUND:
#             right_zone_ball = True
#
#         if x3 is not None and x3 != center_ball_x and x3 < LEFT_BOUND:
#             left_zone_ball = True
#         elif x3 is not None and x3 != center_ball_x and x3 > RIGHT_BOUND:
#             right_zone_ball = True

