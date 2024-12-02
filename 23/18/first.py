text = open('input', 'r')

lines = text.readlines()
sides = [int(line[2]) for line in lines]
terrain = []
for i in range(0, 5_00):
    row = []
    for j in range(0, 5_00):
        row.append('.')
    terrain.append(row)

r, c = 0, 0
for line in lines:
    direction = line[0]
    length = int(line[2])
    # print(f'Moving {length} steps in direction {direction}')
    for i in range(0, length):
        terrain[r][c] = '#'
        if direction == 'R':
            c = c + 1
        elif direction == 'D':
            r += 1
        elif direction == 'L':
            c -= 1
        elif direction == 'U':
            r -= 1


file = open('output', 'w')
for row in terrain:
    file.write(''.join(row))
file.close()







# odpoved bude nejaka ta Pickova teorie
print(len(sides))
print(sum(sides))