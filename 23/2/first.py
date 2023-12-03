text = open('input', 'r')


def is_too_much(line: str, color: str, max: int):
    idx = 0
    while True:
        idx = line.find(color, idx+1)
        if idx == -1:
            break
        count = int(line[idx-3:idx-1].strip(' '))
        if count > max:
            return True
    return False


game_id_sum = 0
while True:
    line = text.readline()
    if not line:
        break

    blue_count = is_too_much(line, 'blue', 14)
    red_count = is_too_much(line, 'red', 12)
    green_count = is_too_much(line, 'green', 13)
    print(f'B={blue_count}, R={red_count}, G={green_count} \n{line}')
    if blue_count or red_count or green_count:
        continue

    first_space_idx = line.find(' ')
    colon_idx = line.find(':')
    print(int(line[first_space_idx:colon_idx]))
    game_id_sum += int(line[first_space_idx:colon_idx])

print(game_id_sum)
