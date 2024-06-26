# =============================================================================
# MAZER
# Author: Luke Sawczak
# 
# A tool for generating mazes for Path Through the Sands.
# =============================================================================

import random, math

def generate_maze() -> list:

    # Random size
    n_rows = random.randint(6, 12)
    n_cols = random.randint(2 + n_rows, 12 + n_rows) # Landscape looks better

    # Make lines
    border = list(':' for _ in range(n_cols))
    line = [':'] + list(' ' for _ in range(n_cols - 2)) + [':']
    lines = list(line[:] for _ in range(n_rows - 2))

    # Make grid using slice copy
    rows = [border[:]]
    rows.extend(lines[:])
    rows.append(border[:])

    # Determine end & buggy position
    c_E = random.randint(1, n_cols - 2)
    c_B = random.randint(1, n_cols - 2)
    
    # No same col -- no winning without turning
    while c_B == c_E:
        c_B = random.randint(1, n_cols - 2)

    # Place end & buggy
    rows[0][c_E] = 'E'
    rows[n_rows - 1][c_B] = 'B'

    # Place turns....
    place_turns(rows, c_E, c_B)

    # Reduce to one possible path
    reduce_clutter(rows, n_rows - 1, c_B)

    return rows

def connect_turns(maze: list, ar: int, ac: int, br: int, bc: int) -> bool:
    """
    Connect the two given points (ar, ac) and (br, bc) by placing one or more
    turns between them. Return True iff they were successfully connected.
    """

    # Handy
    n_rows = len(maze)
    n_cols = len(maze[0])
    rows = sorted((ar, br))
    cols = sorted((ac, bc))

    corners = set(((0, 0), (0, n_cols - 1), (n_rows - 1, 0), (n_rows - 1, n_cols - 1)))
    north_south = rows == [0, n_rows - 1]
    east_west = cols == [0, n_cols - 1]
    one_apart = (abs(ar - br) == 1) or (abs(ac - bc) == 1)
    right_angles = ((ar, bc), (br, ac))
    right_angles = list(filter(lambda T: maze[T[0]][T[1]] != ':', right_angles))

    # Rule out corners -- cannot reach a corner
    if (ar, ac) in corners or (br, bc) in corners:
        return False

    # If they already share a row or column, no need
    elif (ar == br) or (ac == bc):
        return True

    else:

        one_or_two = []
        if right_angles:
            one_or_two.append('one')
        if (not one_apart) or (north_south or east_west):
            one_or_two.append('two')

        # One-point join
        if random.choice(one_or_two) == 'one':
            row, col = random.choice(right_angles)
            maze[row][col] = 'o'

        # Two-point join
        else:
            col_or_row = []
            if not north_south:
                col_or_row.append('col')
            if not east_west:
                col_or_row.append('row')

            # Two points share a row
            if random.choice(col_or_row) == 'row':
                row = random.randint(rows[0] + 1, rows[1] - 1)
                maze[row][ac] = 'o'
                maze[row][bc] = 'o'

            # Two points share a col
            else:
                col = random.randint(cols[0] + 1, cols[1] - 1)
                maze[ar][col] = 'o'
                maze[br][col] = 'o'

        return True

def place_turns_optimal(maze: list, c_E: int, c_B: int) -> None:
    """
    Replace positions in the given list of lists with 'o' such that
    an optimal path of 90-degree turns can be made between E and B.
    """
    connect_turns(maze, 0, c_E, len(maze) - 1, c_B)

