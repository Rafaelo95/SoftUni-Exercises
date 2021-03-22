string = input()
string_to_list = [x for x in string]

n = int(input())
matrix = [[] for _ in range(n)]
current_row = 0
current_col = 0


for el in matrix:
    data = input()
    for item in data:
        el.append(item)


for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            current_row = row
            current_col = col

m = int(input())
for _ in range(m):
    command = input()

    if command == 'down':
        next_row = current_row + 1
        next_col = current_col

        if next_row in range(n) and next_col in range(n):
            if matrix[next_row][next_col] != '-':
                string_to_list.append(matrix[next_row][next_col])
            matrix[next_row][next_col] = 'P'
            matrix[current_row][current_col] = '-'
            current_row = next_row
            current_col = next_col
        else:
            string_to_list.pop()

    elif command == 'up':
        next_row = current_row - 1
        next_col = current_col

        if next_row in range(n) and next_col in range(n):
            if matrix[next_row][next_col] != '-':
                string_to_list.append(matrix[next_row][next_col])
            matrix[next_row][next_col] = 'P'
            matrix[current_row][current_col] = '-'
            current_row = next_row
            current_col = next_col
        else:
            string_to_list.pop()

    elif command == 'right':
        next_row = current_row
        next_col = current_col + 1

        if next_row in range(n) and next_col in range(n):
            if matrix[next_row][next_col] != '-':
                string_to_list.append(matrix[next_row][next_col])
            matrix[next_row][next_col] = 'P'
            matrix[current_row][current_col] = '-'
            current_row = next_row
            current_col = next_col
        else:
            string_to_list.pop()

    elif command == 'left':
        next_row = current_row
        next_col = current_col - 1

        if next_row in range(n) and next_col in range(n):
            if matrix[next_row][next_col] != '-':
                string_to_list.append(matrix[next_row][next_col])
            matrix[next_row][next_col] = 'P'
            matrix[current_row][current_col] = '-'
            current_row = next_row
            current_col = next_col
        else:
            string_to_list.pop()

print(''.join(string_to_list))
for element in matrix:
    print(''.join(element))
