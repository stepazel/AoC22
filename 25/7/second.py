from functools import lru_cache

lines = open('input', 'r').readlines()


@lru_cache(maxsize=None)
def find_split_count(row_idx, col_idx, count):
    if count != 0 and count % 100 == 0:
        print(count)
    if row_idx == len(lines) - 1:
        return count + 1
    else:
        field = lines[row_idx][col_idx]

        if field == '.':
            return find_split_count(row_idx + 1, col_idx, count)

        return find_split_count(row_idx, col_idx - 1, count) + find_split_count(row_idx, col_idx + 1, count)


print((find_split_count(0, 70, 0)))
