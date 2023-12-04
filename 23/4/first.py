text = open('input', 'r')


answer = 0
while True:
    line = text.readline()
    if not line:
        break

    numbers = [int(s) for s in line.split() if s.isdigit()]
    winning_numbers = numbers[0:10]
    my_numbers = numbers[10:]
    count = 0
    for number in my_numbers:
        if number in winning_numbers:
            count += 1

    if count > 0:
        answer += 2**(count-1)
print(answer)
