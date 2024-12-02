text = open('1/input', 'r')

appearances = {}
first_column = []
while True:
    line = text.readline()
    if not line:
        break

    first_number = int(line[:5])
    second_number = int(line[8:]) 

    first_column.append(first_number)

    if (second_number not in appearances):
        appearances[second_number] = 1
    else:
        appearances[second_number] += 1

sum = 0
for id in first_column:
    score = 0
    if id in appearances:
        score = id * appearances[id]
    sum += score

print(sum)



    