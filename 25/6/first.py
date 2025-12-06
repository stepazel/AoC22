text = open('input', 'r')

grid = []
while True:
    line = text.readline()[:-1]
    if not line:
        break

    row = [x for x in line.split(' ') if x != ' ' and x != '']
    grid.append(row)
    print(row)

total_result = 0
for col_idx in range(0, len(grid[0])):
    result = 0
    operation = grid[4][col_idx]
    for row_idx in range(4):
        number = int(grid[row_idx][col_idx])
        if operation == '*':
            if result == 0:
                result += 1
            result *= number
        else:
            result += number

    total_result += result

print(total_result)

