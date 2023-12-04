text = open('input', 'r')


def get_element(row_idx, col_idx):
    if row_idx < 0 or col_idx < 0 or col_idx >= len(matrix) - 1 or row_idx >= len(matrix[0]) - 1:
        return 'X'
    return matrix[row_idx][col_idx]


def add(key: str, number: int):
    if key in star_nbs:
        star_nbs[key].append(number)
    else:
        star_nbs[key] = [number]


def find_stars_in_surrounding(row_idx, col_idx, number):
    for i in range(len(number) + 2):
        for j in [-1, 0, 1]:
            key = str(row_idx + j) + ' ' + str(col_idx - i)
            if get_element(row_idx + j, col_idx - i) == '*':
                add(key, int(number))


matrix = []
star_nbs = {}
while True:
    line = text.readline()
    if not line:
        break

    row = []
    for s in line:
        row.append(s)

    matrix.append(row)

number = ''
for row_idx in range(0, len(matrix)):
    row = matrix[row_idx]

    for col_idx in range(0, len(row)):
        char = row[col_idx]
        if char.isdigit():
            number += char
        else:
            if number != '':
                find_stars_in_surrounding(row_idx, col_idx, number)
            number = ''

suma = 0
for _, items in star_nbs.items():
    if len(items) == 2:
        suma += items[0] * items[1]

print(suma)
