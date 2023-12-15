import sys

sys.setrecursionlimit(1000000)
text = open('input', 'r')
starting_pos = 21, 29
diagram = [line.strip() for line in text.readlines()]
diagram[starting_pos[0]][starting_pos[1]].replace('S', 'L')

connections = {
    '|': ['N', 'S'],
    '-': ['W', 'E'],
    'L': ['N', 'E'],
    'J': ['W', 'N'],
    '7': ['W', 'S'],
    'F': ['S', 'E'],
    '.': []
}


def get_pipe(row: int, col: int) -> str | None:
    try:
        return diagram[row][col]
    except IndexError:
        return None


def get_position_based_on_direction(row, col, direction) -> tuple:
    match direction:
        case 'N':
            return row - 1, col
        case 'W':
            return row, col - 1
        case 'S':
            return row + 1, col
        case 'E':
            return row, col + 1


def get_loop_length(previous_pos, pos):
    if pos == starting_pos:
        return 1

    row, col = pos
    pipe = get_pipe(row, col)
    possible_connections = connections[pipe]
    next_pos = get_position_based_on_direction(row, col, possible_connections[0])
    if next_pos == previous_pos:
        next_pos = get_position_based_on_direction(row, col, possible_connections[1])
    return get_loop_length(pos, next_pos) + 1


print(get_loop_length(starting_pos, get_position_based_on_direction(starting_pos[0], starting_pos[1], 'N')))
print(get_loop_length(starting_pos, get_position_based_on_direction(starting_pos[0], starting_pos[1], 'E')))
