text = open('input', 'r')

result = 0


# 811111111111119
# 1. 8111 > 8
# 2. 1111 > 1


# 818181911112111
# 8181 > 8:0
#  1818 > 8:2
#    181 > 8:4
#      19 > 9:6
#        1 > 1:7
#         1 > 1:8
#          1
#        1111
#         1112

# Vyberu range bank[last_max_index:-(11 - current_digit)

def get_max_digit(current_bank, last_max_index, current_digit):

    # current_range = current_bank[last_max_index:-(11 - current_digit)]
    current_range = current_bank[last_max_index:len(current_bank) - (11 - current_digit)]
    current_index = last_max_index

    max_index = current_index
    max_digit = 0
    for battery in current_range:
        if int(battery) > max_digit: # je 1 na indexu 3 vetsi nez 0?
            max_digit = int(battery)
            max_index = current_index
        current_index += 1

    # print(f'For {current_range} at {current_digit}. digit: Max = {max_digit}, index = {max_index}')
    return max_digit, max_index + 1



while True:
    bank = text.readline()[:-1]
    if not bank:
        break

    largest_joltage = 0
    current_max, current_pos = 0, 0
    # print(f'Bank = {bank}')
    for digit_index in range(12):
        current_max, current_pos = get_max_digit(bank, current_pos, digit_index)
        largest_joltage += current_max * (10 ** (11 - digit_index))

    # print(f'Largest joltage = {largest_joltage}')
    result += largest_joltage

print(result)


# 987654321111
# 811111111119
# 434234234278
# 888911112111


# 3121910778619
# 3121910778619
