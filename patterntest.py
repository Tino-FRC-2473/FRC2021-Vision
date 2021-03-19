DISTANCE_THRESHOLD = 14  # ft, distance to closest red balls w/ wiggle room
PATHS = ['AR', 'AB', 'BR', 'BB']

# dist is distance to closest ball, x_coords is array of the center coords of all balls detected
def determinePattern(dist, x_coords):
    path = (dist < DISTANCE_THRESHOLD)  # true -> red, false -> blue

    if len(x_coords) == 3:
        x1 = x_coords[0]  # closest ball
        x2 = x_coords[1]  # 2nd closest ball
        x3 = x_coords[2]  # 3rd closest ball

        if path:  # compare the red paths
            # 180px = max deviation from x3 ball being aligned w/ x1 ball in path b red
            if abs(x3-x1) > 180:
                path = PATHS[0]  # path a red
            else:
                path = PATHS[2]  # path b red

        else:  # compare the blue paths
            if abs(x2-x1) > 450:  # subject to change, horizontal distance buffer (in px)
                path = PATHS[1]  # path a blue
            else:
                path = PATHS[3]  # path b blue
    else:
        path = "Undetermined"

    return path
