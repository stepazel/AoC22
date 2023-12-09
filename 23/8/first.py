import sys
sys.setrecursionlimit(1_000_000)
text = open('input', 'r')
network = {}
instructions = text.readline().replace('\n', '')
text.readline()
while True:
    line = text.readline()
    if not line:
        break

    label, left, right = line[0:3], line[7:10], line[12:15]
    network[label] = {'L': left, 'R': right}


def get_next_label(label: str, step: int):
    if label == 'ZZZ':
        return step
    return get_next_label(network[label][instructions[step % len(instructions)]], step + 1)


print(f'Number of steps to reach ZZZ from AAA is {get_next_label('AAA', 0)}')
