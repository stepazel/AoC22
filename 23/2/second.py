text = open('input', 'r')


def find_largest_count_for_color(line: str, color: str):
    idx = 0
    max_for_color = 0
    while True:
        idx = line.find(color, idx+1)
        if idx == -1:
            break

        count = int(line[idx-3:idx-1].strip(' '))
        if count > max_for_color:
            max_for_color = count
    return max_for_color


set_power_sum = 0
while True:
    line = text.readline()
    if not line:
        break

    blue_min_number = find_largest_count_for_color(line, 'blue')
    red_min_number = find_largest_count_for_color(line, 'red')
    green_min_number = find_largest_count_for_color(line, 'green')

    set_power_sum += blue_min_number * red_min_number * green_min_number

print(set_power_sum)



