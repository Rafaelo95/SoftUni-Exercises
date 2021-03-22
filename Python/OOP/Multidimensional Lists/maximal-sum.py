rows, cols = list(map(int, input().split()))

matrix = []

for i in range(rows):
    elements = list(map(int, input().split()))
    matrix.append(elements)

best_sum = -99999999
best_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = []
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                sub_matrix.append(matrix[r][c])
                current_sum += matrix[r][c]
        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = sub_matrix

print(f"Sum = {best_sum}")
for row in range(1, len(best_matrix) + 1):
    if row % 3 == 0:
        print(best_matrix[row - 1])
        continue
    print(best_matrix[row - 1], end=' ')
