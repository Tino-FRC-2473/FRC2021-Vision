ball_distance
ball_left
ball_right
distance_threshold = 10 #units in feet, smallest distance of red ball as marker

# Path A red: 1
# Path A blue: 2
# Path B red: 3
# Path B blue: 4

def patternGenerator(distance, left, right):
    if(distance < distance_threshold):
        if(ball_left is not None):
            return 1
        else:
            return 2
    else:
        if(ball_right is None):
            return 3
        else:
            return 4
