
text = open('input', 'r').read()

start = 0
end = 14
while True:
    group_of_four = text[start:end]
    if group_of_four[13] == '\n':
        break

    contains_two_occurrences = False
    for char in group_of_four:
        if group_of_four.count(char) > 1:
            contains_two_occurrences = True

    if not contains_two_occurrences:
        break

    start += 1
    end += 1


print(end)