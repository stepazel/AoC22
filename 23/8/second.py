import math
import sys

sys.setrecursionlimit(64_000_000)
text = open('input', 'r')
network = {}
instructions = text.readline().replace('\n', '')
text.readline()
labels_ending_with_a = []
labels_ending_with_z = []
while True:
    line = text.readline()
    if not line:
        break

    label, left, right = line[0:3], line[7:10], line[12:15]
    if label[2] == 'A':
        labels_ending_with_a.append(label)
    if label[2] == 'Z':
        labels_ending_with_z.append(label)
    network[label] = {'L': left, 'R': right}


def get_next_label(label: str, step: int = 0):
    if label[2] == 'Z':
        return step
    return get_next_label(network[label][instructions[step % len(instructions)]], step + 1)


first_occurrences: list[int] = []
for label in labels_ending_with_a:
    step = get_next_label(label)
    first_occurrences.append(step)
print(math.lcm(*first_occurrences))
