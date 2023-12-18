text = open('input', 'r')


lines = text.readlines()
positions = []

for line in lines:
    row = [s for s in line if s != '\n']
    positions.append(row)

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


distance = len(positions)
total_load = 0
for row in positions:
    total_load += row.count('O') * distance
    distance -= 1
print(total_load)
