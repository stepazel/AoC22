steps = open('input', 'r').readline().split(',')
steps[-1] = steps[-1].strip()


def get_hash(string: str, value: int = 0, pos: int = 0) -> int:
    if pos == len(string):
        return value
    code = ord(string[pos])
    value += code
    value = value * 17
    value = value % 256
    return get_hash(string, value, pos + 1)


answer = 0
for step in steps:
    answer += get_hash(step)
print(answer)  # 512283
