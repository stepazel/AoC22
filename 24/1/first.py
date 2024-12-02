text = open('1/input', 'r')

first_column = []
second_column = []

while True:
    line = text.readline()
    if not line:
        break

    first_number = int(line[:5])
    second_number = int(line[8:])    
    first_column.append(first_number)
    second_column.append(second_number)

first_column.sort()
second_column.sort()

sum = 0
for i in range(0, len(first_column)):
    diff = abs(first_column[i] - second_column[i])
    sum += diff

print(sum)
