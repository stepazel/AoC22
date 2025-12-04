text = open('input', 'r')

grid = []
while True:
    line = text.readline()[:-1]
    if not line:
        break

    grid.append([roll for roll in line])


def is_outer_roll(y_new, x_new):
    if y_new not in range(len(grid)) or x_new not in range(len(grid[0])):
        return False

    point = grid[y_new][x_new]

    if point == '@':
        return True

    return False

accessible_rolls_count = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != '@':
            continue


        offsets = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        adjacent_rolls_count = 0
        for offset in offsets:
            y_offset, x_offset = offset
            if is_outer_roll(y + y_offset, x + x_offset):
                adjacent_rolls_count += 1

        if adjacent_rolls_count < 4:
            accessible_rolls_count += 1


print(accessible_rolls_count)
