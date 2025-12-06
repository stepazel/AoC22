text = open('input', 'r')

lines = text.readlines()
ranges = []
for i in range(169): # 169 | 4
    id_range = [int(x) for x in lines[i][:-1].split('-')]
    ranges.append(id_range)

for current_idx, current_range in enumerate(ranges):
    for i in range(0, len(ranges)):
        if current_idx == i:
            continue

        range_to_compare = ranges[i]
        range_start,range_end = current_range[0], current_range[1]
        compare_start, compare_end = range_to_compare[0], range_to_compare[1]

        if range_start == 'ne' or compare_start == 'ne':
            continue

        if range_start >= compare_start and range_end <= compare_end: # je podinterval
            current_range[0] = 'ne'
            break

        if compare_start <= range_start <= compare_end:
            current_range[0] = compare_end + 1

        if compare_start <= range_end <= compare_end:
            current_range[1] = compare_start - 1


available_ids_count = 0
for new_range in ranges:
    print(new_range)
    if new_range[0] == 'ne':
        continue

    if new_range[1] == new_range[0]:
        continue

    available_ids_count += new_range[1] - new_range[0] + 1

print(available_ids_count)
