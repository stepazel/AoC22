import re
text = open('3/input', 'r')

result = 0
while True:
    line = text.readline()
    muls = re.findall("(mul\(\d+,\d+\))", line)
    numbers = [int(number) for number in re.findall(r'\d+', ''.join(muls))]

    for i in range(0, len(numbers), 2):
        result += numbers[i] * numbers[i+1]
    if not line:
        break

print(result)


