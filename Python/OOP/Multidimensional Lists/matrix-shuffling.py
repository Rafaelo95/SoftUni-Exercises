rows, cols = list(map(int, input().split()))

matrix = []

for _ in range(rows):
    data = input().split()
    matrix.append(data)

while True:

    command = input()
    if command == "END":
        break

    tokens = command.split()
    action = tokens[0]
    if action != "swap" or len(tokens) != 5:
        print("Invalid input!")
        continue

    row1 = int(tokens[1])
    col1 = int(tokens[2])
    row2 = int(tokens[3])
    col2 = int(tokens[4])

    if row1 > rows or row2 > rows or\
            col1 > cols or col2 > cols:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(' '.join(row))