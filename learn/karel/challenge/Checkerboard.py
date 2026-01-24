from karel.stanfordkarel import *

"""
Karel should fill the entire world with beepers in a checkerboard pattern.
"""

def main():
    """
    Main function to fill the world with beepers in a checkerboard pattern.
    Handles general cases and edge cases for grids with a single column.
    """
    # Handle grids with more than one column.
    multi_grid_process()

    # Handle edge case for a single-column grid.
    single_grid_process()

    # Reset Karel's position to bottom-left corner facing east.
    karel_go_home()

def multi_grid_process():        
    while front_is_clear():
        process_single_row()
        if front_is_clear():    
            move()
            process_single_row()

def single_grid_process():
    face_up()
    while front_is_clear():
        place_beeper_if_none()
        move_if_possible()
        move_if_possible()
        place_beeper_if_none()

def karel_go_home():
    face_down()
    move_to_end()
    face_left()
    move_to_end()
    face_right()

def process_single_row():
    """ Processes a single row:
    - Places beepers in an alternating pattern (checkerboard).
    - Moves Karel to the next row above. """
    face_right()
    place_alternating_line_beepers()
    face_up()
    if front_is_clear():
        move()
        face_left()
        move_to_end()
        face_right()
            
def place_alternating_line_beepers():
    """
    Places beepers along a row in a checkerboard pattern, skipping one cell between beepers.
    """
    place_beeper_if_none()
    while front_is_clear():
        move_two_and_place_beeper()

def move_to_end():
    """
    Moves Karel forward until hitting a wall.
    """
    while front_is_clear():
        move()

def move_if_possible():
    """
    Moves Karel forward one step if possible.
    """
    if front_is_clear():
        move()

def face_up():
    # keeps turning left till we are facing north / up
    while not_facing_north():
        turn_left()

def place_beeper_if_none():
    # if current corner, does not have a beeper, puts one there
    if no_beepers_present():
        put_beeper()            

def face_down():
    # turns left repeatedly till karel is facing down/ south
    while not_facing_south():
        turn_left()

def face_right():
    # turn left, till face right/ east
    while not_facing_east():
        turn_left()

def face_left():
    # turn left till facing left, good if you are facing right and one left turn wont do
    while not_facing_west():
        turn_left()

def move_two_and_place_beeper():
    # skip 1 and place a beeper if there are enough corners
    move_if_possible()
    if(front_is_clear()):
        move()
        place_beeper_if_none()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
