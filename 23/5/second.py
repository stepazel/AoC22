import re

text = open('input', 'r')

ranges = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}
map_keys = list(ranges.keys())


def get_location_number(source_number: int, key_position=0):
    destination_number = source_number
    key_name = map_keys[key_position]

    for range in ranges[key_name]:
        if range[0][0] <= source_number <= range[0][1]:
            print(
                f'Source number {source_number} belongs to a range <{range[0][0]}; {range[0][1]}>. Adding offset {range[2]}')
            destination_number = source_number + range[2]  # range[2] is the offset

    if key_name == 'humidity-to-location':
        print(f'{source_number:,} => {destination_number:,}  |  {key_position}. {key_name}')
        return destination_number
    print(f'{source_number:,} => {destination_number:,}  |  {key_position}. {key_name}\n')
    return get_location_number(destination_number, key_position + 1)


def get_seed_number(source_number: int, key_position=6, log=False):  # start from the end
    destination_number = source_number
    key_name = map_keys[key_position]
    # range[0] is source, range[1] is destination, but right now it is VICEVERSA!
    for range in ranges[key_name]:
        source_range = range[1]
        if source_range[0] <= source_number <= source_range[1]:
            destination_number = source_number - range[2]

    if key_name == 'seed-to-soil':
        if log:
            print(f'{source_number:,} => {destination_number:,}  |  {key_position}. {key_name}')
        return destination_number
    if log:
        print(f'{source_number:,} => {destination_number:,}  |  {key_position}. {key_name}\n')
    return get_seed_number(destination_number, key_position - 1, log=log)


def num_there(string):
    return any(char.isdigit() for char in string)


def get_numbers_from_line(line: str) -> list:
    return [int(s) for s in re.findall(r'\d+', line)]


first_line = text.readline()
seeds = get_numbers_from_line(first_line)  # ignore

seed_initial_ranges = []
for i in range(0, len(seeds), 2):
    seed_initial_ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

seed_initial_ranges.sort()

while True:
    line = text.readline()
    if not line:
        break

    if not num_there(line) and line != '\n':
        key_name = line.split(' ')[0]
        while True:
            line = text.readline()
            if not line or line == '\n':
                break
            numbers = get_numbers_from_line(line)
            assert len(numbers) == 3
            destination_range_start = numbers[0]
            source_range_start = numbers[1]
            range_length = numbers[2]
            offset = (source_range_start - destination_range_start) * -1
            # create the ranges with offsets
            ranges[key_name].append([
                (source_range_start, source_range_start + range_length - 1),
                (destination_range_start, destination_range_start + range_length - 1),
                offset
            ])

location_number = 0
count = 0
while True:
    if location_number % 1_000_000 == 0:
        print(location_number)
    seed_number = get_seed_number(location_number)
    for range in seed_initial_ranges:
        if range[0] <= seed_number <= range[1]:
            count += 1
            print(location_number)
            raise Exception(f'Found it.')
    location_number += 1
