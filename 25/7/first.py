lines = open('input', 'r').readlines()


def find_splitters(row_idx, col_idx, splitters):
    if (row_idx, col_idx) in splitters:
        return splitters

    if row_idx >= len(lines):
        return splitters
    else:
        field = lines[row_idx][col_idx]

        if field == '.':
            return find_splitters(row_idx + 1, col_idx, splitters)

        splitters += [(row_idx, col_idx)]
        find_splitters(row_idx, col_idx - 1, splitters)
        find_splitters(row_idx, col_idx + 1, splitters)
        return splitters


print(print(len(find_splitters(0,70, []))))

