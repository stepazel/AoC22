from itertools import chain

text = open('input', 'r')

matrix = []
while True:
    line = text.readline()
    if not line:
        break

    row = []
    for s in line:
        if s == '\n':
            continue
        row.append(s)

    matrix.append(row)


def get_element(row_idx, col_idx):
    if row_idx < 0 or col_idx < 0 or col_idx >= len(matrix) or row_idx >= len(matrix[0]):
        return 'X'
    return matrix[row_idx][col_idx]


def extract_neighbors_of_digit(row_idx, col_idx):
    neighbors = []
    prev_char: str = get_element(row_idx, col_idx - 1)
    next_char: str = get_element(row_idx, col_idx + 1)
    # always append the top and bottom ones

    # neighbors.append([matrix[row_idx - 1][col_idx], matrix[row_idx + 1][col_idx]])
    neighbors.append(get_element(row_idx - 1, col_idx))
    neighbors.append(get_element(row_idx + 1, col_idx))
    if not prev_char.isdigit():
        neighbors.append([
            get_element(row_idx, col_idx - 1),  # the left one
            get_element(row_idx - 1, col_idx - 1),  # top-left
            get_element(row_idx + 1, col_idx - 1),  # bottom-left
        ])
    if not next_char.isdigit():
        neighbors.append([
            get_element(row_idx, col_idx + 1),  # right
            get_element(row_idx - 1, col_idx + 1),  # top-right
            get_element(row_idx + 1, col_idx + 1)  # bottom-right
        ])
    x = list(chain.from_iterable(neighbors))
    return x


suma = 0
number = ''
neighbors: list = []
for row_idx in range(0, len(matrix)):
    row = matrix[row_idx]

    for col_idx in range(0, len(row)):
        char = row[col_idx]
        if char.isdigit():
            number += char
            neighbors.append(extract_neighbors_of_digit(matrix, row_idx, col_idx))
            if col_idx == 139:
                neighbors_str = ''.join(list(chain.from_iterable(neighbors)))
                neighbors_str = neighbors_str.replace('X', '')
                neighbors_str = neighbors_str.replace('.', '')
                if not neighbors_str.isalnum() and number != '' and neighbors_str != '':
                    suma += int(number)
                number = ''
                neighbors = []
        else:
            neighbors_str = ''.join(list(chain.from_iterable(neighbors)))
            neighbors_str = neighbors_str.replace('X', '')
            neighbors_str = neighbors_str.replace('.', '')

            if not neighbors_str.isalnum() and number != '' and neighbors_str != '':
                suma += int(number)
            number = ''
            neighbors = []

print(suma)
