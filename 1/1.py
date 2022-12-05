
text = open('input', 'r')

firstMaxCalories = 0
secondMaxCalories = 0
thirdMaxCalories = 0
currentCalories = 0
while True:
    line = text.readline()
    if not line:
        break

    if line == "\n":
        if currentCalories > firstMaxCalories:
            thirdMaxCalories = secondMaxCalories
            secondMaxCalories = firstMaxCalories
            firstMaxCalories = currentCalories
        elif currentCalories > secondMaxCalories:
            thirdMaxCalories = secondMaxCalories
            secondMaxCalories = currentCalories
        elif currentCalories > thirdMaxCalories:
            thirdMaxCalories = currentCalories
        currentCalories = 0
        continue

    currentCalories += int(line)

print (firstMaxCalories + secondMaxCalories + thirdMaxCalories)
print(f"1st: {firstMaxCalories} \n 2nd: {secondMaxCalories} \n 3rd {thirdMaxCalories}")
