text = open('input', 'r')
lines = text.readlines()
positions = []

for line in lines:
    row = [s for s in line if s != '\n']
    positions.append(row)

loads = []
prev_positions = []
for j in range(0, 200):
    prev_positions = positions.copy()
    if j % 10_000 == 0:
        print(j)
    # tilt north
    for col_idx in range(0, len(positions[0])):
        count_rocks = 0
        for row_idx in range(len(positions) - 1, -1, -1):
            el = positions[row_idx][col_idx]
            if el == 'O':
                positions[row_idx][col_idx] = '.'
                count_rocks += 1
            if el == '#':
                for i in range(1, count_rocks + 1):
                    positions[row_idx + i][col_idx] = 'O'
                count_rocks = 0
            if row_idx == 0:
                for i in range(0, count_rocks):
                    positions[row_idx + i][col_idx] = 'O'

    # tilt west
    for row_idx in range(0, len(positions)):
        count_rocks = 0
        for col_idx in range(len(positions[0]) - 1, -1, -1):
            el = positions[row_idx][col_idx]
            if el == 'O':
                positions[row_idx][col_idx] = '.'
                count_rocks += 1
            if el == '#':
                for i in range(1, count_rocks + 1):
                    positions[row_idx][col_idx + i] = 'O'
                count_rocks = 0
            if col_idx == 0:
                for i in range(0, count_rocks):
                    positions[row_idx][col_idx + i] = 'O'

    # tilt south
    for col_idx in range(0, len(positions[0])):
        count_rocks = 0
        for row_idx in range(0, len(positions)):
            el = positions[row_idx][col_idx]
            if el == 'O':
                positions[row_idx][col_idx] = '.'
                count_rocks += 1
            if el == '#':
                for i in range(1, count_rocks + 1):
                    positions[row_idx - i][col_idx] = 'O'
                count_rocks = 0
            if row_idx == len(positions) - 1:
                for i in range(0, count_rocks):
                    positions[row_idx - i][col_idx] = 'O'

    # tilt east
    for row_idx in range(0, len(positions)):
        count_rocks = 0
        for col_idx in range(0, len(positions[0])):
            el = positions[row_idx][col_idx]
            if el == 'O':
                positions[row_idx][col_idx] = '.'
                count_rocks += 1
            if el == '#':
                for i in range(1, count_rocks + 1):
                    positions[row_idx][col_idx - i] = 'O'
                count_rocks = 0
            if col_idx == len(positions[0]) - 1:
                for i in range(0, count_rocks):
                    positions[row_idx][col_idx - i] = 'O'
    distance = len(positions)
    total_load = 0
    for row in positions:
        total_load += row.count('O') * distance
        distance -= 1

    loads.append(total_load)

occurrences = [i for i, load in enumerate(loads) if load == 100988]  # this number was found manually in the output
first, second = occurrences[0], occurrences[1]
seq_len = second - first
x = 1000000000 - first - 1
seq_pos = x % seq_len
seq = loads[first:second]
print(seq[seq_pos])
