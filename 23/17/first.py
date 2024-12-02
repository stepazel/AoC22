import sys

text = open('test_input', 'r')
# sys.setrecursionlimit(10_000_000)

city_blocks = []

# je to nejaky problem hledani minimalni kostry ne
for line in text.readlines():
    row = [int(s) for s in line[:-1]]
    city_blocks.append(row)

path_losses = []
# find_path(0, 0, 'B', 0, 0)
print(min(path_losses))