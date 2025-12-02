text = open('input', 'r').readline()
invalid_ids_sum = 0


ranges = [(x.split('-')) for x in text.split(',')]

for custom_range in ranges:
    for i in range(int(custom_range[0]), int(custom_range[1]) + 1):
        id = str(i)
        if len(id) % 2 == 1:
            continue

        firstpart, secondpart = id[:len(id) // 2], id[len(id) // 2:]

        if firstpart == secondpart:
            # print(f'{firstpart} - {secondpart}')
            invalid_ids_sum += i

print(invalid_ids_sum)





