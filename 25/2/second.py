text = open('input', 'r').readline()
invalid_ids_sum = 0

def is_pattern(id):
    for split_len in range(1, len(id) // 2 + 1):  # funguje
        parts = [id[i:i+split_len] for i in range(0, len(id), split_len)]
        if parts.count(parts[0]) == len(parts):
            return True
    return False

ranges = [(x.split('-')) for x in text.split(',')]
for custom_range in ranges:
    for i in range(int(custom_range[0]), int(custom_range[1]) + 1):
        id = str(i)
        if is_pattern(id):
            invalid_ids_sum += i

print(invalid_ids_sum)





