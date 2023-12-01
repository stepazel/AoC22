text = open('input', 'r')
suma = 0

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

while True:
    line = text.readline()
    if not line:
        break

    min_idx = 10000
    max_idx = 0
    first_number = ''
    last_number = ''
    for word in numbers:
        idx = line.find(word)
        ridx = line.rfind(word)
        if idx == -1:
            continue

        if idx < min_idx:
            min_idx = idx
            first_number = word
        if ridx > max_idx:
            last_number = word
            max_idx = ridx

    number = f'{first_number}{last_number}'
    for word, digit in numbers_dict.items():
        number = number.replace(word, str(digit))

    number = number[0] + number[-1]
    suma = suma + int(number)
print(suma)