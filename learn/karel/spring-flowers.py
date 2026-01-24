from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    """
    Can use either :
    bloom_first_two_flowers()
     or 
    bloom_all_flowers()
    but not both, comment out one
    
    """
    # bloom_first_two_flowers()
    bloom_all_flowers()


def bloom_first_two_flowers():
     # For just two flowers 
     # moves to next obstacle after that
    bloom_one_flower()
    bloom_one_flower()
    move_to_end()



def bloom_all_flowers():
    # find all stems and draw flowers
    # this code will work for any number of flowers.
    while front_is_clear():
        bloom_one_flower()   
    
    # at end you will be stranded at end of right wall on top
    # climb down and face right
    face_down()
    move_to_end()
    face_right()    

def bloom_one_flower():
    # move to a stem
    while front_is_clear():
        move()
    # climb up a stem
    position_to_top_of_stem_or_top_of_world()
    if front_is_clear():
        bloom_flower()
    # moves down a flower and faces right
    move_to_end()    
    face_right()

def move_to_end():
    # moves to end (until front is blocked)
    while front_is_clear():
        move()

def bloom_flower():
    # place_beeper_square
    
    # at a stem bloom a flower (square of beepers)
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()

def position_to_top_of_stem_or_top_of_world():
    # move_to_obstacle_top
    face_up()
    while right_is_blocked() and front_is_clear():
        move()

def face_up():
    while not_facing_north():
        turn_left()

def face_down():
    while not_facing_south():
        turn_left()

def face_right():
    while not_facing_east():
        turn_left()

def face_left():
    while not_facing_west():
        turn_left()     

# turn right by making 3 turn lefts
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
