import re
from functools import reduce
text = open('input', 'r')

times = [int(s) for s in re.findall(r'\d+', text.readline())]
distances = [int(s) for s in re.findall(r'\d+', text.readline())]

record_times_counts = []
for i in range(len(times)):
    max_time = times[i]
    record = distances[i]
    record_times_count = 0
    for time in range(max_time):
        if (max_time - time) * time > record:
            record_times_count += 1
    record_times_counts.append(record_times_count)

print(reduce(lambda x, y: x*y, record_times_counts))

