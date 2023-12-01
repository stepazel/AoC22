text = open('input', 'r')
suma = 0
while True:
    line = text.readline()
    if not line:
        break

    digits = [s for s in line if s.isdigit()]
    num = str(digits[0] + digits[-1])
    suma = suma + int(num)

print(suma)