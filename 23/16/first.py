import functools
import sys

sys.setrecursionlimit(50_000_000)

text = open('test_input', 'r')

layout = []
for line in text.readlines():
    layout.append([s for s in line[:-1]])


@functools.cache
def get_new_coordinates(row: int, col: int, direction: str) -> (int, int):
    match direction:
        case 'N':
            return row - 1, col
        case 'S':
            return row + 1, col
        case 'E':
            return row, col + 1
        case 'W':
            return row, col - 1


@functools.cache
def get_new_direction(direction: str, tile: str) -> str:
    if direction == 'N':
        if tile == '\\':
            return 'W'
        if tile == '/':
            return 'E'

    if direction == 'S':
        if tile == '\\':
            return 'E'
        if tile == '/':
            return 'W'

    if direction == 'E':
        if tile == '\\':
            return 'S'
        if tile == '/':
            return 'N'

    if direction == 'W':
        if tile == '\\':
            return 'N'
        if tile == '/':
            return 'S'

visited_beams = []
# @functools.cache
def get_visited_tiles(row: int, col: int, direction: str, visited_tiles: tuple):
    if row == len(layout) or row == -1 or col == len(layout[0]) or col == -1:
        return visited_tiles

    if (f'{row}{col}') not in visited_tiles:
        visited_tiles = visited_tiles + (f'{row}{col}',)
    beam_path = f'{row}.{col}.{direction}'
    if beam_path in visited_beams:
        print(beam_path)
        return visited_tiles

    tile = layout[row][col]
    # if tile != '.':
    #     visited_beams.append(beam_path)
    # print(f'At ({row},{col}) tile {tile} with direction={direction}.')

    if tile == '\\' or tile == '/':
        visited_beams.append(beam_path)
        direction = get_new_direction(direction, tile)

    if tile == '|':
        if direction in ['W', 'E']:
            visited_beams.append(beam_path)
            return get_visited_tiles(row - 1, col, 'N', visited_tiles) + get_visited_tiles(row + 1, col, 'S',
                                                                                           visited_tiles)

    if tile == '-':
        if direction in ['S', 'N']:
            visited_beams.append(beam_path)
            return get_visited_tiles(row, col + 1, 'E', visited_tiles) + get_visited_tiles(row, col - 1, 'W',
                                                                                           visited_tiles)

    new_row, new_col = get_new_coordinates(row, col, direction)
    return get_visited_tiles(new_row, new_col, direction, visited_tiles)


visited_tiles = get_visited_tiles(0, 0, 'E', ())
# print(len(visited_tiles))
print(len(set(visited_tiles)))
# 7551 is too low
# co 427339