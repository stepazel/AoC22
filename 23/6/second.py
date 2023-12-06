text = open('input', 'r')
max_time = int(text.readline().replace(' ', '').split(':')[1])
record = int(text.readline().replace(' ', '').split(':')[1])

record_times_count = 0
for time in range(max_time):
    if (max_time - time) * time > record:
        record_times_count += 1

print(f'a={max_time}, c={record}')

print(record_times_count)  # 21039729