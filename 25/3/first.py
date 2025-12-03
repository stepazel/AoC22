text = open('input', 'r')

result = 0

while True:
    bank = text.readline()[:-1]
    if not bank:
        break

    largest_joltage = 0

    for battery_position in range(len(bank)):
        first_digit = int(bank[battery_position]) * 10
        for second_battery_position in range(battery_position + 1, len(bank)):
            joltage = first_digit + int(bank[second_battery_position])
            if joltage > largest_joltage:
                largest_joltage = joltage

    result += largest_joltage

print(result)



