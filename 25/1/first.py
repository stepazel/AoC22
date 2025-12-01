text = open('input', 'r')


position = 50
result = 0

# This is solution for the second part. Forgot to commit the first part.
while True:
    line = text.readline()
    if not line:
        break

    direction = line[0]
    rotation = int(line[1:])

    for i in range(0, rotation):
        if direction == 'R':
            position += 1
        else:
            position -= 1
        if abs(position) % 100 == 0:
            result += 1

print(result)


