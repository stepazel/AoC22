text = open('input', 'r')

universe, galaxies, label, row = [], {}, 1, 0
empty_rows = []
empty_cols = []
# construct the universe array and find empty rows
while True:
    line = text.readline()
    if not line:
        break

    universe.append([])
    for s in line.replace('\n', ''):
        element = 0
        if s == '#':
            element = label
            label += 1
        universe[row].append(element)
    if all(el == 0 for el in universe[row]):
        empty_rows.append(row)
    row += 1

# find empty cols
col = []
col_idx = 0
while True:
    try:
        col = [row[col_idx] for row in universe]
    except IndexError:
        break
    if all(row[col_idx] == 0 for row in universe):
        empty_cols.append(col_idx)
    col_idx += 1


# index the galaxies dictionary
for row_idx in range(0, len(universe)):
    for col_idx in range(0, len(universe[0])):
        el = universe[row_idx][col_idx]
        if el != 0:
            galaxies[el] = row_idx, col_idx

distance = 999_999
def get_shortest_path_length(first_galaxy, second_galaxy):
    first_coordinates = galaxies[first_galaxy]
    second_coordinates = galaxies[second_galaxy]
    first_galaxy_row, first_galaxy_col = first_coordinates[0], first_coordinates[1]
    second_galaxy_row, second_galaxy_col = second_coordinates[0], second_coordinates[1]
    empty_rows_count = [first_galaxy_row < empty_row < second_galaxy_row
                        or second_galaxy_row < empty_row < first_galaxy_row for empty_row in empty_rows].count(True)
    empty_cols_count = [first_galaxy_col < empty_col < second_galaxy_col
                        or second_galaxy_col < empty_col < first_galaxy_col for empty_col in empty_cols].count(True)
    return (
            (abs(first_coordinates[0] - second_coordinates[0]) + empty_rows_count * distance) +
            (abs(first_coordinates[1] - second_coordinates[1]) + empty_cols_count * distance))

answer = 0
for galaxy in galaxies.keys():
    for galaxy_after in filter(lambda key: key > galaxy, galaxies.keys()):
        answer += get_shortest_path_length(galaxy, galaxy_after)
print(answer)


