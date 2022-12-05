from string import ascii_lowercase, ascii_letters

text = open('input', 'r')


def get_charscore_from_string(first_half, second_half):
    for char in second_half:
        if first_half.find(char) != -1:
            return ascii_letters.index(char) + 1


score = 0
while True:
    line = text.readline()
    if not line:
        break

    line = line.strip()
    length = len(line)
    first_half = line[:length // 2]
    second_half = line[length // 2:]
    score += get_charscore_from_string(first_half, second_half)

print(score)
