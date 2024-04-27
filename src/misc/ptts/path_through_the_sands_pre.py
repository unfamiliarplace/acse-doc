# =============================================================================
# PATH THROUGH THE SANDS (no Command version)
# Group: 
# 
# An exciting game in which you guide a dune buggy through the desert sands.
# =============================================================================

# =============================================================================
# IMPORTS & CONSTANTS
# =============================================================================

import time
import os
MOVE_DELAY = 500 / 1000 # Seconds between moves

# =============================================================================
# MAZE
# =============================================================================

def generate_maze() -> list:
    """
    Return a list of list of strings representing a PTTS maze.
    Placeholder for the starter code -- the real one will be random,
    but will have the structure you see below:

    - The maze is a rectangle (not necessarily square)
    - The borders are : and the desert is a blank space
    - The buggy starts at B and the end of the maze is at E
    - The buggy can only turn at crossroads, marked by o

    The buggy always starts facing north and the exit is always
    on the north side.

    In the example below, the path through the maze is RLSLRRL.
    """
    
    maze = [
        list(':::::::E:::::::::'),
        list(':               :'),
        list(':   o  o        :'),
        list(':               :'),
        list(':   o        o  :'),
        list(':               :'),
        list(':            o  :'),
        list(':               :'),
        list(':         o  o  :'),
        list(':               :'),
        list('::::::::::B::::::')
    ]
    return maze

def locate_buggy(maze: list) -> list:
    """
    Return the buggy's position as a list of [row, column].
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'B':
                return [row, col]

# =============================================================================
# TURNS
# =============================================================================

def get_turn() -> str:
    """
    Return the user's choice for a turn, either L for left, R for right,
    S for straight, or D for done.
    """
    choice = input('Enter [L]eft, [R]ight, or [S]traight: ').strip().upper()
    while choice not in ['L', 'R', 'S']:
        print('Invalid')
        choice = input('Enter [L]eft, [R]ight, or [S]traight: ').strip().upper()
    return choice


# =============================================================================
# MOVEMENT
# =============================================================================
    
def traverse(maze: list) -> bool:
    """
    Traverse the given maze.
    Return True iff the buggy makes it to the end of the maze.
    Return False iff the buggy hits a dead end.
    """
    
    # Initialize
    row, col = locate_buggy(maze)
    facing = 0
    standing_on = ':'

    # First print & delay    
    print_maze(maze)
    time.sleep(MOVE_DELAY)

    while True:

        # Move
        standing_on, row, col = move(maze, standing_on, row, col, facing)
        print_maze(maze)
        time.sleep(MOVE_DELAY)

        # Win?
        if standing_on == 'E':
            return True

        # Lose?
        elif standing_on == ':':
            return False
        
        # Rotate?
        elif standing_on == 'o':
            turn = get_turn()
            facing = rotate(facing, turn)

def rotate(degrees: int, turn: str) -> int:
    """
    Given the degrees the buggy is currently facing (0-360) and a turn (LRS),
    return the new degrees. 0 degrees is north.

    >>> rotate(180, 'L')
    90
    >>> rotate(180, 'S')
    180
    >>> rotate(270, 'R')
    0
    """

    if turn == 'R':
        degrees += 90
    elif turn == 'L':
        degrees -= 90

    if degrees == 360:
        degrees = 0
    elif degrees == -90:
        degrees = 270

    return degrees
        
def move(maze: list, standing_on: str, row: int, col: int, facing: int) -> list:
    """
    Given a maze as a list of lists, the character the robot is standing on,
    the robot's current row and column and direction facing as degrees,
    move the robot. Then, return the new character stood on, the new rol,
    and the new column.
    """
    
    # Get the next position
    new_row, new_col = get_next_position(maze, row, col, facing)

    # Shift
    new_standing_on = maze[new_row][new_col]
    maze[new_row][new_col] = 'B'
    maze[row][col] = standing_on

    # Return updated values
    return [new_standing_on, new_row, new_col]

def get_next_position(maze: list, row: int, col: int, facing: int) -> list:
    """
    Given the maze, the current row & column, and direction (as degrees),
    return a list [row & column] of the next position.
    """
    
    if facing == 0:
        return [row - 1, col]
    elif facing == 90:
        return [row, col + 1]
    elif facing == 180:
        return [row + 1, col]
    elif facing == 270:
        return [row, col - 1]

# =============================================================================
# PRINTING
# =============================================================================

def print_maze(maze: list) -> None:
    """
    Print the given maze, a list of list of strings.
    """
    os.system('cls')
    result = ''
    for row in maze:
        result += ''.join(row) + '\n'
    print(result + '\n')

def print_intro() -> None:
    """
    Print an introduction message for the player.
    """
    print('Welcome!\n')

def print_success() -> None:
    """
    Print a success message for the player.
    """
    print('You win!\n')

def print_failure() -> None:
    """
    Print a failure message for the player.
    """
    print('You lose!\n')

# =============================================================================
# PLAYING
# =============================================================================

def play() -> None:
    """
    Play the game.
    (1) Print an intro message
    (2) Generate a maze & print it
    (3) Get the turns from the player
    (4) Traverse the maze following the turns
    (5) Report success or failure
    """
    print_intro()
    
    maze = generate_maze()
    print_maze(maze)

    success = traverse(maze)
    
    if success:
        print_success()
    else:
        print_failure()

# Start the game
if __name__ == '__main__':
    play()
    input()
