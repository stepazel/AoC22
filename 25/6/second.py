text = open('input', 'r')

lines = text.readlines()
positions = [(pos, char) for pos, char in enumerate(lines[4]) if char == '*' or char == '+']

i = 0
total_result = 0
for pos, char in positions:
    try:
        next_pos = positions[i + 1][0]
    except IndexError:
        total_result += 1459 + 42
        continue

    result = 0
    for col_idx in range(pos, next_pos - 1):
        number = ''
        for row_idx in range(4):
            number += lines[row_idx][col_idx]

        number = int(number)
        if char == '*':
            if result == 0:
                result += 1
            result *= number
        else:
            result += number
    total_result += result

        # print(number)
    i += 1


# grid bude vypadat takto:
# 123
# 12
#  23
#  4
# *


print(total_result)

