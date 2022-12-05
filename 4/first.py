text = open('input', 'r')

count = 0
while True:
    line = text.readline()
    if not line:
        break

    ranges = line.split(',')
    first_range_strings = ranges[0].split('-')
    second_range_strings = ranges[1].split('-')
    a = int(first_range_strings[0])
    b = int(first_range_strings[1])
    x = int(second_range_strings[0])
    y = int(second_range_strings[1].strip())

    # print(f"{a}-{b},{x}-{y}")

    # if a <= x <= b and a <= y <= b:
    #     count += 1
        # print(f"<{a},{b}>   <{x},{y}>")
        # continue
    #
    # if x <= a <= y and x <= b <= y:
    #     count += 1
    #     print(f"<{a},{b}>   <{x},{y}>")
        # continue

    if a <= x <= b or a <= y <= b or x <= a <= y or x <= b <= y:
        count += 1



print(count)
