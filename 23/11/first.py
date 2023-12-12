text = open('test_input', 'r')

universe, galaxies, label, row = [], {}, 1, 0
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
        universe.insert(row + 1, [0 for i in universe[row]])
        row += 1
    row += 1

def insert_col_to_matrix(matrix, col_idx: int):
    for row_idx in range(0, len(matrix)):
        matrix[row_idx].insert(col_idx, 0)


def index_of(number: int):
    for row_idx in range(0, len(universe)):
        for col_idx in range(0, len(universe[0])):
            if universe[row_idx][col_idx] == number:
                return row_idx, col_idx

col = []
col_idx = 0
while True:
    try:
        col = [row[col_idx] for row in universe]
    except IndexError:
        break
    if all(row[col_idx] == 0 for row in universe):
        insert_col_to_matrix(universe, col_idx + 1)
        col_idx += 1
    col_idx += 1

for row_idx in range(0, len(universe)):
    for col_idx in range(0, len(universe[0])):
        el = universe[row_idx][col_idx]
        if el != 0:
            galaxies[el] = row_idx, col_idx


def get_shortest_path_length(first_galaxy, second_galaxy):
    first_coordinates = galaxies[first_galaxy]
    second_coordinates = galaxies[second_galaxy]
    print(f'For {first_galaxy} - {second_galaxy}: {abs(first_coordinates[0] - second_coordinates[0]) + abs(first_coordinates[1] - second_coordinates[1])}')
    print(f'It is a sum of {abs(first_coordinates[0] - second_coordinates[0])} and {abs(first_coordinates[1] - second_coordinates[1])}')
    return abs(first_coordinates[0] - second_coordinates[0]) + abs(first_coordinates[1] - second_coordinates[1])

answer = 0
for galaxy in galaxies.keys():
    for galaxy_after in filter(lambda key: key > galaxy, galaxies.keys()):
        answer += get_shortest_path_length(galaxy, galaxy_after)

print(answer)


