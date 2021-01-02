rows, cols = list(map(int, input().split()))

matrix = []

for _ in range(rows):
    matrix.append(input().split())

counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        first_letter = matrix[row][col]
        second_letter = matrix[row][col + 1]
        third_letter = matrix[row + 1][col]
        fourth_letter = matrix[row + 1][col + 1]

        if first_letter == second_letter == third_letter == fourth_letter:
            counter += 1

print(counter)
