# I need to find first group of 4 chars where there no char repeats
# then i need to find the position of the 4th char of this group
# bvwbjplbgvbhsrlpgdmjqwftvncz -> j 5
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw -> r 11

text = open('input', 'r').read()
# group_of_four = text[0:4]
# print(group_of_four)

start = 0
end = 4
while True:
    group_of_four = text[start:end]
    if group_of_four[3] == '\n':
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