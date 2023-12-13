import functools

text = open('input', 'r')


def drop_slice(x, slice):
    return x[slice:]


def drop_first(x):
    return drop_slice(x, 1)


@functools.cache
def check_options(springs: str, pattern: tuple) -> int:
    if not pattern:
        if "#" not in springs:
            return 1
        else:
            return 0
    if not springs:
        return 0

    current_spring = springs[0]
    if current_spring == '.':
        return check_options(drop_first(springs), pattern)

    if current_spring == '?':
        return (check_options('#' + springs[1:], pattern) +
                check_options('.' + springs[1:], pattern))

    if current_spring == '#':
        group_length = pattern[0]
        if (len(springs[:group_length]) >= group_length
            and springs[:group_length].count('.') == 0) \
                and (len(springs) <= group_length or springs[group_length] != '#'):
            springs = drop_slice(springs, group_length + 1)
            pattern = drop_first(pattern)
            return check_options(springs, pattern)
        return 0


answer = 0
while True:
    line = text.readline()
    if not line:
        break

    conditions = line.split(' ')[0]
    unfolded_conditions = (f'{conditions}?' * 5)[:-1]
    pattern = line.split(' ')[1][:-1]
    unfolded_pattern = (f'{pattern},' * 5)[:-1]
    pattern_array = [int(s) for s in unfolded_pattern.split(',')]
    number_of_combinations = check_options(unfolded_conditions, tuple(pattern_array))
    answer += number_of_combinations

print(answer)
