# =============================================================================
# PATH THROUGH THE SANDS
# Group: 
# 
# An exciting game in which you guide a dune buggy through the desert sands.
# =============================================================================

# =============================================================================
# IMPORTS & CONSTANTS
# =============================================================================

import time
try:
    import mazer
    MAZER_ACTIVE = True
except:
    MAZER_ACTIVE = False

MOVE_DELAY = 500 / 1000 # Seconds between moves

# =============================================================================
# MAZE
# =============================================================================

def generate_maze() -> list:
    """
    Return a list of lists of strings representing a maze.

    See the default example below for the structure:

    - The maze is a rectangle (not necessarily square)
    - The borders are : and the desert is a blank space
    - The buggy starts at B and the end of the maze is at E
    - The buggy can only turn at crossroads, marked by o

    The buggy always starts at the bottom facing north,
    and the exit is always on the north side.

    In the example below, the path through the maze is RLSLRRL.
    """

    # Determine whether to generate a random maze or not
    if MAZER_ACTIVE:
        choice = input('Enter R for random maze; blank to use default: ')
        while choice.strip().upper() not in ('R', ''):
            print('?')
            choice = input('Enter R for random maze; blank to use default: ')
    else:
        choice = ''
    
    if choice:
        return mazer.generate_maze()

    else:
        return [
            # col 0123456789......16
            list(':::::::E:::::::::'), # row 0
            list(':               :'), # row 1
            list(':   o  o        :'), # row 2
            list(':               :'), # row 3
            list(':   o        o  :'), # row 4
            list(':               :'), # row 5
            list(':            o  :'), # row 6
            list(':               :'), # row 7
            list(':         o  o  :'), # row 8
            list(':               :'), # row 9
            list('::::::::::B::::::')  # row 10
        ]

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
    choice = input('Enter [L]eft, [R]ight, [S]traight, or [D]one: ').strip().upper()
    while choice not in ['L', 'R', 'S', 'D']:
        print('Invalid')
        choice = input('Enter [L]eft, [R]ight, [S]traight, or [D]one: ').strip().upper()
    return choice

def get_turns() -> list:
    """
    Prompt the user for turns ('L', 'R', or 'S') and return
    the sequence they enter as a list.
    """
    turns = []
    turn = get_turn()
    while turn != 'D':
        turns.append(turn)
        turn = get_turn()
    return turns

# =============================================================================
# MOVEMENT
# =============================================================================
    
def traverse(maze: list, turns: list) -> bool:
    """
    Traverse the given maze using the given list of turns ('L', 'R', 'S').
    Return True iff the buggy makes it to the end of the maze.
    Return False iff the buggy hits a dead end.
    """
    
    # Initialize
    row, col = locate_buggy(maze)
    facing = 0
    current_turn = 0
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

            # Can only turn if there are any left
            if current_turn < len(turns):
                turn = turns[current_turn]
                facing = rotate(facing, turn)
                current_turn += 1

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
    new_row, new_col = get_next_position(row, col, facing)

    # Shift
    new_standing_on = maze[new_row][new_col]
    maze[new_row][new_col] = 'B'
    maze[row][col] = standing_on

    # Return updated values
    return [new_standing_on, new_row, new_col]

def get_next_position(row: int, col: int, facing: int) -> list:
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

    turns = get_turns()    
    success = traverse(maze, turns)
    
    if success:
        print_success()
    else:
        print_failure()

# Start the game
if __name__ == '__main__':
    play()

    input('Hit Enter to quit')
