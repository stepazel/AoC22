import re
text = open('input', 'r')
maps = {
    'seed-to-soil': {},
    'soil-to-fertilizer': {},
    'fertilizer-to-water': {},
    'water-to-light': {},
    'light-to-temperature': {},
    'temperature-to-humidity': {},
    'humidity-to-location': {}
}
map_keys = list(maps.keys())


def get_item(map_name: str, key: int):
    if key not in maps[map_name]:
        return key
    return maps[map_name][key]


def get_item_recursively(key: int, map_position=0):
    map_name = map_keys[map_position]
    if map_position == len(maps) - 1:  # if we reached the last 'humidity-to-location' map
        return get_item(map_name, key)

    return get_item_recursively(get_item(map_name, key), map_position + 1)


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

            # create the map
            for i in range(range_length):
                maps[key_name][source_range_start + i] = destination_range_start + i

location_numbers_from_seeds = [get_item_recursively(seed_number) for seed_number in seeds]
print(min(location_numbers_from_seeds))

# For test input
# assert get_item('seed-to-soil', 79) == 81
# assert get_item('seed-to-soil', 14) == 14
# assert get_item('seed-to-soil', 55) == 57
# assert get_item('seed-to-soil', 13) == 13
# assert get_item_recursively(79) == 82
# assert get_item_recursively(14) == 43
# assert get_item_recursively(55) == 86
# assert get_item_recursively(13) == 35
