text = open('input', 'r')
lines = text.readlines()

patterns = []
pattern_length = 0
for row_idx in range(0, len(lines)):
    row = lines[row_idx]
    if row == '\n':
        pattern_rows = [line.strip() for line in lines[row_idx - pattern_length:row_idx] if line != '\n']
        patterns.append(pattern_rows)
        pattern_length = 0
    pattern_length += 1


def get_col(matrix, col_idx):
    col = ''
    for row_idx in range(0, len(matrix)):
        col += matrix[row_idx][col_idx]
    return col


def is_row_of_reflection(pos):
    offset = 1
    while True:
        if pos - offset < 0 or pos + 1 + offset >= len(pattern):
            return True
        current_row = pattern[pos - offset]
        next_row = pattern[pos + 1 + offset]
        if current_row != next_row:
            return False
        offset += 1


def get_number_of_rows(pattern: list, pos: int = 0):
    if pos == len(pattern) - 1:
        return 0
    if pattern[pos] == pattern[pos + 1]:
        if is_row_of_reflection(pos):
            return pos + 1
    return get_number_of_rows(pattern, pos + 1)


def is_line_of_reflection(pos, next_pos):
    offset = 1
    while True:
        if pos - offset == -1 or pos + 1 + offset == len(pattern[0]):  # reached the end
            return True
        col = get_col(pattern, pos - offset)
        next_col = get_col(pattern, pos + 1 + offset)
        if col != next_col:
            return False
        offset += 1


def get_number_of_cols(pattern: list, pos: int = 0) -> int:
    if pos == len(pattern[0]) - 1:
        return 0
    col = get_col(pattern, pos)
    next_col = get_col(pattern, pos + 1)
    if col == next_col:
        if is_line_of_reflection(pos, pos + 1):
            return pos + 1
    return get_number_of_cols(pattern, pos + 1)


answer = 0
for pattern in patterns:
    answer += get_number_of_cols(pattern)
    answer += 100 * get_number_of_rows(pattern)

print(answer)
