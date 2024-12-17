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
        if row[i] == 'X':
            results = []

            results.append(row[i-3:i+1][::-1]) # left
            results.append(row[i:i+4]) # right
            if j - 3 >= 0: # Can go up
                results.append(''.join([matrix[j - offset][i] for offset in range(4)])) # up
                if i - 3 >= 0: # I can go left
                    results.append(''.join([matrix[j - offset][i - offset] for offset in range(4)])) # up left
                if i + 3 < len(row):
                    results.append(''.join([matrix[j - offset][i + offset] for offset in range(4)])) # up right


            if j + 3 < len(matrix): # Can go down
                results.append(''.join([matrix[j + offset][i] for offset in range(4)])) # down
                if i - 3 >= 0:
                    results.append(''.join([matrix[j + offset][i - offset] for offset in range(4)])) # down left
                if i + 3 < len(row):
                    results.append(''.join([matrix[j + offset][i + offset] for offset in range(4)])) # down right

            
            count += results.count('XMAS')            
print(count)
        