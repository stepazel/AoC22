text = open('4/input', 'r')

matrix = []
while True:
    line = text.readline()
    if not line:
        break
    matrix.append(line)

count = 0
for j in range(0, len(matrix)):
    row = matrix[j]
    for i in range(0, len(row)):        
        if row[i] == 'A':
            results = []

            if j - 1 >= 0 and j + 1 < len(matrix) and i - 1 >= 0 and i + 1 < len(row): # Can go in all directions
                up_left = matrix[j - 1][i - 1]
                up_right = matrix[j - 1][i + 1]
                down_left = matrix[j + 1][i - 1]
                down_right = matrix[j + 1][i + 1]
                corners = up_left + up_right + down_right + down_left
                if corners == 'MSSM' or corners == 'MMSS' or corners == 'SSMM' or corners == 'SMMS':
                    count += 1

print(count)
        