def place_turns(maze: list, c_E: int, c_B: int) -> None:
    """
    Replace positions in the given list of lists with 'o' such that
    a path of 90-degree turns can be made between E and B.
    """

    # Idea that would work but be kind of lame and possibly take a long time to run
    # Start with one point in c_E and one in c_B, random rows
    # Then generate random placements and check validity till one is OK
    # Valid = starting from B, there is one turning point sharing a row or a col;
    #         each such turning point has another not yet visited;
    #         UNTIL one is found that shares a row or col with E

    n_rows = len(maze)
    n_cols = len(maze[0])
    n = min(n_rows * n_cols // 10, 25) # Cap to avoid massive path generation

    top_row, top_col, top_prev = 0, c_E, 'row'
    bot_row, bot_col, bot_prev = n_rows - 1, c_B, 'row'

    for _ in range(n // 2):
        top_row, top_col, top_rev = next_point(n_rows, n_cols, top_row, top_col, top_prev)
        maze[top_row][top_col] = 'o'

        bot_row, bot_col, bot_prev = next_point(n_rows, n_cols, bot_row, bot_col, bot_prev)
        maze[bot_row][bot_col] = 'o'
    
    connect_turns(maze, top_row, top_col, bot_row, bot_col)


def next_point(n_rows: int, n_cols: int, row: int, col: int, prev_share: str='') -> list:
    """
    Return a reachable point from (row, col). The return format is
    (new_row, new_col, share) where share is either 'row' or 'col'
    indicating which dimension was shared.
    """

    row_or_col = []
    if (prev_share != 'row') and (0 < row < (n_rows - 1)):
        row_or_col.append('row')
    if (prev_share != 'col') and (0 < col < (n_cols - 1)):
        row_or_col.append('col')

    # Share a row
    if random.choice(row_or_col) == 'row':
        new_col = random.randint(1, n_cols - 2)
        while new_col == col:
            new_col = random.randint(1, n_cols - 2)
        return (row, new_col, 'row')

    # Share a col
    else:
        new_row = random.randint(1, n_rows - 2)
        while new_row == row:
            new_row = random.randint(1, n_rows - 2)
        return (new_row, col, 'col')

def reduce_clutter(maze: list, row: int, col: int) -> None:
    """
    Reduce the turns to form one valid path through the maze.
    Choose based on path length.
    """

    paths = get_valid_paths(maze, row, col, '', [], set())
    paths = sorted(paths, key=len)

    # Reduce # of 2-point paths
    while len(paths) > 1 and len(paths[0]) == 3:
        paths.pop(0)

    path = random.choice(paths[:max(len(paths) // 2, 1)])
    # path = random.choice(paths)
    # path = paths[0]

    eliminate_not_on_path(maze, path)

def reduce_clutter_2(maze: list, row: int, col: int) -> None:
    """
    Reduce the turns to form one valid path through the maze.
    Choose based on path density (most unique rows & columns).
    """

    paths = get_valid_paths(maze, row, col, '', [], set())

    path_stats = []
    for path in paths:
        n_stops = len(path)
        n_rows = len(set(p[0] for p in paths))
        n_cols = len(set(p[1] for p in paths))
        n_unique = n_rows + n_cols

        path_stats.append((path, n_stops, n_rows, n_cols, n_unique))

    paths = sorted(path_stats, key=lambda path: path[4])
    path = paths[-1][0]

    eliminate_not_on_path(maze, path)
    

def eliminate_not_on_path(maze: list, path: tuple) -> None:
    """Eliminate points not on the given path."""
    path = set(path)
    for row in range(1, len(maze) - 1):
        for col in range(1, len(maze[0]) - 1):
            if (row, col) not in path:
                maze[row][col] = ' '

def get_valid_paths(maze: list, row: int, col: int, direction: str,
                    path: list, paths: set) -> set:
    """
    Return a set of tuples of points (row, col) to get from B to E.
    (B is not included.) Return an empty set if there are no valid paths.
    """

    # Don't test any paths that are going to be longer than our longest one
    # (unless our longest one is too simple, i.e. just two crossroads + E)
    if paths:
        longest_yet = len(max(paths, key=len))
        if longest_yet > 3 and len(path) + 1 >= longest_yet:
            return paths

    def _check_position(row: int, col: int, path: list, direction: str):
        there = maze[row][col]

        if there == 'E':
            path.append((row, col))
            paths.add(tuple(path))

        elif there == 'o' and (row, col) not in set(path):
            path.append((row, col))
            get_valid_paths(maze, row, col, direction, path, paths)

    
    # if direction not in ('S', 'N'): # Decided to allow straight turns

    if direction != 'S':
        # Check northwards
        for i in range(row - 1, -1, -1):
            _check_position(i, col, path[:], 'N')

    if direction != 'N':
        # Check southwards
        for i in range(row + 1, len(maze)):
            _check_position(i, col, path[:], 'S')

    # if direction not in ('E', 'W'): # Decided to allow straight turns

    if direction != 'W':
        # Check eastwards
        for i in range(col + 1, len(maze[0])):
            _check_position(row, i, path[:], 'E')
    
    if direction != 'E':
        # Check westwards
        for i in range(col - 1, -1, -1):
            _check_position(row, i, path[:], 'W')
    
    return paths


def print_maze(maze: list) -> None:
    s = ''
    for row in maze:
        s += ''.join(row) + '\n'
    print(f'{s}\n')


def test() -> None:
    maze = generate_maze()
    print_maze(maze)


if __name__ == '__main__':
    test()
