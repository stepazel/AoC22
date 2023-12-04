text = open('input', 'r')

# At start, we only have 1 instance of each card
card_instances = {}
for i in range(1, 207):
    card_instances[i] = 1


def get_count_of_winning_numbers(numbers):
    winning_numbers = numbers[0:10]
    my_numbers = numbers[10:]
    count = 0
    for number in my_numbers:
        if number in winning_numbers:
            count += 1
    return count


position = 1
while True:
    line = text.readline()
    if not line:
        break

    numbers = [int(s) for s in line.split() if s.isdigit()]
    count = get_count_of_winning_numbers(numbers)

    for i in range(1, count + 1):
        try:
            card_instances[position + i] += card_instances[position]
        except IndexError:
            pass
    position += 1
print(str(sum(card_instances.values())))




