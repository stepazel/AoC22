text = open('commands', 'r')

storage = {
    1: ['W', 'R', 'F'],
    2: ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
    3: ['P', 'M', 'Z', 'N', 'L'],
    4: ['J', 'C', 'H', 'R'],
    5: ['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
    6: ['G', 'C', 'W', 'L', 'F', 'Z'],
    7: ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
    8: ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
    9: ['J', 'W', 'H', 'G', 'R', 'S', 'V']
}

while True:
    line = text.readline()
    if not line:
        break

    digits = [int(s) for s in line.split() if s.isdigit()]
    count = digits[0]
    source_stack = digits[1]
    target_stack = digits[2]

    end_items = storage[source_stack][-count:]
    # end_items.reverse() for the first part
    del storage[source_stack][-count:]

    storage[target_stack].extend(end_items)

print(storage)

