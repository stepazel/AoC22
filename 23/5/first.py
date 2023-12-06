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


def num_there(string):
    return any(char.isdigit() for char in string)


def get_numbers_from_line(line: str) -> list:
    return [int(s) for s in re.findall(r'\d+', line)]


first_line = text.readline()
seeds = get_numbers_from_line(first_line)

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
            # offset = range_length if destination_range_start > source_range_start else range_length * -1
            offset = (source_range_start - destination_range_start) * -1
            # create the ranges with offsets
            ranges[key_name].append([
                (source_range_start, source_range_start + range_length - 1),
                (destination_range_start, destination_range_start + range_length - 1),
                offset
            ])


def get_location_number(source_number: int, key_position=0):
    destination_number = source_number
    key_name = map_keys[key_position]

    for range in ranges[key_name]:
        if range[0][0] <= source_number <= range[0][1]:
            destination_number = source_number + range[2]  # range[2] is the offset

    if key_name == 'humidity-to-location':
        return destination_number
    return get_location_number(destination_number, key_position + 1)

print(get_location_number(3419578085))
# For test input
# assert get_item('seed-to-soil', 79) == 81
# assert get_item('seed-to-soil', 14) == 14
# assert get_item('seed-to-soil', 55) == 57
# assert get_item('seed-to-soil', 13) == 13
# assert get_destination_number(79) == 82
# assert get_destination_number(14) == 43
# assert get_destination_number(55) == 86
# assert get_destination_number(13) == 35
# location_numbers = [get_location_number(seed_number) for seed_number in seeds]
# location_numbers_2 = [get_location_number(seed_number) for seed_number in seeds_second_part]
# print(min(location_numbers))
# 3 biliony wtf
# 3 677 773 912
# print(min(location_numbers_2))
# assert min(location_numbers) == 35
# assert min(location_numbers_2) == 46
