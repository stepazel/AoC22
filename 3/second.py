from string import ascii_letters

text = open('input', 'r')

def find_same_chars_in_strings(first_string, second_string):
    chars = ''
    for char in second_string:
        if first_string.find(char) != -1:
            chars = chars + char
    return chars


def get_char_from_chars(chars, third_string):
    for char in third_string:
        if chars.find(char) != -1:
            return char

score = 0
while True:
    first_line = text.readline().strip()
    second_line = text.readline().strip()
    third_line = text.readline().strip()

    if not first_line:
        break

    found_chars = find_same_chars_in_strings(first_line, second_line)

    same_char = get_char_from_chars(found_chars, third_line)

    score += ascii_letters.index(same_char) + 1

    print(f'{first_line} + {second_line} + {third_line} => {found_chars} + {same_char}')

print(score)
