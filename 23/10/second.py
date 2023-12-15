import sys

sys.setrecursionlimit(1000000)

text = open('input', 'r')
starting_pos = 21, 29
starting_dir = 'E'
char = 'L'
diagram = []
for line in text.readlines():
    if 'S' in line:
        line = line.replace('S', char)
    diagram.append(line.strip())
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


def make_loop(previous_pos, pos, loop: list):
    loop = loop + [pos]
    if pos == starting_pos:
        return loop

    row, col = pos
    pipe = get_pipe(row, col)
    possible_connections = connections[pipe]
    next_pos = get_position_based_on_direction(row, col, possible_connections[0])
    if next_pos == previous_pos:
        next_pos = get_position_based_on_direction(row, col, possible_connections[1])
    return make_loop(pos, next_pos, loop)


loop = make_loop(starting_pos, get_position_based_on_direction(starting_pos[0], starting_pos[1], starting_dir), [])
new_diagram = []
for row_idx in range(0, len(diagram)):
    new_diagram.append([])
    for col_idx in range(0, len(diagram[0])):
        if (row_idx, col_idx) not in loop:
            new_diagram[row_idx].append('.')
        else:
            new_diagram[row_idx].append(diagram[row_idx][col_idx])


def walk_until_end(starting_position: tuple, direction: str, count: int = 0) -> int:
    if starting_position[0] < 0 or starting_position[1] < 0:
        return count
    try:
        tile = new_diagram[starting_position[0]][starting_position[1]]
    except IndexError:
        return count
    new_position = get_position_based_on_direction(starting_position[0], starting_position[1], direction)

    if tile in ['|', 'L', 'J']:
        return walk_until_end(new_position, direction, count + 1)
    return walk_until_end(new_position, direction, count)


def is_odd(number: int) -> bool:
    return number % 2 == 1


tiles_inside_count = 0
for row_idx in range(0, len(new_diagram)):
    for col_idx in range(0, len(new_diagram[0])):
        if new_diagram[row_idx][col_idx] != '.':
            continue
        east_count = walk_until_end((row_idx, col_idx), 'E')

        if is_odd(east_count):
            tiles_inside_count += 1
print(tiles_inside_count)  # 371
