import re
text = open('3/input', 'r')
with open('3/input', 'r') as f:
    text = [word.strip() for word in f]
text = ''.join(text)


result = 0
muls = {m.start():m.group() for m in re.finditer("(mul\(\d+,\d+\))", text)}
dos = {m.start():m.group() for m in re.finditer(r"(do())", text)}
donts = {m.start():m.group() for m in re.finditer(r"(don't())", text)}

mul_count = 0
# for key, value in muls.items():
print(len(muls))
do = True
for i in range(0, len(text)):
    if i in dos:
        do = True
    if i in donts:
        do = False
    
    if do and i in muls:
        numbers = [int(number) for number in re.findall(r'\d+', ''.join(muls[i]))]
        result += numbers[0] * numbers[1]

print(result)